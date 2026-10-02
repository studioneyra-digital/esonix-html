# Marquee

**Nivel:** Organismo · 07  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Marquee */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#marquee`

## Descripción

Franja del footer: «Connect With Us • Let's Grow» en bucle horizontal infinito (CSS puro), con el badge del logo centrado y estático encima. El texto duplicado del bucle es `aria-hidden`, con una frase para lectores al lado.

## Snippets

**Sobre fondo oscuro**

```html
<div class="marquee" data-surface="inverse">
  <div class="marquee__viewport" aria-hidden="true">
    <div class="marquee__track">
      <div class="marquee__group">
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
      </div>
      <div class="marquee__group">
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Connect With Us</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
    <span class="marquee__text">Let's Grow</span>
    <span class="marquee__dot" aria-hidden="true">•</span>
      </div>
    </div>
  </div>
  <p class="visually-hidden">Connect with us. Let's grow.</p>
  <div class="marquee__badge" aria-hidden="true">
    <span class="icon icon--hexagon marquee__badge-icon" aria-hidden="true"></span>
    <span class="marquee__badge-text">Esonix</span>
  </div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.marquee` | Contenedor; recorta el texto que sangra a los costados |
| `.marquee__viewport + aria-hidden` | Capa visual del bucle, oculta para lectores |
| `.marquee__track / __group` | Dos grupos idénticos; la animación mueve -50% (el ancho de uno) |
| `.marquee__text / __dot` | Frase y separador del bucle |
| `.visually-hidden` | Frase única «Connect with us. Let's grow.» para lectores |
| `.marquee__badge + aria-hidden` | Badge circular estático (ícono + «Esonix»), decorativo |

## Tokens que consume

- `--text-hero`
- `--weight-bold`
- `--leading-tight`
- `--color-text-inverse / -highlight`
- `--color-background-inverse`
- `--text-h2 / -h3 / -sm`
- `--tracking-wide`
- `--spacing-1 / -4 / -9 / -10`
- `--radius-full`
- `--border-width-sm`

## Accesibilidad

Texto animado + duplicado en `aria-hidden`, con una frase visualmente oculta equivalente al lado. Badge decorativo (el nombre ya está en el logo). Animación detenida con `prefers-reduced-motion: reduce`.

## Decisiones y excepciones

- El diseño no muestra el badge en movimiento: se deja estático (solo el texto de fondo gira); animarlo también habría sido una invención no declarada.
- Duración del bucle (30s) no sale del diseño (es una franja estática): se deriva para que se lea cómodo, no para que compita por atención.
- Separador «•» en vez del espacio del diseño: distingue las dos frases sin depender solo del salto de línea.
