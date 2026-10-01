# SEO - obligatorio en toda página nueva

Sin build ni componente central: cada página HTML es un archivo suelto (ver `docs/stack.md`), así que el bloque de `<head>` de esta sección se copia entero en cada página nueva como plantilla fija — no se improvisa por página, aunque no haya un componente que lo fuerce.

## Meta tags básicos
- Cada página define `title` único y descriptivo (50-60 caracteres) y `meta description` (140-160 caracteres), escritos directo en el `<head>` de esa página — nunca heredados/copiados sin revisar de otra página.
- `<title>` sigue el patrón `{Título específico} | {Marca}`.
- Mantener un bloque `<head>` estándar (title, meta description, canonical, OG, Twitter, JSON-LD) documentado como snippet a copiar al crear cada página nueva, en el mismo orden siempre — así una revisión rápida detecta qué falta.

## Open Graph / Twitter Cards
- Toda página incluye `og:title`, `og:description`, `og:image`, `og:url`, `og:type`.
- `og:image` con dimensiones fijas (1200x630), generado por página cuando el contenido lo amerite (ej. blog posts).
- Twitter Card: `summary_large_image` como default.

## URLs y canonical
- URLs en minúsculas, con guiones (`-`), sin trailing slash inconsistente — definir la convención una vez (ver `docs/stack.md`) y aplicarla a mano en cada archivo/carpeta: no hay config central (`astro.config.mjs` o equivalente) que la fuerce.
- `<link rel="canonical">` obligatorio en cada página, con la URL absoluta real de esa página (dominio final, no `localhost`) — escrita a mano, ya que no hay `site` de config que la genere.
- Redirects 301 (no 302) para URLs cambiadas: se configuran a nivel de hosting (`_redirects` en Netlify, reglas del servidor/`.htaccess`), no hay middleware de aplicación que los resuelva.

## Structured Data (JSON-LD)
- Incluir schema.org según tipo de página: `Organization`/`WebSite` en home, `BreadcrumbList` en páginas internas, `Article` en blog, `Product` si aplica.
- JSON-LD inyectado en un `<script type="application/ld+json">` dentro del `<head>` de cada página, como parte del mismo bloque estándar de arriba — nunca duplicado entre header/footer compartidos y la página (no hay partials, pero sí puede repetirse por copy-paste si no se revisa).

## Semántica HTML
- Un solo `<h1>` por página, jerarquía de headings sin saltos (`h1`→`h2`→`h3`).
- Landmarks semánticos (`<main>`, `<nav>`, `<header>`, `<footer>`, `<article>`) — no todo en `<div>`.
- Enlaces internos con texto descriptivo (nunca "click aquí").
- `<html lang="...">` obligatorio en cada página, con el código de idioma real de esa página (mono-idioma por defecto — ver sección i18n más abajo si el proyecto es multi-idioma).
- `<meta name="viewport" content="width=device-width, initial-scale=1">` obligatorio en cada página.

## Internacionalización (i18n)
Fuera de alcance del theme base (mono-idioma por defecto, ver `docs/stack.md`). Si un proyecto de cliente concreto necesita multi-idioma, se resuelve así — no antes:

- Una carpeta por idioma (`/es/`, `/en/`) con las páginas HTML duplicadas y traducidas, cada una con su propio `<html lang="...">`.
- Cada página con versión en otro idioma incluye `<link rel="alternate" hreflang="{código}" href="{url absoluta}">` por cada variante disponible, más un `x-default` apuntando al idioma por defecto del sitio — escrito a mano en cada página, sin generación automática.
- El `hreflang` es recíproco: si la página en `es` referencia `en`, la página en `en` referencia de vuelta a `es` — un solo sentido rompe la señal para buscadores.
- `sitemap.xml` (ver "Archivos técnicos" abajo) incluye las variantes de idioma con sus `hreflang` correspondientes.

## Páginas fuera de indexación
- Todas las páginas bajo `/kit` (showcase de componentes, no contenido real del sitio) llevan `<meta name="robots" content="noindex, nofollow">` en su propio `<head>` — se copia siempre en las páginas de `/kit`, nunca se omite.
- Las rutas bajo `/kit` se excluyen a mano de `sitemap.xml`.
- Mismo criterio para cualquier página de borrador/staging/interna que no deba indexarse.

## Imágenes
- Usar `<picture>` con `<source>` en WebP/AVIF + `<img>` como fallback (nunca solo un `<img>` con formato legacy si hay alternativa moderna disponible), con `width`/`height` explícitos siempre (evita CLS).
- `alt` descriptivo obligatorio (ver sección de accesibilidad, ya cubierto en `accessibility.md`).
- Lazy loading por defecto (`loading="lazy"`), excepto imagen above-the-fold (`loading="eager"` + `fetchpriority="high"`).

## Performance (Core Web Vitals)
- Inicialización diferida de scripts pesados (GSAP timelines, Swiper) vía `IntersectionObserver` en vez de correr todo en `DOMContentLoaded` — ver `docs/stack.md` ("Equivalente a islands"). Impacta directo en LCP/TBT.
- Fonts: `font-display: swap` y precargar solo la fuente crítica con `<link rel="preload">`.
- Evitar CLS: dimensiones explícitas en imágenes/embeds, sin contenido que se inserte sin reservar espacio.
- Umbrales objetivo (medidos con Lighthouse/PageSpeed Insights, no solo estimados): LCP < 2.5s, CLS < 0.1, INP < 200ms. Cualquier página que no los cumpla se documenta como pendiente antes de deploy, no se ignora en silencio.

## Archivos técnicos
- `sitemap.xml` se escribe/mantiene a mano en la raíz del sitio (o con un script simple que liste los `.html` de `dist/` antes de deploy) — no hay generador automático de framework.
- `robots.txt` en la raíz del sitio, referenciando el sitemap.
- Dominio final: definirlo una sola vez y usarlo consistente en todos los `canonical`/OG de todas las páginas — al no haber config central, revisar manualmente al pasar de staging a producción.
- Favicon, `apple-touch-icon` y `manifest.webmanifest` (si aplica PWA): mismo bloque `<head>` copiado en cada página, no queda a criterio de cada una.

## Verificación (antes de dar por cerrada una página o hacer deploy)
- Inspeccionar el `<head>` realmente servido (view-source), confirmando que title, meta description, canonical, OG/Twitter y JSON-LD aparecen con los valores correctos — al copiar el bloque estándar entre páginas es fácil dejar un valor sin actualizar.
- Validar el JSON-LD con [Rich Results Test](https://search.google.com/test/rich-results) de Google.
- Correr Lighthouse/PageSpeed sobre los archivos servidos tal cual van a producción (no solo abiertos como `file://` local).
- Confirmar que `sitemap.xml` lista URLs reales del dominio final (no `localhost`) y que las rutas `noindex` (ej. `/kit`) no aparecen en él.

## Contenido
- Cada página de contenido (no componentes del kit) define su propio `title`/`description` en su `<head>` — nunca copiar sin revisar el de otra página.
- Slugs de blog/artículos: descriptivos, con keyword principal, sin fechas ni IDs numéricos.
