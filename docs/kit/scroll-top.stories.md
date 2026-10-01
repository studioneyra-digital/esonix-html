# Scroll Top

**Nivel:** Átomo · 12  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Scroll Top */`) · showcase en `dist/kit/index.html#scroll-top`

## Descripción

Botón fijo que vuelve al inicio. Aparece tras media pantalla; el anillo dibuja el avance del scroll. Vive en el body de la página.

## Snippets

**Snippet (va una sola vez, al final del `<body>`)**

```html
<button type="button" class="scroll-top" aria-label="Back to top">
  <span class="icon icon--arrow-up" aria-hidden="true"></span>
</button>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.scroll-top` | Círculo fijo de 48px; oculto con visibility hasta que main.js agrega .is-visible |
| `.is-visible` | La pone main.js al pasar el 50% del alto del viewport |
| `--scroll-progress` | Propiedad 0–100 que main.js actualiza; llena el anillo con conic-gradient |
| `main.js › initScrollTop` | Sin JS el botón queda oculto: el sitio sigue usable |

## Tokens que consume

- `--color-action-primary (anillo)`
- `--color-border-default (pista)`
- `--color-surface-default`
- `--spacing-5 / -9`
- `--z-sticky`
- `--ease-base`

## Accesibilidad

`aria-label`; oculto con `visibility`; al activarlo mueve el foco al `<body>`; respeta reducir movimiento.

## Decisiones y excepciones

- El diseño muestra el botón con su anillo parcialmente lleno pero no dice cuándo aparece: se asume al pasar media pantalla (`SHOW_AFTER = 0.5` en main.js).
- En escritorio queda a 48px de los bordes (medido en el diseño); en mobile, a 20px.
