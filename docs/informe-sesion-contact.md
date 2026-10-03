# Informe — Sesión del 2026-10-03: Contact publicada

Insumo para retomar el proyecto en otra sesión. Complementa `docs/traspaso-etapa-5.md` (reglas del flujo y trampas
de QA) y `docs/plan-etapa-5.md` (spec y estado de cada página). Si hay contradicción, manda el traspaso.

## 1. Resultado

La página **Contact** quedó construida, verificada, commiteada y publicada. Con ella están hechas **todas las
páginas interiores que tienen diseño** en `docs/design/` (About Us, Service Details, Contact).

| Entrega | Commit |
|---|---|
| Spec y plan de Contact; se borra la excepción de `!important` de `CLAUDE.md` §11 | `2dbc8bb` |
| Átomo `.btn--accent` con círculo petróleo + molécula Quote Form `--plain` | `f03e555` |
| Página `contact.html`, enlaces, sitemap, ficha del kit; se borra el plan ejecutado de Service Details | `e17980d` |
| Traspaso actualizado | `a044ccd` |

- Rama `feat/design-to-web-esonix` (sin PR abierto; `a044ccd` aún no está en `origin`).
- **`esonix-html`** (`main`): `c303ac2` → `bf5732a`, publicado con `git subtree split` sin force. El commit `a044ccd`
  (solo docs) no está en ese repo; entra en la próxima publicación.

## 2. Decisiones del usuario (vigentes, no volver a preguntar)

- **Contact:** datos de contacto del sitio (`+880 (123) 456 789`, `support@esonix.com`, «Seattle, WA, USA» sin
  calle), no los del PNG; mapa de Google Maps embebido en desktop y mobile; desplegable con label «Service» y los
  5 servicios (no «Select Option»).
- **Padding de las Sections:** queda en 96 px (`.section`), aunque el diseño muestre ≈ 120.
- **`CLAUDE.md` §11:** sin excepciones de `!important`. `main.css` tiene cero reales.
- Las anteriores siguen: dominio `https://esonix.example`, footer de la Home, `h1` interior con `--text-h1`,
  FormSubmit a studioneyra@gmail.com, sin autoplay, fotos sustitutas de la biblioteca.

## 3. Qué se construyó

**Átomo.** `.btn--accent` ahora trae el círculo petróleo con flecha blanca (antes ámbar sobre ámbar). El «Schedule a
call» del header redefine su propio círculo en blanco y no cambió.

**Molécula.** Quote Form `--plain`: sin card, sin `<h3>` propio (el título es el `h2` de la Section y el `<form>` lo
toma con `aria-labelledby`), campos de filete con el Select sobre el mismo filete, dos columnas desde `md`
(Name · Email / Phone · Service; mensaje, botón y avisos a lo ancho), mensaje de 128 px, botón `--accent`.
`quote_form()` en `molecules_kit.py` pasó de `outline=bool` a `variant='' | 'outline' | 'plain'` más
`labelledby` y `subject`; el `'plain'` exige `labelledby` (assert). Mismo JS y mismos cuatro estados que los otros
formularios.

**Página.** `dist/contact.html`: Page Hero (foto `h1-blog-img-3.webp`, breadcrumb Home › Contact Us), Section
`contact` (eyebrow + `h2` + formulario | foto `h1-about-img-1.webp` con tarjeta `<address>` translúcida | mapa
`iframe` lazy), JSON-LD `ContactPage` + `BreadcrumbList`, entrada en `sitemap.xml`. CSS `contact__*` a mano en el
bloque `sections:` de `main.css`; ficha `contact` en `sections_kit.py`.

**Enlaces.** Los 9 `href="#site-footer"` de `index.html` (menú, «Schedule a call», off-canvas, «Get Started» del
hero y de Pricing, «Join with Us», «Contact Us» de la CTA) pasan a `contact.html`; `sync_shared.py` los propagó. Ya no
queda ningún `#site-footer` en `dist/`.

## 4. Hallazgos al construir (pueden reaparecer)

1. **`data-surface="inverse"` pinta fondo opaco** con especificidad (0,1,1): no sirve para un panel translúcido.
   La tarjeta de contacto no lo lleva y solo redefine `--color-border-focus: var(--color-border-focus-inverse)`
   (misma solución que la píldora del header `--inner`).
2. **Enlace activo de primer nivel del header `--inner`:** `.site-nav__link[aria-current]` (petróleo) pisaba el
   blanco de `--inner` y quedaba casi invisible sobre la píldora oscura. Era la primera página con el enlace actual
   de primer nivel (en About y Service Details es un subenlace). Corregido en `organisms_css.py`: ámbar.
3. **El `.btn--accent` heredaba un círculo ámbar:** cualquier botón accent con círculo nuevo lo necesitaba petróleo.
4. **Hijos ocultos de una grilla:** `input[type=hidden]` y `div[hidden]` no generan caja, así que no ocupan celdas
   en la grilla de dos columnas del formulario.
5. **Mapa:** sin `hl=en`, Google muestra la interfaz en el idioma del navegador. En capturas `fullPage` el iframe
   sale gris (Chromium solo lo pinta dentro del viewport): capturarlo con `locator.screenshot()`.
6. **QA con playwright-cli:** el sandbox de `run-code` no tiene el global `URL`; un predicado de `page.route` con
   `new URL(...)` rompe cada petición y la ruta rota queda en la sesión (cerrar y abrir otra). Usar
   `u => u.hostname === '...'` o el glob `'https://formsubmit.co/**'`. Detalle en el traspaso y en la memoria
   `playwright-cli-qa-recipes`.
7. Una sesión de playwright dejó una carpeta `dist/.playwright-cli/` (se publicaría): revisar `dist/` antes de
   commitear.

## 5. Verificación realizada

- **Anchos:** 1920, 1440, 1280, 1024, 768, 480 y 390 px sin desborde; formulario en dos columnas desde 768.
- **Contra el PNG a 1920:** columnas 642/598 (645/600), filetes cada 91 (90), mensaje 128 (≈ 123), botón a 40 del
  filete (41), foto 598×647 (600×650), tarjeta 352×167 (350×160), mapa a 128 de la foto (≈ 120).
- **Teclado:** orden Name → Email → Phone → Service → Message → botón → teléfono → email; foco visible; el Tab entra
  al mapa (9 paradas) y sale al newsletter del footer.
- **Formulario** con FormSubmit interceptado (no se envió nada real): vacío → 5 errores y foco en Name; enviado →
  `role="status"`, formulario limpio y label del Select en reposo; falla de red → `role="alert"` y datos conservados.
- **Lenis sobre el mapa:** la rueda sigue moviendo la página (no se traba).
- **Contraste de la tarjeta** contra el píxel más claro del fondo: 5.78:1 (390) a 7.77:1 (1920); mínimo 4.5.
- **axe:** sin violaciones en la página (1440 y 390) ni en las fichas Contact, Quote Form y Button del kit. En la
  Home solo el falso positivo conocido («01»/«03» decorativos). Kit sin ids duplicados, consola limpia, enlaces sin
  404, `prefers-reduced-motion` ok, `sync_shared.py --check` y sus 6 pruebas ok, `anti-patrones.md` sin hallazgos.

## 6. Desvíos frente al diseño (declarados en `plan-etapa-5.md`)

- Padding superior 96 px contra ≈ 120 (decisión del usuario); `h1` y `h2` con tokens (48/36 px) contra ≈ 61/51.
- «Contact» activo del header en **ámbar** contra blanco en el diseño (único desvío no decidido de antemano por el
  usuario; quedó sin objeción al aprobar la página).
- Mobile: 56 px del botón a la foto contra 51; mapa con alto propio (el PNG lo corta y en mobile no lo muestra).
- Fotos sustitutas: el hero (1308 px) se ve algo blando a 1920 bajo el velo.

## 7. Pendientes

**Del usuario**
- Consentimiento previo para el mapa si el sitio debe cumplir GDPR (Google carga peticiones y cookies al acercarse).
- Confirmar la activación de FormSubmit en el primer envío real (correo de activación a studioneyra@gmail.com).
- Lector de pantalla real, Rich Results Test del JSON-LD, Lighthouse en el hosting final.

**Técnicos**
- Cuando exista la página Services: enlazar el nivel «Services» del breadcrumb de Service Details (texto hoy) y
  sumarlo al `BreadcrumbList` de su JSON-LD.
- El Hero de la Home no tiene `data-surface="inverse"` (foco oscuro sobre la foto): commit aparte, fuera de alcance.
- Publicar de nuevo en `esonix-html` cuando haya cambios (receta de `CLAUDE.md` §10).

**Bloqueado:** Services, Portfolios, Case Study y Testimonials no tienen PNG en `docs/design/`. No hay nada más que
construir hasta que existan.

## 8. Cómo retomar

1. Leer `docs/traspaso-etapa-5.md` (reglas del flujo de archivos, receta de QA, trampas) y esta nota.
2. Con un PNG nuevo: recortarlo por tramos a resolución real (receta en el traspaso §4), escribir su spec en
   `plan-etapa-5.md` y su plan en `docs/plan-etapa-5-<pagina>.md`, y **esperar el visto bueno** antes de construir.
3. Construir por tareas, siguiendo el reparto que funcionó: átomos y moléculas con Sonnet (esfuerzo medio);
   página y QA con Opus (esfuerzo alto); cambiar con `/model` entre tareas, no a mitad de una.
4. Usar el skill `frontend-design` y auditar contra `docs/anti-patrones.md`.
5. Servidores de QA: `serve.py` vive en el scratchpad de la sesión y se pierde (subclase de `ThreadingHTTPServer`
   con `Cache-Control: no-store`; puerto 8765 sobre la raíz del proyecto, 8766 sobre `docs/design`; lanzarlos con
   `run_in_background` y `timeout` de 7 200 000 ms; se detienen al agotarlo).
6. Commits con rutas explícitas (nunca `git add -A`); no versionar `.playwright-cli/` ni `.vscode/`.
