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

  /* ===== Site Header fijo: estado is-scrolled ===== */
  /* Solo con .site-header--fixed. Al alejarse del tope la barra pasa a fondo inverso (legible sobre las
     secciones claras); en el tope vuelve al velo translúcido sobre la foto del hero. */
  function initSiteHeader() {
    var header = document.querySelector('.site-header--fixed');
    if (!header) { return; }
    var SCROLLED_AFTER = 0.1; // fracción del alto del viewport desde la que se considera «con scroll»

    function update() {
      header.classList.toggle('is-scrolled', window.scrollY > window.innerHeight * SCROLLED_AFTER);
    }
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  }
  initSiteHeader();

  /* ===== Site Nav: submenús del header (desktop) ===== */
  /* Patrón de divulgación: cada botón abre su submenú (aria-expanded) con click o con hover de mouse;
     se cierra con Escape (el foco vuelve al botón), al salir el foco del ítem o con un click afuera.
     Solo un submenú abierto a la vez. */
  function initSiteNav() {
    var triggers = Array.prototype.slice.call(document.querySelectorAll('.site-nav__trigger'));
    if (!triggers.length) { return; }
    var CLOSE_DELAY = 200; // ms de gracia al salir con el mouse, para llegar al panel sin que se cierre

    function setOpen(trigger, open) {
      trigger.setAttribute('aria-expanded', String(open));
      if (!open) { delete trigger.dataset.openedBy; }
    }
    function closeAll(except) {
      triggers.forEach(function (trigger) {
        if (trigger !== except) { setOpen(trigger, false); }
      });
    }

    triggers.forEach(function (trigger) {
      var item = trigger.closest('.site-nav__item');
      var closeTimer = null;

      trigger.addEventListener('click', function () {
        // Si el hover ya lo abrió, el click lo deja abierto (no lo cierra en la cara del usuario)
        if (trigger.dataset.openedBy === 'hover') {
          trigger.dataset.openedBy = 'click';
          return;
        }
        var open = trigger.getAttribute('aria-expanded') !== 'true';
        closeAll(trigger);
        setOpen(trigger, open);
        if (open) { trigger.dataset.openedBy = 'click'; }
      });

      item.addEventListener('pointerenter', function (event) {
        if (event.pointerType !== 'mouse') { return; }
        window.clearTimeout(closeTimer);
        if (trigger.getAttribute('aria-expanded') === 'true') { return; }
        closeAll(trigger);
        setOpen(trigger, true);
        trigger.dataset.openedBy = 'hover';
      });
      item.addEventListener('pointerleave', function (event) {
        if (event.pointerType !== 'mouse') { return; }
        closeTimer = window.setTimeout(function () {
          // Un submenú abierto por click o con el foco adentro no se cierra solo por mover el mouse
          if (trigger.dataset.openedBy === 'hover' && !item.contains(document.activeElement)) {
            setOpen(trigger, false);
          }
        }, CLOSE_DELAY);
      });

      item.addEventListener('focusout', function (event) {
        // Un click en el relleno del panel también saca el foco (relatedTarget null): no cuenta como salir
        if (event.relatedTarget === null && item.matches(':hover')) { return; }
        if (!item.contains(event.relatedTarget)) { setOpen(trigger, false); }
      });
      item.addEventListener('keydown', function (event) {
        if (event.key !== 'Escape' || trigger.getAttribute('aria-expanded') !== 'true') { return; }
        setOpen(trigger, false);
        trigger.focus();
      });
    });

    document.addEventListener('click', function (event) {
      if (!event.target.closest('.site-nav__item')) { closeAll(); }
    });
  }
  initSiteNav();

  /* ===== Off-canvas: menú mobile ===== */
  /* Se abre desde cualquier botón [data-offcanvas-open] con aria-controls apuntando a su id. Abierto:
     el resto de <body> queda inert (el foco no sale del panel), Lenis se detiene y la página no
     scrollea. Se cierra con Escape, el fondo, «Close», un enlace del panel o si el botón que lo abrió
     deja de verse (el header usa container query: el botón «Menu» se oculta cuando entra el menú). */
  function initOffcanvas() {
    var offcanvas = document.querySelector('[data-offcanvas]');
    if (!offcanvas) { return; }
    // Hijo directo de <body>: así un ancestro con transform no lo recorta y el inert es por hermanos
    if (offcanvas.parentElement !== document.body) { document.body.appendChild(offcanvas); }

    var openers = Array.prototype.slice.call(document.querySelectorAll('[data-offcanvas-open][aria-controls="' + offcanvas.id + '"]'));
    var closeButton = offcanvas.querySelector('.offcanvas__close');
    var inerted = [];
    var lastOpener = null;

    function isOpen() { return offcanvas.classList.contains('is-open'); }

    function open(opener) {
      lastOpener = opener || null;
      offcanvas.classList.add('is-open');
      document.documentElement.classList.add('has-offcanvas');
      openers.forEach(function (button) { button.setAttribute('aria-expanded', 'true'); });
      Array.prototype.forEach.call(document.body.children, function (child) {
        if (child !== offcanvas && !child.inert) { child.inert = true; inerted.push(child); }
      });
      if (window.Esonix.lenis) { window.Esonix.lenis.stop(); }
      closeButton.focus();
    }

    function close(returnFocus) {
      if (!isOpen()) { return; }
      offcanvas.classList.remove('is-open');
      document.documentElement.classList.remove('has-offcanvas');
      openers.forEach(function (button) { button.setAttribute('aria-expanded', 'false'); });
      inerted.forEach(function (child) { child.inert = false; });
      inerted = [];
      if (window.Esonix.lenis) { window.Esonix.lenis.start(); }
      if (returnFocus && lastOpener) { lastOpener.focus(); }
    }

    openers.forEach(function (button) {
      button.addEventListener('click', function () { open(button); });
    });
    offcanvas.addEventListener('click', function (event) {
      if (event.target.closest('[data-offcanvas-close]')) { close(true); return; }
      if (event.target.closest('a[href]')) { close(false); }
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && isOpen()) { close(true); }
    });
    // Si al ensanchar la ventana el botón que lo abrió se oculta, se cierra sin devolverle el foco
    window.addEventListener('resize', function () {
      if (isOpen() && lastOpener && !lastOpener.getClientRects().length) { close(false); }
    });
  }
  initOffcanvas();
})();
