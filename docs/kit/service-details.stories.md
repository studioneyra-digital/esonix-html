# Service Details

**Nivel:** Section · 18  
**Dónde:** markup en `dist/service-details.html` (entre `<!-- section:service-details -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#service-details`

## Descripción

Plantilla de servicio: artículo (intro, foto + Check List, Document Required, Key Features, video, FAQ --framed) y aside (Service Nav + Quote Form --outline). 29fr | 14fr desde lg; mobile apilado con Divider.

## Snippet

```html
<section class="section service-details" aria-labelledby="service-details-title">
  <div class="container service-details__grid">
    <article class="service-details__article">
      <div class="service-details__intro" data-reveal>
        <h2 class="service-details__title" id="service-details-title">Explore our Service Lists</h2>
        <p>We provide comprehensive business consulting services designed to help organizations overcome challenges, unlock growth opportunities, and achieve long-term success. Our expert consultants analyze your current operations, identify gaps, and develop tailored strategies that align with your vision and market demands. From planning to execution, we ensure measurable results that drive sustainable growth. Our consulting services focus on improving operational efficiency, strengthening..</p>
      </div>

      <div class="service-details__media">
        <img class="service-details__photo" src="assets/img/h1-process-img-3.webp" alt="Consultants shaking hands with a client across a meeting table" width="1000" height="580" loading="lazy" data-reveal="mask">
        <div class="service-details__block" data-reveal>
          <h3 class="service-details__subtitle service-details__subtitle--sm">Mistakes to avoid to the dummy</h3>
          <ul class="check-list" role="list">
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Market research and competitive analysis</li>
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Operational efficiency and process optimization</li>
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Risk assessment and decision-making support</li>
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Strategic business planning and roadmap</li>
          </ul>
        </div>
      </div>

      <div class="service-details__block" data-reveal>
        <h3 class="service-details__subtitle">Document Required</h3>
        <ul class="service-details__docs" role="list">
          <li class="service-details__doc">
            <span class="icon icon--badge-check" aria-hidden="true"></span>
            <h4 class="service-details__doc-title">Learner's License</h4>
            <p>It is a temporary driving permit issued to individuals who are learning to drive a motor vehicle.</p>
          </li>
          <li class="service-details__doc">
            <span class="icon icon--badge-check" aria-hidden="true"></span>
            <h4 class="service-details__doc-title">Application Form</h4>
            <p>An Application Form is an official document used to collect necessary information from an individual for a specific purpose.</p>
          </li>
          <li class="service-details__doc">
            <span class="icon icon--badge-check" aria-hidden="true"></span>
            <h4 class="service-details__doc-title">Proof of Address</h4>
            <p>Proof of Address is an official document used to verify an individual's current residential address.</p>
          </li>
          <li class="service-details__doc">
            <span class="icon icon--badge-check" aria-hidden="true"></span>
            <h4 class="service-details__doc-title">Passport Size Photo</h4>
            <p>A Passport Size Photo is a small, standardized photograph used for official identification &amp; documentation purposes.</p>
          </li>
        </ul>
      </div>

      <div class="service-details__block" data-reveal>
        <h3 class="service-details__subtitle">Key Features</h3>
        <ul class="check-list" role="list">
          <li><span class="icon icon--circle-check" aria-hidden="true"></span>Our business consulting services are built to help organizations adapt, grow</li>
          <li><span class="icon icon--circle-check" aria-hidden="true"></span>We combine strategic insight with deep industry expertise to deliver solutions</li>
          <li><span class="icon icon--circle-check" aria-hidden="true"></span>From identifying growth opportunities to optimizing operations and guiding execution</li>
          <li><span class="icon icon--circle-check" aria-hidden="true"></span>Our approach emphasizes clarity, collaboration, &amp; measurable impact—ensuring strategies</li>
        </ul>
      </div>

      <div class="service-details__video" data-reveal="mask">
        <img src="assets/img/download.webp" alt="" width="735" height="720" loading="lazy">
        <button type="button" class="icon-btn icon-btn--glass icon-btn--lg service-details__play" aria-label="Play video: Business Optimization overview" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Business Optimization overview"><span class="icon icon--play" aria-hidden="true"></span></button>
      </div>

      <p data-reveal>Our financial and operational consulting services empower businesses to optimize resources, manage risks, and improve cash flow. We provide detailed market analysis, budgeting frameworks, and performance tracking systems that support informed decision-making &amp; long-term stability. We guide companies through digital transformation by integrating modern technologies, automation tools,</p>

      <div class="accordion accordion--framed" data-reveal>
        <details class="accordion-item" name="service-faq" open>
          <summary class="accordion-item__summary">
            <span class="accordion-item__question">1. What industries do you specialize in?</span>
            <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
          </summary>
          <div class="accordion-item__panel">
            <p>Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.</p>
          </div>
        </details>
        <details class="accordion-item" name="service-faq">
          <summary class="accordion-item__summary">
            <span class="accordion-item__question">2. How long does a consulting project typically last?</span>
            <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
          </summary>
          <div class="accordion-item__panel">
            <p>Project duration varies depending on the scope and objectives. Some projects may take a few weeks, while others—such as long-term strategic transformation—can extend over several months.</p>
          </div>
        </details>
        <details class="accordion-item" name="service-faq">
          <summary class="accordion-item__summary">
            <span class="accordion-item__question">3. What does a business consultant do?</span>
            <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
          </summary>
          <div class="accordion-item__panel">
            <p>A business consultant reviews how your company works, finds what holds it back and builds a plan with you: strategy, process optimization, sales improvement and financial advisory.</p>
          </div>
        </details>
        <details class="accordion-item" name="service-faq">
          <summary class="accordion-item__summary">
            <span class="accordion-item__question">4. Will consulting disrupt my daily operations?</span>
            <span class="accordion-item__toggle" aria-hidden="true"><span class="icon icon--arrow-right" aria-hidden="true"></span></span>
          </summary>
          <div class="accordion-item__panel">
            <p>No. We plan each phase around your schedule and work alongside your team, so changes roll out step by step while the business keeps running.</p>
          </div>
        </details>
      </div>
    </article>

    <hr class="divider service-details__divider">

    <!-- Envoltorio sin semántica: un <aside> acá sería un landmark complementary dentro de main y de la
         region de la Section (axe: landmark-complementary-is-top-level). Lo que importa ya son landmarks
         con nombre propio: la <nav> «Exclusive Services» y el <form> «Get a Quote». -->
    <div class="service-details__aside">
      <nav class="service-nav" aria-labelledby="service-nav-title" data-reveal>
        <h2 class="service-nav__title" id="service-nav-title">Exclusive Services</h2>
        <ul class="service-nav__list" role="list">
          <li><a class="service-nav__link" href="#">Strategic Planning<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="service-details.html" aria-current="page">Business Optimization<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">IT Consulting<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Change Management<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Leadership<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
        </ul>
      </nav>

      <form class="quote-form quote-form--outline" id="service-quote-form" data-quote-form action="https://formsubmit.co/studioneyra@gmail.com" method="post" novalidate aria-labelledby="service-quote-title" data-reveal>
        <h2 class="quote-form__title" id="service-quote-title">Get a Quote</h2>
        <input type="hidden" name="_subject" value="New quote request (Business Optimization) from esonix.example">
        <div hidden><label for="service-quote-honey">Leave this field empty</label><input type="text" id="service-quote-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
        <div class="field field--filled">
          <label class="field__label" for="service-quote-name">Name<span aria-hidden="true">*</span></label>
          <input class="input input--filled field__control" type="text" id="service-quote-name" name="name" placeholder=" " required aria-describedby="service-quote-name-error" autocomplete="name">
          <p class="field__error" id="service-quote-name-error"></p>
        </div>
        <div class="field field--filled">
          <label class="field__label" for="service-quote-email">Email<span aria-hidden="true">*</span></label>
          <input class="input input--filled field__control" type="email" id="service-quote-email" name="email" placeholder=" " required aria-describedby="service-quote-email-error" autocomplete="email">
          <p class="field__error" id="service-quote-email-error"></p>
        </div>
        <div class="field field--filled">
          <label class="field__label" for="service-quote-phone">Phone<span aria-hidden="true">*</span></label>
          <input class="input input--filled field__control" type="tel" id="service-quote-phone" name="phone" placeholder=" " required aria-describedby="service-quote-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
          <p class="field__error" id="service-quote-phone-error"></p>
        </div>
        <div class="field field--filled field--select">
          <label class="field__label" for="service-quote-service">Service<span aria-hidden="true">*</span></label>
          <select class="input input--filled field__control" id="service-quote-service" name="service" required aria-describedby="service-quote-service-error">
            <option value="" hidden selected></option>
            <option>Strategic Planning</option>
            <option>Business Optimization</option>
            <option>IT Consulting</option>
            <option>Change Management</option>
            <option>Leadership</option>
          </select>
          <p class="field__error" id="service-quote-service-error"></p>
        </div>
        <div class="field field--filled">
          <label class="field__label" for="service-quote-message">Message<span aria-hidden="true">*</span></label>
          <textarea class="input input--filled field__control" id="service-quote-message" name="message" placeholder=" " required aria-describedby="service-quote-message-error"></textarea>
          <p class="field__error" id="service-quote-message-error"></p>
        </div>
        <button type="submit" class="btn quote-form__submit">
          <span data-submit-label>Submit Now</span>
          <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
        </button>
        <div class="quote-form__messages">
          <p class="quote-form__status" role="status" data-form-status></p>
          <p class="quote-form__alert" role="alert" data-form-alert></p>
        </div>
      </form>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.service-details__grid` | Una columna en mobile; desde lg 29fr | 14fr con 32px de separación |
| `.service-details__article / __aside` | Columnas con bloques a 32px |
| `.service-details__media` | Foto (420×262) y «Mistakes…» mitad y mitad desde md |
| `.service-details__docs / __doc` | Document Required: grilla 2×2 desde md, ícono badge-check ámbar; `align-content: start` alinea las descripciones de una misma fila |
| `.service-details__video + .service-details__play` | Foto 87:40 con el play que abre el Video Modal |
| `.service-details__subtitle(--sm)` | h3 de 28px; --sm de 18 a 24px («Mistakes…») |
| `hr.service-details__divider` | Separador entre artículo y aside, solo por debajo de lg |
| `div.service-details__aside` | Envoltorio del Service Nav y el Quote Form --outline (sin semántica: ver decisiones) |

## Tokens que consume

- `--text-h2 / -h3 / -h4 / -h6 / -body-lg`
- `--color-text-secondary / -highlight`
- `--radius-md`
- `--spacing-1 / -5 / -7 / -9`
- `Check List, Divider, Icon Button, Field, Select (átomos)`
- `Service Nav, Quote Form (moléculas)`
- `Accordion, Video Modal (organismos)`

## Accesibilidad

h1 → h2 → h3 → h4; la nav y el formulario del aside son landmarks nombrados por sus h2; Service Nav con `aria-current`; play con nombre y `aria-haspopup`; foto del video decorativa.

## Decisiones y excepciones

- Copy del diseño, literal (relleno de la plantilla incluido); se corrigió «residen- tial» y se cerraron con punto dos descripciones.
- Fotos sustitutas de la biblioteca (decisión del usuario): el diseño usa fotos que no están en `dist/assets/img`.
- h1 «Business Optimization» y breadcrumb Home › Services › Business Optimization (decisión del usuario); «Services» es texto hasta que exista su página, y el JSON-LD omite ese nivel.
- El h2 del artículo usa --text-h2 (36px) contra 32 del diseño: con --text-h3 quedaba igual que los h3 de 28.
- El aside es un `<div>`, no un `<aside>`: dentro de `<main>` y de la region de la Section, un landmark complementary queda anidado (axe: landmark-complementary-is-top-level). La `<nav>` y el `<form>` que contiene ya son landmarks con nombre propio.
- El aside no es sticky: el diseño no lo muestra y es más alto que el viewport.
