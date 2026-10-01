# Icon Button

**Nivel:** Átomo · 03  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Icon Button */`) · showcase en `dist/kit/index.html#icon-button`

## Descripción

Círculo con un ícono. Contorno sobre fondo claro; `--glass` sobre fotos; `--sm`/`--lg`. También es el Social Icon (`--sm` con glifo de red).

## Snippets

**Contorno sobre fondo claro (flechas del carrusel)**

```html
<button type="button" class="icon-btn" aria-label="Previous service"><span class="icon icon--arrow-left" aria-hidden="true"></span></button>
<button type="button" class="icon-btn" aria-label="Next service"><span class="icon icon--arrow-right" aria-hidden="true"></span></button>
```

**Glass sobre foto: «+» del equipo (reposo y activo) y play del video**

```html
<button type="button" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="Show details for Olivia Bennet" aria-expanded="false"><span class="icon icon--plus" aria-hidden="true"></span></button>
<button type="button" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="Hide details for Emma Wilson" aria-expanded="true"><span class="icon icon--plus" aria-hidden="true"></span></button>
<button type="button" class="icon-btn icon-btn--glass icon-btn--lg" aria-label="Play testimonial video"><span class="icon icon--play" aria-hidden="true"></span></button>
```

**Social Icon (`icon-btn--sm` con glifo de red)**

```html
<a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a>
<a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a>
<a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a>
<a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.icon-btn` | Círculo de 48px con contorno, fondo blanco e ícono de 18px |
| `.icon-btn--sm` | 40px: «+» del equipo y redes sociales |
| `.icon-btn--lg` | 64px: play del testimonio en video |
| `.icon-btn--glass` | Velo translúcido con ícono blanco para fotos; hover y estado activo en amarillo |
| `aria-expanded / aria-pressed="true"` | Estado activo del glass (amarillo): el botón de «+» abierto |
| `aria-label` | Obligatorio: el botón no tiene texto visible |

## Tokens que consume

- `--color-surface-default`
- `--color-border-default / -strong`
- `--color-overlay / --color-overlay-light`
- `--color-action-secondary`
- `--color-action-on-secondary`
- `--color-text-highlight (play)`
- `--spacing-8 / -9 / -10`
- `--text-body / -h6 / -h5`
- `--ease-fast`

## Accesibilidad

`aria-label` obligatorio con la acción y el objeto; `aria-expanded`/`aria-pressed` para el estado; 40px mínimo.

## Decisiones y excepciones

- El play del diseño no lleva relleno (solo anillo); aquí comparte el velo del `--glass` para no abrir una variante por un matiz.
- El anillo de foco es el global: sobre una foto que no sea `data-surface="inverse"` puede perderse; las cards con foto lo resuelven en Moléculas.
