# Page Hero

**Nivel:** Section · 13  
**Dónde:** markup en `dist/about-us.html` (entre `<!-- section:page-hero -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#page-hero`

## Descripción

Cabecera de páginas interiores: foto con velo, breadcrumb en píldora y `<h1>` abajo a la izquierda en el `.container`. 750px (desktop) / 420px (mobile). Reserva el alto del header fijo.

## Snippet

```html
<section class="page-hero" aria-labelledby="page-title" data-surface="inverse">
  <div class="page-hero__media">
    <img src="assets/img/about-page-header-bg.webp" alt="" width="1920" height="750" fetchpriority="high">
  </div>
  <div class="container page-hero__content">
    <nav class="breadcrumb" aria-label="Breadcrumb" data-reveal>
      <ol class="breadcrumb__list">
        <li><a href="./">Home</a></li>
        <li><span aria-current="page">About Us</span></li>
      </ol>
    </nav>
    <h1 class="page-hero__title" id="page-title" data-reveal>Consulting That Delivers Measurable Results</h1>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.page-hero + data-surface="inverse"` | Foto de fondo y texto blanco; la superficie inversa da el foco claro sobre la foto |
| `.page-hero__media` | Capa de la foto (object-fit: cover) con el velo en ::after (izquierda y abajo) |
| `.container.page-hero__content` | Breadcrumb y h1 apilados, alineados con el contenido de las secciones |
| `nav.breadcrumb[aria-label="Breadcrumb"] > ol.breadcrumb__list` | Píldora translúcida; el guion entre ítems es contenido generado sin texto alternativo |
| `span[aria-current="page"]` | La página actual, sin enlace |
| `h1.page-hero__title` | Título de la página con --text-h1; corta en 45rem |

## Tokens que consume

- `--text-h1`
- `--color-overlay / -overlay-light`
- `--color-text-inverse`
- `--header-offset`
- `--radius-full`
- `--spacing-1 / -2 / -5 / -6 / -7 / -10 / -11`

## Accesibilidad

Único `<h1>`. Breadcrumb: `<nav aria-label="Breadcrumb">` + `<ol>`, actual con `aria-current="page"`, separador sin texto. Foto decorativa precargada (LCP). `data-surface="inverse"`: foco claro.

## Decisiones y excepciones

- `--text-h1` (48/36px) en lugar de los ≈ 62/41px que mide el diseño: decisión del usuario, sin token nuevo.
- Reutilizable en las 7 páginas interiores: cambia la foto, el último ítem del breadcrumb y el h1.
- La foto es `about-page-header-bg.webp` (1920×750, el recorte exacto del diseño); en mobile se encuadra con `object-position`.
- Service Details usa `h1-process-img-2.webp` y Contact `h1-blog-img-3.webp` (fotos sustitutas de la biblioteca, 1000 y 1308px de ancho: a 1920 se ven algo blandas bajo el velo).
