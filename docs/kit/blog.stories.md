# Blog

**Nivel:** Section · 12  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:blog -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#blog`

## Descripción

Section Head `--center`, tres Card Post en `.container-wide` (3 columnas desde lg) y «View All Blog» centrado.

## Snippet

```html
<section class="section blog" id="blog" aria-labelledby="blog-title">
  <div class="container">
    <div class="section-head section-head--center">
      <div class="section-head__main">
        <p class="eyebrow eyebrow--center">Latest Blog Post</p>
        <h2 class="section-title section-head__title" id="blog-title">Latest Business Insights &amp;&nbsp;Expert Advice</h2>
      </div>
    </div>
  </div>
  <div class="container-wide">
    <div class="blog__grid">
      <article class="card-post">
        <div class="card-post__media">
          <img class="card-post__img" src="assets/img/h1-blog-img-1.webp" alt="" width="1308" height="600" loading="lazy">
          <span class="badge badge--marker card-post__date"><time datetime="2026-10-21">21 Oct, 2026</time></span>
        </div>
        <div class="card-post__body">
          <h3 class="card-post__title">How Consulting Improves Business Performance</h3>
          <p>With expert advice &amp; customized solutions, businesses can strengthen their competitive position</p>
          <a href="#" class="link-arrow">
            Read More<span class="visually-hidden"> about how consulting improves business performance</span>
            <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
          </a>
        </div>
      </article>
      <article class="card-post">
        <div class="card-post__media">
          <img class="card-post__img" src="assets/img/h1-blog-img-2.webp" alt="" width="1308" height="600" loading="lazy">
          <span class="badge badge--marker card-post__date"><time datetime="2026-10-18">18 Oct, 2026</time></span>
        </div>
        <div class="card-post__body">
          <h3 class="card-post__title">Effective Financial Planning for Sustainable Growth</h3>
          <p>Strong financial planning also supports investment in innovation, team development.</p>
          <a href="#" class="link-arrow">
            Read More<span class="visually-hidden"> about effective financial planning for sustainable growth</span>
            <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
          </a>
        </div>
      </article>
      <article class="card-post">
        <div class="card-post__media">
          <img class="card-post__img" src="assets/img/h1-blog-img-3.webp" alt="" width="1308" height="600" loading="lazy">
          <span class="badge badge--marker card-post__date"><time datetime="2026-10-07">07 Oct, 2026</time></span>
        </div>
        <div class="card-post__body">
          <h3 class="card-post__title">Key Steps to Achieve Sustainable Business Growth</h3>
          <p>Companies that focus on long-term success prioritize strong customer relationships.</p>
          <a href="#" class="link-arrow">
            Read More<span class="visually-hidden"> about key steps to achieve sustainable business growth</span>
            <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
          </a>
        </div>
      </article>
    </div>
    <div class="blog__actions">
      <a href="#" class="btn">
        View All Blog
        <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
      </a>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.blog__grid` | Una columna en mobile; 3 columnas desde lg (524px a 1920) |
| `.blog__actions` | Fila centrada del botón |
| `&&nbsp;Expert` | Espacio duro: el título corta antes de «& Expert Advice», como el diseño |

## Tokens que consume

- `--spacing-6 / -9 / -10`
- `Eyebrow, Button, Badge, Link Arrow (átomos)`
- `Card Post (molécula)`

## Accesibilidad

«Read More» con el título oculto; fechas con `<time datetime>`; fotos decorativas.

## Decisiones y excepciones

- El export desktop repite el encabezado del Blog (uno cortado encima del otro): se trata como artefacto y va uno solo.
- Los «Read More» y «View All Blog» llevan a `#`: no hay páginas de blog todavía.
