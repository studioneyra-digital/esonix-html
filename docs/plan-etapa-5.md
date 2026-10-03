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

### Estado: hecha, en revisión
Infraestructura commiteada (`1b517dd`); la página, construida y verificada, espera aprobación para su commit.

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

## Páginas siguientes
Services, Service Details, Portfolios, Case Study, Testimonials y Contact: se describen y planifican cuando lleguen sus PNG (ya están Service Details y Contact Us en `docs/design/`).
