# Pricing

**Nivel:** Section · 06  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:pricing -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#pricing`

## Descripción

Section Head `--center`, Switch mensual/anual y tres Card Pricing (3 columnas desde xl, una centrada antes). `main.js` cambia los precios y lo anuncia en `role="status"`.

## Snippet

```html
<section class="section pricing" id="pricing" aria-labelledby="pricing-title">
  <div class="container">
    <div class="section-head section-head--center">
      <div class="section-head__main">
        <p class="eyebrow eyebrow--center">Our Pricing Plan</p>
        <h2 class="section-title section-head__title" id="pricing-title">Plans Designed for Every Stage of Growth</h2>
      </div>
    </div>
    <div class="pricing__billing" data-pricing>
      <span class="pricing__billing-label" aria-hidden="true">Monthly</span>
      <input class="switch" type="checkbox" role="switch" id="pricing-annual">
      <label class="pricing__billing-label" for="pricing-annual">Annually Save 30%</label>
      <p class="visually-hidden" role="status" data-pricing-status></p>
    </div>
    <div class="pricing__grid">
      <article class="card-pricing">
        <header class="card-pricing__head">
          <span class="card-pricing__icon"><span class="icon icon--rocket" aria-hidden="true"></span></span>
          <div>
            <h3 class="card-pricing__name">Starter Plan</h3>
            <p>Core strategies for business success</p>
          </div>
        </header>
        <p class="card-pricing__price"><span class="card-pricing__amount" data-price-monthly="$39.9" data-price-annual="$27.9">$39.9</span> <span>/ Month</span></p>
        <a href="contact.html" class="btn btn--block">
          Get Started<span class="visually-hidden"> with the Starter Plan</span>
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
            <p>Drive innovation &amp; long-term success</p>
          </div>
        </header>
        <p class="card-pricing__price"><span class="card-pricing__amount" data-price-monthly="$49.9" data-price-annual="$34.9">$49.9</span> <span>/ Month</span></p>
        <a href="contact.html" class="btn btn--block btn--accent">
          Get Started<span class="visually-hidden"> with the Enterprise Plan</span>
          <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
        </a>
        <ul class="card-pricing__list">
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Customized Business Strategy</li>
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Advanced Market Research</li>
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Ongoing Performance Monitoring</li>
          <li class="card-pricing__item is-muted"><span class="icon icon--circle-check" aria-hidden="true"></span> Priority Support &amp; Advisory</li>
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
        <p class="card-pricing__price"><span class="card-pricing__amount" data-price-monthly="$59.9" data-price-annual="$41.9">$59.9</span> <span>/ Month</span></p>
        <a href="contact.html" class="btn btn--block">
          Get Started<span class="visually-hidden"> with Premium Features</span>
          <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
        </a>
        <ul class="card-pricing__list">
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Long-Term Success Planning</li>
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Actionable Growth Strategies</li>
          <li class="card-pricing__item"><span class="icon icon--circle-check" aria-hidden="true"></span> Industry Expert Guidance</li>
          <li class="card-pricing__item is-muted"><span class="icon icon--circle-check" aria-hidden="true"></span> Dedicated Business Support</li>
        </ul>
      </article>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.section-head--center` | Eyebrow --center y h2 centrados |
| `.pricing__billing + data-pricing` | Fila del switch: «Monthly» (aria-hidden), el switch y su <label>; 18px en mobile y 24px desde lg |
| `input.switch[role="switch"]#pricing-annual` | Encendido = precios anuales; su nombre es «Annually Save 30%» |
| `[data-pricing-status][role="status"]` | Región oculta que anuncia el cambio (solo al mover el switch) |
| `[data-price-monthly][data-price-annual]` | Importe que main.js reemplaza; sin JS queda el mensual |
| `.pricing__grid` | Una columna de hasta 32rem; tres columnas desde xl |

## Tokens que consume

- `--text-h6 / -h4`
- `--color-text-primary`
- `--spacing-5 / -6 / -8 / -9 / -10`
- `Eyebrow, Switch, Button (átomos)`
- `Card Pricing (molécula)`

## Accesibilidad

Switch nativo (`role="switch"`) con `<label>` «Annually Save 30%»; «Monthly» con `aria-hidden`. `role="status"` anuncia el cambio solo al moverlo. «Get Started» con el nombre del plan oculto.

## Decisiones y excepciones

- Precios anuales con el 30% de descuento redondeado como el diseño: 39.9 → 27.9, 49.9 → 34.9, 59.9 → 41.9. «/ Month» no cambia (precio mensual equivalente).
- Tres columnas recién desde xl: a 1024px quedaban de 296px y cortaban nombres y beneficios en varias líneas.
- El export mobile repite «Long-Term Success Planning» en Premium Features: no se replica.
- Los «Get Started» llevan al footer (contacto): el diseño no dice adónde van.
