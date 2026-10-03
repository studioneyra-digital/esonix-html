# Testimonials

**Nivel:** Section · 08  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:testimonials -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#testimonials`

## Descripción

Bloque oscuro (foto desenfocada + velo), encabezado centrado y Carousel con dots en `.container-wide`; arranca en el tercer slide (Isabella). Radio en las 4 esquinas en mobile y solo arriba desde lg.

## Snippet

```html
<section class="section testimonials" id="testimonials" aria-labelledby="testimonials-title" data-surface="inverse">
  <div class="section-bg">
    <img src="assets/img/h1-testimonial-bg-img.webp" alt="" width="1920" height="1000" loading="lazy">
  </div>
  <div class="container">
    <div class="section-head section-head--center">
      <div class="section-head__main">
        <p class="eyebrow eyebrow--center eyebrow--inverse">Client Feedback</p>
        <h2 class="section-title section-head__title" id="testimonials-title">Client Stories That Speak for Themselves</h2>
      </div>
    </div>
  </div>
  <div class="container-wide">
    <div class="carousel" id="carousel-testimonials" data-carousel data-carousel-start="2" role="region" aria-roledescription="carousel" aria-label="Client stories">
      <div class="swiper carousel__viewport">
        <div class="swiper-wrapper">
          <div class="swiper-slide carousel__slide">
            <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
              <img class="card-photo__img" src="assets/img/h1-testimonial-large-img-1.webp" alt="" width="1048" height="920" loading="lazy">
              <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Michael Brooks" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Michael Brooks"><span class="icon icon--play" aria-hidden="true"></span></button>
              <div class="card-testimonial__body">
                <figcaption class="card-testimonial__footer">
                  <p class="card-testimonial__author"><span><span class="card-testimonial__name">Michael Brooks,</span> Founder, Brooks &amp; Co.</span></p>
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
                  <img class="avatar avatar--portrait" src="assets/img/h1-testimonial-thumb-img-1.webp" alt="" width="80" height="80" loading="lazy">
                  <span><span class="card-testimonial__name">James Anderson,</span> Entrepreneur, Brand Strategist</span>
                </p>
              </figcaption>
            </figure>
          </div>
          <div class="swiper-slide carousel__slide">
            <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
              <img class="card-photo__img" src="assets/img/h1-testimonial-large-img-2.webp" alt="" width="1048" height="920" loading="lazy">
              <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Isabella Harris" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Isabella Harris"><span class="icon icon--play" aria-hidden="true"></span></button>
              <div class="card-testimonial__body">
                <figcaption class="card-testimonial__footer">
                  <p class="card-testimonial__author"><span><span class="card-testimonial__name">Isabella Harris,</span> CEO &amp; Founder</span></p>
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
                  <img class="avatar avatar--portrait" src="assets/img/h1-testimonial-thumb-img-2.webp" alt="" width="80" height="80" loading="lazy">
                  <span><span class="card-testimonial__name">David Thompson,</span> Sales Director, HR Consultant</span>
                </p>
              </figcaption>
            </figure>
          </div>
          <div class="swiper-slide carousel__slide">
            <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
              <img class="card-photo__img" src="assets/img/h1-testimonial-large-img-3.webp" alt="" width="1048" height="920" loading="lazy">
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
                  <img class="avatar avatar--portrait" src="assets/img/h1-testimonial-thumb-img-3.webp" alt="" width="80" height="80" loading="lazy">
                  <span><span class="card-testimonial__name">Sophia Martinez,</span> Marketing Director</span>
                </p>
              </figcaption>
            </figure>
          </div>
        </div>
      </div>
      <div class="dots dots--inverse" role="group" aria-label="Choose a story" data-carousel-dots="Show story"></div>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.testimonials + data-surface="inverse"` | Fondo oscuro; recorta los slides que sangran y la foto al radio |
| `.section-bg` | Capa de la foto (filter: blur(--blur-photo)) con el velo en ::after; patrón compartido con Feedback (About Us) |
| `.section-head--center + .eyebrow--inverse` | Encabezado centrado, eyebrow amarillo |
| `data-carousel-start="2"` | Arranca en el tercer testimonio, como el diseño |

## Tokens que consume

- `--blur-photo`
- `--color-background-inverse`
- `--radius-xl`
- `--spacing-9 / -10 / -11 / -12 / -13`
- `Eyebrow --inverse, Pagination Dots (átomos)`
- `Card Testimonial (molécula)`
- `Carousel, Video Modal (organismos)`

## Accesibilidad

Región «Client stories» con dots nombrados y `aria-current`. Play con `aria-haspopup="dialog"`. Foto decorativa con velo.

## Decisiones y excepciones

- Orden de los testimonios tomado del diseño: el parcial de la izquierda es un testimonio en video y Isabella (activa, tercer dot) es la tercera; Michael Brooks y Sophia Martinez son placeholder.
- Radio en las cuatro esquinas en mobile y solo arriba desde lg: así lo muestra cada PNG.
- Foto de fondo `h1-testimonial-bg-img` con `--blur-photo` y velo inverso al 85%, para que el texto blanco tenga contraste sobre la foto clara.
