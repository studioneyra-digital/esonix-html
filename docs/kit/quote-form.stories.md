# Quote Form

**Nivel:** Molécula · 13  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Quote Form */`) · showcase en `dist/kit/index.html#quote-form`

## Descripción

Card con 4 Field y botón. Sin JS envía normal a FormSubmit; con JS valida, envía por fetch y muestra estados. Destino = `action`.

## Snippets

**En vivo: la validación es real; sin destino, el envío termina en el estado de error**

```html
<form class="quote-form" id="quote-demo-form" data-quote-form action="#kit-demo" method="post" novalidate aria-labelledby="quote-demo-title">
  <h3 class="quote-form__title" id="quote-demo-title">Get a free Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-demo-honey">Leave this field empty</label><input type="text" id="quote-demo-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field">
    <label class="field__label" for="quote-demo-name">Your name<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="text" id="quote-demo-name" name="name" placeholder=" " required aria-describedby="quote-demo-name-error" autocomplete="name">
    <p class="field__error" id="quote-demo-name-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-demo-email">Your email<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="email" id="quote-demo-email" name="email" placeholder=" " required aria-describedby="quote-demo-email-error" autocomplete="email">
    <p class="field__error" id="quote-demo-email-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-demo-phone">Phone number<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="tel" id="quote-demo-phone" name="phone" placeholder=" " required aria-describedby="quote-demo-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
    <p class="field__error" id="quote-demo-phone-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-demo-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input field__control" id="quote-demo-message" name="message" placeholder=" " required aria-describedby="quote-demo-message-error"></textarea>
    <p class="field__error" id="quote-demo-message-error"></p>
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
```

**Error de validación**

```html
<form class="quote-form" id="quote-error-form" action="#" method="post" novalidate aria-label="Get a free Quote, validation error example">
  <h3 class="quote-form__title" id="quote-error-title">Get a free Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-error-honey">Leave this field empty</label><input type="text" id="quote-error-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field">
    <label class="field__label" for="quote-error-name">Your name<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="text" id="quote-error-name" name="name" placeholder=" " required aria-describedby="quote-error-name-error" aria-invalid="true" autocomplete="name">
    <p class="field__error" id="quote-error-name-error">This field is required.</p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-error-email">Your email<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="email" id="quote-error-email" name="email" placeholder=" " required aria-describedby="quote-error-email-error" aria-invalid="true" autocomplete="email" value="emma@">
    <p class="field__error" id="quote-error-email-error">Enter a valid email address.</p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-error-phone">Phone number<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="tel" id="quote-error-phone" name="phone" placeholder=" " required aria-describedby="quote-error-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
    <p class="field__error" id="quote-error-phone-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-error-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input field__control" id="quote-error-message" name="message" placeholder=" " required aria-describedby="quote-error-message-error"></textarea>
    <p class="field__error" id="quote-error-message-error"></p>
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
```

**Enviando**

```html
<form class="quote-form" id="quote-sending-form" action="#" method="post" novalidate aria-label="Get a free Quote, sending example">
  <h3 class="quote-form__title" id="quote-sending-title">Get a free Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-sending-honey">Leave this field empty</label><input type="text" id="quote-sending-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field">
    <label class="field__label" for="quote-sending-name">Your name<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="text" id="quote-sending-name" name="name" placeholder=" " required aria-describedby="quote-sending-name-error" autocomplete="name" value="Emma Wilson">
    <p class="field__error" id="quote-sending-name-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sending-email">Your email<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="email" id="quote-sending-email" name="email" placeholder=" " required aria-describedby="quote-sending-email-error" autocomplete="email" value="emma@company.com">
    <p class="field__error" id="quote-sending-email-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sending-phone">Phone number<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="tel" id="quote-sending-phone" name="phone" placeholder=" " required aria-describedby="quote-sending-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}" value="+1 (555) 123 4567">
    <p class="field__error" id="quote-sending-phone-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sending-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input field__control" id="quote-sending-message" name="message" placeholder=" " required aria-describedby="quote-sending-message-error">We need help with our pricing strategy.</textarea>
    <p class="field__error" id="quote-sending-message-error"></p>
  </div>
  <button type="submit" class="btn quote-form__submit" aria-disabled="true">
    <span data-submit-label>Sending…</span>
    <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
  </button>
  <div class="quote-form__messages">
    <p class="quote-form__status" role="status" data-form-status></p>
    <p class="quote-form__alert" role="alert" data-form-alert></p>
  </div>
</form>
```

**Enviado**

```html
<form class="quote-form" id="quote-sent-form" action="#" method="post" novalidate aria-label="Get a free Quote, sent example">
  <h3 class="quote-form__title" id="quote-sent-title">Get a free Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-sent-honey">Leave this field empty</label><input type="text" id="quote-sent-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field">
    <label class="field__label" for="quote-sent-name">Your name<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="text" id="quote-sent-name" name="name" placeholder=" " required aria-describedby="quote-sent-name-error" autocomplete="name">
    <p class="field__error" id="quote-sent-name-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sent-email">Your email<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="email" id="quote-sent-email" name="email" placeholder=" " required aria-describedby="quote-sent-email-error" autocomplete="email">
    <p class="field__error" id="quote-sent-email-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sent-phone">Phone number<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="tel" id="quote-sent-phone" name="phone" placeholder=" " required aria-describedby="quote-sent-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
    <p class="field__error" id="quote-sent-phone-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-sent-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input field__control" id="quote-sent-message" name="message" placeholder=" " required aria-describedby="quote-sent-message-error"></textarea>
    <p class="field__error" id="quote-sent-message-error"></p>
  </div>
  <button type="submit" class="btn quote-form__submit">
    <span data-submit-label>Get Started</span>
    <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
  </button>
  <div class="quote-form__messages">
    <p class="quote-form__status" role="status" data-form-status>Thanks! Your message was sent. We will get back to you soon.</p>
    <p class="quote-form__alert" role="alert" data-form-alert></p>
  </div>
</form>
```

**Error de envío**

```html
<form class="quote-form" id="quote-failed-form" action="#" method="post" novalidate aria-label="Get a free Quote, send error example">
  <h3 class="quote-form__title" id="quote-failed-title">Get a free Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-failed-honey">Leave this field empty</label><input type="text" id="quote-failed-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field">
    <label class="field__label" for="quote-failed-name">Your name<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="text" id="quote-failed-name" name="name" placeholder=" " required aria-describedby="quote-failed-name-error" autocomplete="name" value="Emma Wilson">
    <p class="field__error" id="quote-failed-name-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-failed-email">Your email<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="email" id="quote-failed-email" name="email" placeholder=" " required aria-describedby="quote-failed-email-error" autocomplete="email" value="emma@company.com">
    <p class="field__error" id="quote-failed-email-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-failed-phone">Phone number<span aria-hidden="true">*</span></label>
    <input class="input field__control" type="tel" id="quote-failed-phone" name="phone" placeholder=" " required aria-describedby="quote-failed-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}" value="+1 (555) 123 4567">
    <p class="field__error" id="quote-failed-phone-error"></p>
  </div>
  <div class="field">
    <label class="field__label" for="quote-failed-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input field__control" id="quote-failed-message" name="message" placeholder=" " required aria-describedby="quote-failed-message-error">We need help with our pricing strategy.</textarea>
    <p class="field__error" id="quote-failed-message-error"></p>
  </div>
  <button type="submit" class="btn quote-form__submit">
    <span data-submit-label>Get Started</span>
    <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
  </button>
  <div class="quote-form__messages">
    <p class="quote-form__status" role="status" data-form-status></p>
    <p class="quote-form__alert" role="alert" data-form-alert>Your message could not be sent. Please check your connection and try again.</p>
  </div>
</form>
```

**--outline con campos --filled y Select (Service Details)**

```html
<form class="quote-form quote-form--outline" id="quote-outline-form" action="#" method="post" novalidate aria-label="Get a Quote, validation error example">
  <h3 class="quote-form__title" id="quote-outline-title">Get a Quote</h3>
  <input type="hidden" name="_subject" value="New quote request from esonix.example">
  <div hidden><label for="quote-outline-honey">Leave this field empty</label><input type="text" id="quote-outline-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="field field--filled">
    <label class="field__label" for="quote-outline-name">Name<span aria-hidden="true">*</span></label>
    <input class="input input--filled field__control" type="text" id="quote-outline-name" name="name" placeholder=" " required aria-describedby="quote-outline-name-error" aria-invalid="true" autocomplete="name">
    <p class="field__error" id="quote-outline-name-error">This field is required.</p>
  </div>
  <div class="field field--filled">
    <label class="field__label" for="quote-outline-email">Email<span aria-hidden="true">*</span></label>
    <input class="input input--filled field__control" type="email" id="quote-outline-email" name="email" placeholder=" " required aria-describedby="quote-outline-email-error" aria-invalid="true" autocomplete="email" value="emma@">
    <p class="field__error" id="quote-outline-email-error">Enter a valid email address.</p>
  </div>
  <div class="field field--filled">
    <label class="field__label" for="quote-outline-phone">Phone<span aria-hidden="true">*</span></label>
    <input class="input input--filled field__control" type="tel" id="quote-outline-phone" name="phone" placeholder=" " required aria-describedby="quote-outline-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
    <p class="field__error" id="quote-outline-phone-error"></p>
  </div>
  <div class="field field--filled field--select">
    <label class="field__label" for="quote-outline-service">Service<span aria-hidden="true">*</span></label>
    <select class="input input--filled field__control" id="quote-outline-service" name="service" required aria-describedby="quote-outline-service-error" aria-invalid="true">
      <option value="" hidden selected></option>
      <option>Strategic Planning</option>
      <option>Business Optimization</option>
      <option>IT Consulting</option>
      <option>Change Management</option>
      <option>Leadership</option>
    </select>
    <p class="field__error" id="quote-outline-service-error">Choose an option.</p>
  </div>
  <div class="field field--filled">
    <label class="field__label" for="quote-outline-message">Message<span aria-hidden="true">*</span></label>
    <textarea class="input input--filled field__control" id="quote-outline-message" name="message" placeholder=" " required aria-describedby="quote-outline-message-error"></textarea>
    <p class="field__error" id="quote-outline-message-error"></p>
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
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `form.quote-form[data-quote-form]` | Activa el envío por fetch y la validación de main.js |
| `action="https://formsubmit.co/<destino>" method="post" novalidate` | Destino (sin JS, envío normal); novalidate deja la validación a main.js |
| `.quote-form--outline` | Card con borde, sin fondo ni sombra; título de 24px (aside de Service Details) |
| `.field--filled / .field--select` | Campos en caja gris y el Select «Service» (ver Field y Select) |
| `input[name="_subject"] / div[hidden] > input[name="_honey"]` | Asunto del correo y trampa antibots de FormSubmit |
| `button[aria-disabled="true"] > [data-submit-label]` | Enviando: el botón no responde y su texto pasa a «Sending…» |
| `p[role="status"][data-form-status]` | Mensaje de enviado |
| `p[role="alert"][data-form-alert]` | Mensaje de error de envío; los datos se conservan |

## Tokens que consume

- `--color-surface-default`
- `--radius-lg / -sm`
- `--shadow-md`
- `--color-feedback-success-* / -error-*`
- `--spacing-3 / -4 / -5 / -6 / -8`
- `Field, Input, Button (átomos)`

## Accesibilidad

Error por campo con `aria-describedby`, foco al primero inválido; `role="status"` / `role="alert"` presentes desde el inicio; `aria-disabled` mientras envía.

## Decisiones y excepciones

- FormSubmit (decisión del usuario): sin cuenta ni clave. El primer envío real manda a studioneyra@gmail.com un correo de activación que hay que confirmar una vez.
- El correo de destino queda visible en el HTML; FormSubmit permite reemplazarlo por un alias aleatorio después de activar.
- Solo el demo «En vivo» lleva `data-quote-form`; su `action` es la propia página del kit (`#kit-demo`), así nunca envía correos: el servidor estático rechaza el POST y se ve el estado de error. Los demás muestran estados estáticos con `action="#"`.
- El teléfono acepta dígitos, espacios, `+`, paréntesis y guiones (mínimo 6).
- --outline usa campos --filled: el diseño de Service Details los muestra en caja gris, con el filete inferior fuerte por contraste (decisión del usuario).
