# Traspaso — Etapa 4 (para retomar en una sesión nueva)

Estado al 2026-10-02. Leer este archivo alcanza para seguir: no hace falta releer `plan.md` ni los PNG enteros. Detalle por grupo en `docs/plan-etapa-4.md`. Borrar este archivo al cerrar la Etapa 4.

## 1. Dónde estamos

- Rama `feat/design-to-web-esonix`, sin push. Commits de la etapa: Grupo 0 `ec35449`, A `6b1c63f`, B `4609855`.
- **Grupo C construido y revisado, SIN COMMIT** (Stats, Testimonials, Team, Logos, FAQ, Blog, Footer). Primer paso: preguntar al usuario si lo aprueba y commitear con rutas explícitas (nunca `git add -A`: el `git status` muestra borrados de otros proyectos del workspace, como `nova-exploration`, que no son de este trabajo; `.playwright-cli/` tampoco va). Mensaje sugerido: `feat(design-to-web): Stats, Testimonials, Team, Logos, FAQ, Blog y Footer (etapa 4, grupo C)`.
- Archivos del Grupo C: `dist/index.html`, `dist/assets/css/main.css`, `dist/kit/index.html`, `docs/tools/{molecules_css,molecules_kit,organisms_kit,sections_kit}.py`, `docs/kit/*.stories.md` (nuevos: stats, testimonials, team, logos, faq, blog, footer; modificados: accordion-item, newsletter, carousel), `docs/plan.md`, `docs/plan-etapa-4.md` y este archivo.
- **Falta el Grupo D (cierre):** `sitemap.xml` y `robots.txt` (`/kit` con `noindex` y fuera del sitemap); revisar imágenes (`width`/`height`, `loading="lazy"`; el hero `eager` + `fetchpriority="high"`; no hay formato legacy, así que no se usa `<picture>`); Lighthouse sobre archivos servidos (LCP < 2.5 s, CLS < 0.1, INP < 200 ms); comparación final contra los PNG en desktop y mobile; auditoría de accesibilidad (axe, teclado, un pase con lector de pantalla); reporte de lo que no se pudo igualar.

## 2. Cómo está armada la página

- `dist/index.html` es la única fuente de las Sections. Cada una va entre `<!-- section:id -->` y `<!-- /section:id -->` (13: hero, what-we-do, services, why-choose-us, finance, pricing, stats, testimonials, team, logos, faq, blog, footer). `python docs/tools/sections_kit.py` las extrae al kit y escribe `docs/kit/<id>.stories.md`; los metadatos de cada ficha son la lista `S` del script.
- CSS de Sections: bloque `/* sections:start … sections:end */` de `main.css`, escrito a mano. Los bloques `atoms:` / `molecules:` / `organisms:` los **reescriben** los generadores `docs/tools/*_css.py`: un cambio de átomo o molécula se hace en el `.py` y se regenera; nunca editar esos bloques a mano.
- Piezas compartidas del bloque de Sections: `.section` (64 / 96px), `.section-title`, `.section-head` (`__main`, `__title`, `__text`, `__actions`; `--split` desde xl con posiciones explícitas en la grilla; `--center`), `.photo-frame`, `.feature-strip`, `.stats__level`, `.logo-grid`, `.page-footer`. Contenedores: `.container` (1320 de contenido desde xxl) y `.container-wide` (1620), con gutter `--spacing-7`, y las custom properties `--container-width` / `--container-wide-width`.
- JS (`main.js`): carrusel con el activo centrado, `data-carousel-start` / `-start-wide` / `-highlight` y copias del loop si hay < 6 slides (`aria-hidden` + `inert`); Word List con ScrollTrigger sin pin; `initPricingSwitch` con anuncio `role="status"` solo al cambiar.

## 3. Decisiones vigentes (no volver a preguntar)

Dominio placeholder `https://esonix.example` · Finance: foto desenfocada fija (capa `position: fixed` recortada por `clip-path`) · «Works» mobile decorativo + `<h2>` oculto · logos mobile: 4 imágenes repetidas hasta 7 celdas · «30+» = «Years of Consulting Experience» · Services destaca el slide activo · «Read More» de la card 02 de Why Choose se mantiene en mobile · Testimonials en el orden del diseño (Isabella tercera) · commits explícitos, un grupo por commit · Sections con CSS Grid y breakpoints del theme (sm 30 / md 48 / lg 64 / xl 80 rem); solo `--why-container` replica los de Bootstrap (excepción escrita en `design-tokens.md`).

## 4. Desvíos conocidos (van al reporte final del Grupo D)

Ritmo entre secciones de 192px (96 + 96) contra ≈170 del diseño · velo de Finance más denso que el diseño, para que haya contraste · acordeón ~50px más corto que la Card CTA a 1920 · cifras de Stats y título de What We Do con el token (36 / 48px) contra ≈42 / 50 del diseño · imagen de Card Post 4:3 (diseño ≈ 1.38) · logos de partners en negro (el diseño, en gris) · íconos Lucide en lugar de los glifos propios del diseño · placeholders: Financial Planning, Brand Strategy, Michael Brooks, Sophia Martinez, respuestas 1, 3 y 4 del FAQ, palabras Advisory / Growth / Strategy · artefactos del export que no se replican: encabezado del Blog duplicado, «Pixenium», «404 Not Error», barra repetida en What We Do mobile, ítem repetido en Premium mobile.

## 5. Cómo verificar (receta probada)

- **Servidor:** `python <scratchpad>/serve.py <raíz del proyecto> 8765`, en segundo plano. Es una subclase de `ThreadingHTTPServer` con `Cache-Control: no-store` (12 líneas, receta en la memoria `playwright-cli-qa-recipes`). Página: `http://127.0.0.1:8765/dist/index.html`; kit: `/dist/kit/index.html`. Para detenerlo, PowerShell: `Get-NetTCPConnection -LocalPort 8765 -State Listen | % { Stop-Process -Id $_.OwningProcess -Force }`.
- **Navegador:** `playwright-cli -s=<nombre> open <url>`, siempre con sesión nombrada, y correrlo desde el scratchpad para que `.playwright-cli/` no ensucie el repo. Los scripts van en un archivo: `run-code --filename=<ruta absoluta>.js` con `async page => { … return JSON.stringify(…) }`.
- **Capturas por sección:** recorrer la página con scroll para disparar los IntersectionObserver y después `page.screenshot({ fullPage: true, clip })` desde el top de cada id. Las capas `position: fixed` (Finance) se capturan con la sección en pantalla, sin `fullPage`. Ojo: tras navegar al kit, volver a la página antes de medir.
- **Diseño a resolución real:** los PNG están en `docs/design/` (desktop 1920 en dos partes, mobile 480). Recortarlos por tramos (~1000px en desktop, ~1400px en mobile) con `page.setContent('<img…>')` + `clip`. Para un tamaño de texto, comparar el ancho del texto en la página (Range de `getBoundingClientRect`) con el del PNG: así se detectaron el Eyebrow (14 → 16px) y el Accordion.
- **Auditoría que pasó en A, B y C:** ids duplicados, referencias ARIA y anclas `#` rotas, un solo h1, foco visible con Tab, `scrollWidth` a 1920 / 1440 / 1280 / 1024 / 768 / 390, «reducir movimiento» (velocidad del carrusel 0, Marquee quieto, Word List en Growth) y consola limpia, en la página y en el kit.

## 6. Trampas ya encontradas

- Swiper con loop + `centeredSlides` y 5 slides deja un hueco al avanzar: se resolvió duplicando la tanda (sección 2).
- Una grilla con `grid-row` explícito y columna automática reordena los ítems: en `--split` las posiciones van con `grid-area` explícito.
- `overflow` no recorta descendientes `position: fixed`; `clip-path` sí. `backdrop-filter` / `filter` / `transform` en un ancestro rompen `position: fixed`.
- La regla de foundations pone en blanco los `h1`–`h6` dentro de `data-surface`: una card blanca anidada en una superficie oscura necesita la excepción `html .card-x :is(h1…h6)`, como la que ya tiene `.card-project`.
- Un `data-surface` propio pinta fondo: el Marquee dentro del footer va sin él, para que se vea la foto.
- Componente con `display: grid` en una fila más alta: sin `align-content: start` reparte el sobrante entre sus filas (le pasaba al Newsletter).
- Texto largo en un track `max-content` estira un ancestro grid o flex: el Marquee lleva `contain: inline-size`.
