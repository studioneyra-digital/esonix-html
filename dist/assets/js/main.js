/*
 * Esonix — JS del theme. Vanilla, cargado con `defer`.
 * Cada componente con comportamiento agrega su propio bloque comentado con su nombre.
 * Los efectos pesados (GSAP, Swiper) se inicializan con IntersectionObserver al entrar al
 * viewport, no en DOMContentLoaded (docs/stack.md, "Equivalente a islands"). Sus librerías tampoco
 * van en el HTML: las pide requireLib() (ver "Carga diferida de librerías").
 */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* ===== Utilidades compartidas ===== */

  /* Inicializa `init(element)` recién cuando el elemento se acerca al viewport (una sola vez).
     `margin`: distancia de anticipación (rootMargin); por defecto 200px. */
  function whenVisible(element, init, margin) {
    if (!('IntersectionObserver' in window)) { init(element); return; }
    var observer = new IntersectionObserver(function (entries, obs) {
      if (!entries[0].isIntersecting) { return; }
      obs.disconnect();
      init(element);
    }, { rootMargin: margin || '200px' });
    observer.observe(element);
  }

  /* Carga diferida de librerías: GSAP + ScrollTrigger (≈ 46 KB gzip) y Swiper (≈ 44 KB) no van como
     <script> en la página: con ellas en el HTML compiten por la red con la foto del hero y el LCP mobile
     sube ~370 ms (Lighthouse, 4G simulada; Etapa 4 · Grupo D). Se piden cuando el primer componente
     que las usa está a una pantalla de distancia (preloadLib), así llegan antes de que se vea; no en el
     evento load, que en una conexión rápida cae antes del LCP y Lighthouse las cuenta igual. Si la
     página ya las trae con <script> (el kit carga Swiper), se usan esas. Salen de la carpeta de main.js. */
  var scriptBase = document.currentScript ? document.currentScript.src.replace(/[^/]*$/, '') : '';
  var scriptPromises = {};
  function loadScript(file) {
    if (!scriptPromises[file]) {
      scriptPromises[file] = new Promise(function (resolve, reject) {
        var script = document.createElement('script');
        script.src = scriptBase + file;
        script.async = false; // las inyectadas juntas se ejecutan en orden (ScrollTrigger después de GSAP)
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }
    return scriptPromises[file];
  }
  var libs = {
    gsap: {
      ready: function () { return Boolean(window.gsap && window.ScrollTrigger); },
      files: ['gsap.min.js', 'ScrollTrigger.min.js'],
      setup: function () {
        window.gsap.registerPlugin(window.ScrollTrigger);
        // Lenis mueve el scroll real: ScrollTrigger se actualiza con su evento (docs/stack.md)
        if (window.Esonix.lenis) { window.Esonix.lenis.on('scroll', window.ScrollTrigger.update); }
      }
    },
    swiper: {
      ready: function () { return typeof window.Swiper === 'function'; },
      files: ['swiper-bundle.min.js'],
      setup: function () {}
    }
  };
  var libPromises = {};
  // Promesa que se cumple con la librería lista; se rechaza si no carga (el componente queda sin JS)
  function requireLib(name) {
    if (!libPromises[name]) {
      var lib = libs[name];
      var loading = lib.ready() ? Promise.resolve() : Promise.all(lib.files.map(loadScript));
      libPromises[name] = loading.then(lib.setup);
    }
    return libPromises[name];
  }
  // Precarga con una pantalla de anticipación sobre el primer componente que la usa
  var PRELOAD_MARGIN = '100% 0px';
  function preloadLib(name, selector) {
    var first = document.querySelector(selector);
    if (!first) { return; }
    whenVisible(first, function () { requireLib(name).catch(function () {}); }, PRELOAD_MARGIN);
  }
  window.Esonix = { whenVisible: whenVisible, requireLib: requireLib, lenis: null };

  /* ===== Scroll suave: Lenis + ScrollTrigger ===== */
  /* Lenis solo se carga en las páginas del sitio (no en /kit). Sin "reducir movimiento":
     con la preferencia activa queda el scroll nativo. Lenis corre en su propio requestAnimationFrame
     desde el inicio; GSAP llega después (carga diferida) y su setup suscribe ScrollTrigger al scroll
     de Lenis. */
  function initSmoothScroll() {
    if (typeof window.Lenis !== 'function' || reducedMotion.matches) { return; }
    var lenis = new window.Lenis();
    window.Esonix.lenis = lenis;
    var raf = function (time) {
      lenis.raf(time);
      window.requestAnimationFrame(raf);
    };
    window.requestAnimationFrame(raf);
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
     van con aria-hidden e inert, y el nombre «N of M», los dots y el destacado cuentan solo los originales.
     Teclado: solo los slides enteros en pantalla entran en el orden de Tab. Con loop, que el foco deslice
     el carrusel (scrollOnFocus de Swiper) reordena los slides en el DOM y el Tab no sale nunca (trampa de
     foco); los controles de los demás van con tabindex="-1" y se llega a ellos con flechas, dots o teclado.
     data-carousel-fade: un slide por vista con fundido (effect: 'fade'); sin copias, porque el fundido no
     muestra vecinos. */
  var MIN_SLIDES = 6;
  var SLIDE_FOCUSABLE = 'a[href], button, input, select, textarea';
  var rootStyle = getComputedStyle(document.documentElement);
  function tokenRem(name) { return parseFloat(rootStyle.getPropertyValue(name)) || 0; }

  function initCarousel(carousel) {
    var viewport = carousel.querySelector('.carousel__viewport');
    var fade = carousel.hasAttribute('data-carousel-fade');
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
    if (!fade && count > 1 && count < MIN_SLIDES) {
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

    var options = {
      loop: true,
      centeredSlides: !fade,
      initialSlide: start,
      speed: parseFloat(rootStyle.getPropertyValue('--ease-slow')) || 0, // 420 ms; 0 con reducir movimiento
      grabCursor: true,
      slidesPerView: 1,
      spaceBetween: fade ? 0 : gapSm,
      breakpointsBase: 'container',
      breakpoints: fade ? {} : breakpoints,
      watchSlidesProgress: true, // marca .swiper-slide-fully-visible (orden de Tab)
      keyboard: { enabled: true, onlyInViewport: true },
      a11y: {
        enabled: true,
        scrollOnFocus: false,
        slideRole: 'group',
        itemRoleDescriptionMessage: 'slide',
        slideLabelMessage: '' // el nombre «N of M» lo pone main.js sin contar las copias
      }
    };
    if (fade) {
      options.effect = 'fade';
      options.fadeEffect = { crossFade: true };
    }
    var swiper = new window.Swiper(viewport, options);
    var total = swiper.slides.length; // originales + copias

    // Orden de Tab: tabindex="-1" (no inert) para que el lector de pantalla siga leyendo todos los slides.
    // Supone que el contenido de los slides no trae tabindex propio.
    var syncTabStops = function () {
      swiper.slides.forEach(function (slide) {
        if (slide.inert) { return; } // copias
        var hidden = !slide.classList.contains('swiper-slide-fully-visible');
        slide.querySelectorAll(SLIDE_FOCUSABLE).forEach(function (element) {
          if (hidden) { element.setAttribute('tabindex', '-1'); } else { element.removeAttribute('tabindex'); }
        });
      });
    };
    swiper.on('transitionEnd', syncTabStops);
    swiper.on('resize', syncTabStops);
    syncTabStops();
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
    if (!carousels.length) { return; }
    preloadLib('swiper', '[data-carousel]');
    carousels.forEach(function (carousel) {
      whenVisible(carousel, function () {
        // Si Swiper no carga, queda el estado sin JS: fila con scroll horizontal nativo
        requireLib('swiper').then(function () { initCarousel(carousel); }, function () {});
      });
    });
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
    var lastOpener = null; // para devolver el foco al cerrar

    document.addEventListener('click', function (event) {
      var opener = event.target.closest('[data-video-id]');
      if (!opener) { return; }
      event.preventDefault();
      lastOpener = opener;
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
      // Con teclado, <dialog> devuelve el foco solo; abierto con el ratón el botón nunca lo tuvo y el
      // foco cae en <body>. Lo devolvemos siempre al botón (en el caso del teclado es donde ya estaba),
      // después de que el navegador termine su propia restauración.
      if (lastOpener && lastOpener.isConnected) {
        requestAnimationFrame(function () { lastOpener.focus(); });
      }
    });
  }
  initVideoModal();

  /* ===== Word List: bloque Finance / Advisory / Growth / Strategy ===== */
  /* Sin pin: cada palabra dispara un ScrollTrigger propio cuando su centro cruza el centro del viewport
     (una franja angosta, 60%–40% de alto) y marca como activos a ella y a su Card Project (data-word-for
     = id de la card). onEnter cubre bajar, onEnterBack cubre subir; nunca hay dos activas a la vez porque
     setActive() desactiva el resto. Con «reducir movimiento» (o si GSAP no carga) queda el estado del
     markup, que ya trae Growth activa como el diseño; en ese caso GSAP ni siquiera se pide. */
  function initWordList() {
    var lists = document.querySelectorAll('[data-word-list]');
    if (!lists.length || reducedMotion.matches) { return; }
    preloadLib('gsap', '[data-word-list]');

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
    lists.forEach(function (list) {
      whenVisible(list, function () {
        requireLib('gsap').then(function () { initOne(list); }, function () {});
      });
    });
  }
  initWordList();

  /* ===== Motion: revelado al entrar en el viewport y contadores ===== */
  /* docs/interaction-motion.md §2. Observa los [data-reveal] y [data-count] que están dentro de .has-reveal
     (la clase la pone el <head> en <html>; en el kit, el contenedor de la demo). Al entrar, el elemento
     recibe is-revealed (la animación es CSS) y el contador arranca. Los que entran en el mismo cuadro se
     escalonan en orden del DOM con --reveal-order, hasta REVEAL_MAX_ORDER pasos. Los que ya quedaron arriba
     del viewport (recarga a mitad de página, salto a un ancla) se muestran sin desfase. Con «reducir
     movimiento» o sin IntersectionObserver el CSS no oculta nada y los contadores quedan con el valor del
     markup. */
  var REVEAL_SELECTOR = '.has-reveal [data-reveal], .has-reveal [data-count]';
  var REVEAL_MAX_ORDER = 6;
  var REVEAL_MARGIN = '0px 0px -10% 0px'; // se activa al pasar el 10 % inferior del viewport
  function tokenMs(name) { return parseFloat(rootStyle.getPropertyValue(name)) || 0; }

  // Cuenta de 0 a target con ease-out; render(valor) pinta cada paso
  function animateCount(target, render, delay) {
    var duration = tokenMs('--duration-count');
    var start = null;
    function step(time) {
      if (start === null) { start = time; }
      var t = duration > 0 ? Math.min((time - start) / duration, 1) : 1;
      render(target * (1 - Math.pow(1 - t, 4)));
      if (t < 1) { window.requestAnimationFrame(step); }
    }
    window.setTimeout(function () { window.requestAnimationFrame(step); }, delay);
  }

  /* Prepara un contador y devuelve la función que lo arranca (o null si el markup no tiene número).
     - .progress: anima el <progress> y el texto del porcentaje. --progress no se toca: la fila del
       porcentaje queda en su lugar final (si se encogiera con el relleno, la etiqueta se partiría en dos
       líneas a mitad de la cuenta y movería el layout) y el relleno llega hasta ella.
     - Cualquier otro (.stat__value): el número del primer nodo de texto («98%», «12K», «3M») pasa a un
       span aria-hidden que cuenta; el lector de pantalla lee el valor final de un texto oculto. Al
       arrancar se mide el ancho del valor final y se reserva, así el sufijo no se mueve. */
  function setupCount(el) {
    if (el.classList.contains('progress')) {
      var bar = el.querySelector('progress');
      var label = el.querySelector('.progress__head [aria-hidden="true"]');
      if (!bar) { return null; }
      var goal = Number(bar.value);
      var unit = label ? label.textContent.replace(/^[\d.,\s]+/, '') : '';
      var renderBar = function (value) {
        var n = Math.round(value);
        bar.value = n;
        if (label) { label.textContent = n + unit; }
      };
      renderBar(0);
      return function (delay) { animateCount(goal, renderBar, delay); };
    }

    var node = el.firstChild;
    var match = node && node.nodeType === 3 ? /^\s*(\d[\d,]*(?:\.\d+)?)(.*?)\s*$/.exec(node.nodeValue) : null;
    if (!match) { return null; }
    var source = match[1];
    var rest = match[2];
    var decimals = (source.split('.')[1] || '').length;
    var grouped = source.indexOf(',') !== -1;
    var target = parseFloat(source.replace(/,/g, ''));
    var format = function (value) {
      return grouped
        ? value.toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals })
        : value.toFixed(decimals);
    };
    var display = document.createElement('span');
    display.className = 'count__display';
    display.setAttribute('aria-hidden', 'true');
    var spoken = document.createElement('span');
    spoken.className = 'visually-hidden';
    spoken.textContent = source + rest;
    el.replaceChild(display, node);
    el.insertBefore(spoken, display.nextSibling);
    var render = function (value) { display.textContent = format(value) + rest; };
    render(0);
    return function (delay) {
      // Medido recién al arrancar: la fuente ya cargó. Valor final, medida y vuelta a 0 en el mismo cuadro.
      render(target);
      display.style.minInlineSize = display.getBoundingClientRect().width + 'px';
      render(0);
      animateCount(target, render, delay);
    };
  }

  function initReveal() {
    var items = Array.prototype.slice.call(document.querySelectorAll(REVEAL_SELECTOR));
    if (!items.length) { return; }
    if (reducedMotion.matches || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('is-revealed'); });
      return;
    }
    var stagger = tokenMs('--reveal-stagger');
    var counters = new Map();
    items.forEach(function (el) {
      if (!el.hasAttribute('data-count')) { return; }
      var start = setupCount(el);
      if (start) { counters.set(el, start); }
    });

    function reveal(el, order) {
      if (el.hasAttribute('data-reveal')) {
        el.style.setProperty('--reveal-order', order);
        el.classList.add('is-revealed');
      }
      var start = counters.get(el);
      if (!start) { return; }
      counters.delete(el);
      // Un contador dentro de un bloque que entra arranca con el desfase de ese bloque
      var host = el.closest('[data-reveal]');
      var hostOrder = host ? Number(host.style.getPropertyValue('--reveal-order')) || 0 : 0;
      start(hostOrder * stagger);
    }

    var observer = new IntersectionObserver(function (entries) {
      var order = 0;
      entries.forEach(function (entry) {
        var el = entry.target;
        if (entry.isIntersecting) {
          observer.unobserve(el);
          reveal(el, Math.min(order, REVEAL_MAX_ORDER));
          if (el.hasAttribute('data-reveal')) { order += 1; }
        } else if (entry.boundingClientRect.bottom <= 0) {
          observer.unobserve(el);
          reveal(el, 0);
        }
      });
    }, { rootMargin: REVEAL_MARGIN });
    items.forEach(function (el) { observer.observe(el); });

    // El foco por teclado nunca cae en algo invisible: si entra a un bloque oculto, se revela en el acto
    document.addEventListener('focusin', function (event) {
      var el = event.target.closest && event.target.closest('.has-reveal [data-reveal]:not(.is-revealed)');
      if (!el) { return; }
      observer.unobserve(el);
      reveal(el, 0);
    });
  }
  initReveal();

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

  /* ===== Quote Form: envío por FormSubmit sin salir de la página ===== */
  /* Sin JS el <form> se envía normal a su action (FormSubmit muestra su página de agradecimiento). Con JS:
     validación propia (mensaje bajo cada campo, aria-invalid y foco al primer error), envío por fetch a la
     variante /ajax/ del mismo action y estados enviando / enviado / error, anunciados en las regiones
     role="status" y role="alert" del formulario. Para cambiar el destino se edita el action del HTML.
     Mientras envía, el botón queda con aria-disabled (no disabled: así no pierde el foco). */
  var FORM_MESSAGES = {
    valueMissing: 'This field is required.',
    selectMissing: 'Choose an option.',
    typeMismatch: 'Enter a valid email address.',
    patternMismatch: 'Enter a valid phone number.',
    sending: 'Sending…',
    sent: 'Thanks! Your message was sent. We will get back to you soon.',
    failed: 'Your message could not be sent. Please check your connection and try again.'
  };

  function fieldError(control) {
    if (control.validity.valueMissing) { return control.tagName === 'SELECT' ? FORM_MESSAGES.selectMissing : FORM_MESSAGES.valueMissing; }
    if (control.validity.typeMismatch) { return FORM_MESSAGES.typeMismatch; }
    if (control.validity.patternMismatch) { return FORM_MESSAGES.patternMismatch; }
    return '';
  }

  // https://formsubmit.co/<destino> → https://formsubmit.co/ajax/<destino>
  function ajaxEndpoint(action) {
    var url = new URL(action, window.location.href);
    if (url.hostname === 'formsubmit.co' && url.pathname.indexOf('/ajax/') !== 0) {
      url.pathname = '/ajax' + url.pathname;
    }
    return url.href;
  }

  function initQuoteForms() {
    document.querySelectorAll('[data-quote-form]').forEach(function (form) {
      var controls = Array.prototype.slice.call(form.querySelectorAll('.field__control'));
      var status = form.querySelector('[data-form-status]');
      var alertRegion = form.querySelector('[data-form-alert]');
      var submit = form.querySelector('[type="submit"]');
      var submitLabel = submit.querySelector('[data-submit-label]');
      var idleLabel = submitLabel.textContent;
      var sending = false;

      // Escribe (o borra) el error de un campo; devuelve true si es válido
      function validate(control) {
        var message = fieldError(control);
        var error = document.getElementById(control.id + '-error');
        if (message) { control.setAttribute('aria-invalid', 'true'); } else { control.removeAttribute('aria-invalid'); }
        if (error) { error.textContent = message; }
        return !message;
      }

      // El error se revisa mientras se corrige, no antes del primer envío
      controls.forEach(function (control) {
        ['input', 'change'].forEach(function (type) {
          control.addEventListener(type, function () {
            if (control.getAttribute('aria-invalid') === 'true') { validate(control); }
          });
        });
      });

      function setSending(value) {
        sending = value;
        if (value) { submit.setAttribute('aria-disabled', 'true'); } else { submit.removeAttribute('aria-disabled'); }
        submitLabel.textContent = value ? FORM_MESSAGES.sending : idleLabel;
      }

      form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (sending) { return; }
        status.textContent = '';
        alertRegion.textContent = '';
        var invalid = controls.filter(function (control) { return !validate(control); });
        if (invalid.length) { invalid[0].focus(); return; }

        setSending(true);
        fetch(ajaxEndpoint(form.action), {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(Object.fromEntries(new FormData(form)))
        }).then(function (response) {
          return response.json().catch(function () { return {}; }).then(function (data) {
            // FormSubmit responde success "true" / "false" como texto
            if (!response.ok || String(data.success) !== 'true') { throw new Error(data.message || String(response.status)); }
          });
        }).then(function () {
          form.reset();
          status.textContent = FORM_MESSAGES.sent;
        }).catch(function () {
          alertRegion.textContent = FORM_MESSAGES.failed;
        }).then(function () {
          setSending(false);
        });
      });
    });
  }
  initQuoteForms();
})();
