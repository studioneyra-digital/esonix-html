# What We Do

**Nivel:** Section · 02  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:what-we-do -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#what-we-do`

## Descripción

Eyebrow + filete; grilla de áreas. Desktop: 3M+ y foto grande a la izquierda; título, texto, barras + CTA y foto chica a la derecha. Mobile: título, texto, foto chica, barras, 3M+, foto grande, sin duplicar contenido.

## Snippet

```html
<section class="section what-we-do" id="what-we-do" aria-labelledby="what-we-do-title">
  <div class="container">
    <div class="what-we-do__head" data-reveal>
      <p class="eyebrow">What We Do</p>
      <hr class="divider">
    </div>
    <div class="what-we-do__grid">
      <h2 class="section-title what-we-do__title" id="what-we-do-title" data-reveal>Driving business growth through smart strategy and expert guidance</h2>
      <p class="what-we-do__text" data-reveal>We believe every business has the potential to grow with the right strategy and support. By understanding your goals, challenges, and vision, we create customized consulting solutions</p>
      <div class="what-we-do__bars" data-reveal>
        <div class="what-we-do__progress">
          <div class="progress" style="--progress: 90" data-count>
            <div class="progress__head">
              <label for="progress-operational">Operational assessment</label>
              <span aria-hidden="true">90%</span>
            </div>
            <progress class="progress__bar" id="progress-operational" value="90" max="100">90%</progress>
          </div>
          <div class="progress" style="--progress: 76" data-count>
            <div class="progress__head">
              <label for="progress-consultation">Consultation &amp; analysis</label>
              <span aria-hidden="true">76%</span>
            </div>
            <progress class="progress__bar" id="progress-consultation" value="76" max="100">76%</progress>
          </div>
          <div class="progress" style="--progress: 85" data-count>
            <div class="progress__head">
              <label for="progress-strategic">Strategic interpretation</label>
              <span aria-hidden="true">85%</span>
            </div>
            <progress class="progress__bar" id="progress-strategic" value="85" max="100">85%</progress>
          </div>
        </div>
        <a href="contact.html" class="btn">
          Get Started
          <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
        </a>
      </div>
      <div class="what-we-do__stat" data-reveal>
        <div class="stat">
          <p class="stat__value" data-count>3M<span class="stat__suffix">+</span></p>
          <p>People Using Our Platform</p>
        </div>
        <div class="avatar-stack">
          <img class="avatar" src="assets/img/h1-testimonial-thumb-img-1.webp" alt="" width="40" height="40" loading="lazy">
          <img class="avatar" src="assets/img/h1-testimonial-thumb-img-2.webp" alt="" width="40" height="40" loading="lazy">
          <img class="avatar" src="assets/img/h1-testimonial-thumb-img-3.webp" alt="" width="40" height="40" loading="lazy">
          <span class="avatar-stack__more"><span class="icon icon--plus" aria-hidden="true"></span></span>
        </div>
      </div>
      <div class="photo-frame what-we-do__img1" data-reveal="mask">
        <img src="assets/img/h1-about-img-1.webp" alt="Three consultants smiling while they review a plan together" width="735" height="720" loading="lazy">
      </div>
      <div class="photo-frame what-we-do__img2" data-reveal="mask">
        <img src="assets/img/h1-about-img-2.webp" alt="Two colleagues reviewing results on a tablet" width="420" height="480" loading="lazy">
      </div>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.what-we-do` | Sección con el padding vertical del theme (en mobile, 32px arriba, como el diseño) |
| `.what-we-do__head` | Eyebrow y filete (Divider) |
| `.what-we-do__grid` | Grilla de áreas: una columna en mobile; desde lg 5fr 4fr 3fr con 64px de separación |
| `.section-title` | h2 con el tamaño de --text-h1 |
| `.what-we-do__bars / __progress` | Barras de Progress (con --progress) y el CTA |
| `.what-we-do__stat` | Stat 3M+ y Avatar Stack, repartidos a los extremos |
| `.photo-frame` | Foto con marco blanco de 8px; __img1 cuadrada, __img2 7:8 |

## Tokens que consume

- `--text-h1`
- `--color-surface-default`
- `--radius-lg / -md`
- `--shadow-sm`
- `--spacing-2 / -4 / -6 / -7 / -8 / -9 / -10 / -12`
- `Eyebrow, Divider, Progress, Button, Avatar Stack (átomos)`
- `Stat (molécula)`

## Accesibilidad

Orden del DOM = orden de lectura; la grilla solo reacomoda la vista. Barras con `<progress>` + `<label for>`. Fotos con `alt` descriptivo; avatares decorativos.

## Decisiones y excepciones

- Grilla CSS con los breakpoints del theme en vez de las columnas de Bootstrap: las proporciones del diseño (500 / 400 / 290px a 1920) no caen en 12 columnas con gutter, y el lg de Bootstrap (992px) no es el del theme (1024px).
- Avatar Stack del kit (avatares de los testimonios) en vez del PNG horneado `h1-about-users.png`, que trae las caras y el «+» en una sola imagen.
- El export mobile repite la primera barra («Operational assessment 90%»): no se replica.
- El h2 mide ≈50px en desktop (`--text-h1` da 48) y ≈32px en mobile (`--text-h1` da 36); se mantiene el token.
- El CTA lleva al footer (contacto): el diseño no dice adónde va.
