# Finance

**Nivel:** Section · 05  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:finance -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#finance`

## Descripción

Word List como sección. Desde lg: bloque a todo el ancho (radio 40px) con foto desenfocada fija detrás, contenido centrado y la Card Project de 524px a la derecha. Bajo lg: «Works» tenue y cards apiladas.

## Snippet

```html
<section class="section finance" id="finance" aria-labelledby="works-title">
  <div class="finance__media">
    <img src="assets/img/h1-portfolio-img-3.webp" alt="" width="1920" height="1084" loading="lazy">
  </div>
  <div class="container">
    <div class="word-list" data-word-list>
      <h2 class="visually-hidden" id="works-title">Works</h2>
      <p class="word-list__watermark" aria-hidden="true">Works</p>
      <ul class="word-list__words" role="list">
        <li><span class="word-list__word" data-word-for="word-finance">Finance</span></li>
        <li><span class="word-list__word" data-word-for="word-advisory">Advisory</span></li>
        <li><span class="word-list__word is-active" data-word-for="word-growth">Growth</span></li>
        <li><span class="word-list__word" data-word-for="word-strategy">Strategy</span></li>
      </ul>
      <div class="word-list__media">
        <article class="card-project word-list__card" id="word-finance">
          <img class="card-project__img" src="assets/img/h1-portfolio-img-3.webp" alt="" width="1920" height="1084" loading="lazy">
          <div class="card-project__caption">
            <span class="card-project__index" aria-hidden="true">// 01</span>
            <h3 class="card-project__title">Corporate Finance Management</h3>
          </div>
        </article>
        <article class="card-project word-list__card" id="word-advisory">
          <img class="card-project__img" src="assets/img/h1-portfolio-img-1.webp" alt="" width="1920" height="1076" loading="lazy">
          <div class="card-project__caption">
            <span class="card-project__index" aria-hidden="true">// 02</span>
            <h3 class="card-project__title">Advisory Services</h3>
          </div>
        </article>
        <article class="card-project word-list__card is-active" id="word-growth">
          <img class="card-project__img" src="assets/img/h1-portfolio-img-2.webp" alt="" width="1920" height="765" loading="lazy">
          <div class="card-project__caption">
            <span class="card-project__index" aria-hidden="true">// 03</span>
            <h3 class="card-project__title">Growth Strategy Planning</h3>
          </div>
        </article>
        <article class="card-project word-list__card" id="word-strategy">
          <img class="card-project__img" src="assets/img/h1-portfolio-img-4.webp" alt="" width="1920" height="1076" loading="lazy">
          <div class="card-project__caption">
            <span class="card-project__index" aria-hidden="true">// 04</span>
            <h3 class="card-project__title">Market Strategy Execution</h3>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.finance + aria-labelledby="works-title"` | Desde lg: bloque de 59rem de alto mínimo con clip-path redondeado |
| `.finance__media` | Capa position: fixed con la foto (filter: blur(--blur-photo)) y el velo; el clip-path de la sección la recorta |
| `.finance .word-list__media` | Columna de cards acotada a 524px, alineada a la derecha con 20px de margen |
| `h2#works-title.visually-hidden` | Nombre de la sección (el diseño no muestra título en desktop) |

## Tokens que consume

- `--blur-photo (nuevo)`
- `--radius-xl`
- `--color-overlay`
- `--color-background-inverse`
- `--spacing-5`
- `Word List (organismo)`
- `Card Project (molécula)`

## Accesibilidad

Nombrada por el `<h2>` oculto «Works». Foto decorativa que no se carga bajo lg. El velo da contraste a la palabra activa. Reduced motion: queda Growth activa.

## Decisiones y excepciones

- Foto fija sin `background-attachment: fixed` (iOS lo ignora y un `filter` en el mismo elemento lo rompe): es una capa `position: fixed` dentro de la sección, recortada por su `clip-path` (que, a diferencia de `overflow`, sí recorta descendientes fijos). Se agranda el doble del desenfoque por lado para que el borde difuminado no se vea.
- Token nuevo `--blur-photo` (12px) junto a `--blur-text` y `--blur-backdrop`; va en `filter` sobre la imagen, nunca en `backdrop-filter`.
- Velo `--color-overlay` (65%), algo más denso que el diseño: la palabra activa en blanco pasa sobre la zona clara de la foto.
- El bloque mide 1905px de ancho en el PNG (artefacto del export): se trata como 100%.
