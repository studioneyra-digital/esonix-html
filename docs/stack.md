# Stack

- **HTML5 + CSS3 nativo + JavaScript vanilla (ES6+). Sin build, sin bundler, sin framework de componentes** 
- Reutilización de componentes por **copy-paste entre páginas**: no hay sistema de includes/partials ni compilador. El markup canónico de cada componente vive documentado en `dist/kit/index.html`; construir una página nueva es copiar ese markup y reemplazar el contenido de ejemplo por el real.
- CSS con custom properties como tokens (ver `docs/design-tokens.md`), repartido en `assets/css/tokens/*.css` (un archivo por familia de token) + un único `assets/css/main.css` para foundations/átomos/moléculas/organismos/sections — cargados como `<link>` normales, en ese orden, en el `<head>` de cada página. Nunca crear un segundo archivo de componentes: todo el CSS de componentes va en `main.css`, comentado por bloque (`/* Hero */`, `/* Card Service */`).
- **Bootstrap 5** (solo su Grid System, vendorizado en `assets/css/bootstrap-grid.min.css`) para containers/grid. El resto de los estilos es CSS propio sobre tokens — no usar utilidades ni componentes de Bootstrap más allá del grid.
- Librerías vendorizadas en `assets/js/` (nunca instaladas vía npm ni cargadas desde un CDN dinámico): jQuery, GSAP + ScrollTrigger, Lenis, Swiper-bundle, WOW.js. Mismas versiones que ya usa el resto del workspace salvo que el proyecto pida lo contrario.
- Interactividad en **JavaScript vanilla**, centralizada en un único `assets/js/main.js` (separar por archivo solo si crece demasiado, y documentar la razón si pasa). Nada de islands ni frameworks de componentes (React/Vue/Svelte) — no hay estado de cliente lo bastante complejo en un sitio de contenido para justificarlo.
- Sin backend/DB. **Sin gestor de paquetes ni `package.json`**: los assets van vendorizados directo en el repo. Para desarrollo local alcanza con abrir el HTML o un servidor estático simple (`npx serve`, extensión Live Server) — no es una dependencia del proyecto, solo conveniencia de desarrollo.
- **Sin CMS ni i18n de fábrica**: contenido hardcodeado en el HTML de cada página, en un solo idioma. 

## Equivalente a "islands" (lazy init)

Sin Astro no hay `client:visible`/`client:idle`. El equivalente es inicializar cualquier efecto pesado (timeline de GSAP, instancia de Swiper, etc.) con **`IntersectionObserver`** recién cuando el elemento entra al viewport, en vez de correr todo en `DOMContentLoaded`:

```js
const el = document.querySelector('.hero-slider');
const observer = new IntersectionObserver((entries, obs) => {
  if (!entries[0].isIntersecting) return;
  initHeroSlider(el); // instancia Swiper/GSAP recién acá
  obs.disconnect();
}, { rootMargin: '200px' });
observer.observe(el);
```

Importar/usar solo los plugins de GSAP que el componente necesite — nunca el bundle completo.

## Lenis + GSAP/ScrollTrigger

- **Lenis** es el motor de scroll (smooth/inertia scroll); no anima nada por sí solo. **GSAP + ScrollTrigger** resuelve animaciones ligadas al scroll y pinning.
- Integración estándar: ScrollTrigger debe sincronizar su ticker con el de Lenis (Lenis controla el scroll real; GSAP escucha su evento `scroll` y actualiza ScrollTrigger en cada `requestAnimationFrame`). No implementar scroll-jacking manual si Lenis + ScrollTrigger ya resuelven el caso.
- Cargar como script normal en `assets/js/`, inicializar de forma diferida según la sección (ver "Equivalente a islands" arriba); importar solo los plugins de GSAP que el componente use, nunca el bundle completo.
- Tokens: toda animación (incluida la ligada a scroll) usa los tokens de `assets/css/tokens/transitions.css` (`--ease-fast/base/slow`, `--duration-spin`); no valores mágicos por componente. `prefers-reduced-motion` ya está resuelto ahí a nivel token — cualquier efecto de scroll (parallax, reveal, pin) hereda la reducción automáticamente y no necesita lógica propia, salvo que además deba desactivar el `ScrollTrigger`/pin en sí (no solo la transición visual).
- Performance: medir impacto en CLS e INP antes de validar cualquier animación en el viewport inicial (hero/above-the-fold).
- Referencia de catálogo de patrones (parallax, reveal, pinning, cursor, etc.) y su mapeo a niveles atómicos: `docs/interactions-catalog.md`.

## Decisiones de la etapa Cimientos

- **CSS y JS del kit:** `assets/css/kit.css` (chrome del showcase: sidebar, fichas, snippets) es la excepción documentada a "un único `main.css`". Se carga solo desde `dist/kit/index.html`, para que las páginas de cliente no descarguen CSS de documentación, y no contiene componentes. El JS del kit va inline en su propia página y no toca `main.js`; si supera unas 300 líneas se evalúa `assets/js/kit.js`, documentando la razón.
- **Fuentes autoalojadas** en `assets/fonts/` (woff2 variable, subset latin, `font-display: swap`): Mona Sans (eje `wght` 200–900, descargada de Fontsource) para todo el sitio y JetBrains Mono (solo `/kit`). Se precarga únicamente Mona Sans. Las licencias SIL OFL 1.1 están en `assets/fonts/LICENSES.md`. Los temas anteriores importaban Google Fonts; aquí no, porque precargar la fuente crítica exige una URL estable.
- **jQuery** figura en el stack, pero el doc pide JS vanilla y ninguna otra librería lo requiere: se vendoriza sin cargarlo hasta que un componente lo necesite.
- **Grid y breakpoints:** las columnas usan las clases del grid de Bootstrap con sus breakpoints (sm 576, md 768, lg 992, xl 1200, xxl 1400); todo `@media` propio usa los del theme (30/48/64/80rem, ver `design-tokens.md`); no se mezclan ambos en un mismo componente. Solo `md` coincide.
- **Navegadores objetivo:** las 2 últimas versiones de Chrome, Edge, Firefox y Safari (el theme usa `color-mix()`, `clamp()`, `:focus-visible` e `inert`).
- **Servidor local:** por `file://` Chromium bloquea por CORS el `<link rel="preload">` de las fuentes y lo registra como error en consola; las fuentes cargan igual por `@font-face`, pero el preload solo funciona por http. Para desarrollar y para medir rendimiento usa un servidor estático (`python -m http.server` o `npx serve`), que no es una dependencia del proyecto.
