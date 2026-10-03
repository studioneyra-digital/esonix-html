# Feedback

**Nivel:** Section · 16  
**Dónde:** markup en `dist/about-us.html` (entre `<!-- section:feedback -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#feedback`

## Descripción

Bloque oscuro con `.section-bg`, encabezado centrado y Carousel `--fade` de 3 citas con dots. Radio abajo (desktop) / arriba (mobile). Reserva `--quote-form-overlap` abajo.

## Snippet

```html
<section class="section feedback" aria-labelledby="feedback-title" data-surface="inverse">
  <div class="section-bg">
    <img src="assets/img/about-video-bg.webp" alt="" width="1920" height="1334" loading="lazy">
  </div>
  <div class="container">
    <div class="section-head section-head--center">
      <div class="section-head__main">
        <p class="eyebrow eyebrow--center eyebrow--inverse">Client Feedback</p>
        <h2 class="section-title section-head__title" id="feedback-title">Client Stories That Speak for Themselves</h2>
      </div>
    </div>
    <div class="carousel carousel--fade" id="carousel-quotes" data-carousel data-carousel-fade role="region" aria-roledescription="carousel" aria-label="Client quotes">
      <div class="swiper carousel__viewport">
        <div class="swiper-wrapper">
          <div class="swiper-slide carousel__slide">
            <figure class="feedback__quote">
              <blockquote class="feedback__text"><p>“Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy, every recommendation was practical, well-researched, &amp; tailored to our goals.”</p></blockquote>
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
              <figcaption class="feedback__author"><strong>Isabella Harris,</strong> CEO &amp; Founder</figcaption>
            </figure>
          </div>
        </div>
      </div>
      <div class="dots dots--inverse" role="group" aria-label="Choose a quote" data-carousel-dots="Show quote"></div>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.feedback + data-surface="inverse"` | Fondo oscuro; recorta la foto al radio |
| `.section-bg` | Capa de la foto desenfocada con el velo inverso al 85% |
| `.carousel.carousel--fade + data-carousel-fade` | Una cita por vez con fundido; dots generados por main.js |
| `figure.feedback__quote / .feedback__text / .feedback__author` | Comillas ámbar (::before), cita de 18/24px y autor |
| `--quote-form-overlap` | Lo que el Quote Form sube sobre el bloque: 80px en mobile, 96px desde lg |

## Tokens que consume

- `--blur-photo`
- `--color-background-inverse`
- `--color-text-highlight`
- `--text-h4 / -h6 / -display`
- `--radius-xl`
- `--spacing-6 / -7 / -10 / -11 / -12 / -13`
- `Eyebrow --inverse, Pagination Dots (átomos)`
- `Carousel (organismo)`

## Accesibilidad

Región «Client quotes», dots nombrados con `aria-current`; `<figure>` + `<blockquote>` + `<figcaption>`. Sin autoplay (WCAG 2.2.2); reduced motion: instantáneo.

## Decisiones y excepciones

- Tres citas: David Thompson (diseño) y las de James Anderson e Isabella Harris, con su texto de la Home (decisión del usuario).
- El diseño desktop marca activo el segundo dot y el mobile el primero; se arranca en David Thompson (primer dot).
- Fondo: `about-video-bg.webp` con el tratamiento de Testimonials, extraído al patrón `.section-bg` (Testimonials migró a él sin cambios visuales).
