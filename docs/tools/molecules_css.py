# Agrega el bloque CSS de las moléculas a main.css (idempotente: reemplaza entre molecules:start / molecules:end).
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
MAIN = str(ROOT / 'dist' / 'assets' / 'css' / 'main.css')

CSS = r'''/* molecules:start */
/* ===== Moléculas ===== */

/* Card Photo — patrón base de las cards con foto de fondo (equipo, testimonio en video, CTA): la imagen
   y el contenido comparten la misma celda de una grilla, y un velo entre ambos da lectura al texto.
   Va siempre con data-surface="inverse" para que el foco se vea sobre la foto. --scrim lo ajusta cada card. */
.card-photo {
  --scrim: linear-gradient(to top, color-mix(in srgb, var(--color-background-inverse) 85%, transparent), transparent 60%);
  position: relative;
  isolation: isolate;
  display: grid;
  overflow: hidden;
  border-radius: var(--radius-lg);
}
.card-photo > * {
  grid-area: 1 / 1;
  min-inline-size: 0;
}
.card-photo::after {
  content: '';
  grid-area: 1 / 1;
  z-index: -1;
  background: var(--scrim);
}
.card-photo__img {
  z-index: -2;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

/* Card Service — foto, ícono y texto. data-surface="brand" la destaca (petróleo, ícono amarillo). El cambio
   de destacado se anima: en el carrusel de Services la destacada es el slide activo y cambia con él. El
   texto va sangrado bajo el título, no bajo el ícono, como el diseño: __head se disuelve en la grilla de
   __body (ícono | título, y el párrafo en la segunda columna). */
.card-service {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-5);
  block-size: 100%;
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
  color: var(--color-text-secondary);
  transition: background-color var(--ease-base), color var(--ease-base), box-shadow var(--ease-base);
}
.card-service__media {
  display: block;
  inline-size: 100%;
  aspect-ratio: 5 / 3;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-service__body {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: var(--spacing-3) var(--spacing-5);
  padding: 0 var(--spacing-5) var(--spacing-5);
}
.card-service__head {
  display: contents;
}
.card-service__body > p {
  grid-column: 2;
}
.card-service__icon {
  font-size: var(--spacing-8);
  color: var(--color-text-primary);
  transition: color var(--ease-base);
}
.card-service__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  transition: color var(--ease-base);
}
.card-service[data-surface] {
  box-shadow: none;
  color: var(--color-text-inverse-secondary);
}
.card-service[data-surface] .card-service__icon {
  color: var(--color-text-highlight);
}

/* Card Feature — número decorativo arriba y texto abajo. Con data-surface="brand" lleva foto de fondo
   (card-feature__bg) bajo un velo petróleo, número amarillo y «Read More». */
.card-feature {
  position: relative;
  isolation: isolate;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: var(--spacing-10);
  block-size: 100%;
  padding: var(--spacing-7);
  overflow: hidden;
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
  color: var(--color-text-secondary);
}
.card-feature__number {
  color: var(--color-border-default); /* decorativo (aria-hidden): exento de contraste */
  font-size: var(--text-h5);
}
.card-feature__body {
  display: grid;
  gap: var(--spacing-3);
  justify-items: start;
}
.card-feature__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}
.card-feature[data-surface] {
  box-shadow: none;
  color: var(--color-text-inverse-secondary);
}
.card-feature[data-surface]::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background-color: color-mix(in srgb, var(--color-action-primary) 85%, transparent);
}
.card-feature[data-surface] .card-feature__number {
  color: var(--color-text-highlight);
}
.card-feature__bg {
  position: absolute;
  inset: 0;
  z-index: -2;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

/* Card Pricing — plan con ícono, precio, botón y lista de beneficios. data-surface="brand" destaca el plan
   (petróleo, botón amarillo). Excepción declarada: la lista es un panel con borde dentro de la card
   (card anidada, anti-patrones #4) porque el diseño lo muestra así. */
.card-pricing {
  display: grid;
  align-content: start;
  gap: var(--spacing-5);
  padding: var(--spacing-6);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
  color: var(--color-text-secondary);
}
.card-pricing__head {
  display: flex;
  align-items: center;
  gap: var(--spacing-4);
}
.card-pricing__icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-9);
  block-size: var(--spacing-9);
  border-radius: var(--radius-full);
  background-color: var(--color-background-subtle);
  color: var(--color-text-primary);
  font-size: var(--text-h5);
}
.card-pricing__name {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}
.card-pricing__price {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-2);
}
.card-pricing__amount {
  color: var(--color-text-primary);
  font-family: var(--font-display);
  font-size: var(--text-h1);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}
.card-pricing__list {
  display: grid;
  gap: var(--spacing-3);
  margin: 0;
  padding: var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-md);
  list-style: none;
}
.card-pricing__item {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
  color: var(--color-text-primary);
  font-weight: var(--weight-medium);
}
.card-pricing__item .icon {
  font-size: var(--text-h6);
  color: var(--color-action-primary);
}
.card-pricing__item.is-muted {
  color: var(--color-text-tertiary);
}
.card-pricing__item.is-muted .icon {
  color: var(--color-border-strong);
}
.card-pricing[data-surface] {
  box-shadow: none;
  color: var(--color-text-inverse-secondary);
}
.card-pricing[data-surface] .card-pricing__icon {
  background-color: var(--color-overlay-light);
  color: var(--color-text-inverse);
}
.card-pricing[data-surface] .card-pricing__amount {
  color: var(--color-text-inverse);
}
.card-pricing[data-surface] .card-pricing__list {
  border-color: var(--color-overlay-light);
  background-color: var(--color-overlay-light);
}
.card-pricing[data-surface] .card-pricing__item {
  color: var(--color-text-inverse);
}
.card-pricing[data-surface] .card-pricing__item .icon {
  color: var(--color-text-inverse);
}
.card-pricing[data-surface] .card-pricing__item.is-muted,
.card-pricing[data-surface] .card-pricing__item.is-muted .icon {
  color: var(--color-text-inverse-secondary);
}

/* Card Testimonial — <figure> con cita y autor. La de texto va en petróleo (data-surface="brand");
   --video es una foto con botón de play (card-photo) y el autor sobre la cita. */
.card-testimonial {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: var(--spacing-8);
  block-size: 100%;
  margin: 0;
  padding: var(--spacing-6);
  border-radius: var(--radius-lg);
}
.card-testimonial__quote {
  margin: 0;
  color: var(--color-text-inverse);
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  line-height: var(--leading-normal);
}
.card-testimonial__footer {
  display: grid;
  gap: var(--spacing-5);
}
.card-testimonial__author {
  display: flex;
  align-items: center;
  gap: var(--spacing-4);
  font-weight: var(--weight-medium);
}
.card-testimonial__name {
  color: var(--color-text-highlight);
}
.card-testimonial--video {
  --scrim: linear-gradient(to top, color-mix(in srgb, var(--color-background-inverse) 92%, transparent) 45%, transparent);
  display: grid;
  block-size: auto;
  padding: 0;
}
.card-testimonial--video .card-testimonial__body {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: var(--spacing-5);
  padding: var(--spacing-6);
}
.card-testimonial__play {
  align-self: start;
  justify-self: center;
  margin-block-start: calc(var(--spacing-10) + var(--spacing-8));
}

/* Card Team — foto con rol arriba a la izquierda, acción arriba a la derecha y nombre abajo.
   --elevated la sube 20px por encima y por debajo de sus vecinas (solo desde lg). */
.card-team__body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: var(--spacing-5);
}
.card-team__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--spacing-3);
}
.card-team__name {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  text-align: center;
}
.card-team--elevated .icon-btn {
  border-color: var(--color-action-secondary);
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
}
@media (min-width: 64rem) {
  .card-team--elevated {
    margin-block: calc(-1 * var(--spacing-5));
  }
}

/* --profile — variante clara (About Us): card blanca con la foto arriba (en el flujo, sin card-photo) y,
   debajo, nombre, cargo y redes. --reverse pone el texto arriba y la foto abajo desde lg (la card central
   del diseño). Medidas a 1920: marco de 12px, nombre 24px, cargo 16px, íconos de 18px. */
.card-team--profile {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-6);
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
}
.card-team__photo {
  display: block;
  inline-size: 100%;
  block-size: auto;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-team__info {
  display: grid;
  justify-items: start;
  gap: var(--spacing-1);
  padding: 0 var(--spacing-5) var(--spacing-5);
}
.card-team--profile .card-team__name {
  text-align: start;
}
.card-team__role {
  color: var(--color-text-secondary);
}
.card-team__socials {
  display: flex;
  gap: var(--spacing-1);
  margin: var(--spacing-4) 0 0 calc(-1 * var(--spacing-2));
  padding: 0;
  list-style: none;
}
/* 32px de área táctil (WCAG 2.5.8) alrededor de un ícono de 18px */
.card-team__social {
  display: grid;
  place-items: center;
  inline-size: var(--spacing-7);
  block-size: var(--spacing-7);
  border-radius: var(--radius-full);
  color: var(--color-text-primary);
  font-size: var(--text-h6);
}
.card-team__social:hover {
  color: var(--color-action-primary-hover);
}
@media (min-width: 64rem) {
  .card-team--reverse {
    flex-direction: column-reverse;
  }
  .card-team--reverse .card-team__info {
    padding: var(--spacing-6) var(--spacing-5) 0;
  }
}

/* Card Post — foto con fecha, título, extracto y «Read More». El texto va con sangría respecto a la foto. */
.card-post {
  display: grid;
  align-content: start;
  gap: var(--spacing-5);
}
.card-post__media {
  position: relative;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  border-radius: var(--radius-lg);
}
.card-post__img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}
.card-post__date {
  position: absolute;
  inset-block-start: var(--spacing-4);
  inset-inline-start: var(--spacing-4);
}
.card-post__body {
  display: grid;
  gap: var(--spacing-3);
  justify-items: start;
  padding-inline: var(--spacing-5);
}
.card-post__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}

/* Card Project — foto con marco blanco y pie con número decorativo («// 01») y título. */
.card-project {
  display: grid;
  gap: var(--spacing-5);
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
}
.card-project__img {
  display: block;
  inline-size: 100%;
  aspect-ratio: 10 / 7;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-project__caption {
  display: flex;
  align-items: baseline;
  gap: var(--spacing-4);
  padding: 0 var(--spacing-3) var(--spacing-3);
}
.card-project__index {
  color: var(--color-text-tertiary);
  font-size: var(--text-sm);
}
.card-project__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}
/* La card es siempre blanca (como el resto), incluso dentro de un data-surface="inverse" (el Word List
   de Etapa 3 la usa sobre fondo oscuro): sin esto, la regla de foundations que pone los títulos en
   blanco dentro de una superficie inversa gana por orden de cascada y el título queda invisible. El
   prefijo html iguala la técnica de especificidad que ya usan las superficies (ver color.css). */
html .card-project :is(h1, h2, h3, h4, h5, h6) {
  color: var(--color-text-primary);
}

/* Card CTA — foto con ícono arriba y, abajo, título, texto y enlace amarillo. */
.card-cta {
  --scrim: linear-gradient(to top, color-mix(in srgb, var(--color-background-inverse) 90%, transparent), color-mix(in srgb, var(--color-background-inverse) 45%, transparent));
}
.card-cta__body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: var(--spacing-8);
  padding: var(--spacing-6);
}
.card-cta__icon {
  display: grid;
  place-items: center;
  inline-size: var(--spacing-9);
  block-size: var(--spacing-9);
  border-radius: var(--radius-full);
  background-color: var(--color-overlay-light);
  font-size: var(--text-h5);
}
.card-cta__text {
  display: grid;
  gap: var(--spacing-3);
  justify-items: start;
}
.card-cta__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}

/* --stacked — variante clara (FAQ de About Us): card blanca con la foto arriba (en el flujo, sin card-photo
   ni ícono) y, debajo, título, texto y «Contact Us ↗» en el color de enlace normal. */
.card-cta--stacked {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-6);
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
}
.card-cta__photo {
  display: block;
  inline-size: 100%;
  block-size: auto;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-cta--stacked .card-cta__text {
  padding: 0 var(--spacing-5) var(--spacing-5);
}

/* Card Hero — tarjeta translúcida (velo oscuro del theme) sobre la foto del hero; es estática (no enlaza). */
.card-hero {
  display: flex;
  gap: var(--spacing-4);
  padding: var(--spacing-2);
  border: var(--border-width-sm) solid var(--color-overlay-light);
  border-radius: var(--radius-md);
  background-color: var(--color-overlay);
  color: var(--color-text-inverse);
}
.card-hero__media {
  flex: none;
  inline-size: calc(var(--spacing-11) * 2);
  block-size: auto;
  border-radius: var(--radius-sm);
  object-fit: cover;
}
.card-hero__body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-block: var(--spacing-2);
  padding-inline-end: var(--spacing-3);
}
.card-hero__index {
  color: var(--color-text-highlight);
  font-size: var(--text-sm);
  font-weight: var(--weight-medium);
}
.card-hero__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
}

/* Stat — cifra grande con etiqueta; el sufijo («+», «%») va atenuado. --center para la versión centrada. */
.stat {
  display: grid;
  gap: var(--spacing-2);
}
.stat__value {
  color: var(--color-text-primary);
  font-family: var(--font-display);
  font-size: var(--text-h1);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}
.stat__suffix {
  color: var(--color-text-tertiary);
}
.stat--center {
  text-align: center;
}

/* Accordion Item — <details> nativo: abre con Enter/Espacio sin JS y, con el mismo atributo name en
   varios ítems, solo uno queda abierto. El «?» y el +/− son decorativos (aria-hidden). Pregunta de 18px
   en mobile y 24px desde lg, semibold, con la separación medida en el diseño (--accordion-gap). */
.accordion-item {
  border-block-end: var(--border-width-sm) solid var(--color-border-subtle);
}
.accordion-item {
  --accordion-gap: var(--spacing-5);
}
.accordion-item__summary {
  display: flex;
  align-items: center;
  gap: var(--accordion-gap);
  padding-block: var(--spacing-5);
  color: var(--color-text-primary);
  font-size: var(--text-h6);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
  list-style: none;
  cursor: pointer;
}
.accordion-item__summary::-webkit-details-marker {
  display: none;
}
.accordion-item__mark {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-full);
  background-color: var(--color-background-subtle);
  font-size: var(--text-body);
  font-weight: var(--weight-bold);
  transition: background-color var(--ease-base);
}
.accordion-item__question {
  flex: 1;
}
.accordion-item__toggle {
  flex: none;
  font-size: var(--spacing-6);
}
.accordion-item__toggle .icon--minus,
.accordion-item[open] .accordion-item__toggle .icon--plus {
  display: none;
}
.accordion-item[open] .accordion-item__toggle .icon--minus {
  display: inline-block;
}
.accordion-item[open] .accordion-item__mark {
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
}
.accordion-item__panel {
  padding-block-end: var(--spacing-6);
  padding-inline-start: calc(var(--spacing-8) + var(--accordion-gap));
  color: var(--color-text-secondary);
}
@media (min-width: 64rem) {
  .accordion-item {
    --accordion-gap: var(--spacing-7);
  }
  .accordion-item__summary {
    padding-block: var(--spacing-7);
    font-size: var(--text-h4);
  }
}

/* Newsletter — <form> con la frase como <label> del campo y el botón de envío dentro del filete. */
.newsletter {
  display: grid;
  align-content: start; /* en la fila del footer, más alta, no reparte el espacio sobrante entre sus filas */
  gap: var(--spacing-5);
}
.newsletter__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
  line-height: var(--leading-snug);
}
.newsletter__field {
  position: relative;
}
.newsletter__field .input {
  padding-inline-end: var(--spacing-9);
}
.newsletter__submit {
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  display: grid;
  place-items: center;
  inline-size: var(--spacing-8);
  padding: 0;
  border: 0;
  background: none;
  color: currentColor;
  font-size: var(--text-h6);
  cursor: pointer;
  transition: color var(--ease-fast);
}
.newsletter__submit:hover {
  color: var(--color-text-highlight);
}

/* Service Nav — «Exclusive Services» de Service Details: card con borde y la lista de servicios en píldoras
   grises con un cuadrado de flecha. La página actual va con aria-current="page": petróleo, texto blanco y el
   cuadrado ámbar. El diseño no muestra el hover: el cuadrado toma el ámbar del activo. */
.service-nav {
  display: grid;
  gap: var(--spacing-6);
  padding: var(--spacing-6) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-default);
  border-radius: var(--radius-md);
}
.service-nav__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
}
.service-nav__list {
  display: grid;
  gap: var(--spacing-4);
  margin: 0;
  padding: 0;
  list-style: none;
}
.service-nav__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding: var(--spacing-2) var(--spacing-2) var(--spacing-2) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-sm);
  background-color: var(--color-background-subtle);
  color: var(--color-text-primary);
  font-weight: var(--weight-medium);
  text-decoration: none;
  transition: background-color var(--ease-fast), color var(--ease-fast);
}
.service-nav__icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-xs);
  background-color: var(--color-surface-default);
  color: var(--color-text-primary);
  font-size: var(--text-body-lg);
  transition: background-color var(--ease-fast), color var(--ease-fast);
}
.service-nav__link:hover {
  color: var(--color-text-primary);
}
.service-nav__link:hover .service-nav__icon,
.service-nav__link[aria-current='page'] .service-nav__icon {
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
}
.service-nav__link[aria-current='page'],
.service-nav__link[aria-current='page']:hover {
  border-color: var(--color-action-primary);
  background-color: var(--color-action-primary);
  color: var(--color-action-on-primary);
}
@media (min-width: 48rem) {
  .service-nav {
    padding: var(--spacing-8);
  }
}

/* Quote Form — card blanca con el título, cuatro Field y el botón (About Us, «Get a free Quote»). Debajo,
   las regiones de estado: enviado (role="status") y error de envío (role="alert"), vacías hasta que
   main.js las llena; vacías no ocupan lugar pero siguen en el árbol de accesibilidad (así se anuncian).
   Sin gap: cada Field ya reserva arriba el lugar de su label, y con gap los campos quedaban a 99px uno
   del otro (el diseño: 75px). */
.quote-form {
  display: grid;
  padding: var(--spacing-6) var(--spacing-5);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-md);
}
/* El nivel del título depende de la página (h2 en About Us, donde el formulario va antes que el h2 de su
   sección; h3 en el kit): el tamaño es siempre el de un h3 */
.quote-form__title {
  margin-block-end: var(--spacing-2);
  font-size: var(--text-h3);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
}
.quote-form__submit {
  justify-self: start;
  margin-block-start: var(--spacing-6);
}
.quote-form__submit[aria-disabled='true'] {
  cursor: progress;
}
.quote-form__messages {
  display: grid;
}
.quote-form__status:not(:empty),
.quote-form__alert:not(:empty) {
  margin-block-start: var(--spacing-5);
  padding: var(--spacing-3) var(--spacing-4);
  border: var(--border-width-sm) solid;
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
}
.quote-form__status:not(:empty) {
  border-color: var(--color-feedback-success-border);
  background-color: var(--color-feedback-success-bg);
  color: var(--color-feedback-success-text);
}
.quote-form__alert:not(:empty) {
  border-color: var(--color-feedback-error-border);
  background-color: var(--color-feedback-error-bg);
  color: var(--color-feedback-error-text);
}
@media (min-width: 48rem) {
  .quote-form {
    padding: var(--spacing-8);
  }
}
/* --outline — card con borde, sin fondo ni sombra (aside de Service Details, «Get a Quote»), con el título
   a 24px y los campos --filled. Misma lógica y estados que el Quote Form base. */
.quote-form--outline {
  border: var(--border-width-sm) solid var(--color-border-default);
  border-radius: var(--radius-md);
  background-color: transparent;
  box-shadow: none;
}
.quote-form--outline .quote-form__title {
  font-size: var(--text-h4);
}
/* --plain — sin card (Contact): sin fondo, sombra, borde ni padding; el título es el h2 de la Section,
   fuera del formulario (aria-labelledby). Campos de filete (como About) y el Select sobre el mismo filete.
   row-gap: el diseño deja 90px entre filetes y el Field ya mide ≈ 83. Desde md, dos columnas (Name · Email,
   Phone · Service); el mensaje, el botón y los avisos ocupan las dos (grid-column: 1 / -1). Los campos
   ocultos (_subject, honeypot) no son items de grilla: el input[type=hidden] y el div[hidden] no generan
   caja. */
.quote-form--plain {
  padding: 0;
  border-radius: 0;
  background-color: transparent;
  box-shadow: none;
  row-gap: var(--spacing-2);
}
.quote-form--plain .quote-form__submit {
  margin-block-start: var(--spacing-7); /* + row-gap = 40px del filete al botón, como el diseño */
}
.quote-form--plain textarea.input {
  min-block-size: var(--spacing-13); /* el mensaje del diseño mide ≈ 123px (96 en el Textarea base) */
}
@media (min-width: 48rem) {
  .quote-form--plain {
    padding: 0;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: var(--spacing-6);
  }
  .quote-form--plain > :is(.field:has(textarea), .quote-form__submit, .quote-form__messages) {
    grid-column: 1 / -1;
  }
}
/* molecules:end */
'''
s = open(MAIN, encoding='utf-8').read()
if '/* molecules:start */' in s:
    s = re.sub(r'/\* molecules:start \*/.*?/\* molecules:end \*/\n', lambda m: CSS, s, flags=re.S)
else:
    s = s.rstrip('\n') + '\n\n' + CSS
open(MAIN, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(CSS.splitlines()), 'líneas')
