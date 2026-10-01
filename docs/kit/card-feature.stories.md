# Card Feature

**Nivel:** Molécula · 02  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Feature */`) · showcase en `dist/kit/index.html#card-feature`

## Descripción

Card de argumento: número decorativo, título y texto. `data-surface="brand"` suma foto de fondo con velo petróleo y «Read More».

## Snippets

**Normal, destacada y normal**

```html
<article class="card-feature">
  <p class="card-feature__number" aria-hidden="true">01</p>
  <div class="card-feature__body">
    <h3 class="card-feature__title">Tailored business solutions</h3>
    <p>We provide tailored business solution designed to match your unique goals</p>
  </div>
</article>
<article class="card-feature" data-surface="brand">
  <img class="card-feature__bg" src="../assets/img/h1-feature-bg-image.webp" alt="" width="1320" height="960" loading="lazy">
  <p class="card-feature__number" aria-hidden="true">02</p>
  <div class="card-feature__body">
    <h3 class="card-feature__title">Results-focused strategies</h3>
    <p>Our results-focused strategies are designed to deliver measurable business growth</p>
    <a href="#card-feature" class="link-arrow link-arrow--inverse">
      Read More<span class="visually-hidden"> about results-focused strategies</span>
      <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
    </a>
  </div>
</article>
<article class="card-feature">
  <p class="card-feature__number" aria-hidden="true">03</p>
  <div class="card-feature__body">
    <h3 class="card-feature__title">Proven success methods</h3>
    <p>With a focus on practical results, we create strategies that deliver lasting value</p>
  </div>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-feature` | Card blanca; número arriba y texto abajo (justify space-between) |
| `.card-feature__number` | Número decorativo en gris claro (aria-hidden) |
| `.card-feature__bg` | Foto de fondo (solo en la destacada); queda bajo el velo |
| `data-surface="brand"` | Destacada: velo petróleo al 85% sobre la foto, número amarillo y texto claro |

## Tokens que consume

- `--color-surface-default`
- `--color-border-default (número)`
- `--color-action-primary (velo)`
- `--color-text-highlight`
- `--radius-lg`
- `--spacing-3 / -7 / -10`
- `--text-h4 / -h5`

## Accesibilidad

Número `aria-hidden` (no es una secuencia); «Read More» con texto oculto que dice de qué habla.

## Decisiones y excepciones

- El diseño pega las tres cards en una franja con un contenedor blanco redondeado; ese contenedor (y el recorte de las esquinas) es de la Section, no de la card.
- El velo petróleo del diseño deja ver la foto con tinte verde; se resuelve con `color-mix()` del token de acción al 85%.
