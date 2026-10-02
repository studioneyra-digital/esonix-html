# Word List

**Nivel:** Organismo · 06  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Word List */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#word-list`

## Descripción

Bloque Finance/Advisory/Growth/Strategy. Desde `lg`: palabras grandes (nítida la activa, desenfocadas las demás) + una Card Project por palabra superpuesta; `main.js` activa la que cruza el centro del viewport (ScrollTrigger, sin pin). Bajo `lg`: «Works» gigante y tenue (decorativo) + cards apiladas, sin efecto.

## Snippets

**Growth activa (estado inicial, como el diseño), sobre fondo oscuro**

```html
<div class="word-list" data-word-list>
  <h2 class="visually-hidden">Works</h2>
  <p class="word-list__watermark" aria-hidden="true">Works</p>
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
| `h2.visually-hidden` | Título real de la sección, solo para lectores (el diseño no lo muestra) |
| `.word-list__watermark + aria-hidden` | «Works» gigante y tenue, decorativo; solo bajo lg |
| `.word-list__words / __word` | Columna de palabras (desde lg): desenfocadas con --blur-text, nítida con .is-active |
| `data-word-for` | En cada palabra: id de su Card Project |
| `.word-list__media / __card` | Cards superpuestas (desde lg, grid-area 1 / 1); bajo lg, apiladas |
| `.is-active` | Lo pone main.js en la palabra y la card activas (el markup trae el estado inicial) |

## Tokens que consume

- `--text-display`
- `--weight-semibold`
- `--leading-tight`
- `--tracking-tight`
- `--color-text-inverse`
- `--color-background-muted (watermark)`
- `--blur-text`
- `--spacing-5 / -6 / -8 / -12`
- `--ease-slow`
- `Card Project (molécula)`

## Accesibilidad

Palabras como contenido real (desenfoque solo visual). `<h2>` oculto como título; «Works» visible `aria-hidden` (gris tenue, sin AA). Con reduced motion no se inicia el ScrollTrigger. Sin JS, cards apiladas.

## Decisiones y excepciones

- Sin `pin`: las palabras no fijan la sección ni estiran el alto artificialmente (evita los bugs de ScrollTrigger + Lenis con pin que advierte `CLAUDE.md`); el alto de scroll lo dan las propias palabras en `--text-display`.
- Activación por cruce del centro del viewport (`ScrollTrigger.create` por palabra, `onEnter`/`onEnterBack`), no por click: el diseño liga el cambio al scroll.
- Inactivas desenfocadas con el token nuevo `--blur-text` (4px) y blanco al 80%, como el diseño. Excepción declarada a contraste AA: es texto en segundo plano a propósito; la palabra activa, la que se lee en cada posición de scroll, tiene contraste completo.
- «Works» en mobile: el diseño lo muestra gigante en gris tenue sobre crema. Se deja decorativo (`aria-hidden`) y el `<h2>` real va oculto (decisión del equipo).
- Solo Finance (Corporate Finance Management) sale del diseño; Advisory, Growth y Strategy son placeholder, con las otras 3 imágenes de portfolio. El export mobile repite «// 01» en todas las cards: no se replica.
- Estado inicial Growth activa, igual que el diseño (el PNG es una sola captura de una posición de scroll).
