# About Us — Plan de implementación

> **Para quien ejecute:** seguir las tareas en orden; cada paso es una casilla (`- [ ]`). Spec: `docs/plan-etapa-5.md` (sección «About Us»). Contexto del proyecto: `CLAUDE.md`, `docs/plan.md`, `docs/tools/README.md`.

**Objetivo:** construir `dist/about-us.html` desde `docs/design/About-Us-Desktop.png` (1920×5937) y `About-Us-Mobile.png` (480×8530), con la infraestructura multipágina (piezas compartidas y kit de Sections de varias páginas) que reutilizan las 6 páginas siguientes.

**Arquitectura:** HTML/CSS/JS estático sin build. `index.html` es la fuente del header, el footer y las hojas de estilo; `docs/tools/sync_shared.py` los copia a las demás páginas entre marcadores `<!-- shared:x -->`. Los componentes nuevos siguen el flujo de generadores del kit (`docs/tools/*_css.py` / `*_kit.py`). Las Sections se escriben a mano en el bloque `sections:` de `main.css`, y `sections_kit.py` extrae su markup de la página que declara cada una.

**Stack:** HTML5, CSS con tokens (`dist/assets/css/tokens/*.css`), JS vanilla (`dist/assets/js/main.js`), Swiper (cargado a demanda por `requireLib`), Python 3 con solo la librería estándar para las herramientas y `playwright-cli` para QA.

## Restricciones globales

- Sin build, sin gestor de paquetes, sin librerías nuevas.
- Sin `!important` (única excepción ya documentada: el Select).
- Solo tokens semánticos en los componentes; nada de `--color-brand-*` / `--color-neutral-*`. Sin magic numbers: si un valor medido no cae en la escala, se deja con comentario de dónde sale (patrón ya usado en `main.css`).
- Los bloques `atoms:` / `molecules:` / `organisms:` de `main.css` **solo se cambian desde su generador** (`docs/tools/*_css.py`). El bloque `sections:` es manual.
- Código y clases en inglés; comentarios y documentación en español; copy del sitio en inglés.
- WCAG 2.2 AA: `<label>` asociado en cada campo, foco visible, contraste ≥ 4.5:1 en texto y ≥ 3:1 en bordes de controles, `prefers-reduced-motion`.
- Breakpoints del theme: `sm` 30rem, `md` 48rem, `lg` 64rem, `xl` 80rem. El cambio de desktop a mobile del diseño es en `lg`.
- Decisiones ya tomadas por el usuario: footer de la Home; «12K+» repetido en el mobile es un error de captura; formulario por **FormSubmit** a `studioneyra@gmail.com` con estados de error y envío; **label flotante**; 3 citas (David Thompson primero, luego James Anderson e Isabella Harris, con su copy de la Home); `h1` del hero interior con **`--text-h1`** (48/36 px, desvío a reportar: el diseño mide ≈ 62/41 px).
- Commits con rutas explícitas, **nunca `git add -A`** (el repo tiene borrados de otros proyectos y `.playwright-cli/`, `.vscode/` sin versionar). Mensaje terminado en `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Cambios respecto de la spec (detectados al planificar)

1. **El slider de citas es una variante del Carousel** (`carousel--fade` + `data-carousel-fade`), no un organismo nuevo: reutiliza la carga diferida de Swiper, los dots y el teclado de `initCarousel`. Así no se duplica funcionalidad (`CLAUDE.md` §9).
2. **Variantes que la spec no listaba y el PNG sí muestra:** `card-cta--stacked` (la CTA del FAQ es una card blanca con la foto arriba, no una foto de fondo), `accordion--boxed` (ítems en caja con borde; el abierto en blanco) y `progress--accent` (la barra «Consulting» es ámbar).
3. **Fondo con foto compartido:** Testimonials (Home) y Feedback (About) usan el mismo tratamiento (foto desenfocada + velo). Se extrae a `.section-bg` en el bloque `sections:` y se migra Testimonials, en vez de duplicar las reglas.
4. **El hero interior no es un recurso precargado compartido:** el bloque `shared:assets` abarca solo las hojas de estilo; el favicon, la precarga de la fuente y la de la foto del hero quedan por página.

## Mapa de archivos

| Archivo | Responsabilidad | Tareas |
|---|---|---|
| `docs/tools/sync_shared.py` (nuevo) | Copiar `shared:assets/header/footer` de `index.html` a las demás páginas y marcar `aria-current` | 1 |
| `docs/tools/test_sync_shared.py` (nuevo) | Pruebas de `sync_shared.py` sobre una carpeta temporal | 1 |
| `docs/tools/sections_kit.py` | Extraer cada Section de la página que la declara (`page`) | 2, 10 |
| `docs/tools/README.md` | Documentar `sync_shared.py` y las Sections multipágina | 1, 2 |
| `docs/tools/atoms_css.py` / `atoms_kit.py` | Textarea, Field, `progress--accent` | 3 |
| `docs/tools/molecules_css.py` / `molecules_kit.py` | `card-team--profile`, `card-cta--stacked`, Quote Form | 4, 5 |
| `docs/tools/organisms_css.py` / `organisms_kit.py` | `carousel--fade`, `accordion--boxed` | 6 |
| `dist/assets/js/main.js` | Envío del Quote Form; modo fade del Carousel | 5, 6 |
| `dist/assets/css/main.css` | Bloques generados (por script) + bloque `sections:` (a mano) | 3–9 |
| `dist/index.html` | Marcadores `shared:`, enlace «About Us», `section-bg` en Testimonials | 1, 7, 8 |
| `dist/about-us.html` (nuevo) | La página | 7–9 |
| `dist/sitemap.xml` | Sumar About Us | 7 |
| `dist/kit/index.html`, `docs/kit/*.stories.md` | Regenerados por los `*_kit.py` | 3–6, 10 |
| `docs/plan.md`, `docs/plan-etapa-5.md` | Estado | 10 |

---

### Tarea 1: Piezas compartidas — marcadores y `sync_shared.py`

**Archivos:**
- Crear: `docs/tools/sync_shared.py`, `docs/tools/test_sync_shared.py`
- Modificar: `dist/index.html` (marcadores), `docs/tools/README.md`

**Interfaces:**
- Produce: marcadores `<!-- shared:assets -->`, `<!-- shared:header -->`, `<!-- shared:footer -->` (con sus cierres `<!-- /shared:x -->`) en `dist/index.html`. Toda página nueva de `dist/` debe traer los tres pares (vacíos alcanza); `python docs/tools/sync_shared.py` los llena. `--check` sale con código 1 si alguna página está desfasada. `--dist <ruta>` cambia la carpeta (para pruebas).

- [ ] **Paso 1: escribir la prueba que falla**

`docs/tools/test_sync_shared.py`:

```python
# Pruebas de sync_shared.py sobre una copia temporal de dist/ (no toca el proyecto).
# Uso: python docs/tools/test_sync_shared.py
import subprocess, sys, tempfile, unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
SCRIPT = TOOLS / 'sync_shared.py'

INDEX = '''<!doctype html>
<html lang="en">
<head>
  <!-- shared:assets -->
  <link rel="stylesheet" href="assets/css/main.css">
  <!-- /shared:assets -->
</head>
<body>
  <!-- shared:header -->
  <header>
    <a class="site-nav__sublink" href="./" aria-current="page">Home Version 01</a>
    <a class="site-nav__sublink" href="about-us.html">About Us</a>
  </header>
  <!-- /shared:header -->
  <main>home</main>
  <!-- shared:footer -->
  <footer>
    <a class="offcanvas__sublink" href="./" aria-current="page">Home Version 01</a>
    <a class="offcanvas__sublink" href="about-us.html">About Us</a>
  </footer>
  <!-- /shared:footer -->
</body>
</html>
'''

PAGE = '''<!doctype html>
<html lang="en">
<head>
  <!-- shared:assets -->
  <!-- /shared:assets -->
</head>
<body>
  <!-- shared:header -->
  <!-- /shared:header -->
  <main>about</main>
  <!-- shared:footer -->
  <!-- /shared:footer -->
</body>
</html>
'''

def run(dist, *args):
    return subprocess.run([sys.executable, str(SCRIPT), '--dist', str(dist), *args], capture_output=True, text=True)

class SyncSharedTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dist = Path(self.tmp.name)
        (self.dist / 'index.html').write_text(INDEX, encoding='utf-8')
        (self.dist / 'about-us.html').write_text(PAGE, encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_copies_blocks_and_marks_current_page(self):
        result = run(self.dist)
        self.assertEqual(result.returncode, 0, result.stderr)
        about = (self.dist / 'about-us.html').read_text(encoding='utf-8')
        self.assertIn('assets/css/main.css', about)
        self.assertIn('<main>about</main>', about)
        # el enlace a la propia página queda marcado, en el header y en el off-canvas
        self.assertIn('<a class="site-nav__sublink" href="about-us.html" aria-current="page">', about)
        self.assertIn('<a class="offcanvas__sublink" href="about-us.html" aria-current="page">', about)
        # y la marca de la home no se copia
        self.assertNotIn('href="./" aria-current="page"', about)

    def test_source_is_not_modified(self):
        run(self.dist)
        self.assertEqual((self.dist / 'index.html').read_text(encoding='utf-8'), INDEX)

    def test_check_reports_stale_pages_and_is_idempotent(self):
        self.assertEqual(run(self.dist, '--check').returncode, 1)
        run(self.dist)
        self.assertEqual(run(self.dist, '--check').returncode, 0)

    def test_missing_marker_fails(self):
        (self.dist / 'broken.html').write_text('<html><body></body></html>', encoding='utf-8')
        result = run(self.dist)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('shared:assets', result.stderr)

if __name__ == '__main__':
    unittest.main()
```

- [ ] **Paso 2: correr la prueba y ver que falla**

Run: `python docs/tools/test_sync_shared.py`
Esperado: 4 errores (`can't open file ... sync_shared.py`).

- [ ] **Paso 3: escribir `sync_shared.py`**

```python
# Copia las piezas comunes del sitio desde dist/index.html (la única fuente) a las demás páginas de dist/:
#   shared:assets  → las hojas de estilo del <head>
#   shared:header  → skip link + header
#   shared:footer  → footer, off-canvas, Scroll Top y scripts
# En cada página marca con aria-current="page" el enlace del menú que apunta a ella (header y off-canvas)
# y quita la marca que trae la home. Correrlo después de cualquier cambio en esas piezas de index.html.
# Uso: python docs/tools/sync_shared.py [--check] [--dist <carpeta>]
#   --check  no escribe; sale con 1 si alguna página está desfasada (sirve antes de commitear)
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
BLOCKS = ('assets', 'header', 'footer')
NAV_LINK = r'<a class="(?:site-nav__link|site-nav__sublink|offcanvas__link|offcanvas__sublink)" href="%s"'

def pattern(name):
    return re.compile(r'[ \t]*<!-- shared:%s -->\n.*?<!-- /shared:%s -->' % (name, name), re.S)

def find_block(html, name, where):
    m = pattern(name).search(html)
    if not m:
        sys.exit('falta el bloque shared:%s en %s' % (name, where))
    return m.group(0)

def mark_current(markup, page_name):
    markup = markup.replace(' aria-current="page"', '')
    return re.sub('(' + NAV_LINK % re.escape(page_name) + ')', r'\1 aria-current="page"', markup)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--dist', default=str(ROOT / 'dist'))
    args = parser.parse_args()

    dist = Path(args.dist)
    source = (dist / 'index.html').read_text(encoding='utf-8')
    shared = {name: find_block(source, name, 'index.html') for name in BLOCKS}

    stale = []
    for page in sorted(dist.glob('*.html')):
        if page.name == 'index.html':
            continue
        html = page.read_text(encoding='utf-8')
        new = html
        for name in BLOCKS:
            find_block(html, name, page.name)
            block = mark_current(shared[name], page.name)
            new = pattern(name).sub(lambda m: block, new, count=1)
        if new != html:
            stale.append(page.name)
            if not args.check:
                page.write_text(new, encoding='utf-8', newline='\n')

    if args.check:
        if stale:
            print('desfasadas:', ', '.join(stale))
            sys.exit(1)
        print('ok: todas las páginas al día')
    else:
        print('actualizadas:', ', '.join(stale) if stale else 'ninguna')

if __name__ == '__main__':
    main()
```

- [ ] **Paso 4: correr la prueba y ver que pasa**

Run: `python docs/tools/test_sync_shared.py`
Esperado: `Ran 4 tests ... OK`.

- [ ] **Paso 5: marcar las piezas en `dist/index.html`**

Envolver, sin cambiar nada de lo que hay adentro:
- `<!-- shared:assets -->` antes de `<link rel="stylesheet" href="assets/css/bootstrap-grid.min.css">` y `<!-- /shared:assets -->` después de `<link rel="stylesheet" href="assets/css/main.css">` (líneas 58–68). Indentado con 2 espacios, como el `<head>`.
- `<!-- shared:header -->` después de `<body>` (antes del skip link) y `<!-- /shared:header -->` después de `</header>` (línea 148).
- `<!-- shared:footer -->` antes de `<!-- section:footer -->` y `<!-- /shared:footer -->` después de `<script src="assets/js/main.js" defer></script>`.

Comprobación: `python -c "import re,pathlib;h=pathlib.Path('dist/index.html').read_text(encoding='utf-8');print([h.count('<!-- shared:%s -->'%n)+h.count('<!-- /shared:%s -->'%n) for n in ('assets','header','footer')])"` → `[2, 2, 2]`.

- [ ] **Paso 6: documentar en `docs/tools/README.md`**

Sumar a la tabla: `| sync_shared.py | Las piezas comunes (hojas de estilo, header, footer + off-canvas + Scroll Top + scripts) de cada página de dist/, copiadas de dist/index.html |`, y una sección:

```markdown
## Piezas compartidas entre páginas

- `dist/index.html` es la fuente del header, el footer (con off-canvas, Scroll Top y scripts) y las hojas de estilo, entre `<!-- shared:x -->` y `<!-- /shared:x -->`. Cada página nueva trae los tres pares de marcadores (pueden ir vacíos).
- `python docs/tools/sync_shared.py` los copia a las demás páginas y marca con `aria-current="page"` el enlace del menú que apunta a cada una. `--check` solo verifica (sale con 1 si hay páginas desfasadas). Pruebas: `python docs/tools/test_sync_shared.py`.
- Nunca editar esas piezas en otra página que no sea `index.html`: se pierden en la siguiente sincronización.
```

Esta tarea se commitea junto con la Tarea 2 (infraestructura), ver Tarea 2 Paso 5.

---

### Tarea 2: `sections_kit.py` multipágina

**Archivos:**
- Modificar: `docs/tools/sections_kit.py`, `docs/tools/README.md`

**Interfaces:**
- Consume: nada nuevo.
- Produce: cada `dict` de `S` acepta `page='about-us.html'` (por defecto `'index.html'`). La ficha y el `.stories.md` nombran esa página como fuente y enlazan a `../<page>#<id>`.

- [ ] **Paso 1: verificar el estado actual (la «prueba» es la idempotencia)**

Run: `python docs/tools/sections_kit.py && git diff --stat -- dist/kit docs/kit`
Esperado: `ok: 13 sections` y ningún cambio. Si hay diff, el kit ya estaba desfasado: detenerse y avisar.

- [ ] **Paso 2: leer cada Section de su página**

Reemplazar en `sections_kit.py` el bloque de lectura (líneas 2–20) por:

```python
# A diferencia de los otros niveles, el markup NO vive en este script: se extrae de la página que declara
# cada sección (clave page, por defecto dist/index.html), entre los marcadores <!-- section:<id> --> y
# <!-- /section:<id> -->. Una sección reutilizada en otra página (con un modificador) no repite la ficha:
# solo la página fuente lleva marcadores. Acá solo van los metadatos de cada ficha. El CSS es el bloque
# sections: de main.css, escrito a mano.
import re, os, textwrap, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
DIST = ROOT / 'dist'
KIT = DIST / 'kit' / 'index.html'
KITCSS = DIST / 'assets' / 'css' / 'kit.css'
STORIES = ROOT / 'docs' / 'kit'

_pages = {}
def page_html(name):
    if name not in _pages:
        _pages[name] = (DIST / name).read_text(encoding='utf-8')
    return _pages[name]

def page_of(a):
    return a.get('page', 'index.html')

def extract(sid, page):
    m = re.search(r'<!-- section:%s -->\n(.*?)\n[ \t]*<!-- /section:%s -->' % (sid, sid), page_html(page), re.S)
    assert m, 'falta el marcador de la sección %s en dist/%s' % (sid, page)
    return textwrap.dedent(m.group(1)).strip('\n')
```

Y en el render:
- `card()`: `'... Fuente: <code>dist/%s</code> (<a href="../%s#%s">ver en la página</a>).</p>' % (a['desc'], page_of(a), page_of(a), a['id'])`.
- `markups = {a['id']: extract(a['id'], page_of(a)) for a in S}`.
- Intro del nivel: `'… A diferencia de los otros niveles, su fuente es la página donde vive cada sección (<code>dist/*.html</code>): cada ficha se arma con lo que hay entre los marcadores <code>&lt;!-- section:id --&gt;</code> de esa página, así el kit y el sitio no se desfasan. …'` (resto igual).
- `.stories.md`: `'**Dónde:** markup en `dist/%s` (entre `<!-- section:%s -->`), …' % (page_of(a), a['id'], a['id'])`.

- [ ] **Paso 3: correr y comprobar que solo cambió la intro del nivel**

Run: `python docs/tools/sections_kit.py && git diff --stat -- dist/kit docs/kit`
Esperado: `ok: 13 sections`; diff de una sola línea en `dist/kit/index.html` (la intro). Los 13 `.stories.md` sin cambios.

- [ ] **Paso 4: README**

En la sección «Sections» de `docs/tools/README.md`, cambiar «La fuente es `dist/index.html`» por «La fuente es la página que declara cada sección (`page` en su `dict`, por defecto `index.html`)», y agregar: «Una sección reutilizada en otra página con un modificador no lleva marcadores allí: la ficha existente documenta el modificador en sus filas.»

- [ ] **Paso 5: checkpoint con el usuario y commit de infraestructura**

Mostrar `git diff --stat`, pedir aprobación y commitear:

```bash
git add dist/index.html docs/tools/sync_shared.py docs/tools/test_sync_shared.py docs/tools/sections_kit.py docs/tools/README.md dist/kit/index.html
git commit -m "feat(design-to-web): piezas compartidas entre páginas y kit de Sections multipágina (etapa 5)"
```

---

### Tarea 3: Átomos — Textarea, Field y `progress--accent`

**Archivos:**
- Modificar: `docs/tools/atoms_css.py` (bloques Input y Progress), `docs/tools/atoms_kit.py` (fichas Input y Progress; ficha nueva Field)
- Regenerados: `dist/assets/css/main.css` (bloque `atoms:`), `dist/kit/index.html`, `docs/kit/input.stories.md`, `progress.stories.md`, `field.stories.md`

**Interfaces:**
- Produce (clases): `textarea.input`; `.field` > `label.field__label` + `.input.field__control` (con `placeholder=" "`) + `p.field__error#<id-del-campo>-error`; `.progress--accent`.

- [ ] **Paso 1: verificar que los generadores están al día**

Run: `python docs/tools/atoms_css.py && python docs/tools/atoms_kit.py && git diff --stat -- dist docs/kit`
Esperado: sin cambios.

- [ ] **Paso 2: CSS en `atoms_css.py`**

Después de la regla `:where([data-surface='inverse'], [data-surface='brand']) .input { … }` (fin del bloque Input), agregar:

```css
/* Textarea — el mismo .input sobre <textarea>: varias líneas, alto mínimo de 96px y solo redimensionable en
   vertical (el diseño muestra el tirador). */
textarea.input {
  display: block;
  min-block-size: var(--spacing-12);
  resize: vertical;
}

/* Field — campo con label flotante (Quote Form). En reposo el <label> ocupa el lugar del placeholder, como el
   diseño; con foco o con texto sube y se achica sobre el filete, así el nombre del campo nunca desaparece
   (accessibility.md: label asociado, no solo placeholder). El campo lleva placeholder=" " para que
   :placeholder-shown distinga vacío de lleno. Debajo, el mensaje de error: vacío (y sin caja) si no hay. */
.field {
  position: relative;
  display: grid;
  gap: var(--spacing-1);
  padding-block-start: var(--spacing-5);
}
.field__label {
  position: absolute;
  inset-block-start: calc(var(--spacing-5) + var(--spacing-3));
  inset-inline-start: 0;
  color: var(--color-text-secondary);
  line-height: var(--leading-normal);
  pointer-events: none;
  transform-origin: left top;
  transition: transform var(--ease-fast);
}
.field:focus-within .field__label,
.field:has(.field__control:not(:placeholder-shown)) .field__label {
  transform: translateY(calc(-1 * (var(--spacing-5) + var(--spacing-3)))) scale(0.875);
}
.field__control::placeholder {
  color: transparent;
}
.field__error {
  color: var(--color-feedback-error-text);
  font-size: var(--text-sm);
}
.field__error:empty {
  display: none;
}
```

En el bloque Progress, después de las reglas `::-moz-progress-bar`, agregar:

```css
/* --accent: relleno ámbar (barra «Consulting» de About Us). */
.progress--accent .progress__bar {
  color: var(--color-action-secondary);
}
.progress--accent .progress__bar::-webkit-progress-value {
  background-color: var(--color-action-secondary);
}
.progress--accent .progress__bar::-moz-progress-bar {
  background-color: var(--color-action-secondary);
}
```

- [ ] **Paso 3: fichas en `atoms_kit.py`**

En la ficha `input`, sumar un bloque y una fila:

```python
    dict(label='Textarea (misma clase)', mods='narrow', html=d('''
      <label for="input-demo-textarea" class="visually-hidden">Message</label>
      <textarea class="input" id="input-demo-textarea" name="message" placeholder="Write your message"></textarea>''')),
```
fila: `('textarea.input', 'Varias líneas: alto mínimo de 96px y redimensionable solo en vertical')`. Cambiar la decisión «Solo existe el estilo de filete…» por: «Solo existe el estilo de filete: es el de los dos formularios del diseño (newsletter y Quote Form de About Us).»

En la ficha `progress`, sumar el bloque `dict(label='--accent', mods='medium', html=…)` con una barra «Consulting» 88% con clase `progress progress--accent` e `id="progress-demo-accent"`, y la fila `('.progress--accent', 'Relleno ámbar (--color-action-secondary); caso de uso: «Consulting» en About Us')`.

Ficha nueva, insertada después de `input`:

```python
A.append(dict(id='field', title='Field',
  desc='Campo con <strong>label flotante</strong>: en reposo el <code>&lt;label&gt;</code> ocupa el lugar del placeholder (como el diseño) y, con foco o con texto, sube y se achica sobre el filete. Envuelve un <a href="#input">Input</a> o un textarea y suma el mensaje de error debajo.',
  desc_md='Label flotante sobre un Input/textarea: en reposo hace de placeholder; con foco o texto sube. Suma el mensaje de error.',
  blocks=[
    dict(label='Vacío, con texto y con error', mods='narrow stack', html=d('''
      <div class="field">
        <label class="field__label" for="field-demo-name">Your name<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="text" id="field-demo-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="field-demo-name-error">
        <p class="field__error" id="field-demo-name-error"></p>
      </div>
      <div class="field">
        <label class="field__label" for="field-demo-email">Your email<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="email" id="field-demo-email" name="email" placeholder=" " autocomplete="email" required value="emma@company.com" aria-describedby="field-demo-email-error">
        <p class="field__error" id="field-demo-email-error"></p>
      </div>
      <div class="field">
        <label class="field__label" for="field-demo-phone">Phone number<span aria-hidden="true">*</span></label>
        <input class="input field__control" type="tel" id="field-demo-phone" name="phone" placeholder=" " autocomplete="tel" required aria-invalid="true" aria-describedby="field-demo-phone-error">
        <p class="field__error" id="field-demo-phone-error">This field is required.</p>
      </div>
      <div class="field">
        <label class="field__label" for="field-demo-message">Message<span aria-hidden="true">*</span></label>
        <textarea class="input field__control" id="field-demo-message" name="message" placeholder=" " required aria-describedby="field-demo-message-error"></textarea>
        <p class="field__error" id="field-demo-message-error"></p>
      </div>''')),
  ],
  rows=[('.field', 'Envoltura: reserva arriba el lugar del label subido'),
        ('label.field__label + for', 'Nombre visible del campo; flota sobre el filete con foco o con texto'),
        ('.input.field__control + placeholder=" "', 'El campo; el placeholder de un espacio habilita :placeholder-shown (es invisible)'),
        ('&lt;span aria-hidden="true"&gt;*&lt;/span&gt; + required', 'Asterisco visual; lo obligatorio lo anuncia required'),
        ('p.field__error#&lt;id&gt;-error + aria-describedby', 'Mensaje de error enlazado; vacío no ocupa lugar'),
        ('aria-invalid="true"', 'Filete en color de error (lo pone main.js al validar)')],
  tokens=['--color-text-secondary (label)', '--color-feedback-error-text', '--text-sm', '--spacing-1 / -3 / -5', '--ease-fast', 'Input (átomo)'],
  a11y='El nombre del campo es un <code>&lt;label&gt;</code> real y visible en los dos estados (cumple «label asociado, no solo placeholder» de <code>accessibility.md</code>). El error se enlaza con <code>aria-describedby</code> y el campo lleva <code>aria-invalid</code>: el lector lee nombre, estado y mensaje. El asterisco es <code>aria-hidden</code> porque <code>required</code> ya anuncia que es obligatorio. Con «reducir movimiento» el label cambia de lugar sin animar.',
  a11y_md='`<label>` real y visible en reposo y con texto; error con `aria-describedby` + `aria-invalid`; asterisco `aria-hidden` (lo anuncia `required`).',
  decisions=['Label flotante (decisión del usuario) en vez del placeholder del diseño: se ve igual en reposo y no desaparece al escribir.',
             'Usa `:has()` para saber si el campo tiene texto; el label puede ir antes del campo en el DOM.',
             'Solo sobre fondo claro: es el único caso del diseño (la card blanca del Quote Form).']))
```

Mover `field` justo después de `input` igual que se hace con `input` respecto de `switch` (línea siguiente a su `append`): `_i = [a['id'] for a in A].index('input'); A.insert(_i + 1, A.pop())`.

- [ ] **Paso 4: regenerar y revisar**

Run: `python docs/tools/atoms_css.py && python docs/tools/atoms_kit.py && git diff --stat -- dist docs/kit`
Esperado: cambian `main.css` (solo dentro de `atoms:`), `kit/index.html`, `input`, `progress` y `field` `.stories.md` (nuevo).

- [ ] **Paso 5: verificar en el navegador**

Con el servidor de QA (receta en la memoria `playwright-cli-qa-recipes`: `serve.py` sobre la raíz del proyecto, puerto 8765), abrir `/dist/kit/index.html#field` con `playwright-cli -s=about5`. Comprobar con `run-code`:
- label del campo vacío dentro del filete (su `top` > `top` del input); al enfocar, sube por encima del input;
- el campo con `value` muestra el label arriba sin foco;
- el error visible solo en el del teléfono, con color de error;
- axe sin violaciones dentro de `#field` y `#progress`.

---

### Tarea 4: Moléculas — `card-team--profile` y `card-cta--stacked`

**Archivos:**
- Modificar: `docs/tools/molecules_css.py` (bloques Card Team y Card CTA), `docs/tools/molecules_kit.py` (fichas `card-team` y `card-cta`)

**Interfaces:**
- Produce: `article.card-team.card-team--profile[.card-team--reverse]` > `img.card-team__photo` + `.card-team__info` > `h3.card-team__name` + `p.card-team__role` + `ul.card-team__socials` > `a.card-team__social`. `article.card-cta.card-cta--stacked` > `img.card-cta__photo` + `.card-cta__text` (h3 `.card-cta__title`, `p`, `a.link-arrow`).

- [ ] **Paso 1: CSS en `molecules_css.py`**

Al final del bloque Card Team (después del `@media` de `--elevated`):

```css
/* --profile — variante clara (About Us): card blanca con la foto arriba (en el flujo, sin card-photo) y,
   debajo, nombre, cargo y redes. --reverse pone el texto arriba y la foto abajo desde lg (la card central
   del diseño). Medidas a 1920: marco de 12px, nombre 24px, cargo 16px, íconos de 18px. */
.card-team--profile {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-6);
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
}
.card-team__photo {
  display: block;
  inline-size: 100%;
  block-size: auto;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-team__info {
  display: grid;
  justify-items: start;
  gap: var(--spacing-1);
  padding: 0 var(--spacing-5) var(--spacing-5);
}
.card-team--profile .card-team__name {
  text-align: start;
}
.card-team__role {
  color: var(--color-text-secondary);
}
.card-team__socials {
  display: flex;
  gap: var(--spacing-1);
  margin: var(--spacing-4) 0 0 calc(-1 * var(--spacing-2));
  padding: 0;
  list-style: none;
}
/* 32px de área táctil (WCAG 2.5.8) alrededor de un ícono de 18px */
.card-team__social {
  display: grid;
  place-items: center;
  inline-size: var(--spacing-7);
  block-size: var(--spacing-7);
  border-radius: var(--radius-full);
  color: var(--color-text-primary);
  font-size: var(--text-h6);
}
.card-team__social:hover {
  color: var(--color-action-primary-hover);
}
@media (min-width: 64rem) {
  .card-team--reverse {
    flex-direction: column-reverse;
  }
  .card-team--reverse .card-team__info {
    padding: var(--spacing-6) var(--spacing-5) 0;
  }
}
```

Al final del bloque Card CTA:

```css
/* --stacked — variante clara (FAQ de About Us): card blanca con la foto arriba (en el flujo, sin card-photo
   ni ícono) y, debajo, título, texto y «Contact Us ↗» en el color de enlace normal. */
.card-cta--stacked {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-6);
  padding: var(--spacing-3);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-sm);
}
.card-cta__photo {
  display: block;
  inline-size: 100%;
  block-size: auto;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.card-cta--stacked .card-cta__text {
  padding: 0 var(--spacing-5) var(--spacing-5);
}
```

- [ ] **Paso 2: fichas en `molecules_kit.py`**

Helper nuevo, junto a `team()`:

```python
SOCIALS = [('facebook', 'Facebook'), ('x-twitter', 'X'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn')]

def profile(img, role, name, reverse=False):
    socials = '\n'.join('          <li><a href="#card-team" class="card-team__social" aria-label="%s on %s">%s</a></li>' % (name, net, ic(icon)) for icon, net in SOCIALS)
    return d('''
      <article class="card-team card-team--profile%s">
        <img class="card-team__photo" src="%s%s" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">%s</h3>
          <p class="card-team__role">%s</p>
          <ul class="card-team__socials" role="list">
%s
          </ul>
        </div>
      </article>''') % (' card-team--reverse' if reverse else '', IMG, img, name, role, socials)
```

En la ficha `card-team`: sumar el bloque `dict(label='--profile (About Us), la central con --reverse', mods='cards', html=profile('h1-team-member-img-1.webp', 'Financial Advisor', 'Olivia Bennet') + '\n' + profile('h1-team-member-img-2.webp', 'Business Analyst', 'Emma Wilson', True) + '\n' + profile('h1-team-member-img-3.webp', 'Corporate Trainer', 'Michael Turner'))`; filas `('.card-team--profile', 'Variante clara: card blanca con marco de 12px, foto arriba, nombre, cargo y redes')`, `('.card-team--reverse', 'Con --profile: texto arriba y foto abajo desde lg')`, `('a.card-team__social + aria-label', 'Red social con área de 32px; el nombre dice persona y red («Olivia Bennet on LinkedIn»)')`; en `a11y` sumar: «En <code>--profile</code> cada red es un enlace nombrado con la persona y la red.»; en `desc`, mencionar la variante.

En la ficha `card-cta`: bloque `dict(label='--stacked (FAQ de About Us)', mods='narrow', html=d('''<article class="card-cta card-cta--stacked">…</article>'''))` con `h2-cta-img.webp` (848×740), el título «Still have questions?», el texto del diseño y `<a href="#card-cta" class="link-arrow">Contact Us <span class="icon icon--arrow-up-right" aria-hidden="true"></span></a>`; fila `('.card-cta--stacked + img.card-cta__photo', 'Variante clara: foto arriba en el flujo, sin ícono; enlace en el color normal')`.

- [ ] **Paso 3: regenerar**

Run: `python docs/tools/molecules_css.py && python docs/tools/molecules_kit.py && git diff --stat -- dist docs/kit`
Esperado: `main.css` (solo `molecules:`), kit, `card-team.stories.md`, `card-cta.stories.md`.

- [ ] **Paso 4: verificar**

`/dist/kit/index.html#card-team` a 1440 y 390 px: a 1440 la card central tiene el texto arriba; a 390 todas la foto arriba. Cada enlace social mide ≥ 24×24 (`getBoundingClientRect`). axe sin violaciones en `#card-team` y `#card-cta`.

---

### Tarea 5: Molécula Quote Form (CSS, JS y ficha)

**Archivos:**
- Modificar: `docs/tools/molecules_css.py` (bloque nuevo antes de `/* molecules:end */`), `docs/tools/molecules_kit.py` (ficha nueva), `dist/assets/js/main.js` (bloque nuevo al final, antes de `})();`)

**Interfaces:**
- Consume: Field (Tarea 3), Button (`.btn` + `.btn__icon`).
- Produce: `form.quote-form[data-quote-form][action=https://formsubmit.co/<destino>][method=post][novalidate]` con `.quote-form__title`, `.field` × 4, `button[type=submit].quote-form__submit` > `[data-submit-label]`, `.quote-form__messages` > `p.quote-form__status[role=status][data-form-status]` + `p.quote-form__alert[role=alert][data-form-alert]`. JS: `initQuoteForms()`.

- [ ] **Paso 1: escribir la prueba de navegador que falla**

Guardar en el scratchpad `qa-quote-form.js` (corre sobre la ficha del kit, que todavía no existe → falla):

```js
async page => {
  const out = {};
  // El demo en vivo del kit envía a su propia página (action="#kit-demo"): se intercepta ese POST.
  // En about-us.html (Tarea 9) el patrón pasa a 'https://formsubmit.co/**'. Nunca se envía de verdad.
  let mode = 'ok';
  await page.route('**/dist/kit/index.html', route => {
    if (route.request().method() !== 'POST') { return route.continue(); }
    return mode === 'ok'
      ? route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ success: 'true', message: 'The form was submitted successfully.' }) })
      : route.abort();
  });
  await page.goto('http://127.0.0.1:8765/dist/kit/index.html#quote-form');
  const form = page.locator('#quote-demo-form');
  out.exists = await form.count();
  // 1. Validación: enviar vacío marca los 4 campos y enfoca el primero
  await form.locator('[type=submit]').click();
  out.invalid = await form.locator('[aria-invalid=true]').count();
  out.focused = await page.evaluate(() => document.activeElement.id);
  out.firstError = await form.locator('#quote-demo-name-error').textContent();
  // 2. Corregir un campo borra su error
  await form.locator('#quote-demo-name').fill('Emma Wilson');
  out.nameInvalidAfterFix = await form.locator('#quote-demo-name').getAttribute('aria-invalid');
  // 3. Email mal formado
  await form.locator('#quote-demo-email').fill('emma@');
  await form.locator('#quote-demo-phone').fill('+1 (555) 123 4567');
  await form.locator('#quote-demo-message').fill('We need help with our pricing strategy.');
  await form.locator('[type=submit]').click();
  out.emailError = await form.locator('#quote-demo-email-error').textContent();
  // 4. Envío correcto: status anunciado y formulario limpio
  await form.locator('#quote-demo-email').fill('emma@company.com');
  await form.locator('[type=submit]').click();
  await page.waitForFunction(() => document.querySelector('#quote-demo-form [data-form-status]').textContent.length > 0);
  out.sent = await form.locator('[data-form-status]').textContent();
  out.clearedName = await form.locator('#quote-demo-name').inputValue();
  // 5. Error de red: alerta, datos conservados, botón usable de nuevo
  mode = 'fail';
  await form.locator('#quote-demo-name').fill('Emma Wilson');
  await form.locator('#quote-demo-email').fill('emma@company.com');
  await form.locator('#quote-demo-phone').fill('+1 (555) 123 4567');
  await form.locator('#quote-demo-message').fill('Second try.');
  await form.locator('[type=submit]').click();
  await page.waitForFunction(() => document.querySelector('#quote-demo-form [data-form-alert]').textContent.length > 0);
  out.failed = await form.locator('[data-form-alert]').textContent();
  out.keptName = await form.locator('#quote-demo-name').inputValue();
  out.busyAfter = await form.locator('[type=submit]').getAttribute('aria-disabled');
  return JSON.stringify(out);
}
```

Esperado al final de la tarea: `exists 1, invalid 4, focused "quote-demo-name", firstError "This field is required.", nameInvalidAfterFix null, emailError "Enter a valid email address.", sent "Thanks! …", clearedName "", failed "Your message could not be sent. …", keptName "Emma Wilson", busyAfter null`.

Run: `playwright-cli -s=about5 run-code --filename=<scratchpad>/qa-quote-form.js`
Esperado ahora: `exists 0` y error de timeout o conteos en 0.

- [ ] **Paso 2: CSS en `molecules_css.py`**

```css
/* Quote Form — card blanca con el título, cuatro Field y el botón (About Us, «Get a free Quote»). Debajo,
   las regiones de estado: enviado (role="status") y error de envío (role="alert"), vacías hasta que
   main.js las llena; vacías no ocupan lugar pero siguen en el árbol de accesibilidad (así se anuncian). */
.quote-form {
  display: grid;
  gap: var(--spacing-4);
  padding: var(--spacing-8);
  border-radius: var(--radius-lg);
  background-color: var(--color-surface-default);
  box-shadow: var(--shadow-md);
}
.quote-form__submit {
  justify-self: start;
  margin-block-start: var(--spacing-5);
}
.quote-form__submit[aria-disabled='true'] {
  cursor: progress;
}
.quote-form__messages {
  display: grid;
}
.quote-form__status:not(:empty),
.quote-form__alert:not(:empty) {
  padding: var(--spacing-3) var(--spacing-4);
  border: var(--border-width-sm) solid;
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
}
.quote-form__status:not(:empty) {
  border-color: var(--color-feedback-success-border);
  background-color: var(--color-feedback-success-bg);
  color: var(--color-feedback-success-text);
}
.quote-form__alert:not(:empty) {
  border-color: var(--color-feedback-error-border);
  background-color: var(--color-feedback-error-bg);
  color: var(--color-feedback-error-text);
}
@media (max-width: 47.99rem) {
  .quote-form {
    padding: var(--spacing-6) var(--spacing-5);
  }
}
```

- [ ] **Paso 3: JS en `main.js`** (bloque nuevo antes del cierre `})();`)

```js
  /* ===== Quote Form: envío por FormSubmit sin salir de la página ===== */
  /* Sin JS el <form> se envía normal a su action (FormSubmit muestra su página de agradecimiento). Con JS:
     validación propia (mensaje bajo cada campo, aria-invalid y foco al primer error), envío por fetch a la
     variante /ajax/ del mismo action y estados enviando / enviado / error, anunciados en las regiones
     role="status" y role="alert" del formulario. Para cambiar el destino se edita el action del HTML.
     Mientras envía, el botón queda con aria-disabled (no disabled: así no pierde el foco). */
  var FORM_MESSAGES = {
    valueMissing: 'This field is required.',
    typeMismatch: 'Enter a valid email address.',
    patternMismatch: 'Enter a valid phone number.',
    sending: 'Sending…',
    sent: 'Thanks! Your message was sent. We will get back to you soon.',
    failed: 'Your message could not be sent. Please check your connection and try again.'
  };

  function fieldError(control) {
    if (control.validity.valueMissing) { return FORM_MESSAGES.valueMissing; }
    if (control.validity.typeMismatch) { return FORM_MESSAGES.typeMismatch; }
    if (control.validity.patternMismatch) { return FORM_MESSAGES.patternMismatch; }
    return '';
  }

  // https://formsubmit.co/<destino> → https://formsubmit.co/ajax/<destino>
  function ajaxEndpoint(action) {
    var url = new URL(action, window.location.href);
    if (url.hostname === 'formsubmit.co' && url.pathname.indexOf('/ajax/') !== 0) {
      url.pathname = '/ajax' + url.pathname;
    }
    return url.href;
  }

  function initQuoteForms() {
    document.querySelectorAll('[data-quote-form]').forEach(function (form) {
      var controls = Array.prototype.slice.call(form.querySelectorAll('.field__control'));
      var status = form.querySelector('[data-form-status]');
      var alertRegion = form.querySelector('[data-form-alert]');
      var submit = form.querySelector('[type="submit"]');
      var submitLabel = submit.querySelector('[data-submit-label]');
      var idleLabel = submitLabel.textContent;
      var sending = false;

      // Escribe (o borra) el error de un campo; devuelve true si es válido
      function validate(control) {
        var message = fieldError(control);
        var error = document.getElementById(control.id + '-error');
        if (message) { control.setAttribute('aria-invalid', 'true'); } else { control.removeAttribute('aria-invalid'); }
        if (error) { error.textContent = message; }
        return !message;
      }

      // El error se revisa mientras se corrige, no antes del primer envío
      controls.forEach(function (control) {
        control.addEventListener('input', function () {
          if (control.getAttribute('aria-invalid') === 'true') { validate(control); }
        });
      });

      function setSending(value) {
        sending = value;
        if (value) { submit.setAttribute('aria-disabled', 'true'); } else { submit.removeAttribute('aria-disabled'); }
        submitLabel.textContent = value ? FORM_MESSAGES.sending : idleLabel;
      }

      form.addEventListener('submit', function (event) {
        event.preventDefault();
        if (sending) { return; }
        status.textContent = '';
        alertRegion.textContent = '';
        var invalid = controls.filter(function (control) { return !validate(control); });
        if (invalid.length) { invalid[0].focus(); return; }

        setSending(true);
        fetch(ajaxEndpoint(form.action), {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(Object.fromEntries(new FormData(form)))
        }).then(function (response) {
          return response.json().catch(function () { return {}; }).then(function (data) {
            // FormSubmit responde success "true" / "false" como texto
            if (!response.ok || String(data.success) !== 'true') { throw new Error(data.message || String(response.status)); }
          });
        }).then(function () {
          form.reset();
          status.textContent = FORM_MESSAGES.sent;
        }).catch(function () {
          alertRegion.textContent = FORM_MESSAGES.failed;
        }).then(function () {
          setSending(false);
        });
      });
    });
  }
  initQuoteForms();
```

- [ ] **Paso 4: ficha en `molecules_kit.py`**

Helper:

```python
def quote_form(fid, action, live=False, state=''):
    # state: '' | 'error' | 'sending' | 'sent' | 'failed' — solo para mostrar estados estáticos en el kit
    def field(name, label, kind, auto, value='', error=''):
        inv = ' aria-invalid="true"' if error else ''
        val = ' value="%s"' % value if value else ''
        attrs = 'id="%s-%s" name="%s" placeholder=" " required aria-describedby="%s-%s-error"%s' % (fid, name, name, fid, name, inv)
        if kind == 'textarea':
            control = '<textarea class="input field__control" %s>%s</textarea>' % (attrs, value)
        else:
            extra = ' pattern="[\\d\\s+\\(\\)\\-]{6,}"' if kind == 'tel' else ''
            control = '<input class="input field__control" type="%s" %s autocomplete="%s"%s%s>' % (kind, attrs, auto, val, extra)
        return '\n'.join(['  <div class="field">',
                          '    <label class="field__label" for="%s-%s">%s<span aria-hidden="true">*</span></label>' % (fid, name, label),
                          '    ' + control,
                          '    <p class="field__error" id="%s-%s-error">%s</p>' % (fid, name, error),
                          '  </div>'])
    err = state == 'error'
    filled = state in ('sending', 'failed')
    busy = ' aria-disabled="true"' if state == 'sending' else ''
    label = 'Sending…' if state == 'sending' else 'Get Started'
    return '\n'.join([
        '<form class="quote-form" id="%s-form"%s action="%s" method="post" novalidate aria-labelledby="%s-title">' % (fid, ' data-quote-form' if live else '', action, fid),
        '  <h3 class="quote-form__title" id="%s-title">Get a free Quote</h3>' % fid,
        '  <input type="hidden" name="_subject" value="New quote request from esonix.example">',
        '  <div hidden><label for="%s-honey">Leave this field empty</label><input type="text" id="%s-honey" name="_honey" tabindex="-1" autocomplete="off"></div>' % (fid, fid),
        field('name', 'Your name', 'text', 'name', 'Emma Wilson' if filled else '', 'This field is required.' if err else ''),
        field('email', 'Your email', 'email', 'email', 'emma@company.com' if filled else ('emma@' if err else ''), 'Enter a valid email address.' if err else ''),
        field('phone', 'Phone number', 'tel', 'tel', '+1 (555) 123 4567' if filled else ''),
        field('message', 'Message', 'textarea', '', 'We need help with our pricing strategy.' if filled else ''),
        '  <button type="submit" class="btn quote-form__submit"%s><span data-submit-label>%s</span><span class="btn__icon">%s</span></button>' % (busy, label, ic('arrow-up-right')),
        '  <div class="quote-form__messages">',
        '    <p class="quote-form__status" role="status" data-form-status>%s</p>' % ('Thanks! Your message was sent. We will get back to you soon.' if state == 'sent' else ''),
        '    <p class="quote-form__alert" role="alert" data-form-alert>%s</p>' % ('Your message could not be sent. Please check your connection and try again.' if state == 'failed' else ''),
        '  </div>',
        '</form>'])
```

Ficha:

```python
M.append(dict(id='quote-form', title='Quote Form',
  desc='Formulario «Get a free Quote» de About Us: card blanca con cuatro <a href="#field">Field</a> y el botón. Funciona sin JS (envío normal a FormSubmit); con JS, <code>main.js</code> valida, envía por <code>fetch</code> sin salir de la página y muestra los estados. El destino es el <code>action</code> del HTML.',
  desc_md='Card con 4 Field y botón. Sin JS envía normal a FormSubmit; con JS valida, envía por fetch y muestra estados. Destino = `action`.',
  blocks=[
    dict(label='En vivo: la validación es real; sin destino, el envío termina en el estado de error', mods='narrow', html=quote_form('quote-demo', '#kit-demo', live=True)),
    dict(label='Error de validación', mods='narrow', html=quote_form('quote-error', '#', state='error')),
    dict(label='Enviando', mods='narrow', html=quote_form('quote-sending', '#', state='sending')),
    dict(label='Enviado', mods='narrow', html=quote_form('quote-sent', '#', state='sent')),
    dict(label='Error de envío', mods='narrow', html=quote_form('quote-failed', '#', state='failed')),
  ],
  rows=[('form.quote-form[data-quote-form]', 'Activa el envío por fetch y la validación de main.js'),
        ('action="https://formsubmit.co/&lt;destino&gt;" method="post" novalidate', 'Destino (sin JS, envío normal); novalidate deja la validación a main.js'),
        ('input[name="_subject"] / div[hidden] &gt; input[name="_honey"]', 'Asunto del correo y trampa antibots de FormSubmit'),
        ('button[aria-disabled="true"] &gt; [data-submit-label]', 'Enviando: el botón no responde y su texto pasa a «Sending…»'),
        ('p[role="status"][data-form-status]', 'Mensaje de enviado'),
        ('p[role="alert"][data-form-alert]', 'Mensaje de error de envío; los datos se conservan')],
  tokens=['--color-surface-default', '--radius-lg / -sm', '--shadow-md', '--color-feedback-success-* / -error-*', '--spacing-3 / -4 / -5 / -6 / -8', 'Field, Input, Button (átomos)'],
  a11y='Los errores se escriben en el mensaje de cada campo (enlazado con <code>aria-describedby</code>) y el foco va al primer campo inválido. Enviado y error de envío se anuncian en regiones vivas que existen desde el inicio (vacías): <code>role="status"</code> (cortés) y <code>role="alert"</code> (inmediato). Mientras envía, el botón usa <code>aria-disabled</code> en lugar de <code>disabled</code> para no perder el foco.',
  a11y_md='Error por campo con `aria-describedby`, foco al primero inválido; `role="status"` / `role="alert"` presentes desde el inicio; `aria-disabled` mientras envía.',
  decisions=['FormSubmit (decisión del usuario): sin cuenta ni clave. El primer envío real manda a studioneyra@gmail.com un correo de activación que hay que confirmar una vez.',
             'El correo de destino queda visible en el HTML; FormSubmit permite reemplazarlo por un alias aleatorio después de activar.',
             'Solo el demo «En vivo» lleva `data-quote-form`; su `action` es la propia página del kit (`#kit-demo`), así nunca envía correos: el servidor estático rechaza el POST y se ve el estado de error. Los demás muestran estados estáticos con `action="#"`.',
             'El teléfono acepta dígitos, espacios, `+`, paréntesis y guiones (mínimo 6).']))
```

- [ ] **Paso 5: regenerar y correr la prueba**

Run: `python docs/tools/molecules_css.py && python docs/tools/molecules_kit.py`, recargar con cache-buster y `playwright-cli -s=about5 run-code --filename=<scratchpad>/qa-quote-form.js`
Esperado: los valores listados en el Paso 1. Consola sin errores. axe sin violaciones en `#quote-form`.

- [ ] **Paso 6: teclado**

Con `page.keyboard.press('Tab')` desde el título de la ficha: el orden es nombre → email → teléfono → mensaje → botón (el honeypot no recibe foco). Enter en el botón con campos vacíos deja el foco en «Your name».

---

### Tarea 6: Organismos — `carousel--fade` y `accordion--boxed`

**Archivos:**
- Modificar: `docs/tools/organisms_css.py` (bloques Carousel y Accordion), `docs/tools/organisms_kit.py` (fichas `carousel` y `accordion`), `dist/assets/js/main.js` (`initCarousel`)

**Interfaces:**
- Produce: `.carousel.carousel--fade[data-carousel][data-carousel-fade]` (una cita por vista, fundido, sin copias); `.accordion.accordion--boxed`.

- [ ] **Paso 1: CSS en `organisms_css.py`**

Al final del bloque Carousel (después de `.carousel .dots { … }`):

```css
/* --fade — un slide por vista que cambia con fundido (las citas de Client Feedback en About Us). main.js lo
   inicia con effect: 'fade' (data-carousel-fade), sin copias ni vecinos a la vista: el viewport recorta. */
.carousel--fade .carousel__viewport {
  --carousel-per-view: 1;
  overflow: clip;
}
```

Al final del bloque Accordion:

```css
/* --boxed — cada ítem en una caja con borde y 32px de separación; el abierto, en blanco (FAQ de About Us). */
.accordion--boxed {
  display: grid;
  gap: var(--spacing-7);
}
.accordion--boxed .accordion-item {
  padding-inline: var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-sm);
  transition: background-color var(--ease-base);
}
.accordion--boxed .accordion-item[open] {
  background-color: var(--color-surface-default);
}
```

- [ ] **Paso 2: modo fade en `initCarousel` (`main.js`)**

Comentario del bloque Carousel: sumar al final «data-carousel-fade: un slide por vista con fundido (effect: 'fade'); sin copias, porque el fundido no muestra vecinos.»

Cambios:

```js
  function initCarousel(carousel) {
    var viewport = carousel.querySelector('.carousel__viewport');
    var fade = carousel.hasAttribute('data-carousel-fade');
    …
    if (!fade && count > 1 && count < MIN_SLIDES) {
      // (bloque de copias sin cambios)
    }
    …
    var options = {
      loop: true,
      centeredSlides: !fade,
      initialSlide: start,
      speed: parseFloat(rootStyle.getPropertyValue('--ease-slow')) || 0, // 420 ms; 0 con reducir movimiento
      grabCursor: true,
      slidesPerView: 1,
      spaceBetween: fade ? 0 : gapSm,
      breakpointsBase: 'container',
      breakpoints: fade ? {} : breakpoints,
      watchSlidesProgress: true, // marca .swiper-slide-fully-visible (orden de Tab)
      keyboard: { enabled: true, onlyInViewport: true },
      a11y: { /* sin cambios */ }
    };
    if (fade) {
      options.effect = 'fade';
      options.fadeEffect = { crossFade: true };
    }
    var swiper = new window.Swiper(viewport, options);
```

- [ ] **Paso 3: fichas en `organisms_kit.py`**

`QUOTES` (datos) y bloque nuevo en `carousel`:

```python
QUOTES = [('David Thompson,', 'Sales Director', '“Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy, every recommendation was practical, well-researched, &amp; tailored to our goals.”'),
          ('James Anderson,', 'Entrepreneur, Brand Strategist', '“We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.”'),
          ('Isabella Harris,', 'CEO &amp; Founder', '“Working with this consulting team completely transformed our business operations.”')]

def quote_slide(name, role, text):
    return d('''
      <figure class="feedback__quote">
        <blockquote class="feedback__text"><p>%s</p></blockquote>
        <figcaption class="feedback__author"><strong>%s</strong> %s</figcaption>
      </figure>''') % (text, name, role)
```

Bloque: `dict(label='--fade: citas con fundido (About Us)', surface='inverse', html=carousel('carousel-quotes', 'Client quotes', [quote_slide(*q) for q in QUOTES], dots='Show quote', attrs=' data-carousel-fade').replace('class="carousel"', 'class="carousel carousel--fade"').replace('aria-label="Choose a story"', 'aria-label="Choose a quote"'))`. Filas: `('.carousel--fade + data-carousel-fade', 'Un slide por vista con fundido; sin copias ni vecinos')`. Las clases `feedback__*` son de la Section Feedback (Tarea 8): en el kit se ven con sus estilos porque `main.css` se carga entero.

En `accordion`: bloque `dict(label='--boxed (FAQ de About Us)', mods='narrow-wide', html=accordion().replace('class="accordion"', 'class="accordion accordion--boxed"').replace('name="faq"', 'name="faq-boxed"'))` y fila `('.accordion--boxed', 'Ítems en caja con borde y 32px de separación; el abierto en blanco')`.

- [ ] **Paso 4: regenerar y verificar**

Run: `python docs/tools/organisms_css.py && python docs/tools/organisms_kit.py`
En el kit (`#carousel`, tercer demo): click en el dot 2 → `aria-current` en el dot 2 y solo la cita 2 con `opacity: 1`; flecha derecha del teclado con el carrusel a la vista avanza; consola sin advertencias de loop de Swiper. Con `emulateMedia({ reducedMotion: 'reduce' })` el cambio es instantáneo. Los carruseles de Services y Testimonials siguen iguales (capturas antes/después en `#carousel`).

---

### Tarea 7: `about-us.html` — esqueleto, `<head>`, Page Hero y Stats `--strip`

**Archivos:**
- Crear: `dist/about-us.html`
- Modificar: `dist/index.html` (enlaces «About Us»), `dist/sitemap.xml`, `dist/assets/css/main.css` (bloque `sections:`)

**Interfaces:**
- Produce: Section `page-hero` (`section.page-hero` > `.page-hero__media` + `.container.page-hero__content` > `nav.breadcrumb` + `h1.page-hero__title`), reutilizable por las 6 páginas siguientes. Modificador `.stats--strip` + `.stats__grid`.

- [ ] **Paso 1: enlaces a la página en `index.html`**

`<li><a class="site-nav__sublink" href="#">About Us</a></li>` → `href="about-us.html"`, y lo mismo en `offcanvas__sublink`.

- [ ] **Paso 2: crear `dist/about-us.html`**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>About Us — Consulting That Delivers Results | Esonix</title>
  <meta name="description" content="Meet Esonix: a consulting team that combines industry expertise and strategic insight to help businesses make smarter decisions and achieve lasting success.">
  <link rel="canonical" href="https://esonix.example/about-us.html">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Esonix">
  <meta property="og:title" content="About Us — Consulting That Delivers Results | Esonix">
  <meta property="og:description" content="Meet Esonix: a consulting team that combines industry expertise and strategic insight to help businesses make smarter decisions and achieve lasting success.">
  <meta property="og:url" content="https://esonix.example/about-us.html">
  <meta property="og:image" content="https://esonix.example/assets/img/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Esonix — Expert guidance for future growth">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="About Us — Consulting That Delivers Results | Esonix">
  <meta name="twitter:description" content="Meet Esonix: a consulting team that combines industry expertise and strategic insight to help businesses make smarter decisions and achieve lasting success.">
  <meta name="twitter:image" content="https://esonix.example/assets/img/og-image.jpg">

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "AboutPage",
        "@id": "https://esonix.example/about-us.html#webpage",
        "url": "https://esonix.example/about-us.html",
        "name": "About Us — Consulting That Delivers Results | Esonix",
        "isPartOf": { "@id": "https://esonix.example/#website" },
        "about": { "@id": "https://esonix.example/#organization" },
        "breadcrumb": { "@id": "https://esonix.example/about-us.html#breadcrumb" }
      },
      {
        "@type": "BreadcrumbList",
        "@id": "https://esonix.example/about-us.html#breadcrumb",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://esonix.example/" },
          { "@type": "ListItem", "position": 2, "name": "About Us", "item": "https://esonix.example/about-us.html" }
        ]
      }
    ]
  }
  </script>

  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="assets/fonts/mona-sans.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/img/about-page-header-bg.webp" as="image" fetchpriority="high">
  <!-- shared:assets -->
  <!-- /shared:assets -->
</head>
<body>
  <!-- shared:header -->
  <!-- /shared:header -->

  <main id="main">
    <!-- section:page-hero -->
    <section class="page-hero" aria-labelledby="page-title">
      <div class="page-hero__media">
        <img src="assets/img/about-page-header-bg.webp" alt="" width="1920" height="750" fetchpriority="high">
      </div>
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol class="breadcrumb__list">
            <li><a href="./">Home</a></li>
            <li><span aria-current="page">About Us</span></li>
          </ol>
        </nav>
        <h1 class="page-hero__title" id="page-title">Consulting That Delivers Measurable Results</h1>
      </div>
    </section>
    <!-- /section:page-hero -->

    <section class="section stats stats--strip" aria-labelledby="facts-title">
      <div class="container stats__grid">
        <h2 class="stats__title" id="facts-title">Facts prove the outcome</h2>
        <ul class="stats__list" role="list">
          <li class="stats__item">
            <div class="stat stat--center">
              <p class="stat__value">98%</p>
              <p>Excellence in Customer Satisfaction</p>
            </div>
            <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span></span><span></span></span>
          </li>
          <li class="stats__item">
            <div class="stat stat--center">
              <p class="stat__value">12K<span class="stat__suffix">+</span></p>
              <p>Projects Successfully Finished</p>
            </div>
            <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span class="is-on"></span><span></span></span>
          </li>
          <li class="stats__item">
            <div class="stat stat--center">
              <p class="stat__value">30<span class="stat__suffix">+</span></p>
              <p>Professional Experience &amp; Growth</p>
            </div>
            <span class="stats__level" aria-hidden="true"><span class="is-on"></span><span class="is-on"></span><span class="is-on"></span></span>
          </li>
        </ul>
      </div>
    </section>
  </main>

  <!-- shared:footer -->
  <!-- /shared:footer -->
</body>
</html>
```

Run: `python docs/tools/sync_shared.py` → `actualizadas: about-us.html`. Luego `python docs/tools/sync_shared.py --check` → `ok`.

- [ ] **Paso 3: CSS (bloque `sections:` de `main.css`, después de la sección Hero)**

```css
/* Page Hero — cabecera de las páginas interiores: foto a sangre con velo, breadcrumb en píldora translúcida
   y el único <h1> abajo a la izquierda, en el .container. Reserva el alto del header fijo, como el Hero de
   la home. Medido en About Us: 750px de alto a 1920 y 420px a 480; el h1 termina ~80px sobre el borde.
   El h1 usa --text-h1 (48/36px; el diseño mide ≈ 62/41px — decisión del usuario, desvío reportado). */
.page-hero {
  position: relative;
  isolation: isolate;
  display: grid;
  align-items: end;
  min-block-size: 26.25rem; /* 420px del diseño mobile */
  overflow: clip;
  padding-block: calc(var(--header-offset) + var(--spacing-7)) var(--spacing-10);
  color: var(--color-text-inverse);
}
.page-hero__media {
  position: absolute;
  inset: 0;
  z-index: -1;
}
.page-hero__media img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  object-position: 55% 30%;
}
.page-hero__media::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    linear-gradient(to right, var(--color-overlay), transparent 70%),
    linear-gradient(to top, var(--color-overlay), transparent 60%);
}
.page-hero__content {
  display: grid;
  justify-items: start;
  gap: var(--spacing-6);
}
.page-hero__title {
  max-inline-size: 45rem; /* corta en dos líneas, como el diseño desktop */
  color: var(--color-text-inverse);
}
@media (min-width: 64rem) {
  .page-hero {
    min-block-size: 46.875rem; /* 750px del diseño desktop */
    padding-block-end: var(--spacing-11);
  }
}

/* Breadcrumb — píldora translúcida con «Home - Página». El separador es contenido generado sin texto
   alternativo; la página actual es un <span aria-current="page">. */
.breadcrumb__list {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-1);
  margin: 0;
  padding: var(--spacing-2) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-overlay-light);
  border-radius: var(--radius-full);
  background-color: var(--color-overlay-light);
  color: var(--color-text-inverse);
  font-weight: var(--weight-medium);
  list-style: none;
}
.breadcrumb__list li + li::before {
  content: '-' / '';
  margin-inline-end: var(--spacing-1);
}
.breadcrumb__list a {
  color: inherit;
  text-decoration: none;
}
.breadcrumb__list a:hover {
  text-decoration: underline;
}
```

Después del bloque Stats (antes de Testimonials):

```css
/* Stats --strip — la misma sección en franja (About Us): sin pastilla y visible en todos los breakpoints.
   Mobile: como Stats. Desde lg: el título a la izquierda (277px medidos a 1920) y las tres cifras en
   columnas separadas por filetes verticales; un filete a todo el ancho cierra la sección. */
@media (min-width: 64rem) {
  .stats--strip {
    display: block;
    padding-block: var(--spacing-8) 0;
    border-block-end: var(--border-width-sm) solid var(--color-border-default);
  }
  .stats--strip .stats__grid {
    display: grid;
    grid-template-columns: minmax(0, 17.3rem) minmax(0, 1fr);
    align-items: center;
  }
  .stats--strip .stats__title {
    margin: 0;
    font-size: var(--text-h4);
    text-align: start;
  }
  .stats--strip .stats__list {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    border-block-end: 0;
  }
  .stats--strip .stats__item {
    padding-block: 0 var(--spacing-8);
    border-block-start: 0;
    border-inline-start: var(--border-width-sm) solid var(--color-border-default);
  }
  .stats--strip .stats__item .stat {
    gap: var(--spacing-10);
  }
}
```

- [ ] **Paso 4: sitemap**

Agregar dentro de `<urlset>`:

```xml
  <url>
    <loc>https://esonix.example/about-us.html</loc>
    <lastmod>2026-10-03</lastmod>
  </url>
```
(usar la fecha real del día de construcción).

- [ ] **Paso 5: comparar contra el PNG**

Recortes en el scratchpad (`crops/about/d0.png`, `d1.png`, `m0.png`). Capturas de la página a 1920 y 480 px por tramos, con la sección en pantalla. Medir con `getBoundingClientRect`:
- hero: alto 750 / 420 (±16); x del h1 = 300 a 1920; breadcrumb encima del h1;
- stats a 1920: título en x = 300; filetes verticales; centros de las cifras (diseño: 767 / 1147 / 1527; con el contenedor de 1320 quedan ≈ 750 / 1098 / 1446: **anotar el desvío**);
- a 480: título centrado, tres cifras apiladas con filetes, sin la pastilla;
- `document.documentElement.scrollWidth === innerWidth` en 1920, 1440, 1024, 768, 390.
- El menú «Pages» del header marca «About Us» (`aria-current`) y Home no.

---

### Tarea 8: Sections About Intro, Team Profiles y Feedback (+ `section-bg`)

**Archivos:**
- Modificar: `dist/about-us.html`, `dist/index.html` (Testimonials → `section-bg`), `dist/assets/css/main.css` (bloque `sections:`)

**Interfaces:**
- Consume: Card Team `--profile` (T4), Carousel `--fade` (T6).
- Produce: Sections `about-intro`, `team-profiles`, `feedback`; patrón `.section-bg` (capa de foto desenfocada + velo) usado por Testimonials y Feedback.

- [ ] **Paso 1: extraer `.section-bg` y migrar Testimonials**

En `main.css`, antes de Testimonials:

```css
/* Section Bg — foto de fondo desenfocada bajo un velo inverso denso, para bloques oscuros
   (Testimonials, Feedback). La sección pone position: relative, isolation e overflow: clip. */
.section-bg {
  position: absolute;
  inset: calc(-2 * var(--blur-photo)); /* el borde difuminado del desenfoque queda fuera del recorte */
  z-index: -1;
}
.section-bg img {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  max-inline-size: none;
  object-fit: cover;
  filter: blur(var(--blur-photo));
}
.section-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background-color: color-mix(in srgb, var(--color-background-inverse) 85%, transparent);
}
```

Borrar las tres reglas `.testimonials__media…` y, en `index.html`, cambiar `<div class="testimonials__media">` por `<div class="section-bg">`. En `sections_kit.py`, ficha `testimonials`: la fila `('.testimonials__media', …)` pasa a `('.section-bg', 'Capa de la foto (filter: blur(--blur-photo)) con el velo en ::after; patrón compartido con Feedback')`.
Comprobación: captura de Testimonials a 1440 antes y después, idénticas.

- [ ] **Paso 2: markup (dentro de `<main>`, después de Stats)**

```html
    <!-- section:about-intro -->
    <section class="section about-intro" aria-labelledby="about-intro-title">
      <div class="container about-intro__grid">
        <div class="about-intro__lead">
          <p class="eyebrow">What We Do</p>
          <h2 class="section-title" id="about-intro-title">Unlocking Business Potential with Tailored Solutions</h2>
          <ul class="about-intro__list" role="list">
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Client-Focused Consulting</li>
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Business Performance Improvement</li>
            <li><span class="icon icon--circle-check" aria-hidden="true"></span>Innovative Business Solutions</li>
          </ul>
          <a href="#team-profiles" class="btn">
            More about us
            <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
          </a>
        </div>
        <div class="about-intro__story">
          <div class="photo-frame about-intro__photo">
            <img src="assets/img/h3-about-img.webp" alt="A consultant smiling as she shakes hands with a client" width="1200" height="1200" loading="lazy">
          </div>
          <div class="about-intro__text">
            <h3 class="about-intro__subtitle">Who we are</h3>
            <p>Our mission is to help businesses make smarter decisions &amp; achieve lasting success. By combining industry expertise, strategic insight</p>
            <p>With years of industry experience, we empower businesses to overcome challenges and unlock new opportunities. From business strategy and market analysis to operational improvement</p>
          </div>
          <hr class="divider">
          <figure class="about-intro__quote">
            <blockquote>
              <p><strong>From Vision to Success</strong> — Providing Expert Business Consulting that Delivers Real Impact. By combining industry expertise, data-driven insights, &amp; a client-focused approach</p>
            </blockquote>
            <figcaption><img src="assets/img/signature-2.png" alt="Signature of Michel Jhon" width="108" height="46" loading="lazy"></figcaption>
          </figure>
        </div>
      </div>
    </section>
    <!-- /section:about-intro -->

    <!-- section:team-profiles -->
    <section class="section team-profiles" id="team-profiles" aria-labelledby="team-profiles-title">
      <div class="container">
        <div class="section-head section-head--center">
          <div class="section-head__main">
            <p class="eyebrow eyebrow--center">Consulting Experts</p>
            <h2 class="section-title section-head__title" id="team-profiles-title">Meet Our Expert Team</h2>
          </div>
        </div>
        <div class="team-profiles__grid">
          <!-- una card por persona: Olivia Bennet / Financial Advisor / h1-team-member-img-1.webp;
               Emma Wilson / Business Analyst / img-2 con card-team--reverse;
               Michael Turner / Corporate Trainer / img-3 -->
        </div>
      </div>
    </section>
    <!-- /section:team-profiles -->
```

Cada card, exactamente como el helper `profile()` de la Tarea 4 con rutas `assets/img/` y `href="#"` en las redes (no hay perfiles todavía), por ejemplo:

```html
          <article class="card-team card-team--profile">
            <img class="card-team__photo" src="assets/img/h1-team-member-img-1.webp" alt="" width="848" height="920" loading="lazy">
            <div class="card-team__info">
              <h3 class="card-team__name">Olivia Bennet</h3>
              <p class="card-team__role">Financial Advisor</p>
              <ul class="card-team__socials" role="list">
                <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
                <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
                <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
                <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
              </ul>
            </div>
          </article>
```
(reemplazar el comentario por las tres cards).

```html
    <!-- section:feedback -->
    <section class="section feedback" aria-labelledby="feedback-title" data-surface="inverse">
      <div class="section-bg">
        <img src="assets/img/about-video-bg.webp" alt="" width="1920" height="1334" loading="lazy">
      </div>
      <div class="container">
        <div class="section-head section-head--center">
          <div class="section-head__main">
            <p class="eyebrow eyebrow--center eyebrow--inverse">Client Feedback</p>
            <h2 class="section-title section-head__title" id="feedback-title">Client Stories That Speak for Themselves</h2>
          </div>
        </div>
        <div class="carousel carousel--fade" id="carousel-quotes" data-carousel data-carousel-fade role="region" aria-roledescription="carousel" aria-label="Client quotes">
          <div class="swiper carousel__viewport">
            <div class="swiper-wrapper">
              <div class="swiper-slide carousel__slide">
                <figure class="feedback__quote">
                  <blockquote class="feedback__text"><p>“Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy, every recommendation was practical, well-researched, &amp; tailored to our goals.”</p></blockquote>
                  <figcaption class="feedback__author"><strong>David Thompson,</strong> Sales Director</figcaption>
                </figure>
              </div>
              <div class="swiper-slide carousel__slide">
                <figure class="feedback__quote">
                  <blockquote class="feedback__text"><p>“We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.”</p></blockquote>
                  <figcaption class="feedback__author"><strong>James Anderson,</strong> Entrepreneur, Brand Strategist</figcaption>
                </figure>
              </div>
              <div class="swiper-slide carousel__slide">
                <figure class="feedback__quote">
                  <blockquote class="feedback__text"><p>“Working with this consulting team completely transformed our business operations.”</p></blockquote>
                  <figcaption class="feedback__author"><strong>Isabella Harris,</strong> CEO &amp; Founder</figcaption>
                </figure>
              </div>
            </div>
          </div>
          <div class="dots dots--inverse" role="group" aria-label="Choose a quote" data-carousel-dots="Show quote"></div>
        </div>
      </div>
    </section>
    <!-- /section:feedback -->
```

Run: `python docs/tools/sync_shared.py --check` → `ok` (las secciones no tocan los bloques compartidos).

- [ ] **Paso 3: CSS (bloque `sections:`)**

```css
/* About Intro — «What We Do» de About Us. Desde lg, dos columnas medidas a 1920: a la izquierda (480px,
   arriba) eyebrow, h2, la lista con checks y el botón; a la derecha (680px) la historia: foto con marco
   5:4, «Who we are» con dos párrafos, filete y la cita con firma. Mobile: apilado en el mismo orden. */
.about-intro__grid {
  display: grid;
  gap: var(--spacing-10);
}
.about-intro__lead {
  display: grid;
  justify-items: start;
  align-content: start;
  gap: var(--spacing-5);
}
.about-intro__list {
  display: grid;
  gap: var(--spacing-4);
  margin: var(--spacing-3) 0 var(--spacing-5);
  padding: 0;
  list-style: none;
}
.about-intro__list li {
  display: flex;
  align-items: center;
  gap: var(--spacing-3);
}
.about-intro__list .icon {
  color: var(--color-text-primary);
  font-size: var(--text-h5);
}
.about-intro__story {
  display: grid;
  gap: var(--spacing-7);
}
.about-intro__photo img {
  aspect-ratio: 5 / 4;
}
.about-intro__text {
  display: grid;
  gap: var(--spacing-4);
  padding-inline: var(--spacing-5);
}
.about-intro__subtitle {
  margin-block-end: var(--spacing-3);
  font-size: var(--text-h4);
  font-weight: var(--weight-medium);
}
.about-intro__quote {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: var(--spacing-5) var(--spacing-7);
  margin: 0;
}
/* Comillas grandes decorativas, a la izquierda de la cita y la firma */
.about-intro__quote::before {
  content: '“' / '';
  grid-row: span 2;
  color: var(--color-text-primary);
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
}
.about-intro__quote blockquote {
  margin: 0;
}
.about-intro__quote strong {
  color: var(--color-text-primary);
  font-weight: var(--weight-regular);
}
.about-intro__quote img {
  display: block;
}
@media (min-width: 64rem) {
  .about-intro__grid {
    grid-template-columns: minmax(0, 30rem) minmax(0, 42.5rem);
    justify-content: space-between;
  }
}

/* Team Profiles — el equipo en About Us: Section Head centrado y tres Card Team --profile, apiladas en
   mobile y en 3 columnas (424px a 1920) desde lg, la central con --reverse. */
.team-profiles__grid {
  display: grid;
  gap: var(--spacing-6);
}
@media (min-width: 64rem) {
  .team-profiles__grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

/* Feedback — Client Feedback de About Us: bloque oscuro con Section Bg, encabezado centrado y el
   Carousel --fade de citas. Radio arriba en mobile y abajo desde lg, como cada PNG. El padding inferior
   reserva lo que la card del Quote Form (Why Trust) sube sobre el bloque (--quote-form-overlap). */
:root {
  --quote-form-overlap: var(--spacing-11); /* ≈ 78px medidos en el diseño mobile */
}
.feedback {
  position: relative;
  isolation: isolate;
  overflow: clip;
  padding-block-end: calc(var(--spacing-10) + var(--quote-form-overlap));
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}
.feedback .carousel {
  gap: var(--spacing-7);
}
.feedback__quote {
  display: grid;
  justify-items: center;
  gap: var(--spacing-6);
  max-inline-size: 58rem; /* la cita corta en 3 líneas a 1920, como el diseño */
  margin: 0 auto;
  text-align: center;
}
.feedback__quote::before {
  content: '“' / '';
  color: var(--color-text-highlight);
  font-family: var(--font-display);
  font-size: var(--text-display);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-tight);
  block-size: 0.6em; /* el glifo solo ocupa la mitad superior de su línea */
}
.feedback__text {
  margin: 0;
  color: var(--color-text-inverse);
  font-size: var(--text-h6);
  font-weight: var(--weight-medium);
  line-height: var(--leading-normal);
}
.feedback__author {
  color: var(--color-text-inverse-secondary);
}
.feedback__author strong {
  color: var(--color-text-inverse);
  font-weight: var(--weight-semibold);
}
@media (min-width: 64rem) {
  :root {
    --quote-form-overlap: var(--spacing-12); /* ≈ 98px a 1920 */
  }
  .feedback {
    padding-block-start: var(--spacing-13);
    border-radius: 0 0 var(--radius-xl) var(--radius-xl);
  }
  .feedback__text {
    font-size: var(--text-h4);
  }
}
```

- [ ] **Paso 4: comparar contra el PNG**

Recortes `d1`–`d4` y `m1`–`m4`. Medir a 1920 y 480 px:
- About Intro: columnas en x = 300 (≈ 470 de ancho) y x = 940 (680); foto 680×548; comillas ≈ 40 px de alto (si difiere más de 8 px, ajustar la regla de las comillas usando otro token de la escala y anotar);
- Team: cards de 424 px con 24 de separación; la central con texto arriba solo desde lg;
- Feedback: alto del bloque ≈ 822 px a 1920 (incluye el espacio reservado para el formulario); cita en 3 líneas a 1920 y ≈ 5 a 480; dots centrados; radio abajo en desktop y arriba en mobile.
- Click en el dot 3 → cambia a Isabella Harris; consola limpia.

---

### Tarea 9: Sections Why Trust (con Quote Form), Logos `--desktop` y FAQ `--centered`

**Archivos:**
- Modificar: `dist/about-us.html`, `dist/assets/css/main.css` (bloque `sections:`)

**Interfaces:**
- Consume: Quote Form (T5), Field (T3), `progress--accent` (T3), `card-cta--stacked` (T4), `accordion--boxed` (T6), `--quote-form-overlap` (T8).
- Produce: Section `why-trust`; modificadores `.logos--desktop`, `.faq--centered`.

- [ ] **Paso 1: markup (después de Feedback)**

```html
    <!-- section:why-trust -->
    <section class="section why-trust" aria-labelledby="why-trust-title">
      <div class="container why-trust__grid">
        <form class="quote-form why-trust__form" id="quote-form" data-quote-form action="https://formsubmit.co/studioneyra@gmail.com" method="post" novalidate aria-labelledby="quote-form-title">
          <h3 class="quote-form__title" id="quote-form-title">Get a free Quote</h3>
          <input type="hidden" name="_subject" value="New quote request from esonix.example">
          <div hidden><label for="quote-honey">Leave this field empty</label><input type="text" id="quote-honey" name="_honey" tabindex="-1" autocomplete="off"></div>
          <div class="field">
            <label class="field__label" for="quote-name">Your name<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="text" id="quote-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="quote-name-error">
            <p class="field__error" id="quote-name-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="quote-email">Your email<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="email" id="quote-email" name="email" placeholder=" " autocomplete="email" required aria-describedby="quote-email-error">
            <p class="field__error" id="quote-email-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="quote-phone">Phone number<span aria-hidden="true">*</span></label>
            <input class="input field__control" type="tel" id="quote-phone" name="phone" placeholder=" " autocomplete="tel" pattern="[\d\s+\(\)\-]{6,}" required aria-describedby="quote-phone-error">
            <p class="field__error" id="quote-phone-error"></p>
          </div>
          <div class="field">
            <label class="field__label" for="quote-message">Message<span aria-hidden="true">*</span></label>
            <textarea class="input field__control" id="quote-message" name="message" placeholder=" " required aria-describedby="quote-message-error"></textarea>
            <p class="field__error" id="quote-message-error"></p>
          </div>
          <button type="submit" class="btn quote-form__submit">
            <span data-submit-label>Get Started</span>
            <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
          </button>
          <div class="quote-form__messages">
            <p class="quote-form__status" role="status" data-form-status></p>
            <p class="quote-form__alert" role="alert" data-form-alert></p>
          </div>
        </form>
        <div class="why-trust__intro">
          <p class="eyebrow">Why Choose Us</p>
          <h2 class="section-title" id="why-trust-title">Why Businesses Trust Our Consulting</h2>
          <div class="why-trust__bars">
            <div class="progress progress--accent" style="--progress: 88">
              <div class="progress__head">
                <label for="progress-consulting">Consulting</label>
                <span aria-hidden="true">88%</span>
              </div>
              <progress class="progress__bar" id="progress-consulting" value="88" max="100">88%</progress>
            </div>
            <div class="progress" style="--progress: 75">
              <div class="progress__head">
                <label for="progress-marketing">Marketing</label>
                <span aria-hidden="true">75%</span>
              </div>
              <progress class="progress__bar" id="progress-marketing" value="75" max="100">75%</progress>
            </div>
          </div>
          <a href="#quote-form" class="link-arrow">
            Contact With Us
            <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
          </a>
        </div>
      </div>
    </section>
    <!-- /section:why-trust -->

    <section class="section logos logos--desktop" aria-labelledby="logos-title">
      <!-- mismo contenido que la sección logos de index.html (h2 oculto, 7 logos y «Join with Us ↗»),
           con «Join with Us» apuntando a #quote-form -->
    </section>

    <section class="section faq faq--centered" aria-labelledby="faq-title">
      <div class="container">
        <div class="section-head section-head--center">
          <div class="section-head__main">
            <p class="eyebrow eyebrow--center">Questions &amp; Answers</p>
            <h2 class="section-title section-head__title" id="faq-title">Your Business Consulting Questions Answered</h2>
          </div>
        </div>
        <div class="faq__grid">
          <div class="accordion accordion--boxed">
            <!-- los 4 <details class="accordion-item" name="faq"> de index.html, sin cambios (el segundo abierto) -->
          </div>
          <article class="card-cta card-cta--stacked faq__cta">
            <img class="card-cta__photo" src="assets/img/h2-cta-img.webp" alt="" width="848" height="740" loading="lazy">
            <div class="card-cta__text">
              <h3 class="card-cta__title">Still have questions?</h3>
              <p>Our results-focused strategies are designed to deliver measurable business growth</p>
              <a href="#quote-form" class="link-arrow">
                Contact Us
                <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
              </a>
            </div>
          </article>
        </div>
      </div>
    </section>
```

Copiar el contenido real de `index.html` donde lo indican los dos comentarios (y borrar los comentarios). Logos y FAQ **no** llevan marcadores `section:` acá (su ficha vive en la home).

- [ ] **Paso 2: CSS (bloque `sections:`)**

Después de Feedback:

```css
/* Why Trust — Why Choose Us de About Us. El Quote Form va primero en el DOM (en mobile se ve primero, como
   el diseño) y sube sobre el bloque Feedback con un margen negativo (--quote-form-overlap). Desde lg: el
   texto a la izquierda (600px a 1920), alineado abajo con la card; el formulario a la derecha (560px). */
.why-trust {
  padding-block-start: 0;
}
.why-trust__grid {
  display: grid;
  gap: var(--spacing-10);
}
.why-trust__form {
  margin-block-start: calc(-1 * var(--quote-form-overlap));
}
.why-trust__intro {
  display: grid;
  justify-items: start;
  gap: var(--spacing-5);
}
.why-trust__bars {
  display: grid;
  gap: var(--spacing-6);
  inline-size: 100%;
  margin-block: var(--spacing-5);
}
@media (min-width: 64rem) {
  .why-trust__grid {
    grid-template-columns: minmax(0, 37.5rem) minmax(0, 35rem);
    justify-content: space-between;
    align-items: end;
  }
  .why-trust__form {
    grid-area: 1 / 2;
  }
  .why-trust__intro {
    grid-area: 1 / 1;
  }
}
```

Después de Logos (dentro del bloque Logos, tras su `@media`):

```css
/* --desktop (About Us): la grilla también desde lg, en 4 columnas (330px a 1920). */
@media (min-width: 64rem) {
  .logos--desktop {
    display: block;
  }
  .logos--desktop .logo-grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}
```

Después de FAQ:

```css
/* FAQ --centered (About Us): encabezado centrado arriba y, debajo, el Accordion --boxed (800px a 1920) y la
   Card CTA --stacked (448px) estirada al alto del acordeón, sobre el crema más oscuro del diseño. */
.faq--centered {
  background-color: var(--color-background-subtle);
}
@media (min-width: 64rem) {
  .faq--centered .faq__grid {
    grid-template-columns: minmax(0, 50rem) minmax(0, 28rem);
  }
}
```

Comprobar el fondo: muestrear un píxel del FAQ en `crops/about/d5.png` (zona sin contenido) y compararlo con `--color-background-subtle`; si no coincide, probar `--color-background-muted` y anotar.

- [ ] **Paso 3: QA del formulario real (sin enviar)**

Correr `qa-quote-form.js` con `page.goto('…/dist/about-us.html#quote-form')` y los ids de la página (`#quote-form`, `#quote-name`…). Mismo resultado esperado que en la Tarea 5. Además, sin interceptar nada, verificar que `ajaxEndpoint` arma `https://formsubmit.co/ajax/studioneyra@gmail.com` (`page.evaluate` con un `fetch` espiado: reemplazar `window.fetch` antes del submit y leer la URL que recibe).

- [ ] **Paso 4: comparar contra el PNG**

Recortes `d3`–`d5` y `m3`–`m6`:
- el formulario empieza ≈ 98 px (1920) / ≈ 78 px (480) dentro del bloque oscuro;
- 1920: texto en x = 300, formulario en x = 1060 (560 de ancho), bordes inferiores alineados;
- 480: formulario primero, luego Why Choose;
- logos 4×2 a 1920, 2×4 a 480;
- FAQ: acordeón 800 / CTA 448 a 1920, misma altura; CTA debajo en mobile.

---

### Tarea 10: Kit de Sections, documentación, QA final y entrega

**Archivos:**
- Modificar: `docs/tools/sections_kit.py`, `docs/plan.md`, `docs/plan-etapa-5.md`
- Regenerados: `dist/kit/index.html`, `docs/kit/*.stories.md`

- [ ] **Paso 1: fichas nuevas en `sections_kit.py`**

Agregar en `S`, antes de `footer` (para que el footer quede último), cinco `dict` con `page='about-us.html'`: `page-hero`, `about-intro`, `team-profiles`, `feedback`, `why-trust`, con `desc`, `desc_md`, `mods='section'`, `rows`, `tokens`, `a11y`, `a11y_md` y `decisions` que recojan lo de las Tareas 7–9, incluyendo como decisiones:
- page-hero: «`--text-h1` (48/36 px) en lugar de los ≈ 62/41 px del diseño, decisión del usuario.»; «El breadcrumb es un `<nav aria-label="Breadcrumb">` con `<ol>`; la página actual va en `<span aria-current="page">`.»
- about-intro: «"More about us" lleva al equipo (`#team-profiles`): el diseño no dice adónde va.»; «La firma es imagen con `alt` ("Signature of Michel Jhon").»
- team-profiles: «Redes con `href="#"`: no hay perfiles todavía.»
- feedback: «Tres citas: David Thompson (diseño) y las de James Anderson e Isabella Harris de la Home (decisión del usuario).»; «Sin autoplay: no hace falta botón de pausa (WCAG 2.2.2).»
- why-trust: «El formulario va primero en el DOM: en mobile se ve primero; en desktop queda a la derecha y el orden de Tab es formulario → texto.»; «"Contact With Us" lleva al formulario.»

Y en las fichas existentes: `stats` suma la fila `('.stats--strip', 'Franja visible en todos los breakpoints, sin pastilla; desde lg, título a la izquierda y cifras en columnas con filetes (About Us)')`; `logos` suma `('.logos--desktop', 'También desde lg, en 4 columnas (About Us)')`; `faq` suma `('.faq--centered', 'Encabezado centrado, Accordion --boxed y Card CTA --stacked en columnas, fondo --color-background-subtle (About Us)')`.

Además, en `for_kit()` neutralizar el formulario para que el demo del kit nunca envíe correos reales (la ficha de la molécula ya tiene un demo en vivo sin destino real):

```python
    out = out.replace(' data-quote-form', '')
    out = re.sub(r'action="https://formsubmit\.co/[^"]*"', 'action="#"', out)
```

Run: `python docs/tools/sections_kit.py` → `ok: 18 sections`.

- [ ] **Paso 2: QA completo de la página**

En `/dist/about-us.html` a 1920, 1440, 1280, 1024, 768, 480 y 390 px:
- sin desborde horizontal (`scrollWidth`);
- axe sin violaciones (salvo los falsos positivos conocidos de contraste sobre fotos con `isolation`, a revisar a mano);
- consola limpia;
- teclado: skip link → header → breadcrumb → … → formulario (orden lógico, foco visible);
- `prefers-reduced-motion`: el carrusel cambia sin animar y el label flotante no anima;
- `python docs/tools/sync_shared.py --check` → ok;
- `python docs/tools/test_sync_shared.py` → OK;
- Home sin regresiones: capturas de Testimonials, Stats (480), Logos (480) y FAQ antes/después.

- [ ] **Paso 3: auditoría contra `docs/anti-patrones.md`**

Recorrer la lista y anotar en el reporte cada excepción (por ejemplo, los valores medidos fuera de escala: `17.3rem`, `30rem`, `42.5rem`, `58rem`, `46.875rem`, `26.25rem`, cada uno con su comentario de origen).

- [ ] **Paso 4: estado y reporte**

- `docs/plan-etapa-5.md`: en «About Us», estado «hecho, en revisión» con el reporte de desvíos (h1 48/36 vs 62/41; centros de las cifras de Stats; lo que salga de las mediciones).
- `docs/plan.md`: fila de la Etapa 5 → «⏳ En curso (About Us en revisión)».

- [ ] **Paso 5: checkpoint con el usuario y commit**

Mostrar capturas a 1920 y 390, el reporte de desvíos y `git status`. Con la aprobación:

```bash
git add dist/about-us.html dist/index.html dist/sitemap.xml dist/assets/css/main.css dist/assets/js/main.js dist/kit/index.html \
  dist/assets/img/about-page-header-bg.webp dist/assets/img/about-video-bg.webp dist/assets/img/h2-cta-img.webp dist/assets/img/h3-about-img.webp dist/assets/img/signature-2.png \
  docs/tools/atoms_css.py docs/tools/atoms_kit.py docs/tools/molecules_css.py docs/tools/molecules_kit.py docs/tools/organisms_css.py docs/tools/organisms_kit.py docs/tools/sections_kit.py \
  docs/kit docs/plan.md docs/plan-etapa-5.md
git commit -m "feat(design-to-web): página About Us (etapa 5)"
```

Recordar al usuario: el primer envío real del formulario dispara el correo de activación de FormSubmit a studioneyra@gmail.com.
