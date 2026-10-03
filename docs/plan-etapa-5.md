# Plan — Etapa 5: páginas interiores

Siete páginas nuevas construidas desde los PNG de `docs/design/`, **una página por entrega**, cada una revisada antes de la siguiente. Orden: About Us → Services → Service Details → Portfolios → Case Study → Testimonials → Contact. Estado general y decisiones previas: `docs/plan.md`. Método de trabajo: el mismo de `plan-etapa-4.md` (recortar el PNG a resolución real antes de construir, reutilizar el kit, valores desde tokens, verificar a 1440 y 390 px midiendo, auditar contra `anti-patrones.md`, reportar desvíos).

## Arquitectura compartida (se construye con About Us)

### Piezas comunes sincronizadas por script
- `dist/index.html` es la fuente del header, el off-canvas, el footer y el Scroll Top. Van entre marcadores `<!-- shared:header -->` / `<!-- /shared:header -->` y `<!-- shared:footer -->` / `<!-- /shared:footer -->` (el off-canvas y el Scroll Top quedan dentro de uno de los dos bloques, según dónde estén hoy en el HTML).
- `docs/tools/sync_shared.py` copia esos bloques a cada página de `dist/*.html` y marca el enlace de la página actual con `aria-current="page"` en el header y el off-canvas. **Correrlo después de cualquier cambio en esas piezas de `index.html`.**
- Cada página sigue siendo HTML completo y editable: sin build, sin includes por JS.

### Kit de Sections con varias páginas
- `sections_kit.py` pasa a leer los marcadores `<!-- section:id -->` de todas las páginas de `dist/`. Cada `id` tiene **una sola fuente**: la página donde se define. Una Section reutilizada en otra página con un modificador no genera ficha nueva; la ficha existente documenta el modificador.
- La ficha indica de qué página sale («Fuente: `dist/about-us.html`»).

### `<head>` y SEO de cada página
- Plantilla «Page head» del kit: `title`, `description`, canonical sobre `https://esonix.example/<archivo>.html`, OG y Twitter, JSON-LD de la página (`AboutPage`, `ContactPage`, `Service`, etc.) con `BreadcrumbList`.
- Cada página se suma a `dist/sitemap.xml`. Los enlaces del menú que hoy son placeholder (`#`) pasan a la página real a medida que existe.

## About Us (`dist/about-us.html`)

Referencias: `docs/design/About-Us-Desktop.png` (1920×5937) y `About-Us-Mobile.png` (480×8530). Ninguno muestra el footer: se usa el de la Home.

### Secciones

| # | Section | Desktop | Mobile | Origen |
|---|---|---|---|---|
| 1 | `page-hero` | Foto `about-page-header-bg.webp` a sangre con velo; breadcrumb en píldora translúcida «Home - About Us»; `h1` blanco abajo a la izquierda | Igual, más bajo | **Nueva**, reutilizable en las 7 páginas |
| 2 | `stats` + `stats--strip` | Franja: título «Facts prove the outcome» a la izquierda, 3 Stat con indicador de puntos separadas por filetes verticales, filete inferior | Título centrado arriba, Stats apiladas con filetes | **Existe** (Home, solo mobile); el modificador quita la píldora y la muestra en todos los breakpoints |
| 3 | `about-intro` | Izquierda: eyebrow «What We Do», `h2` de 3 líneas, lista de 3 ítems con `icon--circle-check`, botón «More about us ↗». Derecha: `photo-frame` con `h3-about-img.webp`, `h3` «Who we are», 2 párrafos, filete, cita con comillas y firma `signature-2.png` | Apilado en el mismo orden | **Nueva** |
| 4 | `team-profiles` | Eyebrow y `h2` centrados; 3 `card-team--profile`, la del medio con `--reverse` (texto arriba, foto abajo) | Apiladas, todas con la foto arriba | **Nueva** (Section) + variante de Card Team |
| 5 | `feedback` | Bloque oscuro con `about-video-bg.webp`, esquinas inferiores redondeadas; eyebrow ámbar, `h2` centrado, `quote-slider` con 3 citas y Dots | Esquinas superiores redondeadas | **Nueva** + organismo nuevo |
| 6 | `why-trust` | Izquierda: eyebrow, `h2`, 2 barras de Progress (Consulting 88% ámbar, Marketing 75% petróleo), Link Arrow «Contact With Us ↗». Derecha: `quote-form` que sube sobre `feedback` | Primero el formulario (solapado con `feedback`), después el bloque de texto | **Nueva** + molécula nueva |
| 7 | `logos` + `logos--desktop` | Grilla 4×2 con borde: 7 logos y «Join with Us ↗» | 2×4 | **Existe** (Home, solo mobile); el modificador la muestra también en desktop |
| 8 | `faq` + `faq--centered` | Eyebrow y `h2` centrados; acordeón a la izquierda; Card CTA con `h2-cta-img.webp` a la derecha | CTA debajo del acordeón | **Existe**; el modificador cambia el encabezado |

Contenido: copy del PNG. El mobile repite «12K+»: es un error de captura, se usan las 3 stats del desktop. Las otras dos citas del slider salen del carrusel de la Home (David Thompson va primero, como en el diseño). El equipo usa `h1-team-member-img-1..3.webp`.

### Componentes nuevos

**Textarea (átomo).** La clase `.input` sobre `<textarea>`, con `resize: vertical`. Hereda filete, hover, `aria-invalid` y superficies oscuras. Se agrega en `atoms_css.py` (el bloque `atoms:` de `main.css` no se edita a mano).

**Label flotante (átomo Input, variante `field`).** Envoltura `.field` con `<label>` real y el campo. En reposo el label ocupa el lugar del placeholder (igual al diseño); con foco o con contenido sube y se achica sobre el filete. CSS puro: `:focus-within` y `:not(:placeholder-shown)` (el campo lleva `placeholder=" "` para habilitar el selector). Cumple «inputs con `<label>` asociado, no solo placeholder» de `accessibility.md`.

**Card Team `--profile` (molécula).** Card blanca: foto arriba, `h3` con el nombre, cargo, 4 redes con Icon Button y `aria-label` («Olivia Bennet on LinkedIn»). `--reverse` invierte el orden solo desde `lg`. Las cards de la Home no cambian.

**Quote Form (molécula `quote-form`).**
- Funciona sin JS: `<form action="https://formsubmit.co/studioneyra@gmail.com" method="post">` (FormSubmit redirige a su página de agradecimiento). Con JS, `main.js` intercepta el envío y hace `fetch` a la variante `/ajax/` de esa misma URL (derivada del `action`, así cambiar de servicio es editar el HTML).
- Campos obligatorios: nombre (`autocomplete="name"`), email (`type="email"`), teléfono (`type="tel"`), mensaje (textarea). Campos ocultos: `_honey` (trampa antibots) y `_subject`.
- Estados:
  - **Validación**: `novalidate` + Constraint Validation API; cada campo inválido recibe `aria-invalid="true"` y un mensaje enlazado con `aria-describedby`; el foco va al primer error; el error se limpia al corregir.
  - **Enviando**: botón deshabilitado con `aria-busy="true"` y texto «Sending…».
  - **Enviado**: mensaje en `role="status"` y formulario limpio.
  - **Error de red o del servicio**: mensaje en `role="alert"`, datos conservados, se puede reintentar.
- Copy de mensajes en inglés (el sitio es en inglés).
- Aviso operativo: el primer envío real dispara un correo de activación de FormSubmit a studioneyra@gmail.com; hasta confirmarlo no llega nada.

**Quote Slider (organismo `quote-slider`).** Swiper con efecto `fade`, cargado con `requireLib('swiper')` cuando se acerca. 3 slides `<figure>` con `<blockquote>` y `<figcaption>`; navegación con el átomo Dots; swipe y teclado. **Sin autoplay** (el diseño no lo pide y así no hace falta control de pausa, WCAG 2.2.2). Comillas ámbar decorativas (`aria-hidden`).

### Solapamiento formulario / feedback
`quote-form` vive dentro de `why-trust`. En desktop un margen negativo lo sube sobre `feedback`, que reserva ese alto en su padding inferior. En mobile el formulario va primero en la grilla de `why-trust` y conserva el solapamiento.

### Kit y documentación
- Fichas nuevas: Textarea y Field (átomos), Card Team `--profile` (molécula), Quote Form (molécula, con los cuatro estados renderizados), Quote Slider (organismo), Sections `page-hero`, `about-intro`, `team-profiles`, `feedback`, `why-trust`; modificadores documentados en `stats` (`--strip`), `logos` (`--desktop`) y `faq` (`--centered`).
- `.stories.md` de cada una.

### Verificación
- Comparar contra los PNG a 1920 y 480 px; revisar a 1440, 1280, 1024, 768 y 390 px sin desborde horizontal.
- Formulario: recorrido solo con teclado; los cuatro estados (el de red, simulando la falla con el endpoint bloqueado en Playwright); sin enviar correos reales durante el QA.
- axe sin violaciones, consola limpia, `prefers-reduced-motion`.
- Header y footer de `about-us.html` idénticos a los de `index.html` tras `sync_shared.py` (salvo `aria-current`).

### Orden de construcción
1. Infraestructura: marcadores `shared:` en `index.html`, `sync_shared.py`, `sections_kit.py` multipágina. Commit propio.
2. Átomos y moléculas: Textarea, Field, Card Team `--profile`, Quote Form (con su JS).
3. Organismo Quote Slider.
4. `about-us.html` con sus Sections, modificadores de `stats` / `logos` / `faq`, `<head>`, sitemap y enlace del menú.
5. Kit, `.stories.md`, QA y reporte de desvíos. Commit de la página.

Plan de implementación detallado: `docs/plan-etapa-5-about-us.md`.

### Estado: hecha y aprobada
Infraestructura commiteada (`1b517dd`); la página, en `52ab257`.

**Cambios respecto de esta spec** (decididos al planificar o al construir):
- El slider de citas es la variante `carousel--fade` del Carousel (no un organismo nuevo).
- Variantes que el PNG mostraba y la spec no listaba: `card-cta--stacked`, `accordion--boxed`, `progress--accent` e ícono `circle-check-outline` (el `circle-check` del theme es relleno).
- **Header de páginas interiores** (decisión del usuario al construir): `site-header--inner`, con el logo alineado al `.container`, la píldora del menú oscura y el botón «Schedule a call ↗». `sync_shared.py` lo aplica desde el marcador (`<!-- shared:header site-header--inner -->`); el botón lleva al footer (contacto) hasta que exista la página Contact.
- `.section-bg`: el fondo desenfocado de Testimonials pasa a un patrón compartido con Feedback (sin cambio visual en la Home).
- El título del formulario es `<h2>` en la página (va antes que el h2 de su sección).

**Desvíos frente al diseño:**
- `h1` del Page Hero con `--text-h1` (48/36px) contra ≈ 62/41px (decisión del usuario).
- Stats `--strip`: centros de las cifras en 751 / 1099 / 1447 px contra 767 / 1147 / 1527 del diseño (el diseño excede el contenedor de 1320 por la derecha).
- Quote Form de 571px contra 585, con los campos a 83px (diseño: 75): el label flotante reserva su lugar arriba.
- Feedback: 797px de alto contra ≈ 822.
- Párrafos de «Who we are» con ~85 caracteres por línea (anti-patrones #13, excepción declarada: así lo muestra el diseño).

**Verificado:** 1920, 1440, 1280, 1024, 768, 480 y 390px sin desborde; axe sin violaciones en la página (1440 y 390); consola limpia; teclado (orden lógico, foco visible, el honeypot fuera del Tab); los cuatro estados del formulario con la red interceptada (nunca se envió a FormSubmit); `prefers-reduced-motion`; `sync_shared.py --check` y sus 6 pruebas; Home sin regresiones (Testimonials con `.section-bg` idéntico).

**Pendiente del usuario / observaciones:**
- El primer envío real del formulario dispara el correo de activación de FormSubmit a studioneyra@gmail.com.
- El Hero de la Home no lleva `data-surface="inverse"`: su anillo de foco por defecto es oscuro sobre la foto (el Page Hero ya lo corrige). Fuera del alcance de esta página.
- axe marca en el kit las citas ocultas (opacidad 0) del carrusel con fundido: falso positivo, en la página no aparece. En la Home quedan los avisos ya conocidos de textos decorativos («01/03» de Card Feature y la marca de agua «Works»).

## Service Details (`dist/service-details.html`)

Referencias: `docs/design/Service-Details-Desktop.png` (1920×3091) y `Service-Details-Mobile.png` (480×4552). Ninguno muestra el footer: se usa el de la Home. Se construye antes que Services (el listado), que todavía no tiene PNG. El archivo conserva el nombre del enlace del menú («Service Details») y funciona como plantilla de servicio: el contenido es el de **Business Optimization**, el servicio activo del diseño.

El mobile tiene un error de captura (el ítem 1 del FAQ aparece dos veces, cerca de y≈2680): se ignora.

### Secciones

| # | Section | Desktop | Mobile | Origen |
|---|---|---|---|---|
| 1 | Header | Logo al `.container`, píldora oscura, «Schedule a call ↗» | Logo + «Menu» | **Existe**: `site-header--inner` |
| 2 | `page-hero` | Foto a sangre con velo; breadcrumb «Home - Services - Business Optimization»; `h1` «Business Optimization» | Igual, más bajo | **Existe** (fuente `about-us.html`): cambian foto, breadcrumb y `h1` |
| 3 | `service-details` | Artículo (870) y aside (420) con 30 px de separación: proporción `29fr 14fr`, gap `--spacing-7`, desde `lg` | Apilado: artículo → Divider → aside | **Nueva** |

**Artículo**, en orden:
1. `h2` «Explore our Service Lists» y un párrafo.
2. `photo-frame` con la foto del apretón de manos (420×262) junto a un `h3` «Mistakes to avoid to the dummy» y un Check List de 4 ítems. En mobile, apilados.
3. `h3` «Document Required» y una grilla 2×2 (1 columna en mobile): ícono `badge-check` ámbar, `h4` con el título del documento y descripción. Es propia de la Section (`service-details__docs`): no hay un segundo caso de uso que justifique un componente.
4. `h3` «Key Features» y un Check List de 4 ítems.
5. Video: `photo-frame` (870×400) con un Icon Button `--glass --lg` centrado que abre el Video Modal existente (`data-video-id="RqueNBILfVU"`).
6. Párrafo.
7. FAQ con `accordion--framed`, 4 ítems numerados, el primero abierto.

**Aside** (`<aside aria-label="Service sidebar">`): Service Nav («Exclusive Services») y Quote Form `--outline` («Get a Quote»), separados por `--spacing-7`. No es sticky: el diseño no lo muestra y el aside es más alto que el viewport.

### Contenido
- Copy del PNG, literal, incluido el relleno de la plantilla («Mistakes to avoid to the dummy», los documentos de licencia de conducir, los párrafos que terminan en «..»). Se corrige «residen- tial» → «residential».
- Fotos (decisión del usuario: sustitutas de la biblioteca, se cambian editando el `src`): hero `h1-process-img-2.webp` (1000 px de ancho: a 1920 se ve algo blanda bajo el velo), apretón de manos `h1-process-img-3.webp`, video `download.webp`.
- FAQ (decisión del usuario: adaptar de la Home):
  1. «What industries do you specialize in ?» → respuesta de la Home sobre industrias.
  2. «How long does a consulting project typically last ?» → texto del PNG (habla de duración, por eso va acá).
  3. «What does a business consultant do ?» → adaptada de «What services do business consultants provide?» de la Home.
  4. «Will consulting disrupt my daily operations ?» → respuesta corta nueva en la línea de la de productividad.
  
  Las preguntas van sin el espacio antes de «?» del diseño, igual que en el FAQ de la Home (tipografía inglesa).
- Service Nav: Strategic Planning, **Business Optimization** (activo, `aria-current="page"`, enlaza a esta página), IT Consulting, Change Management, Leadership. Los demás van a `#` hasta que existan sus páginas.

### Componentes nuevos y variantes

**Check List (átomo `.check-list`).** `<ul role="list">` con `icon--circle-check` (relleno, `--color-text-primary`) y texto `--color-text-secondary`. Lo usan «Mistakes…» y Key Features, y probablemente Case Study. La lista de About (`about-intro__list`, ícono outline) no se toca.

**Input `--filled` y Field `--filled` (variantes de átomo).**
- Los campos del diseño son cajas grises (`--color-background-subtle`, radio `--radius-sm`), no el filete de About.
- El borde del diseño (≈ 1.2:1) no cumple el 3:1 de los controles (WCAG 1.4.11). Decisión del usuario: borde `--color-border-subtle` en tres lados y **filete inferior en `--color-border-strong`**, que conserva el hover y el color de error del Input.
- `.field--filled` mueve el label en reposo dentro de la caja (al padding del campo) y, al subir, lo alinea con el borde.

**Select (átomo, variante del Input).**
- La clase `.input` sobre `<select>` con `appearance: none`. El chevron es una máscara de `icon--chevron-down` en `.field--select::after`, con `pointer-events: none`.
- Label flotante sin JS: el `<select required>` arranca en `<option value="" hidden selected></option>`, vacía. Con valor vacío el select es `:invalid` y el label queda en reposo; con foco o con valor, sube. Como la opción vacía no lleva `disabled`, no aparece el bug de Chromium que motivó la excepción de `!important` de `CLAUDE.md` §11: **no se usa `!important`**.
- Hereda el filete, el hover, `aria-invalid` y las superficies oscuras del Input. El mensaje de error del Quote Form cubre el caso «valor vacío» (`valueMissing`).

**Service Nav (molécula `.service-nav`).**
- `<nav aria-labelledby>` dentro de una card con borde sutil y radio, con un `h2` «Exclusive Services» en `--text-h4` (medido: 24.5/22.5 px) y un `<ul>` de enlaces.
- Cada enlace: píldora con fondo `--color-background-subtle` y borde sutil, texto y un cuadrado blanco con `icon--arrow-right`.
- Activo (`aria-current="page"`): superficie de marca (petróleo), texto inverso y cuadrado con `--color-action-secondary` (ámbar).
- Hover: el cuadrado pasa a ámbar sin cambiar el fondo (el PNG no muestra hover: es el mismo acento que el activo). Foco visible del theme.

**Quote Form `--outline` (variante).**
- Borde sutil, sin fondo blanco ni sombra, con el mismo padding interno que el Service Nav.
- Mismo JS y mismos cuatro estados.
- Campos: Name, Email, Phone, **Service** (Select con los 5 servicios del Service Nav, obligatorio, `name="service"`) y Message.
- Título «Get a Quote» (`h2`), botón «Submit Now».
- Labels sin los puntos suspensivos del diseño y con el asterisco de obligatorio, como en About.

**Accordion `--framed` (variante del organismo).**
- El grupo va en una caja con borde sutil y radio.
- El ítem abierto lleva fondo `--color-background-subtle`, radio y padding propio. Los cerrados, solo un filete inferior entre ellos (el último, sin filete).
- Sin el «?»: la numeración va en el texto de la pregunta.
- Toggle: un único `icon--arrow-right` que rota −45° al abrir (→ pasa a ↗) con `--ease-base`, en lugar del par +/−.
- Reutiliza `<details name>` y la animación de altura de `.accordion`.

**Ícono `badge-check`** (Lucide) en el set de íconos del átomo Icons.

**Video Modal en todas las páginas (corrección).** Ninguna página tiene hoy el `<dialog data-video-modal>`: el play de los testimonios de la Home no hace nada (`initVideoModal()` sale sin modal). Se agrega el `<dialog>` al bloque `shared:footer` de `index.html` y `sync_shared.py` lo copia a todas las páginas; así funciona el play de la Home y el video de Service Details.

### `<head>`, SEO y navegación
- `title` y `description` del servicio; canonical `https://esonix.example/service-details.html`; OG y Twitter con `og-image.jpg`.
- JSON-LD: `WebPage` + `Service` (`serviceType` «Business Optimization», `provider` → `#organization`) + `BreadcrumbList` con Home y Business Optimization. Google exige URL en los niveles intermedios y Services todavía no existe: se agrega el nivel del medio cuando exista.
- Breadcrumb visible: Home (enlace) › Services (texto, sin enlace) › Business Optimization (`aria-current="page"`).
- `index.html`: el enlace «Service Details» del submenú Services pasa a `service-details.html`, y se corre `sync_shared.py`. La página se suma a `sitemap.xml`.

### Kit y documentación
- Fichas nuevas: Check List (átomo), Select (átomo, con fila en Field), Service Nav (molécula), Section `service-details` (fuente `service-details.html`).
- Filas nuevas: `--outline` en Quote Form, `--framed` en Accordion, `badge-check` en Icons. El Page Hero no lleva marcadores en la página nueva.
- `.stories.md` de cada pieza nueva.

### Verificación
- Recortes del PNG medidos antes de construir cada parte. Comparar a 1920 y 480 px; revisar a 1440, 1280, 1024, 768 y 390 px sin desborde horizontal.
- Teclado: Service Nav, Select (abrir, elegir y volver), FAQ (Enter/Espacio, un solo ítem abierto), botón de video → modal → foco de vuelta.
- Formulario: los cuatro estados con FormSubmit interceptado (predicado sobre `hostname`); el Select vacío muestra su error.
- axe sin violaciones nuevas, consola limpia, `prefers-reduced-motion` (la flecha no rota con transición).
- `sync_shared.py --check` y sus pruebas; About y Home sin regresiones (Accordion, Quote Form, Input).

### Orden de construcción
1. Átomos: `badge-check`, Check List, Select (Sonnet, esfuerzo medio).
2. Moléculas: Service Nav y Quote Form `--outline` con el campo Service (Sonnet, esfuerzo medio).
3. Organismo: Accordion `--framed` (Opus, esfuerzo alto).
4. `service-details.html` con su Section, `<head>`, sitemap y enlace del menú (Opus, esfuerzo alto).
5. Kit, `.stories.md`, QA y reporte de desvíos. Commit de la página tras la aprobación.

Plan de implementación detallado: `docs/plan-etapa-5-service-details.md`.

### Estado: hecha, a la espera de aprobación

**Cambios respecto de esta spec** (decididos al planificar o al construir):
- **Input `--filled` y Field `--filled`:** los campos del diseño son cajas grises, no el filete de About. Tres lados en `--color-border-subtle` (como el diseño) y filete inferior en `--color-border-strong`: el borde del diseño queda en ≈ 1.2:1 y no llega al 3:1 que piden los controles (decisión del usuario).
- **Select sin `!important`:** la opción vacía va `hidden selected` pero **sin `disabled`**, y así no aparece el bug de Chromium que fuerza el color del placeholder. `main.css` no tiene ningún `!important` real (la única coincidencia del `grep` está dentro del comentario que explica por qué no hizo falta). La excepción documentada en `CLAUDE.md` §11 quedó sin caso: conviene borrarla.
- **Bug corregido, fuera del alcance de la página:** ninguna página tenía el `<dialog data-video-modal>`, así que los tres botones de play de la Home no hacían nada. El `<dialog>` se agregó al bloque `shared:footer` de `index.html` y `sync_shared.py` lo propagó. Además, al cerrar el modal el foco vuelve al botón que lo abrió (abierto con el ratón, ese botón nunca lo tuvo y la restauración nativa dejaba el foco en `<body>`).
- **El aside es un `<div>`, no un `<aside>`:** dentro de `<main>` y de la region de la Section, un landmark `complementary` queda anidado (axe: `landmark-complementary-is-top-level`, también sin `aria-label`). La `<nav>` «Exclusive Services» y el `<form>` «Get a Quote» que contiene ya son landmarks con nombre propio, así que no se pierde nada.
- **Los ids del Quote Form llevan prefijo `service-quote-`:** con `quote-` chocaban en el kit con los del formulario de About Us, que salen del mismo helper (en cada página por separado no hay colisión, pero el kit junta las dos Sections).
- `align-content: start` en cada documento de «Document Required»: los dos de una fila quedan igual de altos y, sin eso, el más corto repartía el sobrante entre sus filas y su descripción bajaba respecto de la del vecino.

**Desvíos frente al diseño:**
- Padding superior de la Section: 96px (`.section`, el componente compartido) contra ≈ 120 del diseño. Todo el contenido queda 24px más arriba; el alto total de la Section da 2345px contra 2341, así que el ritmo interno coincide. No se toca `.section`: lo usan todas las páginas.
- `h2` «Explore our Service Lists» a 36px contra 32: con `--text-h3` quedaba igual que los h3 de 28 y se perdía la jerarquía.
- Preguntas del FAQ en mobile a 18px contra 20.5 (se mantiene el componente Accordion Item).
- Page Hero mobile de 420px de alto contra ≈ 320 (se mantiene el componente de About).
- Campos del formulario de 59.6px contra 56, con ~84px entre cajas contra 73: ajustarlo pediría valores fuera de la escala de tokens.
- Fotos sustitutas de la biblioteca (decisión del usuario). La del hero (`h1-process-img-2.webp`) mide 1000px de ancho y a 1920 se ve algo blanda; la del video (`download.webp`, 735×720) recortada a 87:40 corta las cabezas.
- Párrafos anchos del artículo con ~88 caracteres por línea (anti-patrones #13, excepción declarada como en About: así lo muestra el diseño).

**Verificado:** 1920, 1440, 1280, 1024, 768, 480 y 390px sin desborde; axe sin violaciones en la página (1440 y 390); consola limpia; sin ids duplicados; teclado (orden artículo → FAQ → nav → formulario, foco visible en la píldora activa, en el Select y en el play); play → modal → Escape → foco de vuelta al botón; formulario vacío con los 5 errores («Choose an option.» en el Select) y foco en Name; envío completo con la red interceptada (estado enviado, formulario limpio y el label del Select de vuelta en reposo) y con error (`role="alert"`); nunca se envió nada a FormSubmit; `prefers-reduced-motion`; `sync_shared.py --check`; Home y About sin regresiones (el enlace del menú lleva a la página y el play de la Home abre el modal).

**Pendiente del usuario / observaciones:**
- El nivel «Services» del breadcrumb es texto sin enlace y el `BreadcrumbList` del JSON-LD lo omite (Google exige URL en los niveles intermedios): sumarlo en los dos lugares cuando exista la página Services.
- En el kit, la ficha de la Section suma un aviso `landmark-unique`: la `<nav>` «Exclusive Services» aparece también en la ficha de la molécula Service Nav. Es el mismo artefacto que ya tienen los carruseles (`#carousel-services` y `#carousel-services-section`) y no existe en la página real.
- `CLAUDE.md` §11 documenta una excepción de `!important` para el Select que no llegó a existir.

## Páginas siguientes
Services, Portfolios, Case Study, Testimonials y Contact: se describen y planifican cuando lleguen sus PNG (Contact Us ya está en `docs/design/`).
