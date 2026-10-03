# Icons

**Nivel:** Átomo · 01  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Icons */`) · showcase en `dist/kit/index.html#icons`

## Descripción

Lucide como máscara CSS: `.icon` hereda color y tamaño del contexto. Las redes sociales no están en Lucide: son SVG propios del mismo trazo.

## Snippets

**Uso**

```html
<span class="icon icon--arrow-up-right" aria-hidden="true"></span>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.icon` | Base: cuadrado de 1em que pinta el glifo con el color del texto |
| `.icon--{nombre}` | Elige el glifo (ver lista). Se agrega un modificador por ícono nuevo en main.css |
| `aria-hidden="true"` | Siempre: el ícono es decorativo y el nombre accesible lo da el texto o el aria-label del contenedor |

## Tokens que consume

- `--text-body (tamaño heredado)`
- `--color-text-primary (color heredado)`

## Accesibilidad

Un ícono nunca es el único portador de significado: el contenedor lleva texto o `aria-label`. En colores forzados pasa a `CanvasText`.

## Decisiones y excepciones

- Lucide es la única librería de iconos permitida; los glifos de redes (facebook, linkedin, instagram, x-twitter) son propios porque Lucide no incluye logos de marca.
- `circle-check` es un círculo relleno con la marca recortada (máscara interna), como el check de las listas de pricing; Lucide solo trae la versión de contorno.
- `play` va relleno (el diseño lo muestra sólido).
- `badge-check` (Document Required de Service Details) es el sello con la marca; `circle-check-outline`, el círculo con la marca en contorno.
