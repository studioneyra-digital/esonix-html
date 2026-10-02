# Marquee

**Nivel:** Organismo · 07  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Marquee */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#marquee`

## Descripción

Franja del footer: «Connect With Us  Let's Grow» en bucle horizontal (CSS puro), translúcido salvo «Grow», con el badge del logo centrado y estático. Texto duplicado `aria-hidden` + una frase para lectores.

## Snippets

**Sobre fondo oscuro**

```html
<div class="marquee" data-surface="inverse">
  <div class="marquee__viewport" aria-hidden="true">
    <div class="marquee__track">
      <div class="marquee__group">
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
      </div>
      <div class="marquee__group">
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        <span class="marquee__text">Connect With Us</span>
        <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
      </div>
    </div>
  </div>
  <p class="visually-hidden">Connect with us. Let's grow.</p>
  <div class="marquee__badge" aria-hidden="true">
    <img class="marquee__badge-logo" src="../assets/img/primary-logo.png" alt="" width="140" height="40">
  </div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.marquee` | Contenedor; recorta el texto que sangra a los costados |
| `.marquee__viewport + aria-hidden` | Capa visual del bucle, oculta para lectores |
| `.marquee__track / __group` | Dos grupos idénticos; la animación mueve -50% (el ancho de uno) |
| `.marquee__text` | Frase del bucle, blanco al 25% |
| `.marquee__accent` | La palabra en blanco pleno («Grow») |
| `.visually-hidden` | Frase única «Connect with us. Let's grow.» para lectores |
| `.marquee__badge + aria-hidden / __badge-logo` | Círculo estático con el logo (primary-logo.png), decorativo |

## Tokens que consume

- `--text-hero / -display (piso en mobile)`
- `--weight-semibold`
- `--leading-tight`
- `--tracking-tight`
- `--color-text-inverse`
- `--color-background-inverse`
- `--shadow-lg`
- `--radius-full`
- `--border-width-sm`
- `--spacing-7 / -10`

## Accesibilidad

Texto animado + duplicado en `aria-hidden`, con una frase visualmente oculta al lado. Badge decorativo. Animación detenida con `prefers-reduced-motion: reduce`.

## Decisiones y excepciones

- Texto translúcido (blanco al 25%) con «Grow» en blanco pleno, como el diseño a resolución real; no hay separador visible entre frases (el diseño tapa ese hueco con el badge).
- Badge con el logo real (`primary-logo.png`), no un ícono: así lo muestra el diseño. Diámetro medido: 160px a 480 → 250px a 1920.
- El diseño no muestra el badge en movimiento: se deja estático (solo el texto de fondo se mueve).
- Duración del bucle (30s): no sale del diseño (es una imagen fija); se deriva para que se lea cómodo.
- `contain: inline-size` en `.marquee`: sin ella, el ancho del texto repetido (miles de px) estira cualquier ancestro grid o flex con columna automática (pasó en el kit) aunque el marquee tenga `overflow: hidden`.
