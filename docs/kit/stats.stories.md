# Stats

**Nivel:** Section · 07  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:stats -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#stats`

## Descripción

Solo mobile. Pastilla sobre filete a todo el ancho, título y tres Stat centrados entre filetes, con indicador de 3 cuadritos (1/2/3 encendidos, decorativo). Oculta desde lg.

## Snippet

```html
<section class="section stats" id="stats" aria-labelledby="stats-title">
  <p class="stats__pill"><span>4,000+ Clients Trust Our Expertise</span></p>
  <div class="container">
    <h2 class="stats__title" id="stats-title">Facts prove the outcome</h2>
    <ul class="stats__list" role="list">
      <li class="stats__item">
        <div class="stat stat--center">
          <p class="stat__value">98%</p>
          <p>Excellence in Customer Satisfaction</p>
        </div>
        <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span></span><span></span></span>
      </li>
      <li class="stats__item">
        <div class="stat stat--center">
          <p class="stat__value">12K<span class="stat__suffix">+</span></p>
          <p>Projects Successfully Finished</p>
        </div>
        <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span class="is-on"></span><span></span></span>
      </li>
      <li class="stats__item">
        <div class="stat stat--center">
          <p class="stat__value">30<span class="stat__suffix">+</span></p>
          <p>Years of Consulting Experience</p>
        </div>
        <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span class="is-on"></span><span class="is-on"></span></span>
      </li>
    </ul>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.stats` | display: none desde lg |
| `.stats__pill` | Pastilla centrada; los filetes a los costados son ::before / ::after |
| `h2.stats__title` | Título de la sección, 22px centrado (corta en 12rem, como el diseño) |
| `ul.stats__list / .stats__item` | Lista de cifras entre filetes |
| `.stats__level + aria-hidden / .is-on` | Indicador decorativo de tres cuadritos |

## Tokens que consume

- `--color-border-default`
- `--color-action-primary`
- `--radius-full`
- `--text-h5`
- `--weight-medium`
- `--spacing-2 / -5 / -7 / -8`
- `Stat --center (molécula)`

## Accesibilidad

Lista nombrada por su `<h2>`; indicador `aria-hidden`. Desde lg, `display: none` (sin duplicar contenido).

## Decisiones y excepciones

- Solo mobile, decisión del equipo (el diseño desktop no la muestra).
- «Years of Consulting Experience» es placeholder (decisión del equipo): el diseño muestra «30+» sin etiqueta.
- El indicador de cuadritos no tiene equivalente en el kit y solo lo usa esta sección: vive en el bloque de Sections, no como átomo.
- Las cifras usan `--text-h1` (36px en mobile); el diseño mide ≈ 42px. Se mantiene el token.
