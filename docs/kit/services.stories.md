# Services

**Nivel:** Section · 03  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:services -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#services`

## Descripción

Section Head `--split` (desde xl) con las flechas + Carousel de Card Service en `.container-wide`: activo centrado y destacado, vecinos sangrando hasta el borde; la sección recorta con `overflow-x: clip`.

## Snippet

```html
<section class="section services" id="services" aria-labelledby="services-title">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="section-head__main" data-reveal>
        <p class="eyebrow">Exclusive Services</p>
        <h2 class="section-title section-head__title" id="services-title">Innovative Solutions for Business Success</h2>
      </div>
      <p class="section-head__text" data-reveal>We believe successful businesses are built through strong planning, efficient management, &amp; innovative decision-making.</p>
      <div class="carousel__arrows section-head__actions" data-reveal>
        <button type="button" class="icon-btn" data-carousel-prev aria-controls="carousel-services" aria-label="Previous service"><span class="icon icon--arrow-left" aria-hidden="true"></span></button>
        <button type="button" class="icon-btn" data-carousel-next aria-controls="carousel-services" aria-label="Next service"><span class="icon icon--arrow-right" aria-hidden="true"></span></button>
      </div>
    </div>
  </div>
  <div class="container-wide">
    <div class="carousel" id="carousel-services" data-carousel data-carousel-highlight data-carousel-start="0" data-carousel-start-wide="1" role="region" aria-roledescription="carousel" aria-label="Services" data-reveal>
      <div class="swiper carousel__viewport">
        <div class="swiper-wrapper">
          <div class="swiper-slide carousel__slide">
            <article class="card-service">
              <img class="card-service__media" src="assets/img/h1-service-img-2.webp" alt="" width="1500" height="900" loading="lazy">
              <div class="card-service__body">
                <div class="card-service__head">
                  <span class="icon icon--target card-service__icon" aria-hidden="true"></span>
                  <h3 class="card-service__title">Marketing Guidance</h3>
                </div>
                <p>Through expert insights and strategic planning, marketing guidance enables businesses to understand customer.</p>
              </div>
            </article>
          </div>
          <div class="swiper-slide carousel__slide">
            <article class="card-service" data-surface="brand">
              <img class="card-service__media" src="assets/img/h1-service-img-3.webp" alt="" width="1500" height="900" loading="lazy">
              <div class="card-service__body">
                <div class="card-service__head">
                  <span class="icon icon--trending-up card-service__icon" aria-hidden="true"></span>
                  <h3 class="card-service__title">Process Optimization</h3>
                </div>
                <p>By analyzing existing operations and implementing effective improvements, process optimization helps business.</p>
              </div>
            </article>
          </div>
          <div class="swiper-slide carousel__slide">
            <article class="card-service">
              <img class="card-service__media" src="assets/img/h1-service-img-4.webp" alt="" width="1500" height="900" loading="lazy">
              <div class="card-service__body">
                <div class="card-service__head">
                  <span class="icon icon--chart-pie card-service__icon" aria-hidden="true"></span>
                  <h3 class="card-service__title">Sales Improvement</h3>
                </div>
                <p>We support businesses in improving sales performance through training, strategy development.</p>
              </div>
            </article>
          </div>
          <div class="swiper-slide carousel__slide">
            <article class="card-service">
              <img class="card-service__media" src="assets/img/h1-service-img-5.webp" alt="" width="1500" height="900" loading="lazy">
              <div class="card-service__body">
                <div class="card-service__head">
                  <span class="icon icon--gem card-service__icon" aria-hidden="true"></span>
                  <h3 class="card-service__title">Financial Planning</h3>
                </div>
                <p>Our advisors build budgets, forecasts and funding plans that keep every decision tied to your numbers.</p>
              </div>
            </article>
          </div>
          <div class="swiper-slide carousel__slide">
            <article class="card-service">
              <img class="card-service__media" src="assets/img/h1-service-img-1.webp" alt="" width="1500" height="900" loading="lazy">
              <div class="card-service__body">
                <div class="card-service__head">
                  <span class="icon icon--lightbulb card-service__icon" aria-hidden="true"></span>
                  <h3 class="card-service__title">Brand Strategy</h3>
                </div>
                <p>We help companies define a clear position and a message that strengthens their market presence.</p>
              </div>
            </article>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.services` | Recorta en horizontal los slides que sangran |
| `.section-head` | Encabezado de sección: __main (eyebrow + h2), __text y __actions, apilados |
| `.section-head--split` | Desde xl: título | texto | flechas en una fila; el texto y las flechas se alinean con la primera línea del h2 |
| `.section-head__title` | h2 acotado a 38rem para cortar donde el diseño |
| `.carousel__arrows.section-head__actions` | Flechas del carrusel (aria-controls = id del carrusel) |
| `data-carousel-highlight data-carousel-start="0" data-carousel-start-wide="1"` | Destaca el slide activo; arranca en Marketing Guidance (1 o 2 por vista) y en Process Optimization (3 por vista) |

## Tokens que consume

- `--text-h1 (section-title)`
- `--spacing-3 / -5 / -8 / -10`
- `Eyebrow, Icon Button (átomos)`
- `Card Service (molécula)`
- `Carousel (organismo)`

## Accesibilidad

Región «Services», slides «N of 5»; copias del loop con `aria-hidden` + `inert`. Flechas antes del carrusel, con `aria-controls`. El destacado es solo visual.

## Decisiones y excepciones

- Se destaca el slide activo (decisión del usuario): en desktop la card oscura queda al centro, como el diseño; en mobile, es la única visible.
- Section Head partido recién desde xl (1280px): a 1024px el título tenía 370px y cortaba en 4 líneas. Antes, apilado como en mobile.
- Financial Planning y Brand Strategy son placeholder (el diseño los muestra cortados en los costados). Los íconos son Lucide equivalentes a los glifos propios del diseño.
- Hueco entre secciones de 192px (96 + 96) contra ≈170px del diseño: se mantiene el ritmo del theme (`.section`).
