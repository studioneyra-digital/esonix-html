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

**--framed (FAQ de Service Details)**

```html
<div class="accordion accordion--framed">
  <details class="accordion-item" name="faq-framed" open>
    <summary class="accordion-item__summary">
      <span class="accordion-item__question">1. What industries do you specialize in?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-framed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__question">2. How long does a consulting project typically last?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>Project duration varies depending on the scope and objectives. Some projects may take a few weeks, while others—such as long-term strategic transformation—can extend over several months.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-framed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__question">3. What does a business consultant do?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>A business consultant reviews how your company works, finds what holds it back and builds a plan with you: strategy, process optimization, sales improvement and financial advisory.</p>
    </div>
  </details>
  <details class="accordion-item" name="faq-framed">
    <summary class="accordion-item__summary">
      <span class="accordion-item__question">4. Will consulting disrupt my daily operations?</span>
      <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
    </summary>
    <div class="accordion-item__panel">
      <p>No. We plan each phase around your schedule and work alongside your team, so changes roll out step by step while the business keeps running.</p>
    </div>
  </details>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.accordion` | Grupo; activa interpolate-size para animar hasta height: auto |
| `.accordion--boxed` | Ítems en caja con borde y 32px de separación; el abierto en blanco |
| `.accordion--framed` | Caja con borde; el abierto en caja gris; filetes entre cerrados; flecha que gira → ↗ (Service Details) |
| `.accordion-item__toggle > .icon--arrow-right` | En --framed, una sola flecha en lugar del par +/− |
| `.accordion-item + name="faq"` | Cada pregunta (molécula); el mismo name deja una sola abierta |
| `open` | Ítem abierto al cargar (el diseño abre el segundo) |

## Tokens que consume

- `--ease-base`
- `--color-border-default / -subtle`
- `--color-background-subtle`
- `--radius-sm`
- `--spacing-4 / -5 / -6`
- `Accordion Item (molécula)`

## Accesibilidad

`<summary>` nativo (Enter/Espacio, estado anunciado). Animación con `--ease-base` (0 con reduced motion); sin soporte, abre sin animar.

## Decisiones y excepciones

- Es un organismo mínimo (el comportamiento lo da HTML nativo): existe para fijar el `name` del grupo y la animación en un solo lugar.
- La cuarta respuesta («Can you help improve team productivity?») es placeholder: el diseño solo muestra abierta la segunda.
- Las preguntas van sin el espacio antes de «?» del diseño (tipografía inglesa).
- --framed: sin el «?» del Accordion Item (el diseño numera las preguntas en el texto); la flecha gira con --ease-base, así con «reducir movimiento» cambia sin animar.
