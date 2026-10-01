# Card Hero

**Nivel:** Molécula · 09  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Hero */`) · showcase en `dist/kit/index.html#card-hero`

## Descripción

Tarjeta translúcida del hero: miniatura, número y título. Estática, no enlaza.

## Snippets

**Sobre foto**

```html
<div class="card-hero">
  <img class="card-hero__media" src="../assets/img/h1-hero-thumb-img.webp" alt="" width="160" height="182" loading="lazy">
  <div class="card-hero__body">
    <span class="card-hero__index">01</span>
    <p class="card-hero__title">Creative Business Insights</p>
  </div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-hero` | Fila con miniatura y texto sobre el velo oscuro del theme (--color-overlay) con borde translúcido |
| `.card-hero__media` | Miniatura de 160px de ancho |
| `.card-hero__index` | Número en amarillo |
| `.card-hero__title` | Título en 24px medium; es un párrafo, no un encabezado |

## Tokens que consume

- `--color-overlay / --color-overlay-light (borde)`
- `--color-text-inverse / -highlight`
- `--radius-md / -sm`
- `--spacing-2 / -3 / -4 / -11`
- `--text-h4`

## Accesibilidad

Sin interacción; título `p` (no compite con el `h1`); el hero aporta el velo.

## Decisiones y excepciones

- El diseño muestra la tarjeta con un velo teñido de petróleo; se usa el `--color-overlay` del theme (el mismo de los badges) en vez de un blanco al 10%, que no daba lectura sobre fotos claras.
