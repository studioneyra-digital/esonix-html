# Card Pricing

**Nivel:** Molécula · 03  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Pricing */`) · showcase en `dist/kit/index.html#card-pricing`

## Descripción

Plan de precios: ícono, nombre, precio, botón y lista. `data-surface="brand"` lo destaca (petróleo, botón amarillo). El último beneficio va atenuado.

## Snippets

**Starter, Enterprise (destacado) y Premium**

```html
<article class="card-pricing">
  <header class="card-pricing__head">
    <span class="card-pricing__icon"><span class="icon icon--rocket" aria-hidden="true"></span></span>
    <div>
      <h3 class="card-pricing__name">Starter Plan</h3>
      <p>Core strategies for business success</p>
    </div>
  </header>
  <p class="card-pricing__price"><span class="card-pricing__amount">$39.9</span> <span>/ Month</span></p>
  <a href="#card-pricing" class="btn btn--block">
    Get Started
    <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
  </a>
  <ul class="card-pricing__list">
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Growth Recommendations</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Monthly Strategy Consultation</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Basic Market Analysis</li>
    <li class="card-pricing__item is-muted"><span class="icon icon--circle-check" aria-hidden="true"></span> Email support</li>
  </ul>
</article>
<article class="card-pricing" data-surface="brand">
  <header class="card-pricing__head">
    <span class="card-pricing__icon"><span class="icon icon--award" aria-hidden="true"></span></span>
    <div>
      <h3 class="card-pricing__name">Enterprise Plan</h3>
      <p>Drive innovation & long-term success</p>
    </div>
  </header>
  <p class="card-pricing__price"><span class="card-pricing__amount">$49.9</span> <span>/ Month</span></p>
  <a href="#card-pricing" class="btn btn--block btn--accent">
    Get Started
    <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
  </a>
  <ul class="card-pricing__list">
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Customized Business Strategy</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Advanced Market Research</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Ongoing Performance Monitoring</li>
    <li class="card-pricing__item is-muted"><span class="icon icon--circle-check" aria-hidden="true"></span> Priority Support & Advisory</li>
  </ul>
</article>
<article class="card-pricing">
  <header class="card-pricing__head">
    <span class="card-pricing__icon"><span class="icon icon--gem" aria-hidden="true"></span></span>
    <div>
      <h3 class="card-pricing__name">Premium Features</h3>
      <p>Unlock greater efficiency and growth</p>
    </div>
  </header>
  <p class="card-pricing__price"><span class="card-pricing__amount">$59.9</span> <span>/ Month</span></p>
  <a href="#card-pricing" class="btn btn--block">
    Get Started
    <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
  </a>
  <ul class="card-pricing__list">
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Long-Term Success Planning</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Actionable Growth Strategies</li>
    <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Industry Expert Guidance</li>
    <li class="card-pricing__item is-muted"><span class="icon icon--circle-check" aria-hidden="true"></span> Dedicated Business Support</li>
  </ul>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-pricing` | Card blanca en grilla; ícono + nombre arriba, precio, botón y lista |
| `.card-pricing__price / __amount` | Precio en Mona Sans semibold del tamaño de h1; «/ Month» va atenuado |
| `.card-pricing__list / __item` | Panel con borde que contiene los beneficios con check relleno |
| `.is-muted` | Beneficio atenuado (solo énfasis visual, no cambia el significado) |
| `data-surface="brand"` | Plan destacado: petróleo, lista en panel claro translúcido; usa btn--accent en el botón |

## Tokens que consume

- `--color-surface-default / -background-subtle`
- `--shadow-sm`
- `--radius-lg / -md`
- `--text-h1 / -h4`
- `--color-action-primary`
- `--color-overlay-light (panel destacado)`
- `--color-text-tertiary / -inverse-secondary (atenuado)`
- `--spacing-3 / -5 / -6 / -9`

## Accesibilidad

Nombre `h3`; beneficios en `<ul>`; check `aria-hidden`; atenuado ≥ AA; «Get Started» repetido puede llevar texto oculto con el plan.

## Decisiones y excepciones

- **Excepción a anti-patrones #4 (card anidada):** la lista de beneficios es un panel con borde dentro de la card porque el diseño lo muestra así. Se declara aquí en lugar de ignorarla.
- El último beneficio atenuado no se marca como «no incluido»: el diseño solo lo muestra tenue y no dice qué significa. Pendiente de confirmar.
- Los iconos de plan (rocket, award, gem) son Lucide equivalentes a los del diseño.
