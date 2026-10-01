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
/* organisms:end */
'''
s = open(MAIN, encoding='utf-8').read()
if '/* organisms:start */' in s:
    s = re.sub(r'/\* organisms:start \*/.*?/\* organisms:end \*/\n', lambda m: CSS, s, flags=re.S)
else:
    s = s.rstrip('\n') + '\n\n' + CSS
open(MAIN, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(CSS.splitlines()), 'líneas')
