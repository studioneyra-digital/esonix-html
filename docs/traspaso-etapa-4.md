# Traspaso — Etapa 4, para retomar en otra sesión

> **Actualización:** el Grupo A se commiteó (`6b1c63f`) y el Grupo B está **construido y en revisión, sin commit** (estado y decisiones en `docs/plan-etapa-4.md`, Grupo B). Lo que sigue describe el punto de partida del B y queda como referencia del análisis; borrar este archivo al commitear el Grupo B.

Documento temporal: describe dónde quedó el trabajo el 2026-10-02 y cómo seguir. Se puede borrar al cerrar el Grupo B. El plan completo de la etapa está en `docs/plan-etapa-4.md`; el estado general, en `docs/plan.md`.

## 1. Estado del repo

- Rama `feat/design-to-web-esonix`, sin push. Último commit: `ec35449` (Grupo 0 de la Etapa 4). Antes: `8e00212` (Etapa 3, grupo C).
- **El Grupo A está construido y revisado visualmente, pero sin commitear.** El usuario no pidió el commit todavía (dijo «continuar con grupo B» tras verlo). Primer paso de la sesión nueva: confirmar con el usuario y commitear el Grupo A **antes** de tocar nada del B, porque ambos editan `main.css` e `index.html`.
- **Del Grupo B no hay ni una línea de código.** El árbol de trabajo es exactamente el Grupo A (verificado archivo por archivo). Solo se hizo análisis del diseño, que está en la sección 4.
- Archivos sin commitear (todos del Grupo A): `dist/index.html`, `dist/assets/img/og-image.jpg`, `dist/assets/css/main.css` (bloque `sections:`), `dist/assets/css/kit.css`, `dist/kit/index.html`, `docs/tools/sections_kit.py`, `docs/tools/organisms_kit.py`, `docs/tools/README.md`, `docs/kit/{hero,what-we-do}.stories.md`, `docs/kit/{site-footer,video-modal}.stories.md`, `docs/design-tokens.md`, `docs/plan.md`, `docs/plan-etapa-4.md` y este archivo. Mensaje sugerido: `feat(design-to-web): esqueleto de index.html, Hero y What We Do (etapa 4, grupo A)`.
- Ignorar en `git status` las carpetas de otros proyectos del workspace (`nova-exploration`, `studioneyra-skills-working`, etc.): no son de este trabajo. Usar `git add` con rutas explícitas y nunca `git add -A`.

## 2. Qué incluye el Grupo A (hecho)

- `dist/index.html` con `<head>` completo de `docs/seo.md`: title y description únicos, canonical y Open Graph sobre `https://esonix.example`, Twitter Card, JSON-LD `Organization` + `WebSite`, preload de la fuente y de la foto del hero. `og-image.jpg` (1200×630) generada desde el hero.
- Header fijo con su off-canvas, Scroll Top, skip link, footer provisorio (se completa en el Grupo C) y scripts en orden: Lenis, GSAP, ScrollTrigger, `main.js`. **Falta sumar Swiper** (CSS y JS) para el carrusel de Services.
- Capa de layout en el bloque `/* sections:start … sections:end */` de `main.css` (escrito a mano; ningún generador lo toca): `--header-offset: 7rem` con `scroll-padding`, `.container` ampliado a 1320 px de contenido desde `xxl`, `.container-wide` de 1620 px, ambos con gutter `--spacing-7`; `.section` (64 px en mobile, 96 px desde `lg`), `.section-title`, `.photo-frame`.
- Secciones **Hero** y **What We Do**, comparadas contra los PNG a 1920 y 480 px (desvíos ≤ 16 px). What We Do reordena en mobile con una grilla de áreas, sin duplicar contenido.
- `docs/tools/sections_kit.py`: **`dist/index.html` es la única fuente**. Cada sección va entre `<!-- section:id -->` y `<!-- /section:id -->`; el script la extrae al kit, cambia las rutas a `../assets/`, agrega el sufijo `-section` a sus ids y arma la ficha y el `.stories.md` desde la lista `S`. Idempotente.
- Decisiones del Grupo A: CSS Grid con los breakpoints del theme en vez de `col-*` (excepción escrita en `design-tokens.md`); Avatar Stack del kit en vez del PNG `h1-about-users.png`; «Get Started» del hero lleva a What We Do y el de What We Do, al footer.
- Correcciones de paso: ids duplicados del kit (`video-modal`, `site-footer`), `Progress` con `--progress` y modificador de kit `--stack`.

## 3. Decisiones del usuario para toda la Etapa 4

Dominio placeholder `https://esonix.example` · fondo de Finance: foto desenfocada **fija** · «Works» en mobile decorativo con `<h2>` real oculto · logos mobile: repetir las 4 imágenes hasta 7 celdas · «30+» de Stats: «Years of Consulting Experience» · carrusel de Services: se destaca el **slide activo** · el kit de Sections se genera desde `index.html`. Los commits se piden de forma explícita, un grupo por commit.

## 4. Grupo B: análisis hecho, por implementar

Alcance: **Services, Why Choose Us, Finance, Pricing.** Los números salen de recortes del diseño a 1920 px y son aproximados (±5 px): confirmarlos con la superposición de la sección 6.

### 4.1 Base del carrusel (tocar primero)

En el diseño desktop el slide activo está **centrado** y es el oscuro: `[parcial izq: Brand Strategy] [Marketing] [Process Optimization, activo] [Sales] [parcial der: Financial]`. Con 5 slides y slide inicial 1 coincide. Hoy el carrusel no centra (activo = primer visible).
- `main.js › initCarousel`: agregar `centeredSlides: true`; leer `data-carousel-start` (por defecto 0) y `data-carousel-start-wide` (cuando el viewport del carrusel mide ≥ 64 rem, o sea 3 por vista); probar si se puede quitar el hack `loopAdditionalSlides: 1` + `loopFix({direction:'prev'})` (con centrado deberían aparecer los vecinos desde la carga).
- Atributo nuevo `data-carousel-highlight`: la card del slide activo recibe `data-surface="brand"` y las demás lo pierden. Comparar `data-swiper-slide-index` con `swiper.realIndex` para cubrir los duplicados del loop; sincronizar en `realIndexChange` y al iniciar.
- Slide inicial: Services `start=0`, `start-wide=1` (mobile abre en Marketing Guidance, como el diseño; desktop, en Process Optimization). Testimonials: `start=2` en ambos anchos (el diseño muestra el tercer dot activo).
- Molécula Card Service (`docs/tools/molecules_css.py`): agregar `transition` (`background-color`, `color`, `box-shadow` con `--ease-base`) a `.card-service`, y de `color` a `.card-service__title` y `.card-service__icon`, para que el cambio de destacado sea suave. El markup inicial lleva `data-surface="brand"` en Process Optimization (es el estado sin JS).
- **A verificar en el navegador** (no está comprobado): que `initialSlide` en loop use el índice real; si `swiper.slides` incluye o no los duplicados (afecta cuántos dots crea el código actual); cómo se ve a 2 por vista centrado (tablet, entre 48 y 64 rem).
- Actualizar la ficha del carrusel en `docs/tools/organisms_kit.py` (descripción, atributos, decisiones: el activo ahora es el centrado; la card destacada fija queda reemplazada) y regenerar con `organisms_css.py` y `organisms_kit.py`.

### 4.2 CSS de las Sections (bloque `sections:` de `main.css`)

- Reemplazar los números repetidos por custom properties: `--container-width: 82.5rem` y `--container-wide-width: 101.25rem`.
- **`.section-head`**: `__main` (eyebrow + h2, separación de ~12 px), `__text` (máx. 25 rem) y `__actions`. Variante `--split` desde `lg` (Services): `grid-template-columns: minmax(0, 36rem) minmax(0, 25rem) auto; justify-content: space-between` (medido a 1920: h2 570 px, texto 396 px, flechas 112 px). El texto y las flechas se alinean con la primera línea del h2, no con el eyebrow: compensar su alto. Variante `--center` (Pricing). Mobile: eyebrow, h2, texto y flechas apilados. El título del head necesita `max-inline-size` ≈ 36–38 rem para cortar donde el diseño («Innovative Solutions for / Business Success»).
- **Services**: sección con `overflow-x: clip` para recortar los slides que sangran; el head dentro de `.container` y el carrusel dentro de `.container-wide` (3 slides de ~524 px con 24 px de separación a 1920). Flechas = Icon Button por defecto (48 px; el diseño ~50). Hueco entre el head y las cards ≈ 64 px.
- **Why Choose Us**: el texto arranca en el borde izquierdo del contenedor de 1320 y la foto llega al borde derecho del de 1620. Solución sin `cqi` ni `vw`: dentro de `.container-wide`, una grilla `grid-template-columns: var(--why-indent) minmax(0, 54fr) minmax(0, 46fr) var(--why-indent)` con `--why-indent: calc((100% - min(100%, var(--container-width))) / 2)` (los porcentajes de `grid-template-columns` se resuelven contra el ancho de la propia grilla). Texto: columna 2, fila 1, con ~85 px arriba. Foto: columnas 3–4, filas 1–2, `aspect-ratio: 1125 / 1095` (≈ 750×730 a 1920). Strip de cards: `grid-column: 2 / 4`, fila 2, `align-self: end`, `position: relative; z-index: 1`, a ras del borde inferior de la foto.
  - **Strip** (`.feature-strip`): contenedor blanco de 1320×321 con 3 Card Feature de 440 px, radio `--radius-lg`, borde `--color-border-subtle` y sombra suave. Las cards normales van sin fondo ni sombra dentro del strip; la del medio es la destacada con foto (`h1-feature-bg-image.webp`). Mobile: apilado, el strip se monta ~91 px sobre la foto (probar `calc(-1 * var(--spacing-11))` y ajustar).
  - El diseño mobile omite el «Read More» de la card 02. **Propuesta: mantenerlo** (es contenido funcional; es una omisión del export, como los otros que no se replican). Informarlo en el reporte final.
- **Finance**: desde `lg`, bloque a todo el ancho con `border-radius` grande (medir; probablemente `--radius-xl`, 40 px), alto ≈ 945 px (≈ `59rem` como `min-block-size`, con el contenido centrado en vertical), foto fija `h1-portfolio-img-3.webp` desenfocada y con velo oscuro. El desenfoque es un `filter` sobre la capa de imagen (nunca `backdrop-filter`): probablemente haga falta un token `--blur-photo` (~12 px) junto a `--blur-text`. La Card Project queda a la derecha con **524 px** de ancho y 20 px de margen derecho (el Word List ocupa columnas de 612 px: hay que acotar `.word-list__media` dentro de la sección). Bajo `lg` no hay bloque: «Works» tenue y cards apiladas sobre el crema, que ya resuelve el organismo. El Word List trae `<h2 class="visually-hidden">Works</h2>`: ponerle `id` y usarlo en `aria-labelledby`. Sobre el diseño: el bloque mide 1905 px de ancho en el PNG (artefacto del export); tratarlo como 100 %.
- **Pricing**: head centrado; switch con `Monthly` (aria-hidden), el `<input class="switch" role="switch">` y `Annually Save 30%` como su `<label>` (texto de 24 px = `--text-h4`, separación de 20 px). Cards en 3 columnas con 24 px (424 px cada una) y en 1 columna con ~48 px en mobile. Hueco: h2 → switch ≈ 40 px, switch → cards ≈ 60–64 px.

### 4.3 JS de Pricing (`main.js`, bloque nuevo)

`initPricingSwitch`: al cambiar el switch, cada `[data-price-monthly][data-price-annual]` muestra el valor que corresponde (`39.9→27.9`, `49.9→34.9`, `59.9→41.9`, con «$»; «/ Month» no cambia). Un `<p class="visually-hidden" role="status">` anuncia «Showing annual prices, 30% off.» **solo al cambiar**, no al cargar. Sin JS los precios quedan mensuales.

### 4.4 Markup y fichas

- `index.html`: sumar `swiper-bundle.min.css` en el `<head>` y `swiper-bundle.min.js` antes de `main.js`; agregar las 4 secciones entre marcadores `section:services`, `section:why-choose-us`, `section:finance`, `section:pricing`.
- Contenidos listos para reutilizar: servicios (`SERVICES` en `organisms_kit.py`; íconos `target`, `trending-up`, `chart-pie`, `gem`, `lightbulb`), cards de pricing (kit de Card Pricing, con las clases `btn--accent` y `data-surface="brand"` en Enterprise), Card Feature y Word List (`WORDS` en `organisms_kit.py`).
- `sections_kit.py`: sumar los 4 `dict` a `S` (ids `services`, `why-choose-us`, `finance`, `pricing`, sin colisión con los ids actuales del kit). Regenerar kit y `.stories.md`, y actualizar `plan.md` y `plan-etapa-4.md`.

## 5. Preguntas abiertas para el usuario

1. ¿Commitear el Grupo A ahora (un commit) antes de seguir?
2. «Read More» de la card 02 en mobile: mantenerlo (propuesta) o replicar la omisión del diseño.
3. Radio y desenfoque exactos del bloque Finance: se confirman al compararlos con el PNG.

## 6. Cómo trabajar y verificar

- **Modelo:** la tabla de `CLAUDE.md` §9 recomienda Opus con esfuerzo alto para esta etapa.
- **Antes de construir una sección, recortar el PNG a resolución real** (leerlo entero escalado confundió texto desenfocado con texto en contorno y un logo con un ícono). Receta en la memoria `playwright-cli-qa-recipes`: servir `docs/design/` por http, `page.goto` primero y luego `setContent` con el `<img>`, y `page.screenshot({ fullPage, clip })` en tramos de ~1000 px (desktop, ancho 1920) o ~1400 px (mobile, ancho 480). Los recortes de esta sesión están en el scratchpad temporal (`.../scratchpad/crops/`, 23 archivos) y pueden haberse borrado: regenerarlos es barato.
- **Medir tipografía:** renderizar el texto en Mona Sans a 100 px, medir su ancho y despejar el tamaño a partir del ancho medido en el PNG (más fiable que estimar alturas).
- **Verificación por superposición (planeada, aún no probada):** con el servidor de la raíz del proyecto, cargar `dist/index.html` a 1920 px y superponer el PNG del diseño con `mix-blend-mode: difference`, desplazado hasta alinear un ancla (p. ej. el eyebrow de la sección); lo alineado queda negro y las diferencias se ven de inmediato. Complementar con `getBoundingClientRect`, `scrollWidth` a 1920/1440/480/390 px, consola limpia, teclado, `prefers-reduced-motion` y el comportamiento del carrusel (siguiente, anterior, dots, loop, resaltado) y del switch de precios.
- **Servidor local:** subclase de `ThreadingHTTPServer` con `Cache-Control: no-store` (12 líneas; ver la memoria). El de un solo hilo rechaza conexiones y el navegador cachea el CSS. En Windows, `pkill` no detiene un `python.exe`: usar PowerShell (`Get-NetTCPConnection` + `Stop-Process`). Ante cualquier desborde, **medir antes de culpar a la caché**.
- Cerrar al terminar la sesión de `playwright-cli` y el servidor; el scratchpad de esta sesión guarda una copia del estado del Grupo A (`groupA-snapshot/`) que ya no hace falta si el Grupo A se commitea primero.

## 7. Trampas ya encontradas

- La regla de foundations que pone todo `h1`–`h6` en blanco dentro de `data-surface` pisa el título de una card blanca anidada en una superficie oscura (ya corregido en `.card-project`). Revisar cualquier card blanca nueva sobre fondo oscuro.
- Texto repetido de gran tamaño en un track `max-content` estira cualquier ancestro grid/flex (se resolvió con `contain: inline-size` en `.marquee`).
- `backdrop-filter` rompe `position: fixed` en descendientes: no usarlo en bloques que contengan elementos fijos.
- Los generadores `atoms_*`, `molecules_*` y `organisms_*` **reescriben** sus bloques de `main.css`: el CSS de Sections va a mano, fuera de esos marcadores. El CSS de moléculas se edita en `molecules_css.py`, no en `main.css`.
