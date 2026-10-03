# Why Choose Us

**Nivel:** Section · 04  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:why-choose-us -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#why-choose-us`

## Descripción

Texto + foto, con la Feature Strip (tres Card Feature en un contenedor blanco) montada sobre el borde inferior de la foto. Desde lg el texto se alinea con `.container` y la foto llega al borde de `.container-wide`. Mobile: apilado, la franja 92px sobre la foto.

## Snippet

```html
<section class="section why-choose" id="why-choose-us" aria-labelledby="why-choose-title">
  <div class="container-wide why-choose__grid">
    <div class="why-choose__intro" data-reveal>
      <p class="eyebrow">Why Choose Us</p>
      <h2 class="section-title why-choose__title" id="why-choose-title">Why Businesses Trust Our Consulting</h2>
      <p class="why-choose__text">We believe every business is unique, which is why we offer tailored consulting services &amp; ongoing support. By working closely with your team, &amp; future objectives.</p>
    </div>
    <img class="why-choose__media" src="assets/img/h1-why-choose-img.webp" alt="A consultant and a client reviewing a plan together at the office" width="1125" height="1095" loading="lazy" data-reveal="mask">
    <div class="feature-strip why-choose__strip">
      <article class="card-feature" data-reveal>
        <p class="card-feature__number" aria-hidden="true">01</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Tailored business solutions</h3>
          <p>We provide tailored business solution designed to match your unique goals</p>
        </div>
      </article>
      <article class="card-feature" data-surface="brand" data-reveal>
        <img class="card-feature__bg" src="assets/img/h1-feature-bg-image.webp" alt="" width="1320" height="960" loading="lazy">
        <p class="card-feature__number" aria-hidden="true">02</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Results-focused strategies</h3>
          <p>Our results-focused strategies are designed to deliver measurable business growth</p>
          <a href="#services" class="link-arrow link-arrow--inverse">
            Read More<span class="visually-hidden"> about results-focused strategies</span>
            <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
          </a>
        </div>
      </article>
      <article class="card-feature" data-reveal>
        <p class="card-feature__number" aria-hidden="true">03</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Proven success methods</h3>
          <p>With a focus on practical results, we create strategies that deliver lasting value</p>
        </div>
      </article>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.container-wide.why-choose__grid` | Grilla: --why-indent | texto 54fr | foto 46fr | --why-indent (columna central única bajo lg) |
| `--why-container / --why-indent` | Ancho de contenido del .container en cada breakpoint y la sangría que resulta; alinea el texto con las otras secciones |
| `.why-choose__intro / __title / __text` | Eyebrow, h2 (corta en 36rem, como el diseño) y párrafo |
| `.why-choose__media` | Foto 1125:1095 que ocupa las dos filas; se estira si el texto es más alto |
| `.feature-strip.why-choose__strip` | Franja blanca con borde: en fila desde lg, apilada antes; montada sobre la foto |
| `.feature-strip .card-feature` | Cards normales sin fondo ni sombra; alto mínimo 18rem (20rem desde lg) |

## Tokens que consume

- `--container-width`
- `--color-surface-default`
- `--color-border-subtle`
- `--radius-lg`
- `--shadow-sm`
- `--border-width-sm`
- `--spacing-3 / -4 / -5 / -9 / -10 / -11`
- `Eyebrow (átomo)`
- `Card Feature (molécula)`

## Accesibilidad

Orden del DOM = lectura (texto, foto, cards). Foto con `alt`; fondo de la card destacada decorativo. «Read More» con nombre completo por texto oculto.

## Decisiones y excepciones

- El «Read More» de la card 02 se mantiene también en mobile (decisión del usuario): el export mobile lo omite, se trata como omisión del export.
- Las columnas de la sangría (`--why-container`) usan los breakpoints de Bootstrap porque replican el ancho de su `.container`; excepción escrita en `design-tokens.md`.
- La Feature Strip vive en el bloque de Sections (no es una molécula del kit): solo la usa esta sección.
- Excepción declarada a anti-patrones #4 (card dentro de card): la Card Feature destacada vive dentro del contenedor blanco de la franja, como el diseño; las otras dos pierden fondo y sombra y se leen como columnas de la franja.
- «Read More» lleva a Services: el diseño no dice adónde va.
