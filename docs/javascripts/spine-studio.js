window.initSpineStudio = function(containerId, options) {
    console.log("[Spine Studio] initSpineStudio called for:", containerId);
    const wrapper = document.getElementById(containerId + "_wrapper");
    if (!wrapper) {
        console.error("[Spine Studio] Wrapper not found for:", containerId);
        return;
    }

    // Force hide default controls
    options.showControls = false;
    options.preserveDrawingBuffer = true; // needed for export
    
    // Save original success callback if any
    const originalSuccess = options.success;
    
    // Initialize player
    let player;
    try {
        player = new spine.SpinePlayer(containerId, options);
        console.log("[Spine Studio] Player initialized:", player);
        
        // Fix for hidden containers (e.g. MkDocs tabs or mobile views)
        // If the player initializes while hidden, its canvas size and WebGL viewport are 0.
        let lastWidth = 0;
        const resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
                const width = entry.contentRect.width;
                if (width > 0 && Math.abs(width - lastWidth) > 1) {
                    lastWidth = width;
                    window.dispatchEvent(new Event('resize'));
                }
            }
        });
        resizeObserver.observe(wrapper);
        
    } catch (err) {
        console.error("[Spine Studio] Error initializing player:", err);
        return;
    }
    
    // Poll for skeleton to setup UI (since success callback might not exist)
    let checkInterval = setInterval(() => {
        if (player.skeleton) {
            clearInterval(checkInterval);
            console.log("[Spine Studio] Skeleton loaded, setting up UI for:", containerId);
            if (!wrapper.querySelector('.spine-studio-playback')) {
                 setupStudioUI(player, containerId, wrapper);
                 if (originalSuccess) originalSuccess(player);
            }
        }
    }, 100);
    
    // Timeout to clear interval
    setTimeout(() => clearInterval(checkInterval), 10000);
};

function setupStudioUI(player, containerId, wrapper) {
    // Build HTML for UI
    const uiHTML = `
        <div class="spine-studio-playback">
            <button class="play-btn" id="${containerId}_play" title="Play/Pause">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor">
                    <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z" id="${containerId}_play_icon"/>
                </svg>
            </button>
            <div class="spine-studio-timeline">
                <span id="${containerId}_time">0.0</span>
                <input type="range" id="${containerId}_slider" min="0" max="100" value="0" step="0.001">
                <span id="${containerId}_duration">0.0</span>
            </div>
            <select id="${containerId}_speed" title="Speed">
                <option value="0.25">0.25x</option>
                <option value="0.5">0.5x</option>
                <option value="1" selected>1.0x</option>
                <option value="1.5">1.5x</option>
                <option value="2">2.0x</option>
            </select>
            <select id="${containerId}_skin" title="Skin">
            </select>
            <select id="${containerId}_anim" title="Animation">
            </select>
        </div>
        
        <div class="spine-studio-sidebar">
            <div style="display: flex; gap: 8px; margin-bottom: 12px;">
                <input type="text" class="spine-studio-parts-search" id="${containerId}_search" placeholder="파츠 검색..." style="margin-bottom: 0; flex: 1;">
                <button id="${containerId}_reset_parts" class="spine-studio-reset-btn" title="모든 파츠 다시 켜기">전체 켜기</button>
            </div>
            <div class="spine-studio-parts-list" id="${containerId}_parts"></div>
            
            <div class="spine-studio-export-btns">
                <button id="${containerId}_export_png" title="현재 화면을 PNG로 저장">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><circle cx="12" cy="12" r="3.2"/><path d="M9 2L7.17 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-3.17L15 2H9zm3 15c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5z"/></svg>
                    PNG 저장
                </button>
                <button class="gif-btn" id="${containerId}_export_gif" title="현재 모션을 GIF로 저장">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M18 4l2 4h-3l-2-4h-2l2 4h-3l-2-4H8l2 4H7L5 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2h-2z"/></svg>
                    GIF 저장
                </button>
            </div>
        </div>
        
        <div class="gif-progress-overlay" id="${containerId}_gif_overlay">
            <div>GIF 렌더링 중...</div>
            <div class="gif-progress-bar-container">
                <div class="gif-progress-bar" id="${containerId}_gif_progress"></div>
            </div>
        </div>
    `;

    // The container already has spine-studio-main with the canvas.
    // Let's inject playback into main, and sidebar into wrapper.
    const mainDiv = wrapper.querySelector('.spine-studio-main');
    
    // Create temp div to extract elements
    const tempDiv = document.createElement('div');
    tempDiv.innerHTML = uiHTML;
    
    mainDiv.appendChild(tempDiv.querySelector('.spine-studio-playback'));
    wrapper.appendChild(tempDiv.querySelector('.spine-studio-sidebar'));
    wrapper.appendChild(tempDiv.querySelector('.gif-progress-overlay'));

    // DOM Elements
    const playBtn = document.getElementById(`${containerId}_play`);
    const playIcon = document.getElementById(`${containerId}_play_icon`);
    const slider = document.getElementById(`${containerId}_slider`);
    const timeDisplay = document.getElementById(`${containerId}_time`);
    const durationDisplay = document.getElementById(`${containerId}_duration`);
    const speedSelect = document.getElementById(`${containerId}_speed`);
    const skinSelect = document.getElementById(`${containerId}_skin`);
    const animSelect = document.getElementById(`${containerId}_anim`);
    
    const searchInput = document.getElementById(`${containerId}_search`);
    const resetPartsBtn = document.getElementById(`${containerId}_reset_parts`);
    const partsList = document.getElementById(`${containerId}_parts`);
    const exportPngBtn = document.getElementById(`${containerId}_export_png`);
    const exportGifBtn = document.getElementById(`${containerId}_export_gif`);

    // Setup Skins
    const skins = player.skeleton.data.skins;
    if (skins && skins.length > 0) {
        skins.forEach(skin => {
            const option = document.createElement('option');
            option.value = skin.name;
            option.textContent = skin.name;
            if (skin.name === player.skeleton.skin?.name) {
                option.selected = true;
            }
            skinSelect.appendChild(option);
        });
        skinSelect.addEventListener('change', (e) => {
            player.skeleton.setSkinByName(e.target.value);
            player.skeleton.setToSetupPose();
        });
    } else {
        skinSelect.style.display = 'none';
    }

    // Setup Animations
    const animations = player.skeleton.data.animations;
    animations.forEach(anim => {
        const option = document.createElement('option');
        option.value = anim.name;
        option.textContent = anim.name;
        if (anim.name === player.animationState.tracks[0]?.animation?.name) {
            option.selected = true;
        }
        animSelect.appendChild(option);
    });

    // Setup Parts Toggle
    const slots = player.skeleton.slots;
    const hiddenSlots = new Set();
    
    // Create checkboxes for each slot
    function renderParts(filterText = "") {
        partsList.innerHTML = '';
        slots.forEach((slot, index) => {
            const name = slot.data.name;
            if (filterText && !name.toLowerCase().includes(filterText.toLowerCase())) return;
            
            const item = document.createElement('div');
            item.className = 'spine-studio-part-item';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.checked = !hiddenSlots.has(name);
            checkbox.id = `${containerId}_part_${index}`;
            
            checkbox.addEventListener('change', (e) => {
                if (e.target.checked) {
                    hiddenSlots.delete(name);
                    slot.setToSetupPose();
                } else {
                    hiddenSlots.add(name);
                }
            });
            
            const label = document.createElement('label');
            label.htmlFor = checkbox.id;
            label.textContent = name;
            label.style.cursor = 'pointer';
            
            item.appendChild(checkbox);
            item.appendChild(label);
            partsList.appendChild(item);
        });
    }
    
    renderParts();
    
    searchInput.addEventListener('input', (e) => {
        renderParts(e.target.value);
    });

    resetPartsBtn.addEventListener('click', () => {
        hiddenSlots.clear();
        slots.forEach(slot => slot.setToSetupPose());
        renderParts(searchInput.value);
    });

    // Canvas Click Hit Test for Parts
    player.canvas.addEventListener('click', (e) => {
        if (!player.sceneRenderer || !player.sceneRenderer.camera) return;
        const rect = player.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        let pt;
        if (typeof spine !== 'undefined' && spine.webgl && spine.webgl.Vector3) {
            pt = new spine.webgl.Vector3(x, y, 0);
        } else if (typeof spine !== 'undefined' && spine.Vector3) {
            pt = new spine.Vector3(x, y, 0);
        } else {
            pt = {
                x: x, y: y, z: 0,
                project: function(matrix) {
                    let m = matrix.values || matrix;
                    let px = this.x, py = this.y, pz = this.z;
                    let w = m[3] * px + m[7] * py + m[11] * pz + m[15];
                    w = w || 1;
                    this.x = (m[0] * px + m[4] * py + m[8] * pz + m[12]) / w;
                    this.y = (m[1] * px + m[5] * py + m[9] * pz + m[13]) / w;
                    this.z = (m[2] * px + m[6] * py + m[10] * pz + m[14]) / w;
                    return this;
                }
            };
        }

        player.sceneRenderer.camera.screenToWorld(pt, player.canvas.clientWidth, player.canvas.clientHeight);

        let hitSlot = null;
        for (let i = slots.length - 1; i >= 0; i--) {
            let slot = slots[i];
            let name = slot.data.name;
            if (hiddenSlots.has(name) || slot.color.a === 0) continue;

            let attachment = slot.getAttachment();
            if (!attachment || !attachment.computeWorldVertices) continue;

            let vertices = [];
            if (attachment.worldVerticesLength !== undefined) {
                attachment.computeWorldVertices(slot, 0, attachment.worldVerticesLength, vertices, 0, 2);
            } else {
                if (attachment.computeWorldVertices.length >= 4) {
                    attachment.computeWorldVertices(slot, vertices, 0, 2);
                } else {
                    attachment.computeWorldVertices(slot.bone, vertices, 0, 2);
                }
            }

            let inside = false;
            for (let j = 0, k = vertices.length - 2; j < vertices.length; k = j, j += 2) {
                let vx1 = vertices[j], vy1 = vertices[j+1];
                let vx2 = vertices[k], vy2 = vertices[k+1];
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
            renderParts(searchInput.value);
        }
    });

    // Playback logic
    let isPlaying = true;
    let isDragging = false;
    
    function updatePlayIcon() {
        if (isPlaying) {
            playIcon.setAttribute('d', "M6 19h4V5H6v14zm8-14v14h4V5h-4z"); // Pause icon
        } else {
            playIcon.setAttribute('d', "M8 5v14l11-7z"); // Play icon
        }
    }

    playBtn.addEventListener('click', () => {
        if (isPlaying) {
            player.paused = true;
            isPlaying = false;
        } else {
            player.paused = false;
            isPlaying = true;
        }
        updatePlayIcon();
    });

    speedSelect.addEventListener('change', (e) => {
        player.animationState.timeScale = parseFloat(e.target.value);
    });

    animSelect.addEventListener('change', (e) => {
        player.animationState.setAnimation(0, e.target.value, true);
    });

    // Sync slider with player and apply parts toggles
    requestAnimationFrame(function syncLoop() {
        if (!player || !player.animationState) return;
        
        // Force hide slots that are toggled off
        if (hiddenSlots.size > 0) {
            slots.forEach(slot => {
                if (hiddenSlots.has(slot.data.name)) {
                    slot.color.a = 0;
                }
            });
        }
        
        const track = player.animationState.getCurrent(0);
        if (track) {
            const duration = track.animationEnd - track.animationStart;
            const time = track.getAnimationTime();
            
            durationDisplay.textContent = duration.toFixed(1);
            slider.max = duration;
            
            if (!isDragging) {
                slider.value = time;
                timeDisplay.textContent = time.toFixed(1);
            }
        }
        requestAnimationFrame(syncLoop);
    });

    slider.addEventListener('mousedown', () => { isDragging = true; });
    slider.addEventListener('mouseup', () => { isDragging = false; });
    slider.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        timeDisplay.textContent = val.toFixed(1);
        const track = player.animationState.getCurrent(0);
        if (track) {
            track.trackTime = val;
            // Force update to render exactly this frame
            player.update(0); 
        }
    });

    // Export PNG
    exportPngBtn.addEventListener('click', () => {
        const canvas = player.canvas;
        const dataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.download = `spine_export_${animSelect.value}_${Date.now()}.png`;
        link.href = dataURL;
        link.click();
    });

    // Export GIF
    exportGifBtn.addEventListener('click', () => {
        exportGif(player, containerId, animSelect.value);
    });
}

function exportGif(player, containerId, animName) {
    // Load gif.js dynamically
    if (!window.GIF) {
        const script = document.createElement('script');
        script.src = "/javascripts/gif.js";
        script.onload = () => startGifExport(player, containerId, animName);
        script.onerror = () => {
            console.error("[Spine Studio] Failed to load gif.js");
            alert("GIF 라이브러리를 로드할 수 없습니다. 네트워크 연결을 확인해주세요.");
        };
        document.head.appendChild(script);
    } else {
        startGifExport(player, containerId, animName);
    }
}

function startGifExport(player, containerId, animName) {
    const overlay = document.getElementById(`${containerId}_gif_overlay`);
    const progressBar = document.getElementById(`${containerId}_gif_progress`);
    overlay.style.display = 'flex';
    progressBar.style.width = '0%';

    const track = player.animationState.getCurrent(0);
    const duration = track ? (track.animationEnd - track.animationStart) : 1;
    
    // Reset to start
    const originalTimeScale = player.animationState.timeScale;
    const originalPaused = player.paused;
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

    const fps = 30;
    const totalFrames = Math.ceil(duration * fps);
    const stepTime = 1 / fps;

    // Load worker from local path to avoid CORS and fetch hanging issues
    const workerScriptUrl = '/javascripts/gif.worker.js';
    
    const config = player.config || {};
    const isAlpha = config.alpha !== undefined ? config.alpha : true;
    const bgColor = config.backgroundColor || '#ffffff';
    const transparentColorHex = isAlpha ? 0xff00ff : null;
    const transparentColorStr = isAlpha ? '#ff00ff' : null;
    
    const gif = new GIF({
        workers: 2,
        quality: 2,
        workerScript: workerScriptUrl,
        transparent: transparentColorHex,
        background: isAlpha ? transparentColorStr : bgColor,
        globalPalette: true
    });

    let currentFrame = 0;

    function renderNextFrame() {
                try {
                    if (currentFrame < totalFrames) {
                        // Advance animation
                        if (typeof player.update === 'function') {
                            player.update(stepTime);
                        } else {
                            player.animationState.update(stepTime);
                            player.animationState.apply(player.skeleton);
                            player.skeleton.updateWorldTransform();
                        }
                        
                        // Force render
                        if (typeof player.drawFrame === 'function') player.drawFrame(false);
                        else if (typeof player.render === 'function') player.render();
                        else if (player.app && typeof player.app.render === 'function') player.app.render(player);
                        
                        // Use a temporary canvas to composite the image over a solid color for chroma key transparency
                        const tempCanvas = document.createElement('canvas');
                        tempCanvas.width = player.canvas.width;
                        tempCanvas.height = player.canvas.height;
                        const ctx = tempCanvas.getContext('2d', { willReadFrequently: true });
                        
                        if (isAlpha) {
                            // Extract pixels with a hard threshold to avoid chroma key fringing on semi-transparent pixels
                            ctx.drawImage(player.canvas, 0, 0);
                            const imageData = ctx.getImageData(0, 0, tempCanvas.width, tempCanvas.height);
                            const data = imageData.data;
                            for (let i = 0; i < data.length; i += 4) {
                                if (data[i + 3] < 128) {
                                    // Fully transparent: assign chroma key color
                                    data[i] = 255;
                                    data[i + 1] = 0;
                                    data[i + 2] = 255;
                                    data[i + 3] = 255;
                                } else {
                                    // Fully opaque: keep original RGB, force alpha to 255
                                    // Prevent character's actual magenta pixels from being chroma-keyed out
                                    if (data[i] === 255 && data[i + 1] === 0 && data[i + 2] === 255) {
                                        data[i] = 254;
                                    }
                                    data[i + 3] = 255;
                                }
                            }
                            ctx.putImageData(imageData, 0, 0);
                        } else {
                            ctx.fillStyle = bgColor;
                            ctx.fillRect(0, 0, tempCanvas.width, tempCanvas.height);
                            ctx.drawImage(player.canvas, 0, 0);
                        }
                        
                        gif.addFrame(tempCanvas, {copy: true, delay: stepTime * 1000});
                        
                        currentFrame++;
                        progressBar.style.width = `${(currentFrame / totalFrames) * 100}%`;
                        
                        setTimeout(renderNextFrame, 10);
                    } else {
                        gif.on('finished', function(blob) {
                            const url = URL.createObjectURL(blob);
                            const link = document.createElement('a');
                            link.download = `spine_export_${animName}_${Date.now()}.gif`;
                            link.href = url;
                            link.click();
                            
                            overlay.style.display = 'none';
                            URL.revokeObjectURL(url);
                            
                            player.animationState.timeScale = originalTimeScale;
                            player.paused = originalPaused;
                        });
                        
                        gif.render();
                    }
                } catch (err) {
                    console.error("[Spine Studio] GIF Render Error:", err);
                    alert("GIF 렌더링 중 오류가 발생했습니다: " + err.message);
                    overlay.style.display = 'none';
                    player.animationState.timeScale = originalTimeScale;
                    player.paused = originalPaused;
                }
            }

            renderNextFrame();
}
