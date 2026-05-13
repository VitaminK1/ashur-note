// lore.js — generic slider initialization for lore/battle cards
(function(){
  'use strict'

  function parseJSON(el, attr){
    try{
      const value = el.getAttribute(attr)
      return value ? JSON.parse(value) : null
    }catch(e){
      return null
    }
  }

  function getTarget(el, attr){
    const id = el.getAttribute(attr)
    return id ? document.getElementById(id) : null
  }

  function setBackgroundFill(slider, val){
    const min = Number(slider.min) || 0
    const max = Number(slider.max) || 100
    const pct = Math.round(((val - min) / (max - min)) * 100)
    const cs = getComputedStyle(slider)
    const fill = cs.getPropertyValue('--lore-fill') || '#6ff0c8'
    const unfilled = cs.getPropertyValue('--lore-unfilled') || 'rgba(255,255,255,0.06)'
    slider.style.background = `linear-gradient(90deg, ${fill.trim()} ${pct}%, ${unfilled.trim()} ${pct}%)`
  }

  function initSlider(slider){
    if(!slider || slider.dataset.loreInited) return null
    slider.dataset.loreInited = '1'

    const levelEl = getTarget(slider, 'data-level-target')
    const seriesMap = parseJSON(slider, 'data-lore-series') || {}
    const levelPrefix = slider.getAttribute('data-level-prefix') || 'Lv.'
    const seriesTargets = Object.entries(seriesMap).map(([id, values]) => {
      const el = document.getElementById(id)
      return {
        values,
        el,
        fallback: el ? el.textContent.trim() : '',
      }
    })

    function update(){
      const min = Number(slider.min) || 0
      const val = Number(slider.value)
      const index = val - min

      if(levelEl) levelEl.textContent = `${levelPrefix}${val}`

      seriesTargets.forEach(target => {
        if(!target.el) return
        if(Array.isArray(target.values) && target.values[index] !== undefined) target.el.textContent = target.values[index]
        else if(target.fallback) target.el.textContent = target.fallback
      })

      setBackgroundFill(slider, val)
    }

    slider.addEventListener('input', update, {passive:true})
    update()
    return { slider, update }
  }

  function initAllSliders(root){
    const scope = root && root.querySelectorAll ? root : document
    const sliders = []

    if(root instanceof HTMLElement && root.matches('input[data-lore-slider]')){
      sliders.push(root)
    }

    scope.querySelectorAll('input[data-lore-slider]').forEach(slider => sliders.push(slider))
    sliders.forEach(initSlider)
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', () => initAllSliders(document))
  } else {
    initAllSliders(document)
  }

  const observer = new MutationObserver((mutations) => {
    for(const mutation of mutations){
      for(const node of mutation.addedNodes){
        if(!(node instanceof HTMLElement)) continue
        if(node.matches('input[data-lore-slider]') || node.querySelector('input[data-lore-slider]')){
          initAllSliders(node)
        }
      }
    }
  })

  observer.observe(document.body, { childList: true, subtree: true })
  window.addEventListener('pageshow', () => initAllSliders(document))
  window.addEventListener('popstate', () => initAllSliders(document))
})()
