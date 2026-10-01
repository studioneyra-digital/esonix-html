# Badge

**Nivel:** Átomo · 06  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Badge */`) · showcase en `dist/kit/index.html#badge`

## Descripción

Etiqueta translúcida sobre foto (rol del equipo, fecha del post). Velo `--color-overlay`; `--marker` suma el cuadrito amarillo.

## Snippets

**Sobre foto**

```html
<span class="badge">Financial Advisor</span>
<span class="badge badge--marker">21 Oct, 2026</span>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.badge` | Píldora de 40px con velo oscuro, borde translúcido y texto blanco de 14px |
| `.badge--marker` | Agrega un cuadrito amarillo antes del texto (fechas) |

## Tokens que consume

- `--color-overlay / --color-overlay-light`
- `--color-text-inverse / -highlight`
- `--text-sm`
- `--weight-medium`
- `--spacing-2 / -4 / -8`
- `--radius-full`

## Accesibilidad

Peor caso (foto blanca) ≈5:1. Las fechas van en `<time datetime>`.

## Decisiones y excepciones

- El diseño muestra un vidrio esmerilado; se usa un velo plano (sin `backdrop-filter`) para no romper `position: fixed` de descendientes ni cargar el render.
