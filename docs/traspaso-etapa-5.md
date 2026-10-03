# Traspaso — Etapa 5: Service Details publicada, sigue Contact

Estado al 2026-10-03. Este archivo alcanza para arrancar la sesión siguiente. La spec y el estado de cada
página están en `docs/plan-etapa-5.md`; se actualiza al cerrar cada página y se borra al cerrar la Etapa 5.

## 1. Dónde estamos

- Rama `feat/design-to-web-esonix`, subida a `origin` (studioneyra-sandbox) con upstream configurado. Sin PR abierto.
- About Us ✅ (`52ab257`). Service Details ✅ aprobada y commiteada (`91edb15`); estado y desvíos en
  `docs/plan-etapa-5.md` §«Service Details».
- **Theme publicado en `esonix-html`** (`main` en `c303ac2`, 2026-10-03), con About Us y Service Details. Cada
  página nueva que se apruebe se publica de nuevo con la receta de `CLAUDE.md` §10 (`git subtree split`, tomar solo
  el último renglón como hash, push sin force; correr desde la raíz de `studioneyra-sandbox`).
- `docs/plan-etapa-5-service-details.md` (plan ya ejecutado) se puede borrar.
- Orden de páginas: About Us ✅ → Service Details ✅ → **Contact (sigue)**. Portfolios, Case Study, Testimonials y
  Services no tienen PNG; Contact sí: `Contact-Us-Desktop.png` (1920×1692) y `Contact-Us-Mobile.png` (480×1788).
- **Contact:** spec en `plan-etapa-5.md` §«Contact», plan en `docs/plan-etapa-5-contact.md` (4 tareas), ambos
  aprobados y commiteados (`2dbc8bb`). **Tareas 1 y 2 hechas y commiteadas (`f03e555`):** `.btn--accent` con
  círculo petróleo (átomo) y Quote Form `--plain` (molécula, dos columnas desde `md`, título externo vía
  `aria-labelledby`, Select de filete). Verificado en el kit a 1440/390, sin regresión en `--outline`/About/
  Service Details/header; `test_sync_shared.py` OK. **Tarea 3 hecha, SIN COMMIT:** `dist/contact.html`, CSS
  `contact__*` en `sections:`, los 9 `#site-footer` de `index.html` → `contact.html` (propagados con
  `sync_shared`), sitemap y ficha `contact` en `sections_kit.py`. Ajustes encontrados al construir: enlace activo de
  primer nivel del header `--inner` quedaba petróleo sobre la píldora oscura (corregido en `organisms_css.py`, ámbar
  como los subenlaces); la tarjeta no puede llevar `data-surface="inverse"` (pinta fondo opaco) y redefine solo el
  token de foco; textarea de `--plain` a `--spacing-13`; mapa con `hl=en`. **Tarea 4 (QA) hecha:** reporte
  completo en `plan-etapa-5.md` §Contact «Estado». **Falta solo la aprobación del usuario → commit de la página
  (rutas explícitas) y publicación en `esonix-html` (CLAUDE.md §10).** `docs/plan-etapa-5-service-details.md`
  ya está borrado (`git rm`, entra en ese commit).

## Decisiones tomadas el 2026-10-03

- `CLAUDE.md` §11: se borró la excepción de `!important` del Select (nunca llegó a usarse). Sin excepciones.
- Padding superior de las Sections: queda en 96 px (`.section`) aunque el diseño muestre ~120.

## 2. Qué quedó construido en Service Details

Todo verificado en el navegador (ver «Verificado» en `plan-etapa-5.md`).

**Átomos:** ícono `badge-check`; `.check-list` (lista con `icon--circle-check`, ícono centrado en la primera
línea con `1lh`); `.input--filled` (caja gris, filete inferior en `--color-border-strong`); `.field--filled` y
`.field--select`. El bloque Field usa ahora `--field-rise`, `--field-pad-block` y `--field-pad-inline`, así el
label flota igual en los dos estilos. El Select es un `<select>` nativo con `appearance: none` y chevron como
máscara en `.field--select::after`; la opción vacía va `hidden selected` **sin `disabled`** y por eso **no hizo
falta `!important`**. Fichas nuevas: `select`, `check-list`.

**Moléculas:** `.service-nav` (card con la lista de servicios en píldoras con cuadrado de flecha; el activo en
petróleo con cuadrado ámbar) y `.quote-form--outline` (borde, sin fondo ni sombra, campos `--filled` y campo
Service obligatorio). El helper `quote_form()` toma `outline=True`; con `outline=False` la salida es idéntica a
la anterior. En `main.js`: `FORM_MESSAGES.selectMissing`, `fieldError()` para `SELECT` y escucha de `change`
además de `input`. Ficha nueva: `service-nav`.

**Organismos:** `.accordion--framed` (caja con borde, el abierto en caja gris, filete solo entre cerrados
consecutivos, una sola flecha que rota −45°). Helper `accordion_framed()` y lista `FAQ_FRAMED`.

**Página:** `dist/service-details.html` (Page Hero reutilizado + Section `service-details`), su CSS en el bloque
`sections:` de `main.css`, la ficha `service-details` en `sections_kit.py`, la entrada del sitemap y los dos
enlaces «Service Details» del menú en `index.html`.

**Dos arreglos fuera del alcance de la página:** el `<dialog data-video-modal>` no existía en ninguna página
(los tres botones de play de la Home no hacían nada); se agregó al bloque `shared:footer` de `index.html` y
`sync_shared.py` lo propagó. Y al cerrar el modal el foco vuelve al botón que lo abrió.

## 3. Reglas del flujo de archivos (no saltarlas)

- **Bloques generados:** `atoms:` / `molecules:` / `organisms:` de `main.css` se cambian solo desde
  `docs/tools/*_css.py`; las fichas, desde `*_kit.py`. El bloque `sections:` se escribe a mano, en la
  subsección «Sections de las páginas interiores» del final.
- **Sections nuevas:** marcar `<!-- section:id -->` en la página, sumar su `dict` con `page='<archivo>.html'`
  en `sections_kit.py` y correrlo. Una Section reutilizada con modificador no lleva marcadores en la página
  nueva (el Page Hero de Service Details, por ejemplo): se documenta como fila en su ficha.
- **Ids únicos en el kit:** el kit junta las Sections de todas las páginas en un solo documento, así que dos
  páginas con el mismo prefijo de ids chocan aunque cada una esté bien. Pasó con el Quote Form (About usa
  `quote-*`; Service Details usa `service-quote-*`). Al construir una página nueva, revisar ids duplicados en
  el kit, no solo en la página.
- **Piezas compartidas:** header, footer y el `<dialog>` del video se editan solo en `index.html`; después
  `sync_shared.py` y verificar con `--check`. Pruebas: `python docs/tools/test_sync_shared.py` (6, pasan).
- **Commits:** rutas explícitas, nunca `git add -A`. `.playwright-cli/` y `.vscode/` no van.

## 4. Receta de QA (lo que funcionó)

- **Servidores:** `serve.py` vive en el scratchpad de la sesión, así que **en una sesión nueva hay que
  recrearlo** (subclase de `ThreadingHTTPServer` con `Cache-Control: no-store`; receta en la memoria
  `playwright-cli-qa-recipes`). Puerto 8765 sobre la raíz del proyecto (`/dist/...`) y 8766 sobre
  `docs/design`. Lanzarlos con `run_in_background` y `timeout` de 7 200 000 ms: con el valor por defecto se
  cortan a la media hora.
- **Recortes del PNG:** también están en el scratchpad y se pierden. Receta: servir `docs/design` por http,
  `page.goto` a esa raíz, `setContent('<img src=...>')` con el viewport del ancho del PNG y
  `screenshot({ fullPage: true, clip })` por tramos (1000 px en desktop, 1400 en mobile). Capturar la página
  por los mismos tramos y comparar de a pares.
- **Medir tipografía:** renderizar el texto en Mona Sans a 100 px en la página del kit y despejar el tamaño
  desde el ancho medido en el PNG.
- **playwright-cli:** `playwright-cli -s=<sesión> run-code --filename=<abs>.js`, con cache-buster
  `?v=Date.now()` en cada `goto`. La sesión hay que abrirla antes (`open <url>`) o `run-code` falla. Sesiones
  ya usadas y cerradas: `sd`, `sd2`, `sd3`.

### Trampas encontradas (van a reaparecer)

- **El primer `[data-video-id]` de la Home está en una slide del carrusel fuera del viewport**, con
  `tabindex="-1"`: `click()` vence por timeout. Apuntar a
  `.swiper-slide-active [data-video-id], [data-video-id]:not([tabindex="-1"])`.
- **El evento `close` de `<dialog>` se dispara ANTES de que el navegador restaure el foco**: ahí
  `document.activeElement` todavía no es `<body>`. Restaurar el foco dentro de `requestAnimationFrame`.
- **El navegador reusa `main.js` de su caché** aunque el servidor mande `no-store`, si la sesión ya lo había
  cargado: el cache-buster del HTML no alcanza. Abrir una sesión nueva de playwright-cli o interceptar la ruta
  del `.js`. Comprobar con `fetch('assets/js/main.js?v=...')` que el archivo servido tiene el cambio.
- **Un heredoc de Bash se come las barras invertidas:** el código Python se escribe con Write/Edit, nunca en un
  heredoc.
- **Hijos de una grilla que se estiran:** si dos ítems de la misma fila tienen distinto contenido, el más corto
  reparte el sobrante entre sus propias filas y su texto se desalinea del vecino. `align-content: start`.
- **El sandbox de `run-code` no tiene el global `URL`:** un predicado de `page.route` con `new URL(u)` tira
  `ReferenceError` en cada petición, y la ruta rota queda registrada en la sesión y rompe todo lo que sigue
  (cerrar la sesión). El predicado ya recibe un objeto URL: `u => u.hostname === 'formsubmit.co'`. Para
  FormSubmit también sirve el glob `'https://formsubmit.co/**'` (no lleva `?v=`). Un iframe de Google Maps sale
  gris en capturas `fullPage`: capturarlo con `locator.screenshot()`.
- **`page.accessibility` no existe en playwright-cli:** para roles y landmarks, usar axe (`axe.run`) y comparar
  A/B quitando el nodo del DOM, en vez de `accessibility.snapshot`.
- Playwright trata `aria-disabled` como deshabilitado (usar `{ force: true }`); `page.route` con glob no
  matchea URLs con `?v=` (usar un predicado); con FormSubmit, interceptar siempre
  `url.hostname === 'formsubmit.co'` y no enviar nunca de verdad.
- **axe:** `page.addScriptTag({ url: 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.2/axe.min.js' })`.
  Falsos positivos conocidos: slides con opacidad 0 del carrusel con fundido, textos decorativos de la Home
  («01/03» y «Works»), fotos detrás de `isolation: isolate`, y en el kit `landmark-unique` /
  `scrollable-region-focusable` por mostrar el mismo componente en su ficha y en la de su Section.
- **Fin de línea:** `index.html` está en CRLF; `main.css`, `about-us.html`, `service-details.html` y el resto,
  en LF. Al editarlos con Python, leer y escribir bytes conservando el fin de línea; Edit lo maneja solo.

## 5. Decisiones vigentes (no volver a preguntar)

Dominio `https://esonix.example` · footer de la Home en todas las páginas · header `--inner` en las interiores ·
`h1` interior con `--text-h1` · formularios por FormSubmit a studioneyra@gmail.com con label flotante y estados ·
sin autoplay en los carruseles · CSS Grid con los breakpoints del theme · fotos sustitutas de la biblioteca
cuando el diseño use fotos que no están en `dist/assets/img`.

## 6. Pendientes abiertos

- El nivel «Services» del breadcrumb de Service Details es texto sin enlace y el `BreadcrumbList` del JSON-LD
  lo omite (Google exige URL en los niveles intermedios): agregarlo en los dos lugares cuando exista la página.
- «Schedule a call» y los «Contact» llevan a `#site-footer` hasta que exista Contact.
- El Hero de la Home no tiene `data-surface="inverse"` (foco oscuro sobre la foto): se puede corregir en un
  commit aparte.
- Para el usuario: confirmar la activación de FormSubmit en el primer envío real; lector de pantalla real;
  Rich Results Test del JSON-LD; Lighthouse en el hosting final.
