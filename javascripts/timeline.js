// timeline.js
// Wrapped in IIFE to manage state across MkDocs Material instant navigation
(function() {
    var animFrameId = null;
    var cleanupFn = null;

    function initTimeline() {
        // Always clean up previous state first
        if (cleanupFn) {
            cleanupFn();
            cleanupFn = null;
        }

        var scrollContainer = document.getElementById('timelineScroll');
        if (!scrollContainer) return;

        var isDown = false;
        var hasDragged = false;
        var startX;
        var scrollLeft;
        var scrollSpeed = 0.5;
        var currentScrollPos = 0;
        var DRAG_THRESHOLD = 5;
        var halfWidth = 0;

        // Clone items for infinite scroll (mark clones to avoid re-cloning)
        var originals = Array.from(scrollContainer.querySelectorAll('.timeline-item:not([data-clone])'));
        originals.forEach(function(item) {
            var clone = item.cloneNode(true);
            clone.setAttribute('data-clone', 'true');
            scrollContainer.appendChild(clone);
        });

        function calculateHalfWidth() {
            if (scrollContainer.scrollWidth > 0) {
                halfWidth = scrollContainer.scrollWidth / 2;
            }
        }

        var calcTimeout = setTimeout(calculateHalfWidth, 500);
        window.addEventListener('resize', calculateHalfWidth);

        function onMouseDown(e) {
            if (e.target.closest('.timeline-links a')) return;
            isDown = true;
            hasDragged = false;
            startX = e.pageX;
            scrollLeft = scrollContainer.scrollLeft;
            pauseAutoScroll();
        }
        function onMouseLeave() { isDown = false; resumeAutoScroll(); }
        function onMouseUp() { isDown = false; resumeAutoScroll(); }
        function onMouseMove(e) {
            if (!isDown) return;
            if (Math.abs(e.pageX - startX) > DRAG_THRESHOLD) {
                hasDragged = true;
                e.preventDefault();
                scrollContainer.scrollLeft = scrollLeft - (e.pageX - startX);
                currentScrollPos = scrollContainer.scrollLeft;
            }
        }
        function onScroll() {
            if (isDown && halfWidth > 0) {
                if (scrollContainer.scrollLeft >= halfWidth) {
                    scrollContainer.scrollLeft -= halfWidth;
                    scrollLeft -= halfWidth;
                } else if (scrollContainer.scrollLeft <= 0) {
                    scrollContainer.scrollLeft += halfWidth;
                    scrollLeft += halfWidth;
                }
            }
        }
        function onTouchStart() { pauseAutoScroll(); }
        function onTouchEnd() { resumeAutoScroll(); }

        scrollContainer.addEventListener('mousedown', onMouseDown);
        scrollContainer.addEventListener('mouseleave', onMouseLeave);
        scrollContainer.addEventListener('mouseup', onMouseUp);
        scrollContainer.addEventListener('mousemove', onMouseMove);
        scrollContainer.addEventListener('scroll', onScroll);
        scrollContainer.addEventListener('touchstart', onTouchStart, {passive: true});
        scrollContainer.addEventListener('touchend', onTouchEnd);

        // Card click → navigate to data-href (only if not dragging)
        scrollContainer.addEventListener('click', function(e) {
            // Let direct link clicks pass through normally
            if (e.target.closest('.timeline-links a')) return;
            if (hasDragged) return;
            var item = e.target.closest('.timeline-item');
            if (item && item.dataset.href) {
                window.location.href = item.dataset.href;
            }
        });

        function step() {
            if (halfWidth > 0 && !isDown) {
                currentScrollPos += scrollSpeed;
                if (currentScrollPos >= halfWidth) currentScrollPos -= halfWidth;
                else if (currentScrollPos < 0) currentScrollPos += halfWidth;
                scrollContainer.scrollLeft = currentScrollPos;
            }
            animFrameId = requestAnimationFrame(step);
        }

        function resumeAutoScroll() {
            currentScrollPos = scrollContainer.scrollLeft;
            if (!animFrameId) animFrameId = requestAnimationFrame(step);
        }

        function pauseAutoScroll() {
            if (animFrameId) {
                cancelAnimationFrame(animFrameId);
                animFrameId = null;
            }
        }

        var startTimeout = setTimeout(resumeAutoScroll, 100);

        // Store cleanup for next navigation
        cleanupFn = function() {
            clearTimeout(calcTimeout);
            clearTimeout(startTimeout);
            if (animFrameId) { cancelAnimationFrame(animFrameId); animFrameId = null; }
            window.removeEventListener('resize', calculateHalfWidth);
        };
    }
    // MkDocs Material instant navigation support
    if (typeof document$ !== "undefined") {
        document$.subscribe(function() { initTimeline(); });
    } else if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTimeline);
    } else {
        initTimeline();
    }
})();
