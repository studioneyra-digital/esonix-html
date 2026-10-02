# Word List

**Nivel:** Organismo · 06  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Word List */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#word-list`

## Descripción

Bloque Finance/Advisory/Growth/Strategy: desde `lg`, palabras grandes (contorno si inactivas) + una Card Project por palabra superpuesta; `main.js` activa la más cercana al centro del viewport al cruzarlo (ScrollTrigger, sin pin). Bajo `lg`: eyebrow «Works» + cards apiladas, sin efecto.

## Snippets

**Growth activa (estado inicial, como el diseño)**

```html
<div class="word-list" data-word-list>
  <p class="eyebrow word-list__eyebrow">Works</p>
  <ul class="word-list__words" role="list">
    <li><span class="word-list__word" data-word-for="word-finance">Finance</span></li>
    <li><span class="word-list__word" data-word-for="word-advisory">Advisory</span></li>
    <li><span class="word-list__word is-active" data-word-for="word-growth">Growth</span></li>
    <li><span class="word-list__word" data-word-for="word-strategy">Strategy</span></li>
  </ul>
  <div class="word-list__media">
  <article class="card-project word-list__card" id="word-finance">
    <img class="card-project__img" src="../assets/img/h1-portfolio-img-3.webp" alt="" width="1920" height="1084" loading="lazy">
    <div class="card-project__caption">
      <span class="card-project__index" aria-hidden="true">// 01</span>
      <h3 class="card-project__title">Corporate Finance Management</h3>
    </div>
  </article>
  <article class="card-project word-list__card" id="word-advisory">
    <img class="card-project__img" src="../assets/img/h1-portfolio-img-1.webp" alt="" width="1920" height="1076" loading="lazy">
    <div class="card-project__caption">
      <span class="card-project__index" aria-hidden="true">// 02</span>
      <h3 class="card-project__title">Advisory Services</h3>
    </div>
  </article>
  <article class="card-project word-list__card is-active" id="word-growth">
    <img class="card-project__img" src="../assets/img/h1-portfolio-img-2.webp" alt="" width="1920" height="765" loading="lazy">
    <div class="card-project__caption">
      <span class="card-project__index" aria-hidden="true">// 03</span>
      <h3 class="card-project__title">Growth Strategy Planning</h3>
    </div>
  </article>
  <article class="card-project word-list__card" id="word-strategy">
    <img class="card-project__img" src="../assets/img/h1-portfolio-img-4.webp" alt="" width="1920" height="1076" loading="lazy">
    <div class="card-project__caption">
      <span class="card-project__index" aria-hidden="true">// 04</span>
      <h3 class="card-project__title">Market Strategy Execution</h3>
    </div>
  </article>
  </div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.word-list + data-word-list` | Contenedor; main.js lo inicia al acercarse al viewport |
| `.word-list__eyebrow` | Eyebrow «Works» (bajo lg; oculto desde lg) |
| `.word-list__words / __word` | Columna de palabras (desde lg); contorno con color-mix, sólida con .is-active |
| `data-word-for` | En cada palabra: id de su Card Project |
| `.word-list__media / __card` | Pila de Card Project (desde lg, superpuestas con grid-area); bajo lg, lista normal |
| `.is-active` | Lo pone main.js en la palabra y la card activas (o el markup, como estado inicial) |

## Tokens que consume

- `--text-giant`
- `--weight-bold`
- `--leading-tight`
- `--color-text-inverse`
- `--border-width-sm`
- `--spacing-2 / -5 / -9 / -12`
- `--ease-slow`
- `Eyebrow (átomo)`
- `Card Project (molécula)`

## Accesibilidad

Palabras como contenido real, sin `aria-hidden`; el énfasis visual no mueve el foco. Con reduced motion, `main.js` no inicia el ScrollTrigger (queda el estado del markup). Sin JS, se ven todas las cards apiladas.

## Decisiones y excepciones

- Sin `pin`: a diferencia de otros sitios con este patrón, las palabras no fijan la sección ni estiran el alto artificialmente (evita los bugs de ScrollTrigger + Lenis con pin que advierte `CLAUDE.md`); el alto de scroll lo dan las propias palabras en tipografía `--text-giant`.
- Activación por proximidad al centro del viewport (`ScrollTrigger.create` por palabra, `onEnter`/`onEnterBack`), no por click: el diseño muestra el cambio ligado al scroll, no una interacción.
- Solo Finance (Corporate Finance Management) sale del diseño; Advisory, Growth y Strategy son placeholder, con las 3 imágenes de portfolio restantes.
- Estado inicial Growth activa, igual que el diseño (el PNG es una sola captura de una posición de scroll).
- Excepción declarada a contraste AA en las palabras inactivas (solo contorno, relleno transparente): es el mismo efecto «fantasma» del diseño, pensado como fondo/anticipo, no como el texto a leer en ese instante — la palabra activa (la que importa en cada posición de scroll) tiene contraste completo, y en mobile las cuatro cards muestran sus títulos con contraste completo siempre.
