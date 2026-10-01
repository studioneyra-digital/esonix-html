# Newsletter

**Nivel:** Molécula · 12  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Newsletter */`) · showcase en `dist/kit/index.html#newsletter`

## Descripción

Formulario de suscripción: la frase es el `<label>` del campo; el botón de envío va dentro del filete.

## Snippets

**Sobre fondo oscuro**

```html
<form class="newsletter" action="#">
  <label class="newsletter__title" for="newsletter-email">Subscribe our newsletter to get latest updates</label>
  <div class="newsletter__field">
    <input class="input" type="email" id="newsletter-email" name="email" placeholder="Enter your email" autocomplete="email" required>
    <button type="submit" class="newsletter__submit" aria-label="Subscribe"><span class="icon icon--send" aria-hidden="true"></span></button>
  </div>
</form>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.newsletter` | Formulario: frase arriba, campo abajo |
| `.newsletter__title` | El label del campo, con aspecto de título de 24px |
| `.newsletter__field` | Posiciona el botón dentro del filete del input |
| `.newsletter__submit` | Botón de envío sin caja; se pone amarillo en hover |

## Tokens que consume

- `--color-text-inverse / -inverse-secondary / -highlight`
- `--text-h4 / -h6`
- `--weight-medium`
- `--spacing-5 / -8 / -9`
- `--ease-fast`

## Accesibilidad

La frase es el `<label for>`; botón con `aria-label`; el aviso de resultado va con `role="status"`.

## Decisiones y excepciones

- El sitio es estático y sin backend: el `action` queda en `#` y el envío se conecta por proyecto (servicio de formularios o email).
