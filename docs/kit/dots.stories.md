# Pagination Dots

**Nivel:** Átomo · 15  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Pagination Dots */`) · showcase en `dist/kit/index.html#dots`

## Descripción

Puntos de paginación. Cada punto es un botón de 24×24px; el activo lleva halo.

## Snippets

**Sobre fondo claro**

```html
<div class="dots" role="group" aria-label="Choose a story">
  <button type="button" class="dots__dot" aria-label="Show story 1"></button>
  <button type="button" class="dots__dot" aria-label="Show story 2"></button>
  <button type="button" class="dots__dot" aria-label="Show story 3" aria-current="true"></button>
  <button type="button" class="dots__dot" aria-label="Show story 4"></button>
  <button type="button" class="dots__dot" aria-label="Show story 5"></button>
  <button type="button" class="dots__dot" aria-label="Show story 6"></button>
</div>
```

**Sobre fondo oscuro (`dots--inverse`)**

```html
<div class="dots dots--inverse" role="group" aria-label="Choose a story">
  <button type="button" class="dots__dot" aria-label="Show story 1"></button>
  <button type="button" class="dots__dot" aria-label="Show story 2"></button>
  <button type="button" class="dots__dot" aria-label="Show story 3" aria-current="true"></button>
  <button type="button" class="dots__dot" aria-label="Show story 4"></button>
  <button type="button" class="dots__dot" aria-label="Show story 5"></button>
  <button type="button" class="dots__dot" aria-label="Show story 6"></button>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.dots` | Fila de puntos; el color activo es --dots-active |
| `.dots--inverse` | Activo amarillo para fondos oscuros |
| `.dots__dot` | Botón de 24×24px; el punto (12px) se dibuja en ::before |
| `aria-current="true"` | Marca el punto activo; el cambio de slide lo mantiene sincronizado (organismo Carrusel) |

## Tokens que consume

- `--color-border-strong (inactivo)`
- `--color-action-primary / --color-text-highlight (activo)`
- `--spacing-1 / -3 / -6`
- `--radius-full`
- `--ease-base`

## Accesibilidad

Cada botón nombra su destino; el activo con `aria-current`; inactivo ≥3:1 sobre claro y oscuro.

## Decisiones y excepciones

- El inactivo del diseño es un gris translúcido más tenue; se usa `border-strong` porque es el único token que llega a 3:1 en ambos fondos.
