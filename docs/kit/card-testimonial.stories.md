# Card Testimonial

**Nivel:** Molécula · 04  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Testimonial */`) · showcase en `dist/kit/index.html#card-testimonial`

## Descripción

Reseña en `<figure>`: cita y autor. La de texto va en petróleo; `--video` es una foto con botón de play (`data-video-id`).

## Snippets

**De texto**

```html
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
```

**En video (`--video`)**

```html
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
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-testimonial` | Contenedor del testimonio (figure); en la de texto, cita arriba y autor abajo |
| `.card-testimonial__quote` | La cita en 24px medium; es un blockquote |
| `.card-testimonial__footer` | Divisor + autor (figcaption) |
| `.card-testimonial__name` | Nombre del autor en amarillo; el cargo va en blanco a continuación |
| `.card-testimonial--video` | Versión en foto (con card-photo): play centrado y autor sobre la cita |
| `data-video-id / data-video-title` | ID y título del video de YouTube: el botón abre el Video Modal (organismo) |

## Tokens que consume

- `--color-action-primary (via data-surface="brand")`
- `--color-text-inverse / -highlight`
- `--color-overlay-light (divisor)`
- `--text-h4`
- `--leading-normal`
- `--radius-lg`
- `--spacing-4 / -5 / -6 / -8`
- `--scrim (card-photo)`

## Accesibilidad

`figure`/`blockquote`/`figcaption`; play con `aria-label`; texto sobre velo de 92%.

## Decisiones y excepciones

- El video del diseño es el de YouTube indicado por el equipo (`RqueNBILfVU`); lo reproduce el organismo Video Modal.
- En el diseño el avatar del autor de texto es un retrato cuadrado de 75px; aquí usa el átomo `avatar--portrait` (80px).
