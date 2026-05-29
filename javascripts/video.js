(function () {
  const objectUrls = new WeakMap();

  function ranges(rangeList) {
    const values = [];
    for (let index = 0; index < rangeList.length; index += 1) {
      values.push([rangeList.start(index), rangeList.end(index)]);
    }
    return values;
  }

  function hasUsableSeekRange(video) {
    if (!Number.isFinite(video.duration) || video.duration <= 0) {
      return true;
    }

    let maxEnd = 0;
    for (const range of ranges(video.seekable)) {
      maxEnd = Math.max(maxEnd, range[1]);
    }

    return maxEnd >= Math.min(video.duration - 0.5, 1);
  }

  function sourceUrl(video) {
    if (video.currentSrc && !video.currentSrc.startsWith("blob:")) {
      return video.currentSrc;
    }

    if (video.src && !video.src.startsWith("blob:")) {
      return video.src;
    }

    const source = video.querySelector("source[src]");
    return source ? source.src : "";
  }

  async function replaceWithBlob(video) {
    if (video.dataset.videoBlobState) {
      return;
    }

    const url = sourceUrl(video);
    if (!url) {
      return;
    }

    video.dataset.videoBlobState = "loading";

    const time = video.currentTime;
    const wasPaused = video.paused;

    try {
      const response = await fetch(url, { cache: "force-cache" });
      if (!response.ok) {
        throw new Error("Video request failed");
      }

      const blob = await response.blob();
      const objectUrl = URL.createObjectURL(blob);
      const previousObjectUrl = objectUrls.get(video);
      if (previousObjectUrl) {
        URL.revokeObjectURL(previousObjectUrl);
      }

      objectUrls.set(video, objectUrl);
      video.src = objectUrl;
      video.load();

      video.addEventListener(
        "loadedmetadata",
        function restorePlayback() {
          if (Number.isFinite(time) && time > 0 && time < video.duration) {
            video.currentTime = time;
          }

          if (!wasPaused) {
            video.play().catch(function () {});
          }

          video.dataset.videoBlobState = "ready";
        },
        { once: true },
      );
    } catch (error) {
      video.dataset.videoBlobState = "failed";
      console.warn("Video seek fallback failed", error);
    }
  }

  function checkVideo(video) {
    if (video.dataset.videoBlobFallback !== "true") {
      return;
    }

    if (!hasUsableSeekRange(video)) {
      replaceWithBlob(video);
    }
  }

  function bindVideo(video) {
    if (video.dataset.videoBlobBound === "true") {
      return;
    }

    video.dataset.videoBlobBound = "true";
    video.addEventListener("loadedmetadata", function () {
      checkVideo(video);
    });

    if (video.readyState >= HTMLMediaElement.HAVE_METADATA) {
      checkVideo(video);
    }
  }

  function initVideoFallback(root) {
    root.querySelectorAll("video[data-video-blob-fallback='true']").forEach(bindVideo);
  }

  function cleanup() {
    document.querySelectorAll("video[data-video-blob-fallback='true']").forEach(function (video) {
      const objectUrl = objectUrls.get(video);
      if (objectUrl) {
        URL.revokeObjectURL(objectUrl);
        objectUrls.delete(video);
      }
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      initVideoFallback(document);
    });
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initVideoFallback(document);
    });
  } else {
    initVideoFallback(document);
  }

  window.addEventListener("pagehide", cleanup);
})();
