# Genera el bloque CSS de los átomos (con los iconos Lucide como máscara) y lo agrega a main.css.
# Idempotente: reemplaza todo lo que haya entre los marcadores atoms:start / atoms:end.
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
MAIN = str(ROOT / 'dist' / 'assets' / 'css' / 'main.css')

# Lucide (24x24, trazo 2). Las redes sociales no están en Lucide: SVG propios de trazo, mismo estilo.
ICONS = {
    'arrow-up-right': "<path d='M7 7h10v10'/><path d='M7 17 17 7'/>",
    'arrow-right': "<path d='M5 12h14'/><path d='m12 5 7 7-7 7'/>",
    'arrow-left': "<path d='m12 19-7-7 7-7'/><path d='M19 12H5'/>",
    'arrow-up': "<path d='m5 12 7-7 7 7'/><path d='M12 19V5'/>",
    'plus': "<path d='M5 12h14'/><path d='M12 5v14'/>",
    'minus': "<path d='M5 12h14'/>",
    'play': "<polygon points='6 3 20 12 6 21 6 3' fill='%23000'/>",
    'check': "<path d='M20 6 9 17l-5-5'/>",
    'circle-check': "<mask id='m'><rect width='24' height='24' fill='%23fff' stroke='none'/><path d='m8 12.5 2.8 2.8L16 9.5' stroke='%23000'/></mask><circle cx='12' cy='12' r='10' fill='%23000' stroke='none' mask='url(%23m)'/>",
    'chevron-down': "<path d='m6 9 6 6 6-6'/>",
    'x': "<path d='M18 6 6 18'/><path d='m6 6 12 12'/>",
    'send': "<path d='M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z'/><path d='m21.854 2.147-10.94 10.939'/>",
    'message-square': "<path d='M22 17a2 2 0 0 1-2 2H6.828a2 2 0 0 0-1.414.586l-2.202 2.202A.71.71 0 0 1 2 21.286V5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2z'/>",
    'layout-grid': "<rect width='7' height='7' x='3' y='3' rx='1'/><rect width='7' height='7' x='14' y='3' rx='1'/><rect width='7' height='7' x='14' y='14' rx='1'/><rect width='7' height='7' x='3' y='14' rx='1'/>",
    'facebook': "<path d='M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z'/>",
    'linkedin': "<path d='M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z'/><rect width='4' height='12' x='2' y='9'/><circle cx='4' cy='4' r='2'/>",
    'instagram': "<rect width='20' height='20' x='2' y='2' rx='5' ry='5'/><path d='M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z'/><line x1='17.5' x2='17.51' y1='6.5' y2='6.5'/>",
    'target': "<circle cx='12' cy='12' r='10'/><circle cx='12' cy='12' r='6'/><circle cx='12' cy='12' r='2'/>",
    'trending-up': "<polyline points='22 7 13.5 15.5 8.5 10.5 2 17'/><polyline points='16 7 22 7 22 13'/>",
    'chart-pie': "<path d='M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z'/><path d='M21.21 15.89A10 10 0 1 1 8 2.83'/>",
    'users': "<path d='M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2'/><circle cx='9' cy='7' r='4'/><path d='M22 21v-2a4 4 0 0 0-3-3.87'/><path d='M16 3.13a4 4 0 0 1 0 7.75'/>",
    'lightbulb': "<path d='M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5'/><path d='M9 18h6'/><path d='M10 22h4'/>",
    'rocket': "<path d='M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z'/><path d='m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z'/><path d='M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0'/><path d='M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5'/>",
    'gem': "<path d='M6 3h12l4 6-10 13L2 9Z'/><path d='M11 3 8 9l4 13 4-13-3-6'/><path d='M2 9h20'/>",
    'award': "<path d='m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526'/><circle cx='12' cy='8' r='6'/>",
    'hexagon': "<path d='M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z'/>",
    'x-twitter': "<path d='M4 4l11.733 16h4.267L8.267 4z'/><path d='M4 20l6.768-6.768m2.46-2.46L20 4'/>",
}

def data_uri(inner):
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' "
           "stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>" + inner + "</svg>")
    return 'data:image/svg+xml,' + svg.replace('<', '%3C').replace('>', '%3E')

icon_rules = '\n'.join(".icon--%s { --icon: url(\"%s\"); }" % (n, data_uri(i)) for n, i in ICONS.items())

CSS = r'''/* atoms:start */
/* ===== Átomos ===== */

/* Icon — Lucide como máscara CSS: hereda color (currentColor) y tamaño (1em) del contexto, sin SVG
   inline ni sprite, así el snippet que se copia no depende de rutas. Las redes sociales no están en
   Lucide: son SVG propios del mismo estilo. Los iconos son decorativos (aria-hidden): el nombre
   accesible lo da el texto o el aria-label del contenedor. */
.icon {
  display: inline-block;
  flex: none;
  inline-size: 1em;
  block-size: 1em;
  background-color: currentColor;
  mask: var(--icon) center / contain no-repeat;
}
@media (forced-colors: active) {
  .icon {
    forced-color-adjust: none;
    background-color: CanvasText;
  }
}
__ICON_RULES__

/* Button — píldora con círculo de ícono. Por defecto petróleo sobre fondo claro (.btn);
   --light sobre fondo oscuro; --block ocupa el ancho de su card (pricing); --accent es el relleno amarillo. */
.btn {
  --btn-bg: var(--color-action-primary);
  --btn-bg-hover: var(--color-action-primary-hover);
  --btn-bg-active: var(--color-action-primary-active);
  --btn-fg: var(--color-action-on-primary);
  --btn-icon-bg: var(--color-action-secondary);
  --btn-icon-fg: var(--color-action-on-secondary);
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-5);
  padding: var(--spacing-1) var(--spacing-1) var(--spacing-1) var(--spacing-6);
  border: 0;
  border-radius: var(--radius-full);
  background-color: var(--btn-bg);
  color: var(--btn-fg);
  font-family: inherit;
  font-size: var(--text-body);
  font-weight: var(--weight-medium);
  line-height: var(--leading-tight);
  text-decoration: none;
  cursor: pointer;
  transition: background-color var(--ease-fast);
}
.btn:hover {
  background-color: var(--btn-bg-hover);
  color: var(--btn-fg);
}
.btn:active {
  background-color: var(--btn-bg-active);
}
.btn__icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-full);
  background-color: var(--btn-icon-bg);
  color: var(--btn-icon-fg);
  font-size: var(--text-body);
}
.btn--light {
  --btn-bg: var(--color-surface-default);
  --btn-bg-hover: var(--color-background-subtle);
  --btn-bg-active: var(--color-background-muted);
  --btn-fg: var(--color-text-primary);
  --btn-icon-bg: var(--color-action-primary);
  --btn-icon-fg: var(--color-action-on-primary);
}
.btn--block {
  --btn-bg: var(--color-background-subtle);
  --btn-bg-hover: var(--color-background-muted);
  --btn-bg-active: var(--color-background-muted);
  --btn-fg: var(--color-text-primary);
  display: flex;
  justify-content: center;
  gap: var(--spacing-2);
  min-block-size: var(--spacing-9);
  padding: var(--spacing-2) var(--spacing-6);
}
.btn--block .icon {
  font-size: var(--text-sm);
}
.btn--accent {
  --btn-bg: var(--color-action-secondary);
  --btn-bg-hover: var(--color-action-secondary-hover);
  --btn-bg-active: var(--color-action-secondary-hover);
  --btn-fg: var(--color-action-on-secondary);
}
.btn:disabled,
.btn[aria-disabled='true'] {
  --btn-bg: var(--color-action-primary-disabled);
  --btn-bg-hover: var(--color-action-primary-disabled);
  --btn-bg-active: var(--color-action-primary-disabled);
  --btn-fg: var(--color-text-tertiary);
  --btn-icon-bg: var(--color-background-muted);
  --btn-icon-fg: var(--color-text-tertiary);
  cursor: not-allowed;
}

/* Icon Button — círculo de un solo ícono. Por defecto contorno sobre fondo claro; --glass sobre fotos
   (el amarillo marca hover y estado activo); --sm y --lg para el "+" del equipo y el play del video.
   También es el Social Icon: un .icon-btn --sm con el glifo de la red. */
.icon-btn {
  --icon-btn-size: var(--spacing-9);
  --icon-btn-bg: var(--color-surface-default);
  --icon-btn-bg-hover: var(--color-background-subtle);
  --icon-btn-fg: var(--color-text-primary);
  --icon-btn-border: var(--color-border-default);
  --icon-btn-border-hover: var(--color-border-strong);
  display: inline-grid;
  place-items: center;
  flex: none;
  inline-size: var(--icon-btn-size);
  block-size: var(--icon-btn-size);
  padding: 0;
  border: var(--border-width-sm) solid var(--icon-btn-border);
  border-radius: var(--radius-full);
  background-color: var(--icon-btn-bg);
  color: var(--icon-btn-fg);
  font-size: var(--text-h6);
  line-height: 1;
  text-decoration: none;
  cursor: pointer;
  transition: background-color var(--ease-fast), color var(--ease-fast), border-color var(--ease-fast);
}
.icon-btn:hover {
  background-color: var(--icon-btn-bg-hover);
  border-color: var(--icon-btn-border-hover);
  color: var(--icon-btn-fg);
}
.icon-btn--sm {
  --icon-btn-size: var(--spacing-8);
  font-size: var(--text-body);
}
.icon-btn--lg {
  --icon-btn-size: var(--spacing-10);
  font-size: var(--text-h5);
}
.icon-btn--glass {
  --icon-btn-bg: var(--color-overlay);
  --icon-btn-fg: var(--color-text-inverse);
  --icon-btn-border: var(--color-overlay-light);
  --icon-btn-border-hover: var(--color-action-secondary);
}
.icon-btn--glass:hover,
.icon-btn--glass[aria-pressed='true'],
.icon-btn--glass[aria-expanded='true'] {
  border-color: var(--color-action-secondary);
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
}
.icon-btn--glass .icon--play {
  color: var(--color-text-highlight);
}
.icon-btn--glass:hover .icon--play,
.icon-btn--glass[aria-pressed='true'] .icon--play {
  color: var(--color-action-on-secondary);
}
.icon-btn:disabled,
.icon-btn[aria-disabled='true'] {
  --icon-btn-bg: var(--color-background-subtle);
  --icon-btn-bg-hover: var(--color-background-subtle);
  --icon-btn-border-hover: var(--icon-btn-border);
  --icon-btn-fg: var(--color-text-tertiary);
  cursor: not-allowed;
}

/* Link Arrow — "Read More ↗" y "Contact Us ↗". El subrayado aparece en hover: el estado no
   depende solo del color. --inverse sobre cards oscuras; --highlight (amarillo) solo sobre fondo oscuro. */
.link-arrow {
  --link-fg: var(--color-text-primary);
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  color: var(--link-fg);
  font-weight: var(--weight-medium);
  text-decoration: none;
  transition: color var(--ease-fast);
}
.link-arrow:hover {
  color: var(--link-fg);
  text-decoration: underline;
  text-decoration-thickness: from-font;
  text-underline-offset: 0.25em;
}
.link-arrow--inverse {
  --link-fg: var(--color-text-inverse);
}
.link-arrow--highlight {
  --link-fg: var(--color-text-highlight);
}

/* Eyebrow — rótulo corto sobre el título de una sección; el cuadrito es decorativo (pseudo-elemento).
   --center lo marca a ambos lados; --inverse (amarillo) solo sobre fondo oscuro. */
.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  color: var(--color-text-primary);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
}
.eyebrow::before,
.eyebrow--center::after {
  content: '';
  flex: none;
  inline-size: calc(var(--spacing-1) * 1.5);
  block-size: calc(var(--spacing-1) * 1.5);
  background-color: currentColor;
}
.eyebrow--center {
  display: flex;
  justify-content: center;
}
.eyebrow--inverse {
  color: var(--color-text-highlight);
}

/* Badge — etiqueta translúcida sobre una foto (rol del equipo, fecha del post). El velo es el overlay
   del theme (petróleo oscuro al 65%): el texto blanco pasa AA sobre cualquier foto. --marker suma el cuadrito amarillo. */
.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-2);
  min-block-size: var(--spacing-8);
  padding-inline: var(--spacing-4);
  border: var(--border-width-sm) solid var(--color-overlay-light);
  border-radius: var(--radius-full);
  background-color: var(--color-overlay);
  color: var(--color-text-inverse);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
  line-height: var(--leading-tight);
}
.badge--marker::before {
  content: '';
  flex: none;
  inline-size: calc(var(--spacing-1) * 1.5);
  block-size: calc(var(--spacing-1) * 1.5);
  background-color: var(--color-text-highlight);
}

/* Avatar — retrato circular. --portrait es el retrato cuadrado de autor del testimonio.
   Avatar Stack solapa avatares con un anillo del color del fondo (--avatar-ring) y cierra con un "+". */
.avatar {
  --avatar-size: var(--spacing-8);
  display: block;
  flex: none;
  inline-size: var(--avatar-size);
  block-size: var(--avatar-size);
  border-radius: var(--radius-full);
  background-color: var(--color-background-muted);
  object-fit: cover;
}
.avatar--portrait {
  --avatar-size: var(--spacing-11);
  border-radius: var(--radius-sm);
}
.avatar-stack {
  --avatar-ring: var(--color-background-default);
  display: inline-flex;
  align-items: center;
  padding-inline-start: var(--border-width-md);
}
.avatar-stack > * {
  box-shadow: 0 0 0 var(--border-width-md) var(--avatar-ring);
}
.avatar-stack > * + * {
  margin-inline-start: calc(-1 * var(--spacing-3));
}
.avatar-stack__more {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-full);
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
  font-size: var(--text-body);
}

/* Progress — <progress> nativo (valor y rol salen del navegador). La etiqueta es un <label for>;
   el porcentaje visible es aria-hidden porque el valor ya se anuncia. */
.progress {
  display: grid;
  gap: var(--spacing-3);
}
.progress__head {
  display: flex;
  justify-content: space-between;
  gap: var(--spacing-4);
  color: var(--color-text-primary);
}
.progress__bar {
  appearance: none;
  inline-size: 100%;
  block-size: calc(var(--border-width-md) + var(--border-width-sm));
  border: 0;
  border-radius: var(--radius-full);
  background-color: var(--color-background-muted);
  color: var(--color-action-primary); /* Firefox pinta el relleno con color */
  overflow: hidden;
}
.progress__bar::-webkit-progress-bar {
  background-color: var(--color-background-muted);
}
.progress__bar::-webkit-progress-value {
  border-radius: var(--radius-full);
  background-color: var(--color-action-primary);
  transition: inline-size var(--ease-slow);
}
.progress__bar::-moz-progress-bar {
  border-radius: var(--radius-full);
  background-color: var(--color-action-primary);
}

/* Switch — checkbox nativo con role="switch": la posición de la perilla es el estado (apagado a la izquierda). */
.switch {
  --switch-width: var(--spacing-11);
  --switch-pad: var(--spacing-1);
  --switch-knob: calc(var(--spacing-7) + var(--spacing-1));
  appearance: none;
  position: relative;
  flex: none;
  inline-size: var(--switch-width);
  block-size: var(--spacing-8);
  margin: 0;
  border-radius: var(--radius-full);
  background-color: var(--color-action-primary);
  cursor: pointer;
  transition: background-color var(--ease-fast);
}
.switch::before {
  content: '';
  position: absolute;
  inset-block: var(--switch-pad);
  inset-inline-start: var(--switch-pad);
  inline-size: var(--switch-knob);
  border-radius: var(--radius-full);
  background-color: var(--color-surface-default);
  transition: transform var(--ease-base);
}
.switch:hover {
  background-color: var(--color-action-primary-hover);
}
.switch:checked::before {
  transform: translateX(calc(var(--switch-width) - var(--switch-knob) - 2 * var(--switch-pad)));
}
.switch:disabled {
  background-color: var(--color-action-primary-disabled);
  cursor: not-allowed;
}

/* Input — campo de texto de una línea con solo el filete inferior (el único caso del diseño: newsletter).
   Sobre superficies oscuras el filete y el placeholder pasan a blanco al 72% para mantener ≥ 3:1. */
.input {
  --input-fg: var(--color-text-primary);
  --input-border: var(--color-border-strong);
  --input-placeholder: var(--color-text-tertiary);
  inline-size: 100%;
  padding: var(--spacing-3) 0;
  border: 0;
  border-block-end: var(--border-width-sm) solid var(--input-border);
  border-radius: 0;
  background: none;
  color: var(--input-fg);
  font-family: inherit;
  font-size: var(--text-body);
  line-height: var(--leading-normal);
  transition: border-color var(--ease-fast);
}
.input::placeholder {
  color: var(--input-placeholder);
  opacity: 1;
}
.input:hover {
  border-block-end-color: var(--input-fg);
}
.input[aria-invalid='true'] {
  --input-border: var(--color-border-error);
}
:where([data-surface='inverse'], [data-surface='brand']) .input {
  --input-fg: var(--color-text-inverse);
  --input-border: var(--color-text-inverse-secondary);
  --input-placeholder: var(--color-text-inverse-secondary);
}

/* Divider — <hr> de un filete. --inverse sobre fondos oscuros. */
.divider {
  inline-size: 100%;
  block-size: 0;
  margin: 0;
  border: 0;
  border-block-start: var(--border-width-sm) solid var(--color-border-subtle);
}
.divider--inverse {
  border-block-start-color: var(--color-overlay-light);
}

/* Pagination Dots — cada punto es un botón de 24×24 (WCAG 2.5.8) con el punto dibujado en ::before.
   El inactivo usa border-strong (≥ 3:1 sobre claro y sobre oscuro); el activo lleva un halo. */
.dots {
  --dots-active: var(--color-action-primary);
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-1);
  margin: 0;
  padding: 0;
}
.dots--inverse {
  --dots-active: var(--color-text-highlight);
}
.dots__dot {
  display: grid;
  place-items: center;
  inline-size: var(--spacing-6);
  block-size: var(--spacing-6);
  padding: 0;
  border: 0;
  border-radius: var(--radius-full);
  background: none;
  cursor: pointer;
}
.dots__dot::before {
  content: '';
  inline-size: var(--spacing-3);
  block-size: var(--spacing-3);
  border-radius: var(--radius-full);
  background-color: var(--color-border-strong);
  transition: background-color var(--ease-base), box-shadow var(--ease-base);
}
.dots__dot:hover::before {
  background-color: var(--dots-active);
}
.dots__dot[aria-current='true']::before {
  background-color: var(--dots-active);
  box-shadow: 0 0 0 var(--spacing-1) color-mix(in srgb, var(--dots-active) 25%, transparent);
}

/* Scroll Top — fijo abajo a la derecha; main.js lo muestra al pasar media pantalla y dibuja en el anillo
   el avance del scroll (--scroll-progress, 0–100). Oculto con visibility para salir del orden de tabulación. */
.scroll-top {
  --scroll-progress: 0;
  position: fixed;
  inset-block-end: var(--spacing-5);
  inset-inline-end: var(--spacing-5);
  z-index: var(--z-sticky);
  display: grid;
  place-items: center;
  inline-size: var(--spacing-9);
  block-size: var(--spacing-9);
  padding: 0;
  border: 0;
  border-radius: var(--radius-full);
  background: conic-gradient(var(--color-action-primary) calc(var(--scroll-progress) * 1%), var(--color-border-default) 0);
  color: var(--color-text-primary);
  font-size: var(--text-h6);
  cursor: pointer;
  isolation: isolate;
  opacity: 0;
  visibility: hidden;
  transform: translateY(var(--spacing-2));
  transition: opacity var(--ease-base), transform var(--ease-base), visibility var(--ease-base);
}
.scroll-top::before {
  content: '';
  position: absolute;
  inset: var(--border-width-md);
  z-index: -1;
  border-radius: var(--radius-full);
  background-color: var(--color-surface-default);
  transition: background-color var(--ease-fast);
}
.scroll-top:hover::before {
  background-color: var(--color-background-subtle);
}
.scroll-top.is-visible {
  opacity: 1;
  visibility: visible;
  transform: none;
}
@media (min-width: 48rem) {
  .scroll-top {
    inset-block-end: var(--spacing-9);
    inset-inline-end: var(--spacing-9);
  }
}
/* atoms:end */
'''.replace('__ICON_RULES__', icon_rules)

s = open(MAIN, encoding='utf-8').read()
if '/* atoms:start */' in s:
    s = re.sub(r'/\* atoms:start \*/.*?/\* atoms:end \*/\n', lambda m: CSS, s, flags=re.S)
else:
    s = s.rstrip('\n') + '\n\n' + CSS
open(MAIN, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(ICONS), 'iconos,', len(CSS.splitlines()), 'líneas')
