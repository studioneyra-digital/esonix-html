# FAQ

**Nivel:** Section · 11  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:faq -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#faq`

## Descripción

Encabezado + Card CTA a la izquierda (columnas de 525 y 720px a 1920) y Accordion a la derecha; apilados en mobile.

## Snippet

```html
<section class="section faq" id="faq" aria-labelledby="faq-title">
  <div class="container faq__grid">
    <div class="faq__intro">
      <div class="section-head">
        <div class="section-head__main">
          <p class="eyebrow">Questions &amp; Answers</p>
          <h2 class="section-title section-head__title" id="faq-title">Frequently Asked Consulting Questions</h2>
        </div>
      </div>
      <article class="card-photo card-cta faq__cta" data-surface="inverse">
        <img class="card-photo__img" src="assets/img/h1-cta-img.webp" alt="" width="1040" height="700" loading="lazy">
        <div class="card-cta__body">
          <span class="card-cta__icon"><span class="icon icon--hexagon" aria-hidden="true"></span></span>
          <div class="card-cta__text">
            <h3 class="card-cta__title">Still have questions?</h3>
            <p>Our results-focused strategies are designed to deliver measurable business growth</p>
            <a href="contact.html" class="link-arrow link-arrow--highlight">
              Contact Us
              <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
            </a>
          </div>
        </div>
      </article>
    </div>
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
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.faq__grid` | Una columna en mobile; desde lg, 33rem | 45rem repartidas a los extremos |
| `.faq__intro` | Encabezado y Card CTA; desde lg, el CTA baja al final de la columna |
| `.accordion + details[name="faq"]` | Acordeón: un solo ítem abierto (el segundo, como el diseño) |
| `.faq--centered` | About Us: encabezado centrado arriba; Accordion --boxed (800px) y Card CTA --stacked (448px) en columnas, sobre --color-background-subtle |

## Tokens que consume

- `--spacing-8 / -10`
- `Eyebrow (átomo)`
- `Card CTA, Accordion Item (moléculas)`
- `Accordion (organismo)`

## Accesibilidad

`<summary>` nativo; «?» y +/− `aria-hidden`. «Contact Us» lleva al footer.

## Decisiones y excepciones

- El acordeón termina ~50px antes que la Card CTA (en el diseño, a ras): sus ítems miden 105px cerrados y 206px abierto contra 113 y 224px del diseño; igualarlos exigiría paddings fuera de la escala.
- Las preguntas van sin el espacio antes de «?» del diseño (tipografía inglesa).
