/**
 * Spine Multi-Viewer: single player with costume (skel file) switching via dropdown.
 * Features: play/pause, timeline, speed, animation select, skin select,
 *           costume dropdown, collapsible parts panel, canvas click hit-test,
 *           PNG export, GIF export.
 */
window.initSpineMultiViewer = function(containerId, costumes, defaultIndex) {
    var wrapper = document.getElementById(containerId + '_wrapper');
    if (!wrapper) return;

    // Run existing cleanup if active
    window._spineMultiCleanups = window._spineMultiCleanups || {};
    if (window._spineMultiCleanups[containerId]) {
        try { window._spineMultiCleanups[containerId](); } catch(e) {}
        delete window._spineMultiCleanups[containerId];
    }

    var windowListeners = [];
    var isCleanedUp = false;

    function addWindowListener(type, fn, opts) {
        window.addEventListener(type, fn, opts);
        windowListeners.push({ type: type, fn: fn, opts: opts });
    }

    var currentIndex = defaultIndex || 0;
    var player = null;
    var isPlaying = true;
    var currentSpeed = 1;
    var hiddenSlots = new Set();
    var undoHistory = [];

    // --- Transform state (zoom / pan) ---
    var transformScale = 1;
    var transformX = 0;
    var transformY = 0;
    var baseScaleX = 1;
    var baseScaleY = 1;
    var baseX = 0;
    var baseY = 0;
    var transformReady = false;

    // --- DOM references ---
    var canvasContainer = document.getElementById(containerId);
    var costumeSelect = wrapper.querySelector('.smv-costume-select');
    var animSelect = wrapper.querySelector('.smv-anim-select');
    var skinSelect = wrapper.querySelector('.smv-skin-select');
    var playBtn = wrapper.querySelector('.smv-play-btn');
    var playIcon = wrapper.querySelector('.smv-play-icon');
    var slider = wrapper.querySelector('.smv-slider');
    var timeDisplay = wrapper.querySelector('.smv-time');
    var durationDisplay = wrapper.querySelector('.smv-duration');
    var speedSelect = wrapper.querySelector('.smv-speed-select');
    var exportPngBtn = wrapper.querySelector('.smv-export-png');
    var exportGifBtn = wrapper.querySelector('.smv-export-gif');
    var partsToggle = wrapper.querySelector('.smv-parts-toggle');
    var partsPanel = wrapper.querySelector('.smv-parts-panel');
    var partsSearch = wrapper.querySelector('.smv-parts-search');
    var partsResetBtn = wrapper.querySelector('.smv-parts-reset');
    var partsList = wrapper.querySelector('.smv-parts-list');
    var gifOverlay = wrapper.querySelector('.smv-gif-overlay');
    var gifProgress = wrapper.querySelector('.smv-gif-progress');
    var gifLabel = wrapper.querySelector('.smv-gif-label');
    var exportSizeSelect = wrapper.querySelector('.smv-export-size');
    var resetBtn = wrapper.querySelector('.smv-reset-btn');
    var transformResetBtn = wrapper.querySelector('.smv-transform-reset');
    var undoBtn = wrapper.querySelector('.smv-undo-btn');

    // --- Parts panel toggle ---
    if (partsToggle && partsPanel) {
        partsToggle.addEventListener('click', function() {
            var isOpen = partsPanel.classList.toggle('open');
            partsToggle.classList.toggle('active', isOpen);
        });
    }

    // --- Costume switching ---
    function loadCostume(index) {
        currentIndex = index;
        var costume = costumes[index];
        if (!costume) return;

        // Update dropdown
        if (costumeSelect) costumeSelect.value = index;

        // Reset parts state
        hiddenSlots.clear();
        undoHistory = [];
        if (partsSearch) partsSearch.value = '';

        // Reset transform state
        transformScale = 1;
        transformX = 0;
        transformY = 0;
        transformReady = false;

        // Dispose existing player
        if (player) {
            try { player.dispose(); } catch(e) { /* ignore */ }
            player = null;
        }
        canvasContainer.innerHTML = '';

        // Create new player
        var opts = {
            skelUrl: costume.skelUrl,
            atlasUrl: costume.atlasUrl,
            backgroundColor: '#00000000',
            alpha: true,
            preserveDrawingBuffer: true,
            showControls: false,
            showLoading: false,
            animation: costume.animation || 'Idle_1',
            skin: costume.skin || 'Normal'
        };

        try {
            player = new spine.SpinePlayer(containerId, opts);
        } catch(e) {
            console.error('[SpineMulti] Error:', e);
            return;
        }

        // Poll for skeleton ready
        var checkInterval = setInterval(function() {
            if (player && player.skeleton) {
                clearInterval(checkInterval);
                onSkeletonReady();
            }
        }, 80);
        setTimeout(function() { clearInterval(checkInterval); }, 10000);
    }

    function onSkeletonReady() {
        // Populate animations
        animSelect.innerHTML = '';
        var anims = player.skeleton.data.animations;
        anims.forEach(function(anim) {
            var opt = document.createElement('option');
            opt.value = anim.name;
            opt.textContent = anim.name;
            var currentAnim = player.animationState.tracks[0] && player.animationState.tracks[0].animation;
            if (currentAnim && anim.name === currentAnim.name) {
                opt.selected = true;
            }
            animSelect.appendChild(opt);
        });

        // Populate skins
        skinSelect.innerHTML = '';
        var skins = player.skeleton.data.skins;
        if (skins && skins.length > 1) {
            skins.forEach(function(skin) {
                var opt = document.createElement('option');
                opt.value = skin.name;
                opt.textContent = skin.name;
                if (player.skeleton.skin && skin.name === player.skeleton.skin.name) {
                    opt.selected = true;
                }
                skinSelect.appendChild(opt);
            });
            skinSelect.style.display = '';
        } else {
            skinSelect.style.display = 'none';
        }

        // Populate parts list
        renderParts();

        // Restore speed
        player.animationState.timeScale = currentSpeed;

        // Restore play state
        player.paused = !isPlaying;
        updatePlayIcon();

        // Capture base skeleton transform
        baseScaleX = player.skeleton.scaleX;
        baseScaleY = player.skeleton.scaleY;
        baseX = player.skeleton.x;
        baseY = player.skeleton.y;
        transformReady = true;

        // Setup canvas click hit-test
        setupCanvasClickHitTest();

        // Setup canvas zoom / pan
        setupCanvasTransform();

        // Start sync loop
        requestAnimationFrame(syncLoop);
    }

    // --- Parts rendering ---
    function renderParts(filterText) {
        if (!partsList || !player || !player.skeleton) return;
        filterText = filterText || '';
        partsList.innerHTML = '';
        var slots = player.skeleton.slots;
        slots.forEach(function(slot, index) {
            var name = slot.data.name;
            if (filterText && name.toLowerCase().indexOf(filterText.toLowerCase()) === -1) return;

            var item = document.createElement('div');
            item.className = 'smv-part-item';

            var checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.checked = !hiddenSlots.has(name);
            checkbox.id = containerId + '_part_' + index;

            checkbox.addEventListener('change', function(e) {
                if (e.target.checked) {
                    hiddenSlots.delete(name);
                    slot.setToSetupPose();
                } else {
                    hiddenSlots.add(name);
                    undoHistory.push(name);
                }
            });

            var label = document.createElement('label');
            label.htmlFor = checkbox.id;
            label.textContent = name;
            label.style.cursor = 'pointer';

            item.appendChild(checkbox);
            item.appendChild(label);
            partsList.appendChild(item);
        });
    }

    if (partsSearch) {
        partsSearch.addEventListener('input', function(e) {
            renderParts(e.target.value);
        });
    }

    if (partsResetBtn) {
        partsResetBtn.addEventListener('click', function() {
            resetAllParts();
        });
    }

    // --- Reset & Undo (main UI) ---
    function resetAllParts() {
        hiddenSlots.clear();
        undoHistory = [];
        if (player && player.skeleton) {
            player.skeleton.slots.forEach(function(slot) { slot.setToSetupPose(); });
        }
        renderParts(partsSearch ? partsSearch.value : '');
    }

    function undoLastHide() {
        if (undoHistory.length === 0) return;
        var lastSlot = undoHistory.pop();
        hiddenSlots.delete(lastSlot);
        if (player && player.skeleton) {
            player.skeleton.slots.forEach(function(slot) {
                if (slot.data.name === lastSlot) slot.setToSetupPose();
            });
        }
        renderParts(partsSearch ? partsSearch.value : '');
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', function() { resetAllParts(); });
    }
    if (undoBtn) {
        undoBtn.addEventListener('click', function() { undoLastHide(); });
    }

    // --- Transform reset ---
    function resetTransform() {
        transformScale = 1;
        transformX = 0;
        transformY = 0;
    }
    if (transformResetBtn) {
        transformResetBtn.addEventListener('click', function() { resetTransform(); });
    }

    // --- Canvas zoom / pan ---
    function setupCanvasTransform() {
        if (!player || !player.canvas) return;
        var canvas = player.canvas;

        // Mouse wheel zoom
        canvas.addEventListener('wheel', function(e) {
            e.preventDefault();
            var delta = e.deltaY > 0 ? -0.05 : 0.05;
            transformScale = Math.max(0.2, Math.min(3, transformScale + delta));
        }, { passive: false });

        // Drag to pan (mouse)
        var dragging = false;
        var lastDragX = 0, lastDragY = 0;

        canvas.addEventListener('mousedown', function(e) {
            if (e.button === 2 || e.shiftKey || e.ctrlKey) {
                e.preventDefault();
                dragging = true;
                lastDragX = e.clientX;
                lastDragY = e.clientY;
                canvas.style.cursor = 'grabbing';
            }
        });

        addWindowListener('mousemove', function(e) {
            if (!dragging) return;
            var dx = e.clientX - lastDragX;
            var dy = e.clientY - lastDragY;
            lastDragX = e.clientX;
            lastDragY = e.clientY;
            transformX += dx * 1.5;
            transformY -= dy * 1.5;  // spine Y is flipped
        });

        addWindowListener('mouseup', function() {
            if (dragging) {
                dragging = false;
                canvas.style.cursor = '';
            }
        });

        // Pinch to zoom + drag to pan (touch)
        var lastTouchDist = 0;
        var lastTouchX = 0, lastTouchY = 0;
        var touching = false;

        canvas.addEventListener('touchstart', function(e) {
            if (e.touches.length === 2) {
                e.preventDefault();
                var dx = e.touches[0].clientX - e.touches[1].clientX;
                var dy = e.touches[0].clientY - e.touches[1].clientY;
                lastTouchDist = Math.sqrt(dx * dx + dy * dy);
                touching = true;
            } else if (e.touches.length === 1) {
                // Single finger: long-press or two-finger for pan
                lastTouchX = e.touches[0].clientX;
                lastTouchY = e.touches[0].clientY;
            }
        }, { passive: false });

        canvas.addEventListener('touchmove', function(e) {
            if (e.touches.length === 2 && touching) {
                e.preventDefault();
                var dx = e.touches[0].clientX - e.touches[1].clientX;
                var dy = e.touches[0].clientY - e.touches[1].clientY;
                var dist = Math.sqrt(dx * dx + dy * dy);
                if (lastTouchDist > 0) {
                    var ratio = dist / lastTouchDist;
                    transformScale = Math.max(0.2, Math.min(3, transformScale * ratio));
                }
                lastTouchDist = dist;

                // Pan with midpoint movement
                var mx = (e.touches[0].clientX + e.touches[1].clientX) / 2;
                var my = (e.touches[0].clientY + e.touches[1].clientY) / 2;
                if (lastTouchX && lastTouchY) {
                    transformX += (mx - lastTouchX) * 1.5;
                    transformY -= (my - lastTouchY) * 1.5;
                }
                lastTouchX = mx;
                lastTouchY = my;
            }
        }, { passive: false });

        canvas.addEventListener('touchend', function() {
            touching = false;
            lastTouchDist = 0;
            lastTouchX = 0;
            lastTouchY = 0;
        });

        // Prevent context menu on canvas for right-click drag
        canvas.addEventListener('contextmenu', function(e) { e.preventDefault(); });
    }

    // --- Canvas click hit-test ---
    function setupCanvasClickHitTest() {
        if (!player || !player.canvas) return;
        player.canvas.addEventListener('click', function(e) {
            if (!player || !player.sceneRenderer || !player.sceneRenderer.camera) return;
            var rect = player.canvas.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;

            var pt;
            if (typeof spine !== 'undefined' && spine.webgl && spine.webgl.Vector3) {
                pt = new spine.webgl.Vector3(x, y, 0);
            } else if (typeof spine !== 'undefined' && spine.Vector3) {
                pt = new spine.Vector3(x, y, 0);
            } else {
                pt = {
                    x: x, y: y, z: 0,
                    project: function(matrix) {
                        var m = matrix.values || matrix;
                        var px = this.x, py = this.y, pz = this.z;
                        var w = m[3] * px + m[7] * py + m[11] * pz + m[15];
                        w = w || 1;
                        this.x = (m[0] * px + m[4] * py + m[8] * pz + m[12]) / w;
                        this.y = (m[1] * px + m[5] * py + m[9] * pz + m[13]) / w;
                        this.z = (m[2] * px + m[6] * py + m[10] * pz + m[14]) / w;
                        return this;
                    }
                };
            }

            player.sceneRenderer.camera.screenToWorld(pt, player.canvas.clientWidth, player.canvas.clientHeight);

            var slots = player.skeleton.slots;
            var hitSlot = null;
            for (var i = slots.length - 1; i >= 0; i--) {
                var slot = slots[i];
                var name = slot.data.name;
                if (hiddenSlots.has(name) || slot.color.a === 0) continue;

                var attachment = slot.getAttachment();
                if (!attachment || !attachment.computeWorldVertices) continue;

                var vertices = [];
                if (attachment.worldVerticesLength !== undefined) {
                    attachment.computeWorldVertices(slot, 0, attachment.worldVerticesLength, vertices, 0, 2);
                } else {
                    if (attachment.computeWorldVertices.length >= 4) {
                        attachment.computeWorldVertices(slot, vertices, 0, 2);
                    } else {
                        attachment.computeWorldVertices(slot.bone, vertices, 0, 2);
                    }
                }

                var inside = false;
                for (var j = 0, k = vertices.length - 2; j < vertices.length; k = j, j += 2) {
                    var vx1 = vertices[j], vy1 = vertices[j + 1];
                    var vx2 = vertices[k], vy2 = vertices[k + 1];
                    if (((vy1 > pt.y) !== (vy2 > pt.y)) && (pt.x < (vx2 - vx1) * (pt.y - vy1) / (vy2 - vy1) + vx1)) {
                        inside = !inside;
                    }
                }

                if (inside) {
                    hitSlot = name;
                    break;
                }
            }

            if (hitSlot) {
                hiddenSlots.add(hitSlot);
                undoHistory.push(hitSlot);
                renderParts(partsSearch ? partsSearch.value : '');
            }
        });
    }

    // --- Playback controls ---
    function updatePlayIcon() {
        if (isPlaying) {
            playIcon.innerHTML = '<path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>';
        } else {
            playIcon.innerHTML = '<path d="M8 5v14l11-7z"/>';
        }
    }

    playBtn.addEventListener('click', function() {
        isPlaying = !isPlaying;
        if (player) player.paused = !isPlaying;
        updatePlayIcon();
    });

    speedSelect.addEventListener('change', function(e) {
        currentSpeed = parseFloat(e.target.value);
        if (player && player.animationState) {
            player.animationState.timeScale = currentSpeed;
        }
    });

    animSelect.addEventListener('change', function(e) {
        if (player && player.animationState) {
            player.animationState.setAnimation(0, e.target.value, true);
        }
    });

    skinSelect.addEventListener('change', function(e) {
        if (player && player.skeleton) {
            player.skeleton.setSkinByName(e.target.value);
            player.skeleton.setToSetupPose();
        }
    });

    // Costume dropdown
    if (costumeSelect) {
        costumeSelect.addEventListener('change', function(e) {
            var idx = parseInt(e.target.value, 10);
            if (idx !== currentIndex) loadCostume(idx);
        });
    }

    // --- Timeline slider ---
    var isDragging = false;
    slider.addEventListener('mousedown', function() { isDragging = true; });
    slider.addEventListener('touchstart', function() { isDragging = true; });
    slider.addEventListener('mouseup', function() { isDragging = false; });
    slider.addEventListener('touchend', function() { isDragging = false; });
    slider.addEventListener('input', function(e) {
        var val = parseFloat(e.target.value);
        timeDisplay.textContent = val.toFixed(1);
        if (player && player.animationState) {
            var track = player.animationState.getCurrent(0);
            if (track) {
                track.trackTime = val;
                if (typeof player.update === 'function') player.update(0);
            }
        }
    });

    function syncLoop() {
        if (isCleanedUp) return;
        if (!player || !player.animationState) return;

        // Apply transform (zoom / pan)
        if (transformReady && player.skeleton) {
            player.skeleton.scaleX = baseScaleX * transformScale;
            player.skeleton.scaleY = baseScaleY * transformScale;
            player.skeleton.x = baseX + transformX;
            player.skeleton.y = baseY + transformY;
        }

        // Force hide toggled-off slots
        if (hiddenSlots.size > 0 && player.skeleton) {
            player.skeleton.slots.forEach(function(slot) {
                if (hiddenSlots.has(slot.data.name)) {
                    slot.color.a = 0;
                }
            });
        }

        var track = player.animationState.getCurrent(0);
        if (track) {
            var duration = track.animationEnd - track.animationStart;
            var time = track.getAnimationTime();
            durationDisplay.textContent = duration.toFixed(1);
            slider.max = duration;
            if (!isDragging) {
                slider.value = time;
                timeDisplay.textContent = time.toFixed(1);
            }
            var pct = duration > 0 ? (time / duration) * 100 : 0;
            slider.style.setProperty('--fill', pct + '%');
        }
        requestAnimationFrame(syncLoop);
    }

    // --- Helper: get selected export size ---
    function getExportSize() {
        return exportSizeSelect ? parseInt(exportSizeSelect.value, 10) : 512;
    }

    // --- Helper: scale and center-crop canvas to target size (square) ---
    function scaleCanvas(srcCanvas, targetSize) {
        var sw = srcCanvas.width, sh = srcCanvas.height;
        var cropSize = Math.min(sw, sh);
        var sx = (sw - cropSize) / 2;
        var sy = (sh - cropSize) / 2;
        
        var out = document.createElement('canvas');
        out.width = targetSize;
        out.height = targetSize;
        var ctx = out.getContext('2d');
        
        ctx.clearRect(0, 0, targetSize, targetSize);
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        ctx.drawImage(srcCanvas, sx, sy, cropSize, cropSize, 0, 0, targetSize, targetSize);
        
        return out;
    }

    // --- PNG export ---
    if (exportPngBtn) {
        exportPngBtn.addEventListener('click', function() {
            if (!player || !player.canvas) return;
            var size = getExportSize();
            var scaled = scaleCanvas(player.canvas, size);
            var dataURL = scaled.toDataURL('image/png');
            var link = document.createElement('a');
            link.download = 'spine_' + costumes[currentIndex].label + '_' + (animSelect.value || '') + '_' + size + 'px_' + Date.now() + '.png';
            link.href = dataURL;
            link.click();
        });
    }

    // --- GIF export ---
    if (exportGifBtn) {
        exportGifBtn.addEventListener('click', function() {
            exportGif();
        });
    }

    function getJavascriptsDir() {
        var scripts = document.getElementsByTagName('script');
        for (var i = 0; i < scripts.length; i++) {
            var src = scripts[i].src;
            if (src && src.indexOf('spine-multi.js') !== -1) {
                return src.substring(0, src.lastIndexOf('/') + 1);
            }
        }
        return '/javascripts/';
    }

    function exportGif() {
        if (!player || !player.canvas) return;
        if (!window.GIF) {
            var script = document.createElement('script');
            script.src = getJavascriptsDir() + 'gif.js';
            script.onload = function() { startGifExport(); };
            script.onerror = function() {
                alert('GIF 라이브러리를 로드할 수 없습니다.');
            };
            document.head.appendChild(script);
        } else {
            startGifExport();
        }
    }

    function startGifExport() {
        if (gifOverlay) gifOverlay.style.display = 'flex';
        if (gifProgress) gifProgress.style.width = '0%';
        if (gifLabel) gifLabel.textContent = '프레임 렌더링 중...';

        var exportSize = getExportSize();
        var track = player.animationState.getCurrent(0);
        var duration = track ? (track.animationEnd - track.animationStart) : 1;

        var originalTimeScale = player.animationState.timeScale;
        var originalPaused = player.paused;
        player.animationState.timeScale = 1;
        player.paused = true;
        if (track) track.trackTime = 0;
        if (typeof player.update === 'function') {
            player.update(0);
        } else {
            player.animationState.update(0);
            player.animationState.apply(player.skeleton);
            player.skeleton.updateWorldTransform();
        }

        var fps = 30;
        var totalFrames = Math.ceil(duration * fps);
        var stepTime = 1 / fps;

        var workerScriptUrl = getJavascriptsDir() + 'gif.worker.js';
        var config = player.config || {};
        var isAlpha = config.alpha !== undefined ? config.alpha : true;
        var bgColor = config.backgroundColor || '#ffffff';
        var transparentColorHex = isAlpha ? 0xff00ff : null;
        var transparentColorStr = isAlpha ? '#ff00ff' : null;

        var gif = new GIF({
            workers: 2,
            quality: 2,
            workerScript: workerScriptUrl,
            transparent: transparentColorHex,
            background: isAlpha ? transparentColorStr : bgColor,
            width: exportSize,
            height: exportSize,
            globalPalette: true
        });

        var currentFrame = 0;

        function renderNextFrame() {
            try {
                if (currentFrame < totalFrames) {
                    if (typeof player.update === 'function') {
                        player.update(stepTime);
                    } else {
                        player.animationState.update(stepTime);
                        player.animationState.apply(player.skeleton);
                        player.skeleton.updateWorldTransform();
                    }
                    if (typeof player.drawFrame === 'function') player.drawFrame(false);
                    else if (typeof player.render === 'function') player.render();
                    else if (player.app && typeof player.app.render === 'function') player.app.render(player);

                    // Scale to export size
                    var scaled = scaleCanvas(player.canvas, exportSize);
                    var tempCanvas = document.createElement('canvas');
                    tempCanvas.width = scaled.width;
                    tempCanvas.height = scaled.height;
                    var ctx = tempCanvas.getContext('2d', { willReadFrequently: true });

                    if (isAlpha) {
                        ctx.drawImage(scaled, 0, 0);
                        var imageData = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height);
                        var data = imageData.data;
                        for (var p = 0; p < data.length; p += 4) {
                            if (data[p + 3] < 128) {
                                data[p] = 255; data[p + 1] = 0; data[p + 2] = 255; data[p + 3] = 255;
                            } else {
                                if (data[p] === 255 && data[p + 1] === 0 && data[p + 2] === 255) { data[p] = 254; }
                                data[p + 3] = 255;
                            }
                        }
                        ctx.putImageData(imageData, 0, 0);
                    } else {
                        ctx.fillStyle = bgColor;
                        ctx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
                        ctx.drawImage(scaled, 0, 0);
                    }

                    gif.addFrame(tempCanvas, { copy: true, delay: stepTime * 1000 });
                    currentFrame++;
                    if (gifProgress) gifProgress.style.width = (currentFrame / totalFrames * 50) + '%';
                    setTimeout(renderNextFrame, 10);
                } else {
                    // Switch to encoding phase
                    if (gifLabel) gifLabel.textContent = 'GIF 인코딩 중...';
                    if (gifProgress) gifProgress.style.width = '50%';

                    gif.on('progress', function(p) {
                        if (gifProgress) gifProgress.style.width = (50 + p * 50) + '%';
                    });

                    gif.on('finished', function(blob) {
                        var url = URL.createObjectURL(blob);
                        var link = document.createElement('a');
                        link.download = 'spine_' + costumes[currentIndex].label + '_' + (animSelect.value || '') + '_' + exportSize + 'px_' + Date.now() + '.gif';
                        link.href = url;
                        link.click();
                        if (gifOverlay) gifOverlay.style.display = 'none';
                        URL.revokeObjectURL(url);
                        player.animationState.timeScale = originalTimeScale;
                        player.paused = originalPaused;
                    });
                    gif.render();
                }
            } catch (err) {
                console.error('[SpineMulti] GIF Error:', err);
                alert('GIF 렌더링 중 오류가 발생했습니다: ' + err.message);
                if (gifOverlay) gifOverlay.style.display = 'none';
                player.animationState.timeScale = originalTimeScale;
                player.paused = originalPaused;
            }
        }

        renderNextFrame();
    }

    // --- ResizeObserver for hidden container fix ---
    var lastWidth = 0;
    var ro = new ResizeObserver(function(entries) {
        for (var i = 0; i < entries.length; i++) {
            var w = entries[i].contentRect.width;
            if (w > 0 && Math.abs(w - lastWidth) > 1) {
                lastWidth = w;
                window.dispatchEvent(new Event('resize'));
            }
        }
    });
    ro.observe(wrapper);

    function cleanup() {
        if (isCleanedUp) return;
        isCleanedUp = true;

        if (ro) {
            try { ro.disconnect(); } catch(e) {}
        }

        windowListeners.forEach(function(item) {
            try { window.removeEventListener(item.type, item.fn, item.opts); } catch(e) {}
        });
        windowListeners = [];

        if (player) {
            try { player.dispose(); } catch(e) {}
            player = null;
        }
    }

    window._spineMultiCleanups[containerId] = cleanup;

    // --- Initial load ---
    loadCostume(currentIndex);
};

if (typeof document$ !== 'undefined') {
    document$.subscribe(function() {
        if (window._spineMultiCleanups) {
            Object.keys(window._spineMultiCleanups).forEach(function(key) {
                if (!document.getElementById(key)) {
                    try {
                        window._spineMultiCleanups[key]();
                    } catch(e) {}
                    delete window._spineMultiCleanups[key];
                }
            });
        }
    });
}
