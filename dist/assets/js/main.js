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

  /* ===== Carousel (Swiper) ===== */
  /* Cada [data-carousel] se inicia al acercarse al viewport. El slide activo va centrado. Flechas: botones
     [data-carousel-prev] / [data-carousel-next] con aria-controls = id del carrusel, en cualquier lugar de
     la página. Dots: un .dots[data-carousel-dots] dentro del carrusel; main.js crea un botón por slide y
     el valor del atributo es el prefijo de su nombre («Show story» → «Show story 3»).
     Slide inicial: data-carousel-start (índice desde 0; por defecto 0) y, si el carrusel mide 64rem o más
     (3 por vista), data-carousel-start-wide. data-carousel-highlight: la card del slide activo recibe
     data-surface="brand" y las demás lo pierden (el markup trae destacada la inicial, el estado sin JS).
     Copias: con el activo centrado se ven a la vez hasta 5 slides (3 enteros y 2 parciales) y el loop de
     Swiper necesita uno de repuesto para que no quede un hueco en un costado durante la transición. Si hay
     menos de MIN_SLIDES, main.js duplica la tanda completa (así el orden del loop no se altera); las copias
     van con aria-hidden e inert, y el nombre «N of M», los dots y el destacado cuentan solo los originales. */
  var MIN_SLIDES = 6;
  var rootStyle = getComputedStyle(document.documentElement);
  function tokenRem(name) { return parseFloat(rootStyle.getPropertyValue(name)) || 0; }

  function initCarousel(carousel) {
    var viewport = carousel.querySelector('.carousel__viewport');
    var rem = parseFloat(rootStyle.fontSize);
    // Mismos pasos que el container query de .carousel en main.css (slides por vista y separación)
    var gapSm = tokenRem('--spacing-5') * rem;
    var gapMd = tokenRem('--spacing-6') * rem;
    var breakpoints = {};
    breakpoints[48 * rem] = { slidesPerView: 2, spaceBetween: gapMd };
    breakpoints[64 * rem] = { slidesPerView: 3, spaceBetween: gapMd };

    // Nombre de cada slide antes de copiar: «N of M» sobre los originales (reemplaza al del módulo a11y)
    var wrapper = viewport.querySelector('.swiper-wrapper');
    var originals = Array.prototype.slice.call(wrapper.children);
    var count = originals.length;
    originals.forEach(function (slide, index) {
      slide.setAttribute('aria-label', (index + 1) + ' of ' + count);
    });
    if (count > 1 && count < MIN_SLIDES) {
      originals.forEach(function (slide) {
        var copy = slide.cloneNode(true);
        copy.removeAttribute('aria-label');
        copy.setAttribute('aria-hidden', 'true');
        copy.inert = true;
        copy.querySelectorAll('[id]').forEach(function (element) { element.removeAttribute('id'); });
        wrapper.appendChild(copy);
      });
    }

    var wide = carousel.getBoundingClientRect().width >= 64 * rem;
    var start = Number(carousel.getAttribute('data-carousel-start')) || 0;
    if (wide && carousel.hasAttribute('data-carousel-start-wide')) {
      start = Number(carousel.getAttribute('data-carousel-start-wide')) || 0;
    }

    var swiper = new window.Swiper(viewport, {
      loop: true,
      centeredSlides: true,
      initialSlide: start,
      speed: parseFloat(rootStyle.getPropertyValue('--ease-slow')) || 0, // 420 ms; 0 con reducir movimiento
      grabCursor: true,
      slidesPerView: 1,
      spaceBetween: gapSm,
      breakpointsBase: 'container',
      breakpoints: breakpoints,
      keyboard: { enabled: true, onlyInViewport: true },
      a11y: {
        enabled: true,
        slideRole: 'group',
        itemRoleDescriptionMessage: 'slide',
        slideLabelMessage: '' // el nombre «N of M» lo pone main.js sin contar las copias
      }
    });
    var total = swiper.slides.length; // originales + copias
    // Índice del original (0 a count - 1) que corresponde al slide activo, sea original o copia
    function activeOriginal() { return swiper.realIndex % count; }

    // Destacado del slide activo. En loop, Swiper reordena los slides: se compara el índice original
    // (data-swiper-slide-index) con realIndex, no la posición en el DOM.
    if (carousel.hasAttribute('data-carousel-highlight')) {
      var syncHighlight = function () {
        swiper.slides.forEach(function (slide) {
          var card = slide.firstElementChild;
          if (!card) { return; }
          if (Number(slide.getAttribute('data-swiper-slide-index')) === swiper.realIndex) {
            card.setAttribute('data-surface', 'brand');
          } else {
            card.removeAttribute('data-surface');
          }
        });
      };
      swiper.on('realIndexChange', syncHighlight);
      syncHighlight();
    }

    if (carousel.id) {
      document.querySelectorAll('[data-carousel-prev][aria-controls="' + carousel.id + '"]').forEach(function (button) {
        button.addEventListener('click', function () { swiper.slidePrev(); });
      });
      document.querySelectorAll('[data-carousel-next][aria-controls="' + carousel.id + '"]').forEach(function (button) {
        button.addEventListener('click', function () { swiper.slideNext(); });
      });
    }

    var dots = carousel.querySelector('[data-carousel-dots]');
    if (dots) {
      var label = dots.getAttribute('data-carousel-dots') || 'Show slide';
      for (var i = 0; i < count; i += 1) {
        var dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'dots__dot';
        dot.setAttribute('aria-label', label + ' ' + (i + 1));
        dot.dataset.index = String(i);
        dots.appendChild(dot);
      }
      dots.addEventListener('click', function (event) {
        var dot = event.target.closest('.dots__dot');
        if (!dot) { return; }
        // Con copias, cada original aparece dos veces en el loop: se va al ejemplar más cercano
        var target = Number(dot.dataset.index);
        var best = target;
        for (var copyIndex = target; copyIndex < total; copyIndex += count) {
          var distance = Math.abs(copyIndex - swiper.realIndex);
          var bestDistance = Math.abs(best - swiper.realIndex);
          if (Math.min(distance, total - distance) < Math.min(bestDistance, total - bestDistance)) { best = copyIndex; }
        }
        swiper.slideToLoop(best);
      });
      var syncDots = function () {
        Array.prototype.forEach.call(dots.children, function (dot, index) {
          if (index === activeOriginal()) { dot.setAttribute('aria-current', 'true'); } else { dot.removeAttribute('aria-current'); }
        });
      };
      swiper.on('realIndexChange', syncDots);
      syncDots();
    }
  }

  function initCarousels() {
    var carousels = document.querySelectorAll('[data-carousel]');
    if (!carousels.length || typeof window.Swiper !== 'function') { return; }
    carousels.forEach(function (carousel) { whenVisible(carousel, initCarousel); });
  }
  initCarousels();

  /* ===== Video Modal ===== */
  /* Cualquier botón con data-video-id (y opcional data-video-title) abre el <dialog data-video-modal>.
     El iframe se crea recién en ese click, así la página no carga YouTube al abrirse, y se quita al
     cerrar para cortar la reproducción. */
  function initVideoModal() {
    var modal = document.querySelector('[data-video-modal]');
    if (!modal || typeof modal.showModal !== 'function') { return; }
    // Hijo directo de <body>: un ancestro con display: none (demo del kit) no lo dejaría mostrarse
    if (modal.parentElement !== document.body) { document.body.appendChild(modal); }
    var frame = modal.querySelector('.video-modal__frame');
    var title = modal.querySelector('.video-modal__title');

    document.addEventListener('click', function (event) {
      var opener = event.target.closest('[data-video-id]');
      if (!opener) { return; }
      event.preventDefault();
      var name = opener.getAttribute('data-video-title') || 'Video';
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(opener.getAttribute('data-video-id')) + '?autoplay=1&rel=0';
      iframe.title = name;
      iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; // incluye pantalla completa
      iframe.referrerPolicy = 'strict-origin-when-cross-origin'; // YouTube rechaza el embed sin referrer
      title.textContent = name;
      frame.replaceChildren(iframe);
      modal.showModal();
      if (window.Esonix.lenis) { window.Esonix.lenis.stop(); }
    });

    modal.addEventListener('click', function (event) {
      // El click en el ::backdrop llega con el propio <dialog> como target
      if (event.target === modal || event.target.closest('[data-video-close]')) { modal.close(); }
    });
    modal.addEventListener('close', function () {
      frame.replaceChildren();
      if (window.Esonix.lenis) { window.Esonix.lenis.start(); }
    });
  }
  initVideoModal();

  /* ===== Word List: bloque Finance / Advisory / Growth / Strategy ===== */
  /* Sin pin: cada palabra dispara un ScrollTrigger propio cuando su centro cruza el centro del viewport
     (una franja angosta, 60%–40% de alto) y marca como activos a ella y a su Card Project (data-word-for
     = id de la card). onEnter cubre bajar, onEnterBack cubre subir; nunca hay dos activas a la vez porque
     setActive() desactiva el resto. Sin «reducir movimiento» (o sin GSAP/ScrollTrigger) queda el estado
     del markup, que ya trae Growth activa como el diseño. */
  function initWordList() {
    var lists = document.querySelectorAll('[data-word-list]');
    if (!lists.length || reducedMotion.matches || !window.gsap || !window.ScrollTrigger) { return; }

    function initOne(list) {
      var words = Array.prototype.slice.call(list.querySelectorAll('.word-list__word'));
      if (words.length < 2) { return; }

      function setActive(word) {
        words.forEach(function (w) {
          var active = w === word;
          w.classList.toggle('is-active', active);
          var card = document.getElementById(w.getAttribute('data-word-for'));
          if (card) { card.classList.toggle('is-active', active); }
        });
      }
      words.forEach(function (word) {
        window.ScrollTrigger.create({
          trigger: word,
          start: 'center 60%',
          end: 'center 40%',
          onEnter: function () { setActive(word); },
          onEnterBack: function () { setActive(word); }
        });
      });
    }
    lists.forEach(function (list) { whenVisible(list, initOne); });
  }
  initWordList();

  /* ===== Pricing: switch mensual / anual ===== */
  /* El switch de [data-pricing] cambia el texto de cada [data-price-monthly][data-price-annual] de la
     misma sección. La región role="status" anuncia el cambio solo cuando el usuario mueve el switch (no
     al cargar). Sin JS quedan los precios mensuales del markup. */
  function initPricingSwitch() {
    document.querySelectorAll('[data-pricing]').forEach(function (billing) {
      var toggle = billing.querySelector('input[role="switch"]');
      var status = billing.querySelector('[data-pricing-status]');
      var scope = billing.closest('section') || document;
      var prices = scope.querySelectorAll('[data-price-monthly][data-price-annual]');
      if (!toggle || !prices.length) { return; }

      function update(announce) {
        var annual = toggle.checked;
        prices.forEach(function (price) {
          price.textContent = price.getAttribute(annual ? 'data-price-annual' : 'data-price-monthly');
        });
        if (announce && status) {
          status.textContent = annual ? 'Showing annual prices, 30% off.' : 'Showing monthly prices.';
        }
      }
      toggle.addEventListener('change', function () { update(true); });
      update(false); // el navegador puede restaurar el switch marcado al volver atrás
    });
  }
  initPricingSwitch();
})();
