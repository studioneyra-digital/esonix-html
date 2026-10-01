# Card Post

**Nivel:** Molécula · 06  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Post */`) · showcase en `dist/kit/index.html#card-post`

## Descripción

Entrada del blog: foto con fecha, título, extracto y «Read More» (con el título oculto para lectores).

## Snippets

**Dos posts**

```html
<article class="card-post">
  <div class="card-post__media">
    <img class="card-post__img" src="../assets/img/h1-blog-img-1.webp" alt="" width="1308" height="600" loading="lazy">
    <span class="badge badge--marker card-post__date"><time datetime="2026-10-21">21 Oct, 2026</time></span>
  </div>
  <div class="card-post__body">
    <h3 class="card-post__title">How Consulting Improves Business Performance</h3>
    <p>With expert advice & customized solutions, businesses can strengthen their competitive position</p>
    <a href="#card-post" class="link-arrow">
      Read More<span class="visually-hidden"> about how consulting improves business performance</span>
      <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
    </a>
  </div>
</article>
<article class="card-post">
  <div class="card-post__media">
    <img class="card-post__img" src="../assets/img/h1-blog-img-2.webp" alt="" width="1308" height="600" loading="lazy">
    <span class="badge badge--marker card-post__date"><time datetime="2026-10-18">18 Oct, 2026</time></span>
  </div>
  <div class="card-post__body">
    <h3 class="card-post__title">Effective Financial Planning for Sustainable Growth</h3>
    <p>Strong financial planning also supports investment in innovation, team development.</p>
    <a href="#card-post" class="link-arrow">
      Read More<span class="visually-hidden"> about effective financial planning for sustainable growth</span>
      <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
    </a>
  </div>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-post__media` | Foto 4:3 con esquinas redondeadas (la fuente es 1308×600; se recorta con cover) |
| `.card-post__date` | Posiciona el badge de fecha sobre la foto (usa badge--marker) |
| `.card-post__body` | Título (h3), extracto y enlace; sangría lateral de 20px |

## Tokens que consume

- `--radius-lg`
- `--spacing-3 / -4 / -5`
- `--text-h4`
- `--weight-medium`

## Accesibilidad

Fecha en `<time datetime>`; «Read More» con título oculto.

## Decisiones y excepciones

- El diseño recorta la foto a ~1.38:1; se usa 4:3 (estándar) en vez de un número suelto.
