# Button

**Nivel:** Átomo · 02  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Button */`) · showcase en `dist/kit/index.html#button`

## Descripción

Píldora de texto con círculo de ícono. Petróleo sobre fondo claro; `--light` para fondo oscuro; `--block` para el ancho de una card; `--accent` el relleno amarillo. `<button>` o `<a>`.

## Snippets

**Sobre fondo claro**

```html
<button type="button" class="btn">
  Get Started
  <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
</button>
<a href="#button" class="btn">
  Learn More
  <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
</a>
```

**Sobre fondo oscuro (`btn--light`)**

```html
<button type="button" class="btn btn--light">
  Get Started
  <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
</button>
```

**Ancho de card (`btn--block`) y su relleno amarillo (`btn--accent`)**

```html
<button type="button" class="btn btn--block">
  Get Started
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn--block btn--accent">
  Get Started
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</button>
```

**Deshabilitado**

```html
<button type="button" class="btn" disabled>
  Get Started
  <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
</button>
<button type="button" class="btn btn--block" disabled>
  Get Started
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</button>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.btn` | Píldora petróleo con texto blanco y círculo amarillo |
| `.btn__icon` | Círculo de 40px que envuelve el ícono (solo en el botón con círculo) |
| `.btn--light` | Para fondos oscuros: píldora blanca, círculo petróleo |
| `.btn--block` | Ocupa todo el ancho, texto centrado y flecha en línea, sin círculo |
| `.btn--accent` | Relleno amarillo con texto oscuro; se usa con --block (plan destacado) |
| `disabled / aria-disabled="true"` | Estado deshabilitado; en un <a> usar aria-disabled y quitar el href |

## Tokens que consume

- `--color-action-primary(-hover/-active/-disabled)`
- `--color-action-secondary(-hover)`
- `--color-action-on-primary`
- `--color-action-on-secondary`
- `--color-surface-default`
- `--color-background-subtle`
- `--spacing-1 / -5 / -6 / -8`
- `--radius-full`
- `--text-body`
- `--weight-medium`
- `--ease-fast`

## Accesibilidad

Texto descriptivo; ícono `aria-hidden`; foco con el anillo global; altura 48px.

## Decisiones y excepciones

- Altura 48px (círculo de 40px + 4px de aire): el diseño mide ~52px, pero sale de la escala de espaciado y no de estimar la imagen.
- Los estados hover, active y disabled no están en el diseño: se derivan de los tokens `action-primary-hover/-active/-disabled` ya definidos.
- No hay variante `--light` + `--block`: el diseño solo usa `--block` sobre cards claras y la destacada oscura usa `--accent`.
