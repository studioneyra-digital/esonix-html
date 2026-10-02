# Accordion Item

**Nivel:** Molécula · 11  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Accordion Item */`) · showcase en `dist/kit/index.html#accordion-item`

## Descripción

Pregunta de la FAQ sobre `<details>` nativo; con el mismo `name` solo uno queda abierto. Sin JS.

## Snippets

**Grupo de tres (el segundo abierto)**

```html
<details class="accordion-item" name="faq-demo">
  <summary class="accordion-item__summary">
    <span class="accordion-item__mark" aria-hidden="true">?</span>
    <span class="accordion-item__question">How can consulting help my business grow?</span>
    <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
  </summary>
  <div class="accordion-item__panel">
    <p>Consulting brings an outside view, proven methods and focused support, so you can find opportunities and act on them faster.</p>
  </div>
</details>
<details class="accordion-item" name="faq-demo" open>
  <summary class="accordion-item__summary">
    <span class="accordion-item__mark" aria-hidden="true">?</span>
    <span class="accordion-item__question">What industries do you specialize in?</span>
    <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
  </summary>
  <div class="accordion-item__panel">
    <p>Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.</p>
  </div>
</details>
<details class="accordion-item" name="faq-demo">
  <summary class="accordion-item__summary">
    <span class="accordion-item__mark" aria-hidden="true">?</span>
    <span class="accordion-item__question">What services do business consultants provide?</span>
    <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--plus" aria-hidden="true"></span><span class="icon icon--minus" aria-hidden="true"></span></span>
  </summary>
  <div class="accordion-item__panel">
    <p>We offer strategy, process optimization, sales improvement and financial advisory.</p>
  </div>
</details>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.accordion-item` | <details> con un filete inferior |
| `.accordion-item__summary` | <summary>: fila con «?», la pregunta y el +/− |
| `.accordion-item__mark` | Círculo con «?»: gris cerrado, amarillo abierto |
| `.accordion-item__toggle` | Muestra «+» cerrado y «−» abierto (CSS puro) |
| `.accordion-item__panel` | Respuesta, alineada bajo el texto de la pregunta |
| `name="…" / open` | Mismo name en varios ítems = acordeón exclusivo; open abre uno por defecto |

## Tokens que consume

- `--color-border-subtle`
- `--color-background-subtle`
- `--color-action-secondary / -on-secondary`
- `--text-h5`
- `--weight-medium`
- `--spacing-5 / -6 / -8`
- `--ease-base`

## Accesibilidad

`<summary>` nativo: Tab, Enter/Espacio y estado anunciado sin ARIA; fila de 48px+; +/− cambia con el estado.

## Decisiones y excepciones

- Pregunta semibold de 24px desde lg y 18px en mobile (el diseño mide ~20px; con 18 los cortes de línea coinciden), con 32px de separación del «?» (20px en mobile): medido en los PNG a resolución real (Etapa 4, Grupo C); antes, 22px medium en todos los anchos.
- Se usa `<details name>` nativo en lugar del `<button aria-expanded>` con JS que planteaba el plan: es exclusivo, accesible y no necesita script. Si hace falta animar la altura, se agrega después con `::details-content`.
- La copia del diseño escribe «in ?»; se normalizó a «in?».
