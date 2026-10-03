# Field

**Nivel:** Átomo · 11  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Field */`) · showcase en `dist/kit/index.html#field`

## Descripción

Label flotante sobre un Input/textarea: en reposo hace de placeholder; con foco o texto sube. Suma el mensaje de error.

## Snippets

**Vacío, con texto y con error**

```html
<div class="field">
  <label class="field__label" for="field-demo-name">Your name<span aria-hidden="true">*</span></label>
  <input class="input field__control" type="text" id="field-demo-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="field-demo-name-error">
  <p class="field__error" id="field-demo-name-error"></p>
</div>
<div class="field">
  <label class="field__label" for="field-demo-email">Your email<span aria-hidden="true">*</span></label>
  <input class="input field__control" type="email" id="field-demo-email" name="email" placeholder=" " autocomplete="email" required value="emma@company.com" aria-describedby="field-demo-email-error">
  <p class="field__error" id="field-demo-email-error"></p>
</div>
<div class="field">
  <label class="field__label" for="field-demo-phone">Phone number<span aria-hidden="true">*</span></label>
  <input class="input field__control" type="tel" id="field-demo-phone" name="phone" placeholder=" " autocomplete="tel" required aria-invalid="true" aria-describedby="field-demo-phone-error">
  <p class="field__error" id="field-demo-phone-error">This field is required.</p>
</div>
<div class="field">
  <label class="field__label" for="field-demo-message">Message<span aria-hidden="true">*</span></label>
  <textarea class="input field__control" id="field-demo-message" name="message" placeholder=" " required aria-describedby="field-demo-message-error"></textarea>
  <p class="field__error" id="field-demo-message-error"></p>
</div>
```

**--filled y --select: vacío, con valor y con error**

```html
<div class="field field--filled">
  <label class="field__label" for="field-demo-filled-name">Name<span aria-hidden="true">*</span></label>
  <input class="input input--filled field__control" type="text" id="field-demo-filled-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="field-demo-filled-name-error">
  <p class="field__error" id="field-demo-filled-name-error"></p>
</div>
<div class="field field--filled field--select">
  <label class="field__label" for="field-demo-filled-service">Service<span aria-hidden="true">*</span></label>
  <select class="input input--filled field__control" id="field-demo-filled-service" name="service" required aria-describedby="field-demo-filled-service-error">
    <option value="" hidden selected></option>
    <option>Strategic Planning</option>
    <option>Business Optimization</option>
    <option>IT Consulting</option>
    <option>Change Management</option>
    <option>Leadership</option>
  </select>
  <p class="field__error" id="field-demo-filled-service-error"></p>
</div>
<div class="field field--filled field--select">
  <label class="field__label" for="field-demo-filled-service-2">Service<span aria-hidden="true">*</span></label>
  <select class="input input--filled field__control" id="field-demo-filled-service-2" name="service" required aria-invalid="true" aria-describedby="field-demo-filled-service-2-error">
    <option value="" hidden selected></option>
    <option>Strategic Planning</option>
    <option>Business Optimization</option>
  </select>
  <p class="field__error" id="field-demo-filled-service-2-error">Choose an option.</p>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.field` | Envoltura: reserva arriba el lugar del label subido |
| `label.field__label + for` | Nombre visible del campo; flota sobre el filete con foco o con texto |
| `.input.field__control + placeholder=" "` | El campo; el placeholder de un espacio habilita :placeholder-shown (es invisible) |
| `<span aria-hidden="true">*</span> + required` | Asterisco visual; lo obligatorio lo anuncia required |
| `p.field__error#<id>-error + aria-describedby` | Mensaje de error enlazado; vacío no ocupa lugar |
| `.field--filled` | Con Input --filled: el label descansa dentro de la caja y sube alineado con su borde |
| `.field--select + option[value=""][hidden][selected]` | Select con chevron; la opción vacía deja el label en reposo |
| `aria-invalid="true"` | Filete en color de error (lo pone main.js al validar) |

## Tokens que consume

- `--color-text-secondary (label)`
- `--color-feedback-error-text`
- `--text-sm`
- `--spacing-1 / -3 / -5`
- `--spacing-4 / -6 (--filled)`
- `--ease-fast`
- `Input (átomo)`

## Accesibilidad

`<label>` real y visible en reposo y con texto; error con `aria-describedby` + `aria-invalid`; asterisco `aria-hidden` (lo anuncia `required`).

## Decisiones y excepciones

- Label flotante (decisión del usuario) en vez del placeholder del diseño: se ve igual en reposo y no desaparece al escribir.
- Usa `:has()` para saber si el campo tiene texto; el label puede ir antes del campo en el DOM.
- Solo sobre fondo claro: son los casos del diseño (Quote Form de About Us y de Service Details).
