# Plan — Theme Esonix (design-to-web)

Home de **Esonix** (consultora) construida desde los diseños de `docs/design/` como theme HTML/CSS/JS estático, por etapas. Cada etapa se entrega para revisión y se audita contra `anti-patrones.md` antes de pasar a la siguiente. Modelo y esfuerzo recomendados por etapa: `CLAUDE.md` §9.

## Estado

| Etapa | Contenido | Estado |
|---|---|---|
| 0 · Cimientos | Tokens, Mona Sans, `main.css`/`main.js` base, kit con Foundations | ✅ Hecha |
| 1 · Átomos | 12 átomos con ficha en el kit y `.stories.md` | ✅ Hecha |
| 2 · Moléculas | 12 moléculas + átomo Input, con ficha en el kit y `.stories.md` | ✅ Hecha |
| 3 · Organismos | Header, menú mobile, carrusel, lista con scroll, marquee, footer, modal | ⏳ En curso (Grupo A hecho, B en revisión) |
| 4 · Sections + `index.html` | Las secciones de la home, responsive | ⬜ |

## Reglas de cada etapa

- Revisar `dist/kit/index.html` antes de construir: no duplicar un componente equivalente.
- Los valores salen de los tokens, no de estimar la imagen. Los componentes usan solo tokens semánticos.
- Cada componente se documenta en el kit (variantes sobre claro y oscuro, snippet copiable, tabla de clases, tokens que consume, accesibilidad) y en `docs/kit/<nombre>.stories.md`.
- Verificar en navegador a 1440 px y 390 px: contraste AA, teclado, sin errores de consola, `prefers-reduced-motion`.
- Si el diseño no muestra un estado o comportamiento, se deriva de tokens existentes y se declara en la ficha; no se inventa en silencio.

## Decisiones tomadas

**Del equipo**
- Tokens de Skyline reemplazados por los de `design-tokens.md`; la fuente es **Mona Sans** (única familia, más JetBrains Mono solo en `/kit`).
- Token propio **`--text-hero`** (≈ 40 px en mobile, ≈ 170 px a 1920 px) para el titular gigante del hero y el marquee del footer.
- Logo solo en PNG: `secondary-logo.png` sobre fondo claro, `primary-logo.png` sobre oscuro.
- Cards destacadas (Process Optimization, Why Choose 02, Emma Wilson elevada, plan Enterprise): **siempre destacadas**, no son hover.
- Card «01 Creative Business Insights» del hero: **estática**.
- Bloque Finance / Advisory / Growth / Strategy: la palabra activa **cambia con el scroll**; las otras cards llevan texto placeholder.
- Testimonio en video: `https://youtu.be/RqueNBILfVU`.
- **Stats y grilla de logos solo en mobile.**
- Copy faltante (teléfono, copyright, dropdowns de Home/Services/Blog, etc.): placeholder. Los errores del export (encabezado del blog duplicado, «Pixenium», «404 Not Error», items repetidos en mobile) no se replican.

**Derivadas de los tokens**
- Tokens agregados: `--color-text-highlight` (amarillo como texto, solo sobre oscuro) y `--color-action-on-secondary` (texto oscuro sobre el amarillo). `brand-accent` apunta a `brand-secondary`: no hay tercer color.
- El gris de cuerpo del diseño (`#727979`) da 4.30:1 sobre el crema y no llega a AA: se usa `neutral-600` (`#646e6e`, 5.09:1).
- Las cards van en blanco puro (`#ffffff`), como el diseño; es la única excepción a «neutros sin matiz».
- El CTA principal es petróleo y el amarillo es relleno con texto oscuro; el amarillo nunca es texto sobre claro (1.4:1).
- `--color-text-inverse-secondary` sube de 72% a 78% de blanco: con 72% el texto atenuado sobre el panel claro del plan destacado daba ≈4.4:1 y no llegaba a AA.
- Nueva superficie `data-surface="brand"` (petróleo `--color-action-primary`) junto a `inverse`; ambas ganan al fondo propio de un componente (especificidad `html [data-surface]`).
- **Excepción a anti-patrones #4 (card anidada):** la lista de beneficios de Card Pricing es un panel con borde dentro de la card porque el diseño lo muestra así.

## Etapa 0 — Cimientos ✅

- `color.css`: escalas de amarillo, petróleo y neutrales cálidos (anclas medidas sobre los PNG); semánticos verificados a AA.
- `typography.css` con Mona Sans autoalojada (`assets/fonts/`, licencias en `LICENSES.md`).
- `main.css` base (foco, superficie inversa, accesibilidad) y `main.js` con Lenis sincronizado a ScrollTrigger, apagado con reduced-motion.
- `kit/index.html` con sidebar funcional y Foundations: Brand, Colors (con contraste calculado en vivo), Typography, Spacing, Radius, Shadows, Borders, Motion, Z-index, Breakpoints y Page head.
- `design-tokens.md`, `stack.md` y `anti-patrones.md` alineados con lo construido.

## Etapa 1 — Átomos ✅

Icons (Lucide como máscara CSS + redes sociales propias) · Button (`--light`, `--block`, `--accent`) · Icon Button (`--glass`, `--sm`, `--lg`; también es el Social Icon) · Link Arrow · Eyebrow · Badge · Avatar y Avatar Stack · Progress (`<progress>` nativo) · Switch (`role="switch"` nativo) · Divider · Pagination Dots · Scroll Top (con anillo de progreso de scroll).

## Etapa 2 — Moléculas ✅

Componen 2–4 átomos y no conocen el contexto de página. Las cards destacadas usan `data-surface="brand"` (petróleo) y las que van sobre foto el patrón `card-photo` con `data-surface="inverse"`. Se sumó el átomo **Input** (la newsletter lo necesita) y 9 iconos Lucide (target, trending-up, chart-pie, users, lightbulb, rocket, gem, award, hexagon).

| Molécula | Variantes y notas |
|---|---|
| Card Service | normal y destacada (oscura); imagen, ícono Lucide, título, texto |
| Card Feature numerada | normal y destacada con foto de fondo; «Read More» solo en la destacada |
| Card Pricing | normal y destacada (Enterprise); lista con checks, el último ítem atenuado |
| Card Testimonial | de texto y de video (botón play que abre el modal de la Etapa 3) |
| Card Team | normal y elevada; badge de rol + botón «+» |
| Card Post | imagen con badge de fecha (`<time>`), título, extracto, «Read More» |
| Card Project | `// 01` + título; usada en el bloque Finance |
| Card CTA con imagen | «Still have questions?» + «Contact Us ↗» |
| Card Hero | translúcida, estática |
| Stat | número + etiqueta (solo mobile) |
| Ítem de acordeón | `<details name>` nativo (exclusivo, sin JS); «?» que se pone amarillo al abrir |
| Campo de newsletter | input con `<label>`, línea inferior y botón enviar |

Resuelto: foco amarillo sobre cards con foto (`data-surface="inverse"`), «Read More» distinguible (título oculto para lectores) y la elevación de la card de equipo con margen negativo desde `lg`. Pendiente para la Section: reservar el espacio de esa elevación, el cambio Monthly / Annually y el contenedor blanco que une las tres cards Feature.

## Etapa 3 — Organismos ⏳

Se entrega en tres grupos, cada uno revisado antes del siguiente:

| Grupo | Organismos | Estado |
|---|---|---|
| A · Navegación | Site Header (con submenús) y Off-canvas | ✅ Hecho |
| B · Contenido interactivo | Carrusel (Swiper), Acordeón FAQ, Modal de video | 🔍 En revisión |
| C · Scroll y cierre | Lista de palabras con ScrollTrigger, Marquee, Footer | ⬜ |

**Grupo A, resuelto:** el header responde al ancho de su contenedor con container queries (48/64/80rem sobre el ancho del header), porque la barra completa necesita ~1150px y con el container de Bootstrap ya se desbordaba a 1280px; los submenús son botones de divulgación con hover, Escape y cierre al salir el foco; el off-canvas deja `inert` el resto de `<body>`, detiene Lenis y desenfoca la página con el nuevo token `--blur-backdrop`. CSS y fichas salen de `docs/tools/organisms_*.py`; el JS está en `main.js`.

**Grupo B, resuelto:** carrusel sobre Swiper 11 (loop con un vecino asomando a cada lado desde la carga, 1/2/3 slides según el ancho del carrusel, igual que el header, a11y de Swiper, flechas vinculadas por `aria-controls` y dots generados por `main.js`); acordeón como grupo de `<details name>` con altura animada por `::details-content`; modal de video con `<dialog>` nativo y el iframe de youtube-nocookie creado recién en el click. El kit carga `swiper-bundle.min.css/js`; la Section que use el carrusel recorta con `overflow-x: clip`.

**Plan original de la etapa:**

- **Header:** logo, links en pill blanca, redes en texto, teléfono con botón de chat; dropdowns de Home, Services, Pages y Blog (Pages con el contenido real del diseño, el resto placeholder).
- **Menú off-canvas mobile:** acordeones, Location, Contact y redes; `inert` en el resto de la página y cierre con Escape.
- **Carrusel (Swiper):** una base reutilizada en Services (flechas) y Testimonials (dots); se inicializa con `IntersectionObserver`.
- **Acordeón:** FAQ con los ítems `<details name="faq">` de la Etapa 2; solo falta el grupo (un ítem abierto a la vez ya lo da el atributo `name`). Si se quiere animar la altura, se hace con `::details-content`.
- **Lista de palabras con scroll (GSAP ScrollTrigger):** la palabra activa queda nítida y su card cambia; en mobile se reemplaza por «Works» + cards apiladas, sin efecto de scroll. Hay 4 imágenes de portfolio disponibles para las 4 cards.
- **Marquee del footer:** «Connect With Us · Let's Grow» con el círculo del logo encima; se detiene con reduced-motion.
- **Footer:** newsletter, Utility Page, Follow Us, Our Offices y barra legal.
- **Modal de video:** `<dialog>` nativo; el iframe de `youtube-nocookie` se crea recién al hacer click, para no cargar YouTube al abrir la página.

## Etapa 4 — Sections + `index.html` ⬜

- Las 11 secciones: Hero, What We Do, Services, Why Choose Us, Finance/Advisory/Growth/Strategy, Pricing, Testimonials, Team, FAQ, Blog y Footer; más **Stats** y **Logos** solo en mobile.
- **Un solo `<h1>`** («Expert Guidance for FutureGrowth»); los títulos de sección son `<h2>` con tamaño `--text-h1` (≈ 48 px, lo que mide el diseño).
- Precios anuales derivados del 30%: 27.9 / 34.9 / 41.9 (no inventados); el switch Monthly / Annually los intercambia.
- Cambio de layout desktop → mobile en `lg` (1024 px). El diseño no muestra tamaños intermedios: tablet se infiere de los dos extremos.
- `<head>` estándar de `seo.md` en la página (title, description, canonical, OG/Twitter, JSON-LD `Organization` y `WebSite`); `sitemap.xml` y `robots.txt`.
- Imágenes con `<picture>` WebP, `width`/`height` explícitos, `loading="lazy"` salvo la del hero.
- Sin animaciones de entrada (reveals): el diseño no las muestra. Se suman en una etapa aparte si se quieren.
- Verificación final: capturas por breakpoint contra los PNG, Lighthouse sobre archivos servidos (LCP < 2.5 s, CLS < 0.1, INP < 200 ms) y reporte de lo que no se pudo igualar.

## Supuestos pendientes de confirmar

- **Header:** fijo «por el momento» (variante `site-header--fixed`; pasa a fondo inverso con scroll, estado derivado de tokens porque el diseño no lo muestra); el círculo del chat es un adorno (confirmado); teléfono real +880 (123) 456 789 en header y off-canvas (confirmado); submenús de Home/Services/Blog con placeholder; ícono «Menu» = Lucide `layout-grid` (el del diseño tiene un cuadro girado). La Section reserva el espacio superior y define `scroll-padding-top`.
- **Carrusel:** card destacada fija (Process Optimization), según lo aprobado; en el diseño mobile la card oscura es la primera visible, lo que sugiere destacar el slide activo. Testimonios de Jonathan Walker, Sophia Martinez y Michael Brooks, y servicios Financial Planning y Brand Strategy, con placeholder; los tres videos usan el único entregado.
- **Modal de video:** no está en el diseño (fondo inverso, velo `--color-overlay`, fundido).
- **Scroll Top** aparece al pasar media pantalla (`SHOW_AFTER = 0.5` en `main.js`); el diseño no lo indica.
- **Estados** hover, active, disabled, switch encendido e input con error, derivados de los tokens existentes.
- **Alturas:** el botón mide 48 px (el diseño ~52 px) y la barra de progreso 3 px, por salir de la escala de espaciado.
- **Badge y play** con velo plano (sin `backdrop-filter`, que rompe `position: fixed` de descendientes).
- **Avatar stack** con avatares reales; las caras del demo son las de los testimonios, no las del PNG horneado (`h1-about-users.png`). Decidir en la Section si se usa el PNG tal cual.
- **Idioma del sitio:** inglés, siguiendo el copy del diseño.
- **Card Team:** el «+» se implementó como enlace al perfil (el diseño no dice qué hace); el amarillo de la card elevada es estático.
- **Card Pricing:** el último beneficio atenuado es solo énfasis visual; no se marcó como «no incluido» porque el diseño no lo aclara.
- **Radios:** las cards del diseño miden ~20px de esquina; se usa `--radius-lg` (24px) en cards y `--radius-md` (16px) en sus fotos.
- **Iconos de servicios, planes y FAQ:** Lucide equivalentes a los glifos del diseño, hasta tener los del cliente.

## Deuda y puntos abiertos

- `docs/personality.md` y `docs/interactions-catalog.md` se citan en otros docs pero no existen.
- Cada componente está documentado en el kit y en su `.stories.md`, generados desde `docs/tools/` (ver su README). Esos scripts son la fuente de los bloques `atoms:` / `molecules:` de `main.css`: editar a mano dentro de esos marcadores se pierde al regenerar.
- Git: rama `feat/design-to-web-esonix`; sin push todavía.
