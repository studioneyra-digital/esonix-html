/*
 * Esonix — JS del theme. Vanilla, cargado con `defer`.
 * Cada componente con comportamiento agrega su propio bloque comentado con su nombre.
 * Los efectos pesados (GSAP, Swiper) se inicializan con IntersectionObserver al entrar al
 * viewport, no en DOMContentLoaded (docs/stack.md, "Equivalente a islands").
 */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ===== Utilidades compartidas ===== */

  /* Inicializa `init(element)` recién cuando el elemento se acerca al viewport (una sola vez) */
  function whenVisible(element, init) {
    if (!('IntersectionObserver' in window)) { init(element); return; }
    var observer = new IntersectionObserver(function (entries, obs) {
      if (!entries[0].isIntersecting) { return; }
      obs.disconnect();
      init(element);
    }, { rootMargin: '200px' });
    observer.observe(element);
  }
  window.Esonix = { whenVisible: whenVisible, lenis: null };

  /* ===== Scroll suave: Lenis + ScrollTrigger ===== */
  /* Lenis solo se carga en las páginas del sitio (no en /kit). Sin "reducir movimiento":
     con la preferencia activa queda el scroll nativo. */
  function initSmoothScroll() {
    if (typeof window.Lenis !== 'function' || reducedMotion.matches) { return; }
    var lenis = new window.Lenis();
    window.Esonix.lenis = lenis;

    if (window.gsap && window.ScrollTrigger) {
      // ScrollTrigger escucha el scroll de Lenis y ambos comparten el ticker de GSAP
      window.gsap.registerPlugin(window.ScrollTrigger);
      lenis.on('scroll', window.ScrollTrigger.update);
      window.gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      window.gsap.ticker.lagSmoothing(0);
    } else {
      var raf = function (time) {
        lenis.raf(time);
        window.requestAnimationFrame(raf);
      };
      window.requestAnimationFrame(raf);
    }
  }
  initSmoothScroll();

  /* ===== Scroll Top ===== */
  /* Aparece al pasar media pantalla; el anillo dibuja el avance del scroll (--scroll-progress, 0–100) */
  function initScrollTop() {
    var button = document.querySelector('.scroll-top');
    if (!button) { return; }
    var SHOW_AFTER = 0.5; // fracción del alto del viewport desde la que se muestra

    function update() {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      var progress = max > 0 ? Math.min(window.scrollY / max, 1) * 100 : 0;
      button.style.setProperty('--scroll-progress', progress.toFixed(1));
      button.classList.toggle('is-visible', window.scrollY > window.innerHeight * SHOW_AFTER);
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();

    button.addEventListener('click', function () {
      if (window.Esonix.lenis) {
        window.Esonix.lenis.scrollTo(0);
      } else {
        window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
      }
      // El botón se oculta al llegar arriba: el foco pasa al <body> para que Tab arranque desde el inicio
      document.body.setAttribute('tabindex', '-1');
      document.body.focus({ preventScroll: true });
      document.body.addEventListener('blur', function release() {
        document.body.removeAttribute('tabindex');
        document.body.removeEventListener('blur', release);
      });
    });
  }
  initScrollTop();
})();
