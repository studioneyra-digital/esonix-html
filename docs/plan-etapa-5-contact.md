# Contact — Plan de implementación

> **Para quien ejecute:** seguir las tareas en orden; cada paso es una casilla (`- [ ]`). Spec: `docs/plan-etapa-5.md` (sección «Contact»). Contexto: `CLAUDE.md`, `docs/traspaso-etapa-5.md`, `docs/tools/README.md`.

**Objetivo:** construir `dist/contact.html` desde `docs/design/Contact-Us-Desktop.png` (1920×1692) y `Contact-Us-Mobile.png` (480×1788).

**Arquitectura:** la página reutiliza el Page Hero, el header `--inner`, el footer, el Quote Form (con su JS) y el Select. Suma una Section nueva (`contact`: título + formulario, foto con tarjeta de contacto y mapa), una variante de molécula (Quote Form `--plain`) y una corrección de átomo (círculo petróleo en `.btn--accent`). Los bloques generados de `main.css` y el kit salen de `docs/tools/*.py`; el bloque `sections:` se escribe a mano.

**Stack:** HTML5, CSS con tokens, JS vanilla (`main.js`, sin cambios previstos), Python 3 (solo librería estándar) para los generadores y `playwright-cli` para la verificación.

## Restricciones globales

- Sin build, sin gestor de paquetes, sin librerías nuevas. Sin `!important`.
- Solo tokens semánticos en componentes. Si una medida no cae en la escala, se redondea al token más cercano y se reporta el desvío.
- Los bloques `atoms:` / `molecules:` / `organisms:` de `main.css` **solo se cambian desde su generador**. La Section nueva va a mano en la subsección «Sections de las páginas interiores», al final del bloque `sections:`.
- Header, footer y off-canvas **se editan solo en `index.html`** y se propagan con `python docs/tools/sync_shared.py` (verificar con `--check`).
- Clases y código en inglés; comentarios y documentación en español; copy del sitio en inglés.
- WCAG 2.2 AA: `<label>` asociado, foco visible, ≥ 4.5:1 en texto y ≥ 3:1 en bordes de controles, `prefers-reduced-motion`.
- Breakpoints: `sm` 30rem, `md` 48rem, `lg` 64rem, `xl` 80rem. El diseño pasa de mobile a desktop en `lg`.
- Decisiones del usuario (esta página):
  - Datos de contacto del sitio: `+880 (123) 456 789`, `support@esonix.com`, «Seattle, WA, USA» (sin calle).
  - Mapa de Google Maps embebido.
  - Desplegable con label «Service» y los 5 servicios.
  - Fotos sustitutas: hero `h1-blog-img-3.webp`, lateral `h1-about-img-1.webp` (decisión vigente; elegidas al planificar).
- Decisiones vigentes de la etapa: dominio `https://esonix.example`, footer de la Home, `h1` interior con `--text-h1`, FormSubmit a `studioneyra@gmail.com`, sin autoplay.
- Fin de línea: `index.html` en CRLF; `main.css` y las demás páginas en LF. Edit lo maneja solo; con Python, leer y escribir bytes. Código Python siempre con Write/Edit y `PYTHONUTF8=1`, nunca en un heredoc.
- Commits con rutas explícitas, **nunca `git add -A`**. Mensaje terminado en `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. La página se commitea una sola vez, tras la aprobación del usuario.

## Medidas tomadas del PNG (desktop 1920 / mobile 480)

Bordes leídos con un canvas sobre el PNG (filas y columnas que no son el crema `254,251,245`):

| Elemento | Desktop | Mobile |
|---|---|---|
| Fin del Page Hero | y=747 | y=321 |
| Eyebrow (glifos) | y=874–887, x=300 | y=407–421, x=14 |
| `h2` (dos líneas) | 910–957 y 970–1017 | 437–470 y 475–508 |
| Filetes de los campos | 1109, 1199 (dos columnas: 300–610 y 635–944) | 597, 687, 778, 868 (14–465) |
| Filete del mensaje | 1369 (300–944) | 1069–1080 (con el tirador) |
| Botón | 300–481 × 1410–1461 | 15–196 × 1119–1171 |
| Foto | 1019–1620 × 865–1515 (600×650, radio ≈ 17) | 14–465 × 1222–1711 (451×489, radio ≈ 17) |
| Tarjeta de contacto | 1040–1389 × 1336–1495 | 35–335 × 1541–1690 |
| Mapa | desde y=1636, x=300–1620, radio ≈ 14, relleno (250,250,248) | — |

Tipografía (ancho del texto renderizado en Mona Sans): `h1` 61 / 40.5; `h2` 51 / 32.7 (peso 500–600); eyebrow 16.5; labels 16; tarjeta 16 con peso 500.

Colores: botón (251,203,121) → `--color-action-secondary`; círculo del botón petróleo con flecha blanca → `--color-action-primary` / `--color-action-on-primary`. Tarjeta: borde un escalón más claro que su interior (blanco translúcido) y fondo oscuro sobre la foto desenfocada → `--color-overlay` + `--color-overlay-light` + `--blur-backdrop`.

## Tarea 1 — Átomo: círculo petróleo en `.btn--accent` (Sonnet, esfuerzo medio)

**Archivos:** `docs/tools/atoms_css.py`, `docs/tools/atoms_kit.py` → regeneran `main.css` (bloque `atoms:`), `dist/kit/index.html` y `docs/kit/button.stories.md`.

- [ ] En `atoms_css.py`, `.btn--accent` suma el círculo:
  ```css
  .btn--accent {
    --btn-bg: var(--color-action-secondary);
    --btn-bg-hover: var(--color-action-secondary-hover);
    --btn-bg-active: var(--color-action-secondary-hover);
    --btn-fg: var(--color-action-on-secondary);
    --btn-icon-bg: var(--color-action-primary);
    --btn-icon-fg: var(--color-action-on-primary);
  }
  ```
  y el comentario del bloque Button dice que el círculo del `--accent` es petróleo (Contact).
- [ ] En `atoms_kit.py`: demo nuevo «Relleno amarillo con círculo (`btn--accent`, Contact)» con `<button class="btn btn--accent">Submit Now<span class="btn__icon">…</span></button>`; la fila de `.btn--accent` pasa a «Relleno amarillo con texto oscuro y círculo petróleo; con --block, sin círculo (plan destacado)».
- [ ] En el generador del Site Header (`docs/tools/organisms_*.py`), el comentario de `.site-header--inner .site-header__cta` dice «en el botón --accent sería ámbar sobre ámbar»: pasa a «el --accent lo trae petróleo; el diseño del header lo muestra blanco». Regenerar ese bloque.
- [ ] Regenerar: `PYTHONUTF8=1 python docs/tools/atoms_css.py && PYTHONUTF8=1 python docs/tools/atoms_kit.py`.
- [ ] Verificar sin regresión: el «Schedule a call» del header sigue con el círculo blanco (`.site-header__cta` redefine `--btn-icon-*`) y el «Get Started» destacado de Pricing no cambia (`--block` no tiene círculo). Contraste: flecha blanca sobre petróleo ≥ 3:1 (ícono), texto oscuro sobre ámbar ≥ 4.5:1.

## Tarea 2 — Molécula: Quote Form `--plain` (Sonnet, esfuerzo medio)

**Archivos:** `docs/tools/molecules_css.py`, `docs/tools/molecules_kit.py` → `main.css` (bloque `molecules:`), kit y `docs/kit/quote-form.stories.md`.

- [ ] CSS en `molecules_css.py`, después de `--outline`:
  ```css
  /* --plain — sin card (Contact): sin fondo, sombra, borde ni padding; el título es el h2 de la Section,
     fuera del formulario. Campos de filete y el Select sobre el mismo filete. Desde md, dos columnas
     (Name · Email, Phone · Service); el mensaje, el botón y los avisos ocupan las dos. row-gap: el diseño
     deja 90px entre filetes y el Field mide ≈ 83. */
  .quote-form--plain {
    padding: 0;
    border-radius: 0;
    background-color: transparent;
    box-shadow: none;
    row-gap: var(--spacing-2);
  }
  .quote-form--plain .quote-form__submit {
    margin-block-start: var(--spacing-7); /* + row-gap = 40px del filete al botón, como el diseño */
  }
  @media (min-width: 48rem) {
    .quote-form--plain {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      column-gap: var(--spacing-6);
      padding: 0;
    }
    .quote-form--plain > :is(.field:has(textarea), .quote-form__submit, .quote-form__messages) {
      grid-column: 1 / -1;
    }
  }
  ```
  Ojo con la especificidad: `.quote-form--plain` va después del `@media (min-width: 48rem) { .quote-form { padding } }` del base, por eso repite `padding: 0` dentro de su propio `@media`. Los avisos ocupan las dos columnas también por debajo de `md` (una sola columna, sin efecto).
- [ ] Comprobar que el Select de filete funciona sin `--filled`: `select.input` toma `--field-pad-inline` = 0 del Field base, el chevron queda al final del filete y el label en reposo mientras la opción vacía está elegida. Si el label en reposo o el chevron se desalinean, corregir en `atoms_css.py` (no en la molécula).
- [ ] `molecules_kit.py`: `quote_form()` pasa de `outline=False` a `variant=''` (`''` | `'outline'` | `'plain'`), conservando idéntica la salida de las dos variantes existentes (comparar el kit antes y después con `git diff --stat` y revisar que solo aparezcan las líneas nuevas). Para `'plain'`:
  - Campos sin `--filled`, Select «Service» sin `--filled` (reutilizar `service_field()` con la clase según la variante).
  - Sin `<h3 class="quote-form__title">`; el `<form>` lleva `aria-labelledby` al título que le pase quien lo llama (parámetro `labelledby`), o `aria-label` en los demos estáticos.
  - Labels Name / Email / Phone / Service / Message; botón `btn btn--accent quote-form__submit` «Submit Now»; `_subject` «New contact message from esonix.example».
  - Demo nuevo en la ficha: «--plain en dos columnas con el Select de filete (Contact)», con su propio prefijo de ids (`quote-plain`), estado `error` para mostrar el Select vacío con su mensaje.
  - Fila nueva: `.quote-form--plain` — «Sin card; dos columnas desde md; el título es el h2 de la Section (`aria-labelledby`)». Decisión nueva: «--plain usa el botón --accent (Contact) y los campos de filete de About».
- [ ] Regenerar: `PYTHONUTF8=1 python docs/tools/molecules_css.py && PYTHONUTF8=1 python docs/tools/molecules_kit.py`.
- [ ] Verificar en el kit a 1440 y 390: dos columnas / una, los cinco errores, foco y Select (abrir, elegir, volver). About y Service Details sin cambios visibles en sus formularios.

## Tarea 3 — `contact.html` (Opus, esfuerzo alto)

**Archivos:** `dist/contact.html` (nuevo), `dist/assets/css/main.css` (bloque `sections:`, a mano), `dist/index.html`, `dist/sitemap.xml`; `sync_shared.py` propaga a `about-us.html` y `service-details.html`.

### 3.1 Esqueleto y `<head>`
- [ ] Partir de `service-details.html`: el mismo `<head>` con `title` «Contact Us — Get in Touch | Esonix», `description` «Contact Esonix to talk about strategy, operations or growth. Call, email or send us a message and our consultants will get back to you soon.», canonical / `og:url` `https://esonix.example/contact.html`, OG y Twitter iguales al resto.
- [ ] JSON-LD:
  ```json
  { "@type": "ContactPage", "@id": "https://esonix.example/contact.html#webpage",
    "url": "https://esonix.example/contact.html", "name": "Contact Us — Get in Touch | Esonix",
    "isPartOf": { "@id": "https://esonix.example/#website" },
    "about": { "@id": "https://esonix.example/#organization" },
    "breadcrumb": { "@id": "https://esonix.example/contact.html#breadcrumb" } }
  ```
  más el `BreadcrumbList` (Home → Contact Us).
- [ ] `preload` de `h1-blog-img-3.webp` con `fetchpriority="high"` (LCP del Page Hero).
- [ ] Marcadores `shared:assets`, `shared:header site-header--inner` y `shared:footer` vacíos, y correr `sync_shared.py` para llenarlos (el script marca «Contact» con `aria-current="page"`).

### 3.2 Page Hero (reutilizado, sin marcadores de Section)
- [ ] Mismo marcado que Service Details: foto `h1-blog-img-3.webp` (`alt=""`, decorativa como en las otras páginas), breadcrumb Home › Contact Us (`aria-current="page"`), `h1` «Contact Us». Revisar el `object-position` del Page Hero con esta foto a 1920 y 480 (las dos caras visibles); si hace falta otro encuadre, `style="--page-hero-position: …"` solo si el componente ya lo admite; si no, reportarlo antes de tocar el componente.

### 3.3 Section `contact`
- [ ] Marcado entre `<!-- section:contact -->` / `<!-- /section:contact -->`:
  ```html
  <section class="section contact" aria-labelledby="contact-title">
    <div class="container">
      <div class="contact__grid">
        <div class="contact__intro">
          <div class="contact__head">
            <p class="eyebrow">Get In Touch</p>
            <h2 class="section-title contact__title" id="contact-title">Let’s Build Something Great Together</h2>
          </div>
          <form class="quote-form quote-form--plain" id="contact-form" data-quote-form action="https://formsubmit.co/studioneyra@gmail.com" method="post" novalidate aria-labelledby="contact-title">
            … salida de quote_form('contact', …, variant='plain', live=True) …
          </form>
        </div>
        <div class="contact__media">
          <img src="assets/img/h1-about-img-1.webp" alt="Smiling Esonix consultants in the office" width="735" height="720" loading="lazy">
          <address class="contact__card" data-surface="inverse">
            <ul class="contact__list" role="list">
              <li><a href="tel:+880123456789">+880 (123) 456 789</a></li>
              <li><a href="mailto:support@esonix.com">support@esonix.com</a></li>
              <li>Seattle, WA, USA</li>
            </ul>
          </address>
        </div>
      </div>
      <iframe class="contact__map" src="https://maps.google.com/maps?q=Seattle%2C%20WA&amp;z=12&amp;output=embed" title="Esonix office location on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </section>
  ```
  El formulario se copia de la salida del helper (Tarea 2) con prefijo `contact-`; no se escribe a mano campo por campo.
- [ ] CSS a mano en `main.css`, subsección «Sections de las páginas interiores»:
  ```css
  /* Contact — título y formulario a la izquierda, foto con la tarjeta de contacto a la derecha y el mapa
     debajo, a todo el contenedor. Desde lg, 43fr | 40fr (645 y 600 px a 1920). */
  .contact__grid {
    display: grid;
    gap: var(--spacing-9);
  }
  .contact__intro,
  .contact__head {
    display: grid;
    align-content: start;
  }
  .contact__head {
    justify-items: start;
    gap: var(--spacing-3);
  }
  .contact__title {
    max-inline-size: 32rem; /* corta después de «Something», como el diseño */
  }
  .contact__media {
    position: relative;
    align-self: start;
  }
  .contact__media img {
    display: block;
    inline-size: 100%;
    block-size: auto;
    aspect-ratio: 12 / 13; /* 600×650 a 1920 y 451×489 a 480 */
    border-radius: var(--radius-md);
    object-fit: cover;
  }
  /* Tarjeta translúcida: la receta de Card Hero (velo y borde del theme) más el desenfoque de la foto. */
  .contact__card {
    position: absolute;
    inset-inline-start: var(--spacing-5);
    inset-block-end: var(--spacing-5);
    inline-size: min(19rem, 100% - 2 * var(--spacing-5));
    padding: var(--spacing-6) var(--spacing-7);
    border: var(--border-width-sm) solid var(--color-overlay-light);
    border-radius: var(--radius-sm);
    background-color: var(--color-overlay);
    backdrop-filter: blur(var(--blur-backdrop));
    color: var(--color-text-inverse);
    font-style: normal;
    font-weight: var(--weight-medium);
  }
  .contact__list {
    display: grid;
    gap: var(--spacing-6);
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .contact__list a {
    color: inherit;
    text-decoration: none;
  }
  .contact__list a:hover {
    text-decoration: underline;
  }
  .contact__map {
    display: block;
    inline-size: 100%;
    block-size: auto;
    aspect-ratio: 4 / 3;
    margin-block-start: var(--spacing-10);
    border: 0;
    border-radius: var(--radius-md);
    background-color: var(--color-background-subtle); /* mientras carga, como la caja del diseño */
  }
  @media (min-width: 64rem) {
    .contact__grid {
      grid-template-columns: minmax(0, 43fr) minmax(0, 40fr);
      gap: var(--spacing-11);
    }
    .contact__card {
      inline-size: min(22rem, 100% - 2 * var(--spacing-5));
    }
    .contact__map {
      aspect-ratio: 11 / 4; /* 1320×480: el PNG corta el mapa y no muestra su alto */
      margin-block-start: var(--spacing-13);
    }
  }
  ```
  `backdrop-filter` crea un bloque contenedor para descendientes `fixed`: la tarjeta no tiene ninguno, así que la trampa de `css-pitfalls-vanilla-sites` no aplica. Si `--color-overlay` no da 4.5:1 sobre la zona más clara de la foto, reforzar el velo con un token existente antes que con un valor nuevo, y reportarlo.
- [ ] Separación entre título y formulario: el Field ya reserva 32 px arriba para su label; medir contra el PNG (del `h2` al primer label hay ≈ 59 px de glifo a glifo) y ajustar con un gap de `.contact__intro` solo si el desvío supera unos pocos px.

### 3.4 Enlaces a Contact, sitemap y kit
- [ ] `index.html` (CRLF, editar con Edit): «Contact» del menú, «Schedule a call» del header y «Contact» del off-canvas → `contact.html`. Correr `PYTHONUTF8=1 python docs/tools/sync_shared.py` y `--check`.
- [ ] `index.html`, cuerpo: «Get Started» del hero, los tres «Get Started» de Pricing, «Join with Us» de Logos y «Contact Us» de la Card CTA → `contact.html`.
- [ ] Confirmar que no queda ningún `href="#site-footer"` en `dist/*.html` salvo los que apunten de verdad al footer (`grep -n "#site-footer" dist/*.html`).
- [ ] `sitemap.xml`: entrada de `https://esonix.example/contact.html` con el mismo formato que las otras.
- [ ] `sections_kit.py`: `dict(id='contact', title='Contact', page='contact.html', …)` con desc, filas (`.contact__grid`, `__intro / __head`, `__media`, `__card`, `__list`, `__map`), tokens, a11y y decisiones (datos del sitio y no del PNG; mapa embebido y sus riesgos; tarjeta sin molécula propia; fotos sustitutas). Correr `PYTHONUTF8=1 python docs/tools/sections_kit.py`.

## Tarea 4 — Kit, QA, reporte y commit (Opus, esfuerzo alto)

- [ ] Recrear los servidores si la sesión es nueva (receta en `traspaso-etapa-5.md` §4) y abrir una sesión nueva de `playwright-cli` (las usadas: `sd`, `sd2`, `sd3`, `ct`).
- [ ] Capturar la página a 1920 y 480 por los mismos tramos que los recortes del PNG y comparar de a pares; medir posiciones (columnas, filetes, botón, foto, tarjeta) contra la tabla de arriba.
- [ ] 1440, 1280, 1024, 768 y 390 px: sin desborde horizontal (`documentElement.scrollWidth`), dos columnas del formulario desde 768, tarjeta dentro de la foto.
- [ ] Teclado: orden del formulario, foco visible en los enlaces de la tarjeta (anillo claro por `data-surface="inverse"`), el Tab entra y sale del mapa.
- [ ] Formulario con FormSubmit interceptado (`page.route` con predicado `url.hostname === 'formsubmit.co'`; nunca enviar de verdad): vacío → cinco errores, foco en Name, «Choose an option.» en el Select; envío correcto → estado enviado y formulario limpio; falla → `role="alert"` y datos conservados.
- [ ] Rueda del mouse sobre el mapa con Lenis activo: la página sigue scrolleando o, si se traba, documentarlo y consultarlo con el usuario.
- [ ] Contraste del texto de la tarjeta sobre la zona más clara de la foto, a 1920 y 480.
- [ ] axe en la página (1440 y 390) y en el kit; ids duplicados en el kit; consola limpia; `prefers-reduced-motion`.
- [ ] Regresiones: header (círculo blanco del «Schedule a call»), Pricing, formularios de About y Service Details, Select `--filled`; `python docs/tools/test_sync_shared.py` (6 pasan).
- [ ] Auditar contra `docs/anti-patrones.md`.
- [ ] Escribir en `plan-etapa-5.md` el «Estado» de Contact (cambios, desvíos, verificado, pendientes), actualizar `traspaso-etapa-5.md` y borrar `docs/plan-etapa-5-service-details.md` (plan ya ejecutado).
- [ ] Tras la aprobación del usuario: commit con rutas explícitas (página, `main.css`, `index.html`, `about-us.html`, `service-details.html`, `sitemap.xml`, kit, generadores, `.stories.md`, docs) y publicación en `esonix-html` con la receta de `CLAUDE.md` §10.
