# Why Trust

**Nivel:** Section · 17  
**Dónde:** markup en `dist/about-us.html` (entre `<!-- section:why-trust -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#why-trust`

## Descripción

Quote Form montado sobre Feedback + eyebrow, h2, dos Progress (una `--accent`) y Link Arrow. Mobile: formulario primero.

## Snippet

```html
<section class="section why-trust" aria-labelledby="why-trust-title">
  <div class="container why-trust__grid">
    <form class="quote-form why-trust__form" id="quote-form" data-quote-form action="https://formsubmit.co/studioneyra@gmail.com" method="post" novalidate aria-labelledby="quote-form-title">
      <h2 class="quote-form__title" id="quote-form-title">Get a free Quote</h2>
      <input type="hidden" name="_subject" value="New quote request from esonix.example">
      <div hidden><label for="quote-honey">Leave this field empty</label><input type="text" id="quote-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
      <div class="field">
        <label class="field__label" for="quote-name">Your name<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="text" id="quote-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="quote-name-error">
        <p class="field__error" id="quote-name-error"></p>
      </div>
      <div class="field">
        <label class="field__label" for="quote-email">Your email<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="email" id="quote-email" name="email" placeholder=" " autocomplete="email" required aria-describedby="quote-email-error">
        <p class="field__error" id="quote-email-error"></p>
      </div>
      <div class="field">
        <label class="field__label" for="quote-phone">Phone number<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="tel" id="quote-phone" name="phone" placeholder=" " autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}" required aria-describedby="quote-phone-error">
        <p class="field__error" id="quote-phone-error"></p>
      </div>
      <div class="field">
        <label class="field__label" for="quote-message">Message<span aria-hidden="true">*</span></label>
        <textarea class="input field__control" id="quote-message" name="message" placeholder=" " required aria-describedby="quote-message-error"></textarea>
        <p class="field__error" id="quote-message-error"></p>
      </div>
      <button type="submit" class="btn quote-form__submit">
        <span data-submit-label>Get Started</span>
        <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
      </button>
      <div class="quote-form__messages">
        <p class="quote-form__status" role="status" data-form-status></p>
        <p class="quote-form__alert" role="alert" data-form-alert></p>
      </div>
    </form>
    <div class="why-trust__intro">
      <p class="eyebrow">Why Choose Us</p>
      <h2 class="section-title" id="why-trust-title">Why Businesses Trust Our Consulting</h2>
      <div class="why-trust__bars">
        <div class="progress progress--accent" style="--progress: 88">
          <div class="progress__head">
            <label for="progress-consulting">Consulting</label>
            <span aria-hidden="true">88%</span>
          </div>
          <progress class="progress__bar" id="progress-consulting" value="88" max="100">88%</progress>
        </div>
        <div class="progress" style="--progress: 75">
          <div class="progress__head">
            <label for="progress-marketing">Marketing</label>
            <span aria-hidden="true">75%</span>
          </div>
          <progress class="progress__bar" id="progress-marketing" value="75" max="100">75%</progress>
        </div>
      </div>
      <a href="#quote-form" class="link-arrow">
        Contact With Us
        <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
      </a>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.why-trust__grid` | Una columna en mobile; desde lg 37.5rem | 35rem (600 y 560px a 1920), alineadas abajo |
| `form.quote-form.why-trust__form` | Primero en el DOM; sube --quote-form-overlap sobre Feedback; desde lg en la columna derecha |
| `.why-trust__intro / __bars` | Eyebrow, h2, barras y enlace |
| `.progress--accent` | La barra «Consulting» en ámbar |

## Tokens que consume

- `--quote-form-overlap`
- `--spacing-5 / -6 / -10`
- `Eyebrow, Progress, Link Arrow, Field (átomos)`
- `Quote Form (molécula)`

## Accesibilidad

Formulario primero en el DOM (Tab: formulario → texto). `<progress>` + `<label for>`. En el kit, formulario neutralizado (no envía).

## Decisiones y excepciones

- El formulario envía por FormSubmit a studioneyra@gmail.com (decisión del usuario); el primer envío real dispara un correo de activación.
- «Contact With Us» lleva al formulario de la misma sección.
- El título del formulario es un `<h2>` (no `<h3>`): el formulario va antes que el h2 de la sección en el DOM, y como h3 quedaba colgando del h2 de Feedback en el esquema de títulos.
- El formulario mide 571px contra 585 del diseño: los campos quedan a 83px (el diseño, 75) porque el label flotante necesita reservar su lugar arriba.
