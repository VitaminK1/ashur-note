// Voice playback for intimacy table buttons
(function () {
  var audio = null;
  var activeBtn = null;
  var globalVolume = 0.5; // default volume

  function stop() {
    if (audio) { audio.pause(); audio = null; }
    if (activeBtn) { activeBtn.classList.remove("playing"); activeBtn = null; }
  }

  // Create or toggle volume control UI dynamically
  function updateVolumeControl() {
    var container = document.getElementById("voice-volume-control");
    
    // Create it if it doesn't exist
    if (!container) {
      container = document.createElement("div");
      container.id = "voice-volume-control";
      container.title = "음성 재생 볼륨 조절";
      container.innerHTML = `
        <svg class="speaker-icon" viewBox="0 0 24 24">
          <path fill="currentColor" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
        </svg>
        <input type="range" id="voice-volume-slider" min="0" max="1" step="0.05" value="${globalVolume}">
      `;
      document.body.appendChild(container);
  
      var slider = container.querySelector("#voice-volume-slider");
      
      // Load saved volume if any
      var savedVolume = localStorage.getItem("voiceVolume");
      if (savedVolume !== null) {
        globalVolume = parseFloat(savedVolume);
        slider.value = globalVolume;
      }
  
      slider.addEventListener("input", function(e) {
        globalVolume = parseFloat(e.target.value);
        localStorage.setItem("voiceVolume", globalVolume);
        if (audio) {
          audio.volume = globalVolume;
        }
      });
    }

    // Toggle visibility based on presence of .voice-btn
    if (document.querySelector(".voice-btn")) {
      container.style.display = "flex";
    } else {
      container.style.display = "none";
    }
  }

  // MkDocs Material integration for instant navigation
  if (typeof document$ !== "undefined") {
    document$.subscribe(function() {
      updateVolumeControl();
      stop();
    });
  } else {
    // Fallback for non-instant loading
    if (document.readyState === 'loading') {
      document.addEventListener("DOMContentLoaded", updateVolumeControl);
    } else {
      updateVolumeControl();
    }
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".voice-btn");
    if (!btn) return;

    var src = btn.getAttribute("data-src");
    if (!src) return;

    // Toggle off if same button
    if (activeBtn === btn) { stop(); return; }

    stop();
    audio = new Audio(src);
    audio.volume = globalVolume;
    activeBtn = btn;
    btn.classList.add("playing");
    audio.play();
    audio.addEventListener("ended", stop);
    audio.addEventListener("error", stop);
  });
})();
