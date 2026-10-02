# Plan — Etapa 4: Sections + `index.html`

Ensamblar la home de Esonix con los componentes de las Etapas 1–3 y compararla contra los PNG de `docs/design/` en cada breakpoint. Se entrega en grupos; cada uno se revisa antes del siguiente. Estado general y decisiones previas: `docs/plan.md`.

## Método

1. Antes de construir cada sección, recortar el PNG a resolución real (tramos de ~1000 px en desktop, ~1400 px en mobile). A escala reducida se leyeron mal tres organismos del Grupo C.
2. Revisar `dist/kit/index.html` para reutilizar componentes; no crear variantes sin caso de uso.
3. Valores desde tokens; contenedores desde el grid de Bootstrap.
4. Verificar a 1440 y 390 px: contraste AA, teclado, consola limpia, `prefers-reduced-motion`, y medir (`getBoundingClientRect`, `scrollWidth`) en vez de juzgar a ojo.
5. Auditar contra `docs/anti-patrones.md` antes de pasar al grupo siguiente.
6. Reportar al final lo que no se pudo igualar.

## Layout medido en el diseño (1920 px)

- **Contenedor de texto y grillas:** 1320 px (What We Do, Pricing, Team, FAQ, Footer).
- **Contenedor ancho:** 1620 px, el del header (Hero, carruseles, Blog, foto de Why Choose).
- **Cambio desktop → mobile:** en `lg` (1024 px). Tablet se infiere de los dos extremos.
- Un solo `<h1>` («FutureGrowth», con «Expert Guidance for» como parte del título); títulos de sección en `<h2>` con tamaño `--text-h1`.

## Secciones

| # | Sección | Desktop | Mobile |
|---|---|---|---|
| 1 | **Hero** | Foto de fondo; texto y «Get Started» claro a la izquierda; Card Hero a la derecha; filete; «Expert Guidance for —» + «FutureGrowth» gigante | Apilado |
| 2 | **What We Do** | Eyebrow y filete; a la izquierda 3M+ con avatares y foto con marco; a la derecha h2, texto, 3 barras de progreso, CTA y foto chica | Cambia el orden: h2, foto chica, barras y CTA; después 3M+ y la foto grande |
| 3 | **Services** | Encabezado en 3 columnas (h2, texto, flechas); carrusel de 3 cards que sangra | 1 card; flechas debajo del texto |
| 4 | **Why Choose Us** | h2 y texto; foto grande a la derecha hasta el borde de 1620; la franja de 3 Card Feature se monta sobre ella | Apilado |
| 5 | **Finance** (Word List) | Bloque redondeado a todo el ancho con foto desenfocada fija; 4 palabras y una Card Project | «Works» gigante y tenue sobre crema y cards apiladas |
| 6 | **Pricing** | Encabezado centrado, switch Monthly/Annually, 3 cards | Apilado |
| 7 | **Stats** (solo mobile) | — | Pastilla «4,000+ Clients Trust Our Expertise»; «Facts prove the outcome»; 3 Stat con indicador de 3 puntos |
| 8 | **Testimonials** | Fondo oscuro con foto y esquinas redondeadas arriba; encabezado centrado; carrusel con dots | 1 card |
| 9 | **Team** | Encabezado en 2 columnas; 3 cards; la del medio 20 px más alta arriba y abajo | Apilado |
| 10 | **Logos** (solo mobile) | — | Grilla de 2 columnas con borde: 7 logos y una celda «Join with Us ↗» |
| 11 | **FAQ** | Izquierda: h2 y Card CTA; derecha: acordeón | Apilado |
| 12 | **Blog** | Encabezado centrado; 3 Card Post; botón «View All Blog» | Apilado |
| 13 | **Footer** | Marquee, 4 columnas y barra legal | Utility Page y Follow Us en 2 columnas |

## Grupos

### Grupo 0 · Correcciones — hecho (`ec35449`)
Word List, Marquee, Footer y Progress corregidos contra el diseño a resolución real.

### Grupo A · Esqueleto, Hero y What We Do
**Estado: hecho (`6b1c63f`).** Hecho: `index.html` con `<head>` completo (canonical, OG con `og-image.jpg` 1200×630 generada desde el hero, Twitter, JSON-LD `Organization` + `WebSite`, preload de la fuente y de la foto del hero), header fijo, off-canvas, Scroll Top, footer provisorio; capa de layout (`.container` a 1320 de contenido, `.container-wide` a 1620, `--header-offset`, `scroll-padding`, `.section`, `.section-title`, `.photo-frame`); Hero y What We Do comparados contra los PNG a 1920 y 480 px (desvíos ≤ 16 px); `sections_kit.py` y fichas en el kit. Decisiones: CSS Grid en vez de `col-*` (excepción en `design-tokens.md`), Avatar Stack del kit en vez de `h1-about-users.png`, `<img>` WebP con dimensiones (no hay formato legacy para un `<picture>`). El patrón de encabezado de sección pasa al Grupo B, donde tiene su primer uso (Services).

- `dist/index.html` con el `<head>` estándar de `docs/seo.md`: title y description únicos, canonical, Open Graph, Twitter Card, JSON-LD `Organization` y `WebSite`, favicon, preload de Mona Sans.
- Header fijo con `scroll-padding-top`, Scroll Top, off-canvas, y scripts en orden (Lenis, GSAP, ScrollTrigger, Swiper, `main.js`).
- Sistema de layout: los dos contenedores, ritmo vertical entre secciones y un patrón de encabezado de sección (eyebrow, h2, texto y acciones; alineado o centrado).
- Secciones Hero y What We Do. En What We Do, el orden cambia en mobile sin duplicar contenido.
- Pendiente de decidir aquí: si el avatar stack usa los avatares del kit o el PNG `h1-about-users.png`.

### Grupo B · Services, Why Choose Us, Finance y Pricing
**Estado: hecho (`4609855`).** Hecho: las cuatro secciones en `index.html` (con Swiper sumado al `<head>` y a los scripts), comparadas contra los PNG a 1920 y 480 px y revisadas a 1440, 1280, 1024, 800 y 390 px (sin desborde horizontal); fichas en el kit desde `sections_kit.py`.
- **Section Head** (`.section-head`, `__main`, `__title`, `__text`, `__actions`): apilado; `--split` desde xl (Services) y `--center` (Pricing). Contenedores con `--container-width` / `--container-wide-width`.
- **Carousel:** activo centrado; `data-carousel-start` / `-start-wide` y `data-carousel-highlight`. Con menos de 6 slides, `main.js` duplica la tanda completa (copias con `aria-hidden` + `inert`): con 5 slides, Swiper dejaba un hueco a la derecha al avanzar. Reemplaza al truco `loopAdditionalSlides` + `loopFix`. Card Service con transición del destacado.
- **Why Choose Us:** grilla con `--why-container` / `--why-indent` (el texto se alinea con el `.container` en todos los anchos y la foto llega al borde del ancho) y `.feature-strip`. «Read More» de la card 02 se mantiene en mobile.
- **Finance:** foto fija como capa `position: fixed` recortada por `clip-path`, token nuevo `--blur-photo` (12px), radio `--radius-xl`.
- **Pricing:** `initPricingSwitch` en `main.js` con anuncio `role="status"` solo al cambiar; tres columnas desde xl.
- **Correcciones a niveles anteriores** (medidas en los PNG): Eyebrow a 16px (`--text-body`, antes 14px); Card Service con el texto sangrado bajo el título e ícono de 40px.

Plan original:
- Carrusel de Services que destaca el **slide activo** (reemplaza la card destacada fija del Grupo B de la Etapa 3).
- Franja de 3 Card Feature sobre la foto de Why Choose, con el contenedor blanco que las une.
- Bloque Finance con foto desenfocada **fija** y el Word List.
- Switch Monthly/Annually con precios anuales derivados del 30 %: 27.9 / 34.9 / 41.9.

### Grupo C · Stats, Testimonials, Team, Logos, FAQ, Blog y Footer
**Estado: en revisión.** Hecho: las siete secciones (footer con marcador `section:footer`, fuera de `<main>`), comparadas contra los PNG a 1920 y 480 px y revisadas a 1280, 1024, 768 y 390 px; 13 fichas de Sections en el kit.
- **Stats** y **Logos**: solo mobile (`display: none` desde lg). Indicador de 3 cuadritos (`.stats__level`) y `.logo-grid` (filetes = fondo de la grilla + gap de 1px) viven en el bloque de Sections.
- **Testimonials:** `data-surface="inverse"`, foto con `--blur-photo` + velo inverso al 85%, radio en las 4 esquinas en mobile y solo arriba desde lg (así los PNG); orden del diseño (Isabella tercera, `data-carousel-start="2"`), también en el kit.
- **Team:** `.section-head--split` sin acciones (columnas explícitas; las acciones crean una 3.ª columna implícita); la grilla reserva con padding los 20px de la card elevada.
- **FAQ:** columnas 33rem | 45rem; la Card CTA baja al final de la columna. **Blog:** 3 columnas desde lg, `&nbsp;` en «&amp; Expert». **Footer:** `.page-footer` con Marquee (sin `data-surface` propio) y foto desenfocada.
- **Correcciones a niveles anteriores:** Accordion Item (pregunta semibold 24px desde lg / 18px mobile, separación `--accordion-gap`); Newsletter con `align-content: start` (el campo se separaba del título en la fila del footer); Section Head `--center` sin margen propio (Pricing lo ajusta en `.pricing .section-head`).
- **Desvíos que quedan:** acordeón ~50px más corto que la Card CTA a 1920; cifras de Stats a 36px (diseño ≈ 42); logos de partners en negro (el diseño los muestra en gris).

Plan original:
- Stats y Logos solo en mobile (`display: none` desde `lg`, sin duplicar contenido).
- Testimonials sobre fondo oscuro con foto y esquinas superiores redondeadas.
- Card Team elevada: reservar el espacio de su elevación con margen negativo desde `lg`.
- Footer completo con el Marquee encima.

### Grupo D · Cierre
- `sitemap.xml` y `robots.txt`; `/kit` queda con `noindex` y fuera del sitemap.
- Imágenes con `<picture>` WebP, `width`/`height` explícitos y `loading="lazy"`, salvo la del hero (`eager` + `fetchpriority="high"`).
- Lighthouse sobre archivos servidos: LCP < 2.5 s, CLS < 0.1, INP < 200 ms.
- Comparación contra los PNG en desktop y mobile, auditoría de accesibilidad (axe, teclado, un pase con lector de pantalla) y reporte de lo que no se pudo igualar.

## Kit · nivel Sections

`index.html` es la única fuente. Un `docs/tools/sections_kit.py` extrae cada sección (entre marcadores `<!-- section:id -->`) para armar su ficha en el kit y su `.stories.md`, de modo que ambos no se desfasen. Se agrega al README de `docs/tools`.

## Decisiones del equipo

| # | Tema | Decisión |
|---|---|---|
| 1 | Dominio | Placeholder `https://esonix.example` para `canonical`, Open Graph y JSON-LD; reemplazar al pasar a producción |
| 2 | Fondo de Finance | Foto desenfocada fija; no cambia con la card activa |
| 3 | «Works» en mobile | Gigante y tenue, decorativo (`aria-hidden`), con `<h2>` real oculto para lectores |
| 4 | Logos mobile | Las 4 imágenes de partners se repiten para completar las 7 celdas |
| 5 | «30+» de Stats | Etiqueta placeholder «Years of Consulting Experience» (el diseño no la trae) |
| 6 | Carrusel de Services | Se destaca el slide activo |

## Supuestos a confirmar durante la etapa

- Fondos reales de Hero, Finance, Testimonials y Footer: el diseño los muestra desenfocados y con velo; se toman de `h1-hero-img`, `h1-feature-bg-image`/portfolio, `h1-testimonial-bg-img` y `h1-footer-bg`.
- Títulos, descriptions y textos de las secciones que el diseño no muestra completos son placeholder.
- Tablet (entre 768 y 1023 px): el diseño no lo muestra; se infiere de desktop y mobile.
- Animaciones de entrada (reveals): el diseño no las muestra; fuera de alcance salvo que se pidan.

## Riesgos conocidos

- **Lenis + ScrollTrigger:** sincronizados en `main.js`; el Word List no usa `pin` para evitarlos.
- **Desbordes por contenido ancho:** el texto del Marquee estiró un ancestro grid del kit; se resolvió con `contain: inline-size`. Al ensamblar la página, medir `scrollWidth` a 390 y 1440 px.
- **`backdrop-filter`:** rompe `position: fixed` en descendientes; no se usa en header ni badges.
- **Card blanca sobre superficie inversa:** el título se pierde si una regla de foundations pisa el color; ya hay una excepción en `.card-project`; revisar cualquier card nueva sobre fondo oscuro.
