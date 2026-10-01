# Carousel

**Nivel:** Organismo · 03  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Carousel */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#carousel`

## Descripción

Base de Swiper (loop, arrastre, teclado) con 1/2/3 slides según el ancho del carrusel (48 y 64rem, container). Los vecinos sangran fuera; la Section recorta con `overflow-x: clip`. Flechas vinculadas por `aria-controls` (en cualquier lugar) o dots generados por `main.js`.

## Snippets

**Services: flechas y card destacada fija**

```html
<div class="carousel__arrows">
  <button type="button" class="icon-btn" data-carousel-prev aria-controls="carousel-services" aria-label="Previous service"><span class="icon icon--arrow-left" aria-hidden="true"></span></button>
  <button type="button" class="icon-btn" data-carousel-next aria-controls="carousel-services" aria-label="Next service"><span class="icon icon--arrow-right" aria-hidden="true"></span></button>
</div>
<div class="carousel" id="carousel-services" data-carousel role="region" aria-roledescription="carousel" aria-label="Services">
  <div class="swiper carousel__viewport">
    <div class="swiper-wrapper">
      <div class="swiper-slide carousel__slide">
        <article class="card-service">
          <img class="card-service__media" src="../assets/img/h1-service-img-2.webp" alt="" width="1500" height="900" loading="lazy">
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
          <img class="card-service__media" src="../assets/img/h1-service-img-3.webp" alt="" width="1500" height="900" loading="lazy">
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
          <img class="card-service__media" src="../assets/img/h1-service-img-4.webp" alt="" width="1500" height="900" loading="lazy">
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
          <img class="card-service__media" src="../assets/img/h1-service-img-5.webp" alt="" width="1500" height="900" loading="lazy">
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
          <img class="card-service__media" src="../assets/img/h1-service-img-1.webp" alt="" width="1500" height="900" loading="lazy">
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
```

**Testimonials: dots, sobre fondo oscuro**

```html
<div class="carousel" id="carousel-testimonials" data-carousel role="region" aria-roledescription="carousel" aria-label="Client stories">
  <div class="swiper carousel__viewport">
    <div class="swiper-wrapper">
      <div class="swiper-slide carousel__slide">
        <figure class="card-testimonial" data-surface="brand">
          <blockquote class="card-testimonial__quote">
            <p>“We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.”</p>
          </blockquote>
          <figcaption class="card-testimonial__footer">
            <hr class="divider divider--inverse">
            <p class="card-testimonial__author">
              <img class="avatar avatar--portrait" src="../assets/img/h1-testimonial-thumb-img-1.webp" alt="" width="80" height="80" loading="lazy">
              <span><span class="card-testimonial__name">James Anderson,</span> Entrepreneur, Brand Strategist</span>
            </p>
          </figcaption>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
          <img class="card-photo__img" src="../assets/img/h1-testimonial-large-img-2.webp" alt="" width="1048" height="920" loading="lazy">
          <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Isabella Harris" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Isabella Harris"><span class="icon icon--play" aria-hidden="true"></span></button>
          <div class="card-testimonial__body">
            <figcaption class="card-testimonial__footer">
              <p class="card-testimonial__author"><span><span class="card-testimonial__name">Isabella Harris,</span> CEO & Founder</span></p>
              <hr class="divider divider--inverse">
            </figcaption>
            <blockquote class="card-testimonial__quote">
              <p>“Working with this consulting team completely transformed our business operations.”</p>
            </blockquote>
          </div>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="card-testimonial" data-surface="brand">
          <blockquote class="card-testimonial__quote">
            <p>“Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy.”</p>
          </blockquote>
          <figcaption class="card-testimonial__footer">
            <hr class="divider divider--inverse">
            <p class="card-testimonial__author">
              <img class="avatar avatar--portrait" src="../assets/img/h1-testimonial-thumb-img-2.webp" alt="" width="80" height="80" loading="lazy">
              <span><span class="card-testimonial__name">David Thompson,</span> Sales Director, HR Consultant</span>
            </p>
          </figcaption>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
          <img class="card-photo__img" src="../assets/img/h1-testimonial-large-img-3.webp" alt="" width="1048" height="920" loading="lazy">
          <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Jonathan Walker" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Jonathan Walker"><span class="icon icon--play" aria-hidden="true"></span></button>
          <div class="card-testimonial__body">
            <figcaption class="card-testimonial__footer">
              <p class="card-testimonial__author"><span><span class="card-testimonial__name">Jonathan Walker,</span> Operations Manager</span></p>
              <hr class="divider divider--inverse">
            </figcaption>
            <blockquote class="card-testimonial__quote">
              <p>“Their business insights and personalized solutions had a real impact on our growth.”</p>
            </blockquote>
          </div>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="card-testimonial" data-surface="brand">
          <blockquote class="card-testimonial__quote">
            <p>“From the first workshop, the team understood our goals and turned them into a plan we could actually execute.”</p>
          </blockquote>
          <figcaption class="card-testimonial__footer">
            <hr class="divider divider--inverse">
            <p class="card-testimonial__author">
              <img class="avatar avatar--portrait" src="../assets/img/h1-testimonial-thumb-img-3.webp" alt="" width="80" height="80" loading="lazy">
              <span><span class="card-testimonial__name">Sophia Martinez,</span> Marketing Director</span>
            </p>
          </figcaption>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
          <img class="card-photo__img" src="../assets/img/h1-testimonial-large-img-1.webp" alt="" width="1048" height="920" loading="lazy">
          <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Michael Brooks" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Michael Brooks"><span class="icon icon--play" aria-hidden="true"></span></button>
          <div class="card-testimonial__body">
            <figcaption class="card-testimonial__footer">
              <p class="card-testimonial__author"><span><span class="card-testimonial__name">Michael Brooks,</span> Founder, Brooks & Co.</span></p>
              <hr class="divider divider--inverse">
            </figcaption>
            <blockquote class="card-testimonial__quote">
              <p>“They stayed committed to every milestone and helped us improve how the whole company works.”</p>
            </blockquote>
          </div>
        </figure>
      </div>
    </div>
  </div>
  <div class="dots dots--inverse" role="group" aria-label="Choose a story" data-carousel-dots="Show story"></div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.carousel + data-carousel + id` | Contenedor (container: carousel); main.js lo inicia al acercarse al viewport |
| `role="region" aria-roledescription="carousel" aria-label` | Región con nombre propio («Services», «Client stories») |
| `.swiper.carousel__viewport / .swiper-wrapper` | Estructura de Swiper; el viewport deja ver los slides vecinos |
| `.swiper-slide.carousel__slide` | Un slide; iguala la altura de las cards |
| `.carousel__arrows` | Fila de flechas (Icon Button); puede vivir fuera del carrusel |
| `data-carousel-prev / data-carousel-next + aria-controls` | Flechas: aria-controls apunta al id del carrusel |
| `.dots + data-carousel-dots="Show story"` | Contenedor de los dots: main.js crea un botón por slide con ese prefijo de nombre |

## Tokens que consume

- `--spacing-5 / -6 (separación)`
- `--spacing-9`
- `--ease-slow (velocidad)`
- `Icon Button y Pagination Dots (átomos)`
- `Card Service y Card Testimonial (moléculas)`

## Accesibilidad

Región con `aria-roledescription="carousel"` y nombre; slides `role="group"` «N of M» (a11y de Swiper, `aria-live="polite"`). Flechas y dots son `<button>`; dot actual con `aria-current`. Sin autoplay; velocidad `--ease-slow` (0 con reduced motion). Sin JS: fila con scroll nativo.

## Decisiones y excepciones

- Slides por vista según el ancho del carrusel (`breakpointsBase: container`), igual que el header: con el container de Bootstrap, 3 slides desde 1200px de viewport y 2 entre 768 y 1199px. El diseño solo muestra 1920 (3) y 480px (1). En la columna del kit a 1440px se ven 2.
- Card destacada fija (Process Optimization), según la decisión aprobada. Ojo: en el diseño mobile la card oscura es la primera visible (Marketing Guidance), lo que sugeriría que se destaca el slide activo. Pendiente de confirmar.
- Testimonios: Jonathan Walker (cortado en el diseño), Sophia Martinez y Michael Brooks son placeholder, igual que dos de los cinco servicios. Los tres videos usan el único video entregado.
- Dots: uno por slide (el diseño muestra 6 para 6 testimonios); el activo es el primer slide visible.
- Swiper vendorizado (11.2.10) con su CSS `swiper-bundle.min.css`; no se usan sus flechas ni su paginación, sino los átomos del theme.
