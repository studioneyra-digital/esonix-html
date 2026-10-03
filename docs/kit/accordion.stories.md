# Accordion

**Nivel:** Organismo · 04  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Accordion */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#accordion`

## Descripción

Grupo de Accordion Items (FAQ): un solo ítem abierto por el `name` compartido (sin JS) y animación de altura con `::details-content`.

## Snippets

**FAQ con un ítem abierto**

```html
<div class="accordion">
  <details class="accordion-item" name="faq">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">How can consulting help my business grow?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Consulting brings an outside view, proven methods and focused support, so you can find opportunities and act on them faster.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq" open>
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">What industries do you specialize in?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">What services do business consultants provide?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>We offer strategy, process optimization, sales improvement and financial advisory.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">Can you help improve team productivity?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Yes. We review how work moves between people and tools, then set up routines and metrics that remove bottlenecks.</p>
    </div>
  </details>
</div>
```

**--boxed (FAQ de About Us)**

```html
<div class="accordion accordion--boxed">
  <details class="accordion-item" name="faq-boxed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">How can consulting help my business grow?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Consulting brings an outside view, proven methods and focused support, so you can find opportunities and act on them faster.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-boxed" open>
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">What industries do you specialize in?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-boxed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">What services do business consultants provide?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>We offer strategy, process optimization, sales improvement and financial advisory.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-boxed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__mark" aria-hidden="true">?</span>
      <span class="accordion-item__question">Can you help improve team productivity?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Yes. We review how work moves between people and tools, then set up routines and metrics that remove bottlenecks.</p>
    </div>
  </details>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.accordion` | Grupo; activa interpolate-size para animar hasta height: auto |
| `.accordion--boxed` | Ítems en caja con borde y 32px de separación; el abierto en blanco |
| `.accordion-item + name="faq"` | Cada pregunta (molécula); el mismo name deja una sola abierta |
| `open` | Ítem abierto al cargar (el diseño abre el segundo) |

## Tokens que consume

- `--ease-base`
- `Accordion Item (molécula)`

## Accesibilidad

`<summary>` nativo (Enter/Espacio, estado anunciado). Animación con `--ease-base` (0 con reduced motion); sin soporte, abre sin animar.

## Decisiones y excepciones

- Es un organismo mínimo (el comportamiento lo da HTML nativo): existe para fijar el `name` del grupo y la animación en un solo lugar.
- La cuarta respuesta («Can you help improve team productivity?») es placeholder: el diseño solo muestra abierta la segunda.
- Las preguntas van sin el espacio antes de «?» del diseño (tipografía inglesa).
