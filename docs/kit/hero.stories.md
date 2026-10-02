# Hero

**Nivel:** Section · 01  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:hero -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#hero`

## Descripción

Foto a sangre con velo; texto + «Get Started»; Card Hero escalonada a la derecha; franja inferior con el `<h1>` («Expert Guidance for —» + «FutureGrowth» en `--text-hero`). Reserva el alto del header fijo.

## Snippet

```html
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media">
    <picture>
      <source media="(max-width: 29.99rem)" srcset="assets/img/h1-hero-img-mobile.webp" width="800" height="1000">
      <img src="assets/img/h1-hero-img.webp" alt="" width="1920" height="1000" fetchpriority="high">
    </picture>
  </div>
  <div class="container-wide hero__top">
    <div class="hero__intro">
      <p>We work closely with businesses to identify opportunities, solve complex problems and develop strategies</p>
      <a href="#what-we-do" class="btn btn--light">
        Get Started
        <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
      </a>
    </div>
    <div class="card-hero hero__card">
      <img class="card-hero__media" src="assets/img/h1-hero-thumb-img.webp" alt="" width="320" height="364">
      <div class="card-hero__body">
        <span class="card-hero__index">01</span>
        <p class="card-hero__title">Creative Business Insights</p>
      </div>
    </div>
  </div>
  <div class="hero__bottom">
    <div class="container-wide">
      <h1 class="hero__title" id="hero-title">
        <span class="hero__kicker">Expert Guidance for</span>
        <span class="hero__headline">Future<span class="visually-hidden"> </span>Growth</span>
      </h1>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.hero + aria-labelledby` | Sección con la foto de fondo; recorta lo que sangre |
| `.hero__media` | Capa de la foto (object-fit: cover) con el velo en ::after |
| `.container-wide.hero__top` | Contenedor ancho (1620px) con el texto y la card; desde lg, card en la segunda fila y segunda columna |
| `.hero__intro` | Filete corto (276px), texto y botón claro |
| `.card-hero.hero__card` | Card Hero: 360px en mobile, 445px desde lg |
| `.hero__bottom` | Franja con filete a todo el ancho |
| `h1.hero__title / __kicker / __headline` | El titular: kicker con raya y «FutureGrowth» a la derecha desde lg |

## Tokens que consume

- `--text-hero`
- `--text-h4 / -h6`
- `--weight-semibold`
- `--tracking-tight`
- `--color-overlay / -overlay-light`
- `--color-text-inverse / -inverse-secondary`
- `--header-offset`
- `--spacing-4 / -5 / -6 / -7 / -8 / -9 / -13`
- `Button --light, Card Hero`

## Accesibilidad

Único `<h1>`. Foto decorativa (`alt=""`), con `fetchpriority="high"` y preload (LCP); el velo da contraste al texto. «Get Started» enlaza a la sección siguiente.

## Decisiones y excepciones

- Contenedor ancho de 1620px (el del header), medido en el diseño: el texto arranca en x=150 a 1920.
- Card Hero escalonada (debajo del texto, a la derecha), como el diseño; en mobile va a la derecha con 360px.
- En mobile la Card Hero achica su foto a 140px y su título a 18px (`--text-h6`), que es lo que mide el diseño.
- El kicker anula el `letter-spacing` apretado que el `h1` trae de foundations: está pensado para el titular gigante.
- «Get Started» del hero lleva a What We Do: el diseño no dice adónde va.
