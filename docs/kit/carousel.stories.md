# Carousel

**Nivel:** Organismo · 03  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Carousel */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#carousel`

## Descripción

Base de Swiper (loop con el activo centrado, arrastre, teclado) con 1/2/3 slides según el ancho del carrusel (48 y 64rem, container). Los vecinos sangran fuera; la Section recorta con `overflow-x: clip`. Flechas vinculadas por `aria-controls` (en cualquier lugar) o dots generados por `main.js`. `data-carousel-highlight` destaca el slide activo; `data-carousel-start` / `-start-wide` eligen el inicial.

## Snippets

**Services: flechas y slide activo destacado**

```html
<div class="carousel__arrows">
  <button type="button" class="icon-btn" data-carousel-prev aria-controls="carousel-services" aria-label="Previous service"><span class="icon icon--arrow-left" aria-hidden="true"></span></button>
  <button type="button" class="icon-btn" data-carousel-next aria-controls="carousel-services" aria-label="Next service"><span class="icon icon--arrow-right" aria-hidden="true"></span></button>
</div>
<div class="carousel" id="carousel-services" data-carousel data-carousel-highlight data-carousel-start="0" data-carousel-start-wide="1" role="region" aria-roledescription="carousel" aria-label="Services">
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
<div class="carousel" id="carousel-testimonials" data-carousel data-carousel-start="2" role="region" aria-roledescription="carousel" aria-label="Client stories">
  <div class="swiper carousel__viewport">
    <div class="swiper-wrapper">
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
    </div>
  </div>
  <div class="dots dots--inverse" role="group" aria-label="Choose a story" data-carousel-dots="Show story"></div>
</div>
```

**--fade: citas con fundido (Client Feedback de About Us)**

```html
<div class="carousel carousel--fade" id="carousel-quotes" data-carousel data-carousel-fade role="region" aria-roledescription="carousel" aria-label="Client quotes">
  <div class="swiper carousel__viewport">
    <div class="swiper-wrapper">
      <div class="swiper-slide carousel__slide">
        <figure class="feedback__quote">
          <blockquote class="feedback__text"><p>“Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy, every recommendation was practical, well-researched, & tailored to our goals.”</p></blockquote>
          <figcaption class="feedback__author"><strong>David Thompson,</strong> Sales Director</figcaption>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="feedback__quote">
          <blockquote class="feedback__text"><p>“We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.”</p></blockquote>
          <figcaption class="feedback__author"><strong>James Anderson,</strong> Entrepreneur, Brand Strategist</figcaption>
        </figure>
      </div>
      <div class="swiper-slide carousel__slide">
        <figure class="feedback__quote">
          <blockquote class="feedback__text"><p>“Working with this consulting team completely transformed our business operations.”</p></blockquote>
          <figcaption class="feedback__author"><strong>Isabella Harris,</strong> CEO & Founder</figcaption>
        </figure>
      </div>
    </div>
  </div>
  <div class="dots dots--inverse" role="group" aria-label="Choose a quote" data-carousel-dots="Show quote"></div>
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
| `.dots + data-carousel-dots="Show story"` | Contenedor de los dots: main.js crea un botón por slide original con ese prefijo de nombre |
| `data-carousel-start="2"` | Slide inicial (índice desde 0; por defecto 0) |
| `data-carousel-start-wide="1"` | Slide inicial cuando el carrusel mide 64rem o más (3 por vista); si falta, vale data-carousel-start |
| `data-carousel-highlight` | La card del slide activo recibe data-surface="brand" y las demás lo pierden; el markup trae destacada la inicial (estado sin JS) |
| `.carousel--fade + data-carousel-fade` | Un slide por vista con fundido (effect: fade); sin copias ni vecinos a la vista. Las clases feedback__* de las citas son de la Section Feedback |

## Tokens que consume

- `--spacing-5 / -6 (separación)`
- `--spacing-9`
- `--ease-slow (velocidad)`
- `Icon Button y Pagination Dots (átomos)`
- `Card Service y Card Testimonial (moléculas)`

## Accesibilidad

Región con `aria-roledescription="carousel"` y nombre; slides `role="group"` «N of M» (a11y de Swiper, `aria-live="polite"`). Flechas y dots son `<button>`; dot actual con `aria-current`. Tab solo entra en los slides enteros en pantalla (los demás, `tabindex="-1"`). Sin autoplay; velocidad `--ease-slow` (0 con reduced motion). Sin JS: fila con scroll nativo.

## Decisiones y excepciones

- Slides por vista según el ancho del carrusel (`breakpointsBase: container`), igual que el header: con el container de Bootstrap, 3 slides desde 1200px de viewport y 2 entre 768 y 1199px. El diseño solo muestra 1920 (3) y 480px (1). En la columna del kit a 1440px se ven 2.
- Slide activo centrado y destacado (decisión del usuario en la Etapa 4; reemplaza a la card destacada fija): en desktop el diseño muestra la oscura al centro con dos enteras y dos parciales a los costados; en mobile, la oscura es la única visible. Services arranca en Marketing Guidance en mobile y en Process Optimization con 3 por vista, como el diseño; Testimonials, en el tercer slide (el diseño marca el tercer dot).
- Copias: con el activo centrado se ven a la vez hasta 5 slides y el loop de Swiper necesita uno de repuesto; con 5 slides, al avanzar quedaba un hueco en el costado derecho que se llenaba de golpe al final de la transición. Si hay menos de 6, `main.js` duplica la tanda completa (no un solo slide, para no repetir uno dentro de la misma vuelta); las copias van con `aria-hidden` e `inert`, y el nombre «N of M», los dots y el destacado cuentan solo los originales. Reemplaza al truco anterior (`loopAdditionalSlides` + `loopFix`).
- Testimonios: Jonathan Walker (cortado en el diseño), Sophia Martinez y Michael Brooks son placeholder, igual que dos de los cinco servicios. Los tres videos usan el único video entregado.
- Dots: uno por slide original (el diseño muestra 6 para 6 testimonios); el activo es el slide centrado. Con copias, un dot lleva al ejemplar más cercano de ese slide.
- Trampa de foco corregida en la Etapa 4 (Grupo D): con `loop`, el `scrollOnFocus` del módulo a11y de Swiper deslizaba el carrusel hacia el slide enfocado, el loop reordenaba los slides en el DOM y el siguiente Tab volvía a caer adentro, sin salir nunca (WCAG 2.1.2). Ahora `scrollOnFocus: false`, `watchSlidesProgress: true` y `main.js` sincroniza el `tabindex` con `.swiper-slide-fully-visible` en `transitionEnd` y `resize` (patrón de carrusel de la WAI-APG).
- Swiper vendorizado (11.2.10) con su CSS `swiper-bundle.min.css`; no se usan sus flechas ni su paginación, sino los átomos del theme.
