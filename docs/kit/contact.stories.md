# Contact

**Nivel:** Section · 19  
**Dónde:** markup en `dist/contact.html` (entre `<!-- section:contact -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#contact`

## Descripción

Contacto: encabezado + Quote Form --plain | foto con tarjeta translúcida de contacto; mapa de Google Maps debajo. 43fr | 40fr desde lg; mobile apilado.

## Snippet

```html
<section class="section contact" aria-labelledby="contact-title">
  <div class="container">
    <div class="contact__grid">
      <div class="contact__intro">
        <div class="contact__head">
          <p class="eyebrow">Get In Touch</p>
          <h2 class="section-title contact__title" id="contact-title">Let’s Build Something Great Together</h2>
        </div>
        <form class="quote-form quote-form--plain" id="contact-form" data-quote-form action="https://formsubmit.co/studioneyra@gmail.com" method="post" novalidate aria-labelledby="contact-title">
          <input type="hidden" name="_subject" value="New contact message from esonix.example">
          <div hidden><label for="contact-honey">Leave this field empty</label><input type="text" id="contact-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
          <div class="field">
            <label class="field__label" for="contact-name">Name<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="text" id="contact-name" name="name" placeholder=" " required aria-describedby="contact-name-error" autocomplete="name">
            <p class="field__error" id="contact-name-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="contact-email">Email<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="email" id="contact-email" name="email" placeholder=" " required aria-describedby="contact-email-error" autocomplete="email">
            <p class="field__error" id="contact-email-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="contact-phone">Phone<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="tel" id="contact-phone" name="phone" placeholder=" " required aria-describedby="contact-phone-error" autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}">
            <p class="field__error" id="contact-phone-error"></p>
          </div>
          <div class="field field--select">
            <label class="field__label" for="contact-service">Service<span aria-hidden="true">*</span></label>
            <select class="input field__control" id="contact-service" name="service" required aria-describedby="contact-service-error">
              <option value="" hidden selected></option>
              <option>Strategic Planning</option>
              <option>Business Optimization</option>
              <option>IT Consulting</option>
              <option>Change Management</option>
              <option>Leadership</option>
            </select>
            <p class="field__error" id="contact-service-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="contact-message">Message<span aria-hidden="true">*</span></label>
            <textarea class="input field__control" id="contact-message" name="message" placeholder=" " required aria-describedby="contact-message-error"></textarea>
            <p class="field__error" id="contact-message-error"></p>
          </div>
          <button type="submit" class="btn btn--accent quote-form__submit">
            <span data-submit-label>Submit Now</span>
            <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
          </button>
          <div class="quote-form__messages">
            <p class="quote-form__status" role="status" data-form-status></p>
            <p class="quote-form__alert" role="alert" data-form-alert></p>
          </div>
        </form>
      </div>
      <div class="contact__media">
        <img src="assets/img/h1-about-img-1.webp" alt="Smiling Esonix consultants talking in the office" width="735" height="720" loading="lazy">
        <address class="contact__card">
          <ul class="contact__list" role="list">
            <li><a href="tel:+880123456789">+880 (123) 456 789</a></li>
            <li><a href="mailto:support@esonix.com">support@esonix.com</a></li>
            <li>Seattle, WA, USA</li>
          </ul>
        </address>
      </div>
    </div>
    <iframe class="contact__map" src="https://maps.google.com/maps?q=Seattle%2C%20WA&amp;z=12&amp;hl=en&amp;output=embed" title="Esonix office location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.contact__grid` | Una columna en mobile (gap 48px); desde lg 43fr | 40fr con 80px de separación |
| `.contact__intro / __head` | Columna del formulario; __head apila el Eyebrow y el h2 |
| `h2.section-title.contact__title` | Título de la Section y nombre del formulario (`aria-labelledby`); corta en 32rem |
| `.contact__media` | Foto 12:13 con radio --radius-md; contiene la tarjeta |
| `address.contact__card` | Tarjeta translúcida abajo a la izquierda: velo y borde de Card Hero + `backdrop-filter`; 22rem desde lg, 19rem debajo |
| `ul.contact__list[role="list"]` | Teléfono (`tel:`), email (`mailto:`) y ciudad (texto) |
| `iframe.contact__map` | Google Maps embebido, `loading="lazy"`, 11:4 desde lg y 4:3 debajo; fondo gris mientras carga |

## Tokens que consume

- `--text-h1 (section-title)`
- `--color-overlay / -overlay-light`
- `--color-text-inverse`
- `--color-border-focus-inverse`
- `--color-background-subtle`
- `--blur-backdrop`
- `--radius-sm / -md`
- `--spacing-3 / -5 / -6 / -7 / -9 / -10 / -11 / -13`
- `Eyebrow, Field, Select, Button (átomos)`
- `Quote Form (molécula)`

## Accesibilidad

h2 nombra región y formulario; `<address>` con lista y foco claro; iframe del mapa con `title`; foto con `alt`.

## Decisiones y excepciones

- Datos de contacto del sitio (+880 (123) 456 789, support@esonix.com, Seattle, WA, USA), no los del PNG: decisión del usuario, coherente con header, footer y JSON-LD. Sin calle: el sitio no tiene una.
- Mapa de Google Maps embebido (decisión del usuario): el PNG lo deja asomar sin mostrar su alto. Carga Google (peticiones y cookies) al acercarse al viewport; con GDPR haría falta consentimiento previo.
- La tarjeta no lleva `data-surface="inverse"`: la superficie pinta su fondo opaco con más especificidad y taparía el velo. Solo redefine el token de foco, como la píldora del header `--inner`.
- La tarjeta es parte de la Section, no una molécula: tiene un solo caso de uso.
- Foto lateral `h1-about-img-1.webp` (sustituta de la biblioteca; también la usa la Home).
