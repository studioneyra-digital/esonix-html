# Eyebrow

**Nivel:** Átomo · 05  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Eyebrow */`) · showcase en `dist/kit/index.html#eyebrow`

## Descripción

Rótulo corto sobre el título de sección, con cuadrito decorativo. `--center` a ambos lados; `--inverse` amarillo sobre oscuro.

## Snippets

**Alineado a la izquierda**

```html
<p class="eyebrow">What We Do</p>
```

**Centrado (`--center`)**

```html
<p class="eyebrow eyebrow--center">Our Pricing Plan</p>
```

**Sobre fondo oscuro (`--center --inverse`)**

```html
<p class="eyebrow eyebrow--center eyebrow--inverse">Client Feedback</p>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.eyebrow` | Texto de 16px medium con un cuadrito antes |
| `.eyebrow--center` | Centra el bloque y repite el cuadrito después |
| `.eyebrow--inverse` | Texto y cuadrito amarillos (solo sobre fondo oscuro) |

## Tokens que consume

- `--color-text-primary / -highlight`
- `--text-body`
- `--weight-medium`
- `--leading-snug`
- `--spacing-1 / -2`

## Accesibilidad

`<p>`, no encabezado: no altera la jerarquía. El cuadrito es CSS puro.

## Decisiones y excepciones

- El cuadrito mide 6px (1.5 × `--spacing-1`) porque así lo muestra el diseño; sale de la escala por cálculo.
- Texto de 16px (`--text-body`): medido en los PNG a resolución real (Etapa 4, Grupo B), los cuatro eyebrows de la home miden 1,16 veces lo que medían con `--text-sm`, tanto en desktop como en mobile.
