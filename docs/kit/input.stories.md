# Input

**Nivel:** Átomo · 10  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Input */`) · showcase en `dist/kit/index.html#input`

## Descripción

Campo de texto de una línea con filete inferior (caso del diseño: newsletter). Sobre superficies oscuras filete y placeholder pasan a blanco al 78%.

## Snippets

**Sobre fondo claro**

```html
<label for="input-demo-light" class="visually-hidden">Email address</label>
<input class="input" type="email" id="input-demo-light" name="email" placeholder="Enter your email" autocomplete="email">
```

**Sobre fondo oscuro (hereda de `data-surface`)**

```html
<label for="input-demo-dark" class="visually-hidden">Email address</label>
<input class="input" type="email" id="input-demo-dark" name="email" placeholder="Enter your email" autocomplete="email">
```

**Textarea (misma clase)**

```html
<label for="input-demo-textarea" class="visually-hidden">Message</label>
<textarea class="input" id="input-demo-textarea" name="message" placeholder="Write your message"></textarea>
```

**--filled (caja gris)**

```html
<label for="input-demo-filled" class="visually-hidden">Your name</label>
<input class="input input--filled" type="text" id="input-demo-filled" name="name" placeholder="Name">
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.input` | Campo sin caja: solo el filete inferior; ocupa el ancho de su contenedor |
| `.input--filled` | Caja gris con filete inferior fuerte (Quote Form de Service Details) |
| `textarea.input` | Varias líneas: alto mínimo de 96px y redimensionable solo en vertical |
| `aria-invalid="true"` | Estado de error: el filete pasa a color de error (acompañar con un mensaje de texto) |
| `<label for>` | Obligatorio, aunque esté visualmente oculto (`visually-hidden`): el placeholder no es un nombre accesible |
| `type / autocomplete` | El tipo correcto (email, tel…) abre el teclado adecuado en móvil; autocomplete evita volver a pedir un dato |

## Tokens que consume

- `--color-text-primary / -inverse`
- `--color-border-strong / --color-text-inverse-secondary (filete)`
- `--color-text-tertiary (placeholder)`
- `--color-border-error`
- `--spacing-3`
- `--text-body`
- `--ease-fast`

## Accesibilidad

`<label>` asociado (puede ser `visually-hidden`); foco con anillo global; filete ≥3:1.

## Decisiones y excepciones

- Dos estilos: filete (newsletter y Quote Form de About Us) y --filled (Quote Form de Service Details).
- --filled: el borde del diseño (≈ 1.2:1) no llega al 3:1 de un control; se mantiene en tres lados y el filete inferior va en `--color-border-strong` (decisión del usuario).
- El filete del diseño es translúcido y tenue; aquí es blanco al 78% para cumplir 3:1 como borde de control.
