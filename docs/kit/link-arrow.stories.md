# Link Arrow

**Nivel:** Átomo · 04  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Link Arrow */`) · showcase en `dist/kit/index.html#link-arrow`

## Descripción

Enlace con flecha («Read More ↗»). Subraya en hover. `--inverse` sobre cards oscuras; `--highlight` amarillo solo sobre fondo oscuro.

## Snippets

**Sobre fondo claro**

```html
<a href="#link-arrow" class="link-arrow">
  Read More
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</a>
```

**Sobre fondo oscuro: `--inverse` y `--highlight`**

```html
<a href="#link-arrow" class="link-arrow link-arrow--inverse">
  Read More
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</a>
<a href="#link-arrow" class="link-arrow link-arrow--highlight">
  Contact Us
  <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
</a>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.link-arrow` | Texto en color primario, medium, con flecha; subrayado en hover |
| `.link-arrow--inverse` | Texto blanco, para cards y bloques oscuros |
| `.link-arrow--highlight` | Texto amarillo: solo sobre fondo oscuro (nunca sobre el crema, 1.4:1) |

## Tokens que consume

- `--color-text-primary / -inverse / -highlight`
- `--weight-medium`
- `--spacing-2`
- `--ease-fast`

## Accesibilidad

Texto descriptivo; varios «Read More» repetidos llevan `aria-label` con el título del post.

## Decisiones y excepciones

- Para que un «Read More» repetido sea distinguible, el post card (Moléculas) añadirá el título como texto accesible.
