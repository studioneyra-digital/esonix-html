# Agrega el bloque CSS de los organismos a main.css (idempotente: reemplaza entre organisms:start / organisms:end).
# El JS de cada organismo vive en main.js y se edita a mano (ver README).
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
MAIN = str(ROOT / 'dist' / 'assets' / 'css' / 'main.css')

CSS = r'''/* organisms:start */
/* ===== Organismos ===== */

/* Site Header — barra translúcida sobre la foto del hero: logo, menú en píldora blanca, redes en texto
   y teléfono, repartidos con space-between como en el diseño. Por defecto es un bloque normal: la Section decide si
   va superpuesto al hero. Responde al ancho de SU contenedor (container query), no al del viewport: la
   barra completa necesita ~1150px y el header no sabe en qué columna vive (container del hero, kit).
   Umbrales = breakpoints del theme medidos sobre el ancho del header:
   - < 48rem: logo y «Menu», que abre el Off-canvas.
   - ≥ 48rem: menú en píldora y círculo del chat (el número queda solo para lectores).
   - ≥ 64rem: aparece el número de teléfono.  - ≥ 80rem: aparecen las redes (también están en el footer).
   El velo y el borde no son un token de superficie porque el fondo es la foto: velo blanco al 10%
   (--color-overlay-light) y borde blanco al 30%, medidos en el diseño.
   --fixed lo deja fijo arriba (decisión del equipo, «por el momento»): ocupa el ancho de la ventana hasta
   --site-header-max, centrado, y no tapa los clics de la página en el margen que rodea la barra. Como el
   texto es blanco, sobre las secciones claras no se lee con el velo: main.js agrega is-scrolled al
   alejarse del tope y la barra pasa a fondo inverso. Ese estado no está en el diseño: se deriva de tokens.
   La Section que lo use reserva el espacio de arriba y define scroll-padding-top para los anclajes. */
.site-header {
  --site-header-max: 104rem; /* barra de 1620px del diseño a 1920px + el margen de cada lado */
  position: relative; /* bloque contenedor de los textos ocultos (absolutos): container-type no lo es */
  container: site-header / inline-size;
  --color-border-focus: var(--color-border-focus-inverse);
  color: var(--color-text-inverse);
}
.site-header--fixed {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  z-index: var(--z-sticky);
  max-inline-size: var(--site-header-max);
  margin-inline: auto;
  padding: var(--spacing-5);
  pointer-events: none;
}
.site-header--fixed .site-header__bar {
  pointer-events: auto;
  transition: background-color var(--ease-base), border-color var(--ease-base);
}
.site-header--fixed.is-scrolled .site-header__bar {
  border-color: transparent;
  background-color: var(--color-background-inverse);
}
.site-header__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding: var(--spacing-3) var(--spacing-5);
  border: var(--border-width-sm) solid color-mix(in srgb, var(--color-text-inverse) 30%, transparent);
  border-radius: var(--radius-full);
  background-color: var(--color-overlay-light);
}
.site-header__brand {
  flex: none;
  border-radius: var(--radius-sm);
}
.site-header__nav,
.site-header__socials,
.site-header__phone {
  display: none;
}
.site-header__toggle {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-3);
  padding: var(--spacing-2) 0 var(--spacing-2) var(--spacing-2);
  border: 0;
  border-radius: var(--radius-sm);
  background: none;
  color: inherit;
  font-family: inherit;
  font-size: var(--text-body-lg);
  font-weight: var(--weight-medium);
  cursor: pointer;
  transition: color var(--ease-fast);
}
/* Íconos de 32px fijos (--text-h2 es fluido y agrandaba la barra): es una dimensión, sale del espaciado */
.site-header__toggle .icon,
.offcanvas__close .icon {
  inline-size: var(--spacing-7);
  block-size: var(--spacing-7);
}
.site-header__toggle:hover {
  color: var(--color-text-highlight);
}
/* Redes en texto: «FB - TW - LI - IG». El guion es contenido generado con texto alternativo vacío,
   así el lector no lo anuncia; cada abreviatura completa su nombre con texto oculto («FB Facebook»). */
.site-header__socials {
  align-items: center;
  gap: var(--spacing-2);
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: var(--text-body-lg);
  font-weight: var(--weight-semibold);
  white-space: nowrap;
}
.site-header__socials li {
  display: flex;
  gap: var(--spacing-2);
}
.site-header__socials li + li::before {
  content: '-' / '';
}
.site-header__social {
  border-radius: var(--radius-xs);
  color: var(--color-text-inverse);
  text-decoration: none;
}
.site-header__social:hover {
  color: var(--color-text-highlight);
}
.site-header__phone {
  align-items: center;
  gap: var(--spacing-3);
  border-radius: var(--radius-full);
  color: var(--color-text-inverse);
  font-size: var(--text-body-lg);
  font-weight: var(--weight-semibold);
  white-space: nowrap;
  text-decoration: none;
}
.site-header__phone:hover {
  color: var(--color-text-highlight);
}
.site-header__phone-icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-full);
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
  font-size: var(--text-body-lg);
  transition: background-color var(--ease-fast);
}
.site-header__phone:hover .site-header__phone-icon {
  background-color: var(--color-action-secondary-hover);
}
@container site-header (width < 64rem) {
  .site-header__phone-number { position: absolute; inline-size: 1px; block-size: 1px; margin: -1px; padding: 0; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0; } /* = .visually-hidden */
}
@container site-header (min-width: 48rem) {
  .site-header__bar {
    padding: var(--spacing-2) var(--spacing-4);
  }
  .site-header__nav {
    display: block;
  }
  .site-header__phone {
    display: inline-flex;
  }
  .site-header__toggle {
    display: none;
  }
}
@container site-header (min-width: 64rem) {
  .site-header__bar {
    padding-inline: var(--spacing-5) var(--spacing-6);
  }
}
@container site-header (min-width: 80rem) {
  .site-header__socials {
    display: flex;
  }
}

/* --inner — variante de las páginas interiores (About Us…), medida en su diseño: sin barra visible (ni
   velo ni borde), el logo alineado con el contenido del .container y, en lugar de redes y teléfono, la
   píldora del menú oscura y translúcida con el botón «Schedule a call ↗» montado sobre su extremo derecho
   (desde 64rem de barra; antes, solo el menú). Alineación: el ancho máximo replica el del .container de
   Bootstrap en cada breakpoint (con el gutter adentro, como --why-container en Why Choose Us; excepción
   de breakpoints escrita en design-tokens.md) y la barra lleva de relleno medio gutter: así el logo cae
   en la x del contenido en todos los anchos (x=300 a 1920). Con is-scrolled la barra toma el fondo
   inverso, como la de la home; en mobile ocupa todo el ancho, sin radio. */
.site-header__cta {
  display: none;
}
.site-header--inner {
  --site-header-max: 100%;
}
@media (min-width: 36rem) {
  .site-header--inner {
    --site-header-max: 33.75rem;
  }
}
@media (min-width: 48rem) {
  .site-header--inner {
    --site-header-max: 45rem;
  }
}
@media (min-width: 62rem) {
  .site-header--inner {
    --site-header-max: 60rem;
  }
}
@media (min-width: 75rem) {
  .site-header--inner {
    --site-header-max: 71.25rem;
  }
}
@media (min-width: 87.5rem) {
  .site-header--inner {
    --site-header-max: calc(var(--container-width) + var(--spacing-7));
  }
}
.site-header--inner.site-header--fixed {
  padding-inline: 0;
}
.site-header--inner .site-header__bar {
  padding: 0 var(--spacing-4); /* medio gutter del .container (--spacing-7) */
  border-color: transparent;
  background-color: transparent;
}
.site-header--inner .site-header__socials,
.site-header--inner .site-header__phone {
  display: none;
}
.site-header--inner .site-nav__list {
  --color-border-focus: var(--color-border-focus-inverse);
  border: var(--border-width-sm) solid color-mix(in srgb, var(--color-text-inverse) 15%, transparent);
  background-color: color-mix(in srgb, var(--color-background-inverse) 55%, transparent);
}
.site-header--inner .site-nav__link {
  color: var(--color-text-inverse);
}
.site-header--inner .site-nav__link:hover,
.site-header--inner .site-nav__link[aria-expanded='true'] {
  color: var(--color-text-highlight);
}
/* El círculo del botón ámbar va en blanco (en el botón --accent sería ámbar sobre ámbar) */
.site-header--inner .site-header__cta {
  --btn-icon-bg: var(--color-surface-default);
  --btn-icon-fg: var(--color-text-primary);
  position: relative;
  align-self: stretch;
  margin-inline-start: calc(-1 * var(--spacing-7)); /* se monta ~14px sobre la píldora, como el diseño */
  padding-inline-end: var(--spacing-3);
}
@container site-header (width < 64rem) {
  .site-header--inner .site-header__bar {
    border-radius: 0;
  }
}
@container site-header (min-width: 64rem) {
  .site-header--inner .site-header__nav {
    margin-inline-start: auto;
  }
  /* Píldora de 633px a 1920: 56px de relleno y 32px entre ítems, medidos en el diseño */
  .site-header--inner .site-nav__list {
    gap: var(--spacing-7);
    padding-inline: calc(var(--spacing-9) + var(--spacing-2));
  }
  .site-header--inner .site-header__cta {
    display: inline-flex;
  }
}

/* Site Nav — la píldora blanca del header. Home, Services, Pages y Blog son botones de divulgación
   (aria-expanded) y no enlaces: no tienen página propia. main.js abre el submenú con click, con hover de
   mouse y lo cierra con Escape, al salir el foco o con un click afuera. El submenú es petróleo
   (data-surface="brand", el color medido en el diseño), así el foco pasa a amarillo adentro. */
.site-nav__list {
  --color-border-focus: var(--color-action-primary); /* en la píldora blanca el foco vuelve al petróleo */
  display: flex;
  align-items: center;
  gap: var(--spacing-5);
  margin: 0;
  padding: 0 var(--spacing-6);
  list-style: none;
  border-radius: var(--radius-full);
  background-color: var(--color-surface-default);
}
@container site-header (min-width: 64rem) {
  .site-nav__list {
    gap: var(--spacing-6);
    padding-inline: var(--spacing-7);
  }
}
.site-nav__item {
  position: relative;
}
.site-nav__link {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  padding: var(--spacing-5) 0;
  border: 0;
  background: none;
  color: var(--color-text-primary);
  font-family: inherit;
  font-size: var(--text-body-lg);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
  white-space: nowrap;
  text-decoration: none;
  cursor: pointer;
  transition: color var(--ease-fast);
}
.site-nav__link:hover,
.site-nav__link[aria-expanded='true'],
.site-nav__link[aria-current='page'] {
  color: var(--color-action-primary);
}
.site-nav__chevron {
  font-size: var(--text-body);
  transition: transform var(--ease-base);
}
.site-nav__link[aria-expanded='true'] .site-nav__chevron {
  transform: rotate(180deg);
}
.site-nav__submenu {
  position: absolute;
  inset-block-start: calc(100% + var(--spacing-6));
  inset-inline-start: calc(-1 * var(--spacing-5));
  z-index: var(--z-dropdown);
  min-inline-size: calc(var(--spacing-13) + var(--spacing-12)); /* 224px: el panel del diseño mide 220 */
  margin: 0;
  padding: var(--spacing-4) var(--spacing-5);
  list-style: none;
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-lg);
  opacity: 0;
  visibility: hidden;
  transform: translateY(var(--spacing-2));
  transition: opacity var(--ease-base), transform var(--ease-base), visibility var(--ease-base);
}
/* Puente invisible sobre el hueco entre la píldora y el panel: el mouse lo cruza sin cerrar el submenú */
.site-nav__submenu::before {
  content: '';
  position: absolute;
  inset-inline: 0;
  inset-block-end: 100%;
  block-size: var(--spacing-6);
}
/* Al abrir, visibility cambia sin transición para que el panel sea enfocable en el acto (Tab inmediato);
   al cerrar conserva la transición y sigue visible mientras se desvanece. */
.site-nav__trigger[aria-expanded='true'] + .site-nav__submenu {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition: opacity var(--ease-base), transform var(--ease-base), visibility 0s;
}
.site-nav__sublink {
  display: block;
  padding-block: var(--spacing-2);
  border-radius: var(--radius-xs);
  color: var(--color-text-inverse);
  font-weight: var(--weight-medium);
  white-space: nowrap;
  text-decoration: none;
}
.site-nav__sublink:hover,
.site-nav__sublink[aria-current='page'] {
  color: var(--color-text-highlight);
}

/* Off-canvas — menú mobile: panel crema que entra desde la derecha sobre la página desenfocada.
   main.js lo mueve al final de <body>, deja inert el resto de la página, detiene Lenis, lleva el foco
   a «Close» y lo cierra con Escape, con el fondo, con «Close», al elegir un enlace o si el botón que
   lo abrió deja de verse (devuelve el foco a ese botón, salvo en el último caso). Los submenús son
   <details> nativos, exclusivos por name.
   Cerrado queda visibility: hidden: fuera del orden de tabulación y del árbol de accesibilidad. */
.offcanvas {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  visibility: hidden;
  transition: visibility var(--ease-slow);
}
.offcanvas.is-open {
  visibility: visible;
  transition: none; /* visible en el acto: main.js le pasa el foco a «Close» en la misma tarea */
}
.offcanvas__backdrop {
  position: absolute;
  inset: 0;
  background-color: var(--color-overlay-light);
  backdrop-filter: blur(var(--blur-backdrop));
  opacity: 0;
  transition: opacity var(--ease-slow);
}
.offcanvas.is-open .offcanvas__backdrop {
  opacity: 1;
}
.offcanvas__panel {
  --color-border-focus: var(--color-action-primary);
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  inline-size: clamp(16rem, 100% - var(--spacing-13), 24rem); /* deja ver una franja de página, como el diseño */
  padding: var(--spacing-7) var(--spacing-4) var(--spacing-9);
  overflow-y: auto;
  overscroll-behavior: contain;
  background-color: var(--color-background-default);
  color: var(--color-text-primary);
  box-shadow: var(--shadow-lg);
  transform: translateX(100%);
  transition: transform var(--ease-slow);
}
.offcanvas.is-open .offcanvas__panel {
  transform: none;
}
.offcanvas__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding-block-end: var(--spacing-7);
  border-block-end: var(--border-width-sm) solid var(--color-border-default);
}
.offcanvas__brand {
  border-radius: var(--radius-sm);
}
.offcanvas__close {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  padding: var(--spacing-2) 0 var(--spacing-2) var(--spacing-2);
  border: 0;
  border-radius: var(--radius-sm);
  background: none;
  color: inherit;
  font-family: inherit;
  font-size: var(--text-body);
  cursor: pointer;
  transition: color var(--ease-fast);
}
.offcanvas__close:hover {
  color: var(--color-action-primary);
}
.offcanvas__list {
  margin: 0;
  padding: var(--spacing-7) 0 0;
  list-style: none;
}
.offcanvas__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding-block: var(--spacing-2);
  border-radius: var(--radius-xs);
  color: var(--color-text-primary);
  font-size: var(--text-h4);
  line-height: var(--leading-snug);
  text-transform: uppercase;
  text-decoration: none;
  list-style: none;
  cursor: pointer;
  transition: color var(--ease-fast);
}
.offcanvas__link::-webkit-details-marker {
  display: none;
}
.offcanvas__link:hover {
  color: var(--color-action-primary);
}
.offcanvas__link .icon {
  transition: transform var(--ease-base);
}
.offcanvas__group[open] > .offcanvas__link .icon {
  transform: rotate(180deg);
}
.offcanvas__sub {
  margin: 0;
  padding: 0 0 var(--spacing-3) var(--spacing-4);
  list-style: none;
}
.offcanvas__sublink {
  display: block;
  padding-block: var(--spacing-2);
  border-radius: var(--radius-xs);
  color: var(--color-text-secondary);
  text-decoration: none;
}
.offcanvas__sublink:hover {
  color: var(--color-text-primary);
}
.offcanvas__info {
  display: grid;
  color: var(--color-text-secondary);
  gap: var(--spacing-9);
  padding-block-start: var(--spacing-12);
}
.offcanvas__title {
  margin-block-end: var(--spacing-4);
  font-size: var(--text-h5);
  font-weight: var(--weight-regular);
}
.offcanvas__contact {
  display: grid;
  justify-items: start;
  gap: var(--spacing-1);
}
.offcanvas__contact a {
  color: var(--color-text-secondary);
  text-decoration-thickness: var(--border-width-sm);
  text-underline-offset: var(--border-width-md);
}
.offcanvas__contact a:hover {
  color: var(--color-text-primary);
}
/* Redes: el Icon Button --sm con el contorno fuerte que muestra el diseño (≥ 3:1 sobre el crema) */
.offcanvas__socials {
  display: flex;
  gap: var(--spacing-2);
  margin: 0;
  padding: 0;
  list-style: none;
}
.offcanvas__socials .icon-btn {
  --icon-btn-bg: transparent;
  --icon-btn-border: var(--color-border-strong);
  --icon-btn-border-hover: var(--color-text-primary);
}
/* Página detrás del off-canvas abierto: sin scroll (Lenis además se detiene desde main.js) */
html.has-offcanvas {
  overflow: hidden;
}

/* Carousel — base de Swiper reutilizada en Services (flechas) y Testimonials (dots). main.js la inicia
   con IntersectionObserver al acercarse al viewport: loop, velocidad de --ease-slow (0 con reducir
   movimiento) y módulo a11y (cada slide es un group «N of M»). Slides por vista según el ancho del
   carrusel, como el header: 1, 2 desde 48rem y 3 desde 64rem. El container query replica esos anchos
   antes de que Swiper arranque (y sin JS), así no hay salto al iniciar. Los slides de los costados se
   ven fuera del carrusel hasta el borde de la ventana, como el diseño: la Section recorta con
   overflow-x: clip. Las flechas pueden ir en el encabezado de la Section (aria-controls = id). */
.carousel {
  --carousel-gap: var(--spacing-5);
  --carousel-per-view: 1;
  container: carousel / inline-size;
  display: grid;
  gap: var(--spacing-9);
}
/* Sin min-inline-size: 0, el viewport (ítem de grid con overflow visible) toma como mínimo el ancho de
   todos los slides: Swiper recalcula sobre ese ancho y la grilla crece en bucle hasta el límite. */
.carousel > * {
  min-inline-size: 0;
}
.carousel__viewport {
  inline-size: 100%;
}
.carousel .carousel__viewport {
  overflow: visible; /* pisa el overflow: hidden de Swiper: los slides vecinos sangran fuera */
}
.carousel__slide {
  display: flex;
  block-size: auto; /* Swiper fija height: 100%; auto + flex iguala la altura de todas las cards */
}
.carousel__slide > * {
  flex: 1;
  min-inline-size: 0;
}
/* Antes de iniciar (o sin JS): mismos anchos que calculará Swiper, con scroll horizontal nativo */
.carousel__viewport:not(.swiper-initialized) {
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
.carousel__viewport:not(.swiper-initialized) .swiper-wrapper {
  gap: var(--carousel-gap);
}
.carousel__viewport:not(.swiper-initialized) .carousel__slide {
  inline-size: calc((100% - (var(--carousel-per-view) - 1) * var(--carousel-gap)) / var(--carousel-per-view));
  scroll-snap-align: start;
}
@container carousel (min-width: 48rem) {
  .carousel__viewport {
    --carousel-gap: var(--spacing-6);
    --carousel-per-view: 2;
  }
}
@container carousel (min-width: 64rem) {
  .carousel__viewport {
    --carousel-per-view: 3;
  }
}
.carousel__arrows {
  display: flex;
  gap: var(--spacing-3);
}
.carousel .dots {
  justify-self: center;
}
/* --fade — un slide por vista que cambia con fundido (las citas de Client Feedback en About Us). main.js lo
   inicia con effect: 'fade' (data-carousel-fade), sin copias ni vecinos a la vista: el viewport recorta. */
.carousel--fade .carousel__viewport {
  --carousel-per-view: 1;
  overflow: clip;
}

/* Accordion — grupo de Accordion Items (FAQ). Que haya un solo ítem abierto lo da el mismo name en
   todos los <details>, sin JS. El grupo anima la altura con ::details-content e interpolate-size:
   donde no hay soporte, abre y cierra sin animación. La duración sale de --ease-base (0 con reducir
   movimiento). */
.accordion {
  interpolate-size: allow-keywords;
}
.accordion .accordion-item::details-content {
  block-size: 0;
  overflow-y: clip;
  transition: block-size var(--ease-base), content-visibility var(--ease-base) allow-discrete;
}
.accordion .accordion-item[open]::details-content {
  block-size: auto;
}
/* --boxed — cada ítem en una caja con borde y 32px de separación; el abierto, en blanco (FAQ de About Us). */
.accordion--boxed {
  display: grid;
  gap: var(--spacing-7);
}
.accordion--boxed .accordion-item {
  padding-inline: var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-sm);
  transition: background-color var(--ease-base);
}
.accordion--boxed .accordion-item[open] {
  background-color: var(--color-surface-default);
}
/* Sobre el fondo --color-background-subtle de la sección, el «?» cerrado necesita un tono más */
.accordion--boxed .accordion-item__mark {
  background-color: var(--color-background-muted);
}

/* Video Modal — <dialog> nativo: showModal() deja inert el resto de la página, Escape lo cierra y el
   foco vuelve al botón que lo abrió. main.js crea el iframe de youtube-nocookie recién al hacer click
   en un [data-video-id] y lo quita al cerrar (corta la reproducción). Se cierra también con «Close» o
   con un click en el fondo. Ancho: hasta 64rem y nunca más alto que la ventana (16:9). El diseño no
   muestra el modal: fondo inverso, velo del theme y entrada con fundido, todo de tokens. */
.video-modal {
  --video-modal-max: 64rem;
  inline-size: min(100% - var(--spacing-8), var(--video-modal-max), (100dvh - var(--spacing-13)) * 16 / 9);
  max-inline-size: none;
  max-block-size: none;
  margin: auto;
  padding: 0;
  border: 0;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  opacity: 0;
  transform: translateY(var(--spacing-5));
  transition: opacity var(--ease-base), transform var(--ease-base), display var(--ease-base) allow-discrete, overlay var(--ease-base) allow-discrete;
}
.video-modal[open] {
  opacity: 1;
  transform: none;
}
.video-modal::backdrop {
  background-color: var(--color-overlay);
  opacity: 0;
  transition: opacity var(--ease-base), display var(--ease-base) allow-discrete, overlay var(--ease-base) allow-discrete;
}
.video-modal[open]::backdrop {
  opacity: 1;
}
@starting-style {
  .video-modal[open] {
    opacity: 0;
    transform: translateY(var(--spacing-5));
  }
  .video-modal[open]::backdrop {
    opacity: 0;
  }
}
.video-modal__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding: var(--spacing-3) var(--spacing-3) var(--spacing-3) var(--spacing-6);
}
.video-modal__title {
  font-size: var(--text-body-lg);
  font-weight: var(--weight-medium);
}
.video-modal__frame {
  aspect-ratio: 16 / 9;
  background-color: var(--color-background-inverse);
}
.video-modal__frame iframe {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border: 0;
}
/* Página detrás del modal abierto: sin scroll (Lenis además se detiene desde main.js) */
html:has(.video-modal[open]) {
  overflow: hidden;
}

/* Word List — bloque Finance / Advisory / Growth / Strategy. Desde lg: cuatro palabras grandes en una
   columna (nítida la activa, desenfocadas las demás) y a la derecha una Card Project por palabra,
   superpuestas; main.js marca como activas la palabra y la card que cruzan el centro del viewport
   (GSAP ScrollTrigger, sin pin: las propias palabras dan el alto de scroll). Bajo lg, como el diseño
   mobile: el título «Works» gigante y tenue (decorativo, aria-hidden) y las cuatro cards apiladas, sin
   efecto. El <h2> real va oculto en todos los anchos: en desktop el diseño no muestra título. Sin JS o
   con «reducir movimiento» queda el estado del markup (Growth activa, como el diseño). Las palabras van
   en blanco: la Section pone el fondo oscuro desde lg. */
.word-list {
  display: grid;
  gap: var(--spacing-5);
}
.word-list__watermark {
  margin: 0;
  color: var(--color-background-muted);
  font-family: var(--font-display);
  font-size: clamp(4rem, 21vw, 7rem); /* medido en el diseño: «Works» ocupa ~60% del ancho a 480px */
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  text-align: center;
}
.word-list__words {
  display: none;
}
.word-list__media {
  display: grid;
  gap: var(--spacing-6);
}
@media (min-width: 64rem) {
  .word-list {
    grid-template-columns: 1fr 1fr;
    align-items: center;
    gap: var(--spacing-12);
  }
  .word-list__watermark {
    display: none;
  }
  .word-list__words {
    display: grid;
    justify-items: start;
    gap: var(--spacing-8);
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .word-list__word {
    display: inline-block;
    color: color-mix(in srgb, var(--color-text-inverse) 80%, transparent);
    font-family: var(--font-display);
    font-size: var(--text-display);
    font-weight: var(--weight-semibold);
    line-height: var(--leading-tight);
    filter: blur(var(--blur-text));
    transition: filter var(--ease-slow), color var(--ease-slow);
  }
  .word-list__word.is-active {
    color: var(--color-text-inverse);
    filter: none;
  }
  .word-list__card {
    grid-area: 1 / 1;
    min-inline-size: 0;
    opacity: 0;
    visibility: hidden;
    transition: opacity var(--ease-slow), visibility var(--ease-slow);
  }
  .word-list__card.is-active {
    opacity: 1;
    visibility: visible;
  }
}

/* Marquee — franja de arriba del footer: «Connect With Us  Let's Grow» en bucle horizontal (CSS puro: dos
   grupos idénticos y translateX(-50%)), con el badge del logo fijo encima, centrado. Como el diseño, el
   texto va translúcido y solo «Grow» en blanco pleno (.marquee__accent). El texto que arma el bucle es
   aria-hidden, con una sola frase leíble para lectores al lado; el badge también (el nombre ya está en el
   logo del header). El diseño no muestra el badge en movimiento: queda estático. Con «reducir
   movimiento» el texto queda quieto. */
.marquee {
  --marquee-duration: 30s;
  --marquee-badge: clamp(10rem, 8.125rem + 6.25vw, 15.625rem); /* medido en el diseño: 160px a 480 → 250px a 1920 */
  position: relative;
  overflow: hidden;
  padding-block: var(--spacing-10);
  /* El track mide max-content (el texto repetido a --text-hero, miles de px) y overflow no frena que ese
     ancho mínimo suba a un ancestro grid/flex con columna automática, que se estira hasta él. La
     contención de tamaño en el eje inline anula ese aporte: el marquee siempre toma el ancho disponible. */
  contain: inline-size;
}
.marquee__viewport {
  overflow: hidden;
}
.marquee__track {
  display: flex;
  inline-size: max-content;
  animation: marquee-scroll var(--marquee-duration) linear infinite;
}
@keyframes marquee-scroll {
  to {
    transform: translateX(-50%);
  }
}
.marquee__group {
  display: flex;
  flex: none;
  gap: var(--spacing-7);
  padding-inline-end: var(--spacing-7);
}
.marquee__text {
  color: color-mix(in srgb, var(--color-text-inverse) 25%, transparent);
  font-family: var(--font-display);
  /* En mobile el diseño lo muestra más grande que el titular del hero (~75px a 480): --text-display pone
     el piso y --text-hero manda desde ~720px */
  font-size: max(var(--text-hero), var(--text-display));
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  white-space: nowrap;
}
.marquee__accent {
  color: var(--color-text-inverse);
}
.marquee__badge {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  translate: -50% -50%;
  display: grid;
  place-items: center;
  inline-size: var(--marquee-badge);
  block-size: var(--marquee-badge);
  border: var(--border-width-sm) solid color-mix(in srgb, var(--color-text-inverse) 15%, transparent);
  border-radius: var(--radius-full);
  background-color: color-mix(in srgb, var(--color-background-inverse) 85%, transparent);
  box-shadow: var(--shadow-lg);
}
.marquee__badge-logo {
  inline-size: 63%; /* el logo ocupa ~157 de los 250px del círculo en el diseño */
  block-size: auto;
}
@media (prefers-reduced-motion: reduce) {
  .marquee__track {
    animation: none;
  }
}

/* Site Footer — newsletter (molécula), Utility Page, Follow Us, Our Offices y barra legal, siempre sobre
   fondo inverso. Bajo lg: newsletter y oficinas a todo el ancho y las dos listas de enlaces lado a lado,
   como el diseño mobile. Desde lg: la newsletter hasta 24rem (380px en el diseño) y las otras tres
   columnas a su ancho de contenido, repartidas con space-between, que reproduce las posiciones del
   diseño. El filete de la barra legal cruza todo el ancho: el contenido va en un .container interno.
   «Pixenium» y «404 Not Error» son errores del export del diseño (plan.md): no se replican. */
.site-footer__top {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--spacing-9) var(--spacing-6);
}
.site-footer__top > .newsletter,
.site-footer__offices-col {
  grid-column: 1 / -1;
}
.site-footer__title {
  margin: 0 0 var(--spacing-7);
  color: var(--color-text-inverse);
  font-size: var(--text-h4);
  font-weight: var(--weight-semibold);
}
.site-footer__list {
  display: grid;
  gap: var(--spacing-4);
  margin: 0;
  padding: 0;
  list-style: none;
}
.site-footer__list a {
  color: var(--color-text-inverse-secondary);
  text-decoration: none;
  transition: color var(--ease-fast);
}
.site-footer__list a:hover {
  color: var(--color-text-inverse);
}
.site-footer__offices {
  display: grid;
  gap: var(--spacing-6);
}
.site-footer__office-label {
  margin: 0 0 var(--spacing-1);
  color: var(--color-text-inverse-secondary);
}
.site-footer__office-city {
  margin: 0;
  color: var(--color-text-inverse);
  font-size: var(--text-body-lg);
  font-weight: var(--weight-semibold);
}
.site-footer__legal {
  margin-block-start: var(--spacing-12);
  border-block-start: var(--border-width-sm) solid color-mix(in srgb, var(--color-text-inverse) 15%, transparent);
}
.site-footer__legal-inner {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-3) var(--spacing-6);
  padding-block: var(--spacing-8);
  color: var(--color-text-inverse);
}
.site-footer__legal-inner p {
  margin: 0;
}
.site-footer__legal-inner a {
  color: inherit;
  text-decoration: none;
}
.site-footer__legal-inner a:hover {
  color: var(--color-text-inverse-secondary);
}
@media (min-width: 64rem) {
  .site-footer__top {
    grid-template-columns: minmax(0, 24rem) repeat(3, auto);
    justify-content: space-between;
    column-gap: var(--spacing-9);
  }
  .site-footer__top > .newsletter,
  .site-footer__offices-col {
    grid-column: auto;
  }
}
/* organisms:end */
'''
s = open(MAIN, encoding='utf-8').read()
if '/* organisms:start */' in s:
    s = re.sub(r'/\* organisms:start \*/.*?/\* organisms:end \*/\n', lambda m: CSS, s, flags=re.S)
else:
    s = s.rstrip('\n') + '\n\n' + CSS
open(MAIN, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(CSS.splitlines()), 'líneas')
