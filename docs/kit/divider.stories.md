# Divider

**Nivel:** Átomo · 11  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Divider */`) · showcase en `dist/kit/index.html#divider`

## Descripción

Filete de 1px sobre `<hr>`. `--inverse` para fondos oscuros.

## Snippets

**Sobre fondo claro**

```html
<hr class="divider">
```

**Sobre fondo oscuro (`divider--inverse`)**

```html
<hr class="divider divider--inverse">
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.divider` | Filete de 1px con el color de borde sutil |
| `.divider--inverse` | Filete translúcido blanco para fondos oscuros |

## Tokens que consume

- `--color-border-subtle`
- `--color-overlay-light`
- `--border-width-sm`

## Accesibilidad

`<hr>` expone un separador; si es puramente decorativo, usar `border` del componente.

## Decisiones y excepciones

- El filete del hero (parcial, blanco al 30%) es propio del Hero y no pasa por este átomo.
