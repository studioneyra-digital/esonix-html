# Genera las fichas de las Sections: dist/kit/index.html (nivel «Sections») + docs/kit/<id>.stories.md
# A diferencia de los otros niveles, el markup NO vive en este script: se extrae de dist/index.html, la única
# fuente, entre los marcadores <!-- section:<id> --> y <!-- /section:<id> -->. Acá solo van los metadatos de
# cada ficha (descripción, clases, tokens, accesibilidad, decisiones). El CSS es el bloque sections: de
# main.css, escrito a mano.
import re, os, textwrap, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
PAGE = ROOT / 'dist' / 'index.html'
KIT = ROOT / 'dist' / 'kit' / 'index.html'
KITCSS = ROOT / 'dist' / 'assets' / 'css' / 'kit.css'
STORIES = ROOT / 'docs' / 'kit'

page_html = PAGE.read_text(encoding='utf-8')

def extract(sid):
    m = re.search(r'<!-- section:%s -->\n(.*?)\n[ \t]*<!-- /section:%s -->' % (sid, sid), page_html, re.S)
    assert m, 'falta el marcador de la sección %s en dist/index.html' % sid
    return textwrap.dedent(m.group(1)).strip('\n')

def for_kit(markup):
    # Rutas relativas a /kit y ids con sufijo: el kit ya tiene demos con los mismos ids (p. ej. Progress)
    out = markup.replace('src="assets/', 'src="../assets/')
    ids = re.findall(r'\bid="([^"]+)"', out)
    for i in ids:
        out = re.sub(r'(\b(?:id|for|aria-labelledby|aria-controls|aria-describedby)=")%s"' % re.escape(i), r'\g<1>%s-section"' % i, out)
        out = out.replace('href="#%s"' % i, 'href="#%s-section"' % i)
    return out

S = []

S.append(dict(id='hero', title='Hero',
  desc='Foto a sangre con velo oscuro. Arriba, el texto con su filete y «Get Started»; debajo y a la derecha, la <a href="#card-hero">Card Hero</a>. Abajo, una franja con filete a todo el ancho y el único <code>&lt;h1&gt;</code> de la página: «Expert Guidance for —» + «FutureGrowth» en <code>--text-hero</code>. El espacio superior reserva el alto del <a href="#site-header">header fijo</a>.',
  desc_md='Foto a sangre con velo; texto + «Get Started»; Card Hero escalonada a la derecha; franja inferior con el `<h1>` («Expert Guidance for —» + «FutureGrowth» en `--text-hero`). Reserva el alto del header fijo.',
  mods='section',
  rows=[('section.hero + aria-labelledby', 'Sección con la foto de fondo; recorta lo que sangre'),
        ('.hero__media', 'Capa de la foto (object-fit: cover) con el velo en ::after'),
        ('.container-wide.hero__top', 'Contenedor ancho (1620px) con el texto y la card; desde lg, card en la segunda fila y segunda columna'),
        ('.hero__intro', 'Filete corto (276px), texto y botón claro'),
        ('.card-hero.hero__card', 'Card Hero: 360px en mobile, 445px desde lg'),
        ('.hero__bottom', 'Franja con filete a todo el ancho'),
        ('h1.hero__title / __kicker / __headline', 'El titular: kicker con raya y «FutureGrowth» a la derecha desde lg')],
  tokens=['--text-hero', '--text-h4 / -h6', '--weight-semibold', '--tracking-tight', '--color-overlay / -overlay-light', '--color-text-inverse / -inverse-secondary', '--header-offset', '--spacing-4 / -5 / -6 / -7 / -8 / -9 / -13', 'Button --light, Card Hero'],
  a11y='Único <code>&lt;h1&gt;</code> de la página, con las dos partes del titular en el mismo encabezado. La foto de fondo es decorativa (<code>alt=""</code>) y carga con prioridad alta (es el LCP); el velo asegura el contraste del texto blanco. «Get Started» es un enlace a la sección siguiente.',
  a11y_md='Único `<h1>`. Foto decorativa (`alt=""`), con `fetchpriority="high"` y preload (LCP); el velo da contraste al texto. «Get Started» enlaza a la sección siguiente.',
  decisions=['Contenedor ancho de 1620px (el del header), medido en el diseño: el texto arranca en x=150 a 1920.',
             'Card Hero escalonada (debajo del texto, a la derecha), como el diseño; en mobile va a la derecha con 360px.',
             'En mobile la Card Hero achica su foto a 140px y su título a 18px (`--text-h6`), que es lo que mide el diseño.',
             'El kicker anula el `letter-spacing` apretado que el `h1` trae de foundations: está pensado para el titular gigante.',
             '«Get Started» del hero lleva a What We Do: el diseño no dice adónde va.']))

S.append(dict(id='what-we-do', title='What We Do',
  desc='Eyebrow con filete y una grilla de áreas: en desktop, 3M+ con avatares y la foto grande a la izquierda; a la derecha, el título, el texto, las barras de <a href="#progress">Progress</a> con el CTA y la foto chica. En mobile el orden cambia como en el diseño (título, texto, foto chica, barras, 3M+, foto grande) sin duplicar contenido.',
  desc_md='Eyebrow + filete; grilla de áreas. Desktop: 3M+ y foto grande a la izquierda; título, texto, barras + CTA y foto chica a la derecha. Mobile: título, texto, foto chica, barras, 3M+, foto grande, sin duplicar contenido.',
  mods='section',
  rows=[('section.section.what-we-do', 'Sección con el padding vertical del theme (en mobile, 32px arriba, como el diseño)'),
        ('.what-we-do__head', 'Eyebrow y filete (Divider)'),
        ('.what-we-do__grid', 'Grilla de áreas: una columna en mobile; desde lg 5fr 4fr 3fr con 64px de separación'),
        ('.section-title', 'h2 con el tamaño de --text-h1'),
        ('.what-we-do__bars / __progress', 'Barras de Progress (con --progress) y el CTA'),
        ('.what-we-do__stat', 'Stat 3M+ y Avatar Stack, repartidos a los extremos'),
        ('.photo-frame', 'Foto con marco blanco de 8px; __img1 cuadrada, __img2 7:8')],
  tokens=['--text-h1', '--color-surface-default', '--radius-lg / -md', '--shadow-sm', '--spacing-2 / -4 / -6 / -7 / -8 / -9 / -10 / -12', 'Eyebrow, Divider, Progress, Button, Avatar Stack (átomos)', 'Stat (molécula)'],
  a11y='El orden del DOM es el de lectura (título, texto, barras, cifra, fotos); la grilla solo reacomoda la vista, así el orden de tabulación no salta. Cada barra es un <code>&lt;progress&gt;</code> con <code>&lt;label for&gt;</code>. Las fotos llevan <code>alt</code> descriptivo; los avatares son decorativos.',
  a11y_md='Orden del DOM = orden de lectura; la grilla solo reacomoda la vista. Barras con `<progress>` + `<label for>`. Fotos con `alt` descriptivo; avatares decorativos.',
  decisions=['Grilla CSS con los breakpoints del theme en vez de las columnas de Bootstrap: las proporciones del diseño (500 / 400 / 290px a 1920) no caen en 12 columnas con gutter, y el lg de Bootstrap (992px) no es el del theme (1024px).',
             'Avatar Stack del kit (avatares de los testimonios) en vez del PNG horneado `h1-about-users.png`, que trae las caras y el «+» en una sola imagen.',
             'El export mobile repite la primera barra («Operational assessment 90%»): no se replica.',
             'El h2 mide ≈50px en desktop (`--text-h1` da 48) y ≈32px en mobile (`--text-h1` da 36); se mantiene el token.',
             'El CTA lleva al footer (contacto): el diseño no dice adónde va.']))

# ------------------------------------------------------------------ render (mismo formato que los otros niveles)
def indent(txt, n):
    pad = ' ' * n
    return '\n'.join((pad + l) if l.strip() else l for l in txt.split('\n'))

def snippet(sid):
    return textwrap.dedent('''
      <div class="kit-snippet is-collapsed">
        <div class="kit-snippet__bar">
          <button type="button" class="kit-btn" data-kit-toggle aria-expanded="false" aria-controls="%s">Ver código</button>
          <button type="button" class="kit-btn" data-kit-copy>Copiar</button>
        </div>
        <pre id="%s" tabindex="0"><code data-source="demo"></code></pre>
      </div>''' % (sid, sid)).strip('\n')

def card(a, n, markup):
    mods = ''.join(' kit-demo--' + m for m in a.get('mods', '').split())
    p = ['        <section class="kit-card" id="%s" aria-labelledby="%s-title">' % (a['id'], a['id']), '          <header class="kit-card__header">',
         '            <p class="kit-card__tag">Section · %02d</p>' % n, '            <h3 id="%s-title">%s</h3>' % (a['id'], a['title']),
         '            <p class="kit-card__desc">%s Fuente: <code>dist/index.html</code> (<a href="../index.html#%s">ver en la página</a>).</p>' % (a['desc'], a['id']), '          </header>',
         '          <div class="kit-block">', '            <span class="kit-block__label">Tal como está en la página</span>',
         '            <div class="kit-demo%s" lang="en">' % mods, indent(for_kit(markup), 14), '            </div>',
         indent(snippet('snippet-%s-1' % a['id']), 12), '          </div>']
    rows = '\n'.join('                  <tr><th scope="row"><code>%s</code></th><td>%s</td></tr>' % (s, t) for s, t in a['rows'])
    p.append('''          <div class="kit-block">
            <span class="kit-block__label">Clases y atributos</span>
            <div class="kit-table-wrap" tabindex="0" role="region" aria-label="Clases y atributos de %s">
              <table class="kit-table">
                <thead><tr><th scope="col">Clase o atributo</th><th scope="col">Efecto</th></tr></thead>
                <tbody>
%s
                </tbody>
              </table>
            </div>
          </div>''' % (a['title'], rows))
    p.append('          <div class="kit-block">\n            <span class="kit-block__label">Tokens que consume</span>\n            <ul class="kit-spec">\n%s\n            </ul>\n          </div>' % '\n'.join('              <li><code>%s</code></li>' % t for t in a['tokens']))
    p.append('          <p class="kit-note"><strong>Accesibilidad:</strong> %s</p>' % a['a11y'])
    p.append('        </section>')
    return '\n'.join(p)

markups = {a['id']: extract(a['id']) for a in S}
cards = '\n\n'.join(card(a, i, markups[a['id']]) for i, a in enumerate(S, 1))
level = ('      <section class="kit-level" id="sections" aria-labelledby="sections-title">\n        <h2 id="sections-title">Sections</h2>\n'
         '        <p class="kit-level__intro">Bloques de página completa. A diferencia de los otros niveles, su fuente es <code>dist/index.html</code>: cada ficha se arma con lo que hay entre los marcadores <code>&lt;!-- section:id --&gt;</code> de la página, así el kit y la home no se desfasan. Los demos se ven con el ancho de esta columna; los breakpoints responden a la ventana.</p>\n'
         + cards + '\n        <!-- kit:sections-end -->\n      </section>')
nav_items = '\n'.join('            <li><a class="kit-nav__link" href="#%s"><span class="kit-nav__num">%02d</span> %s</a></li>' % (a['id'], i, a['title']) for i, a in enumerate(S, 1))
nav = ('        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-sections">Sections</p>\n'
       '          <ul class="kit-nav__list" aria-labelledby="nav-sections">\n' + nav_items + '\n          </ul>\n        </div>')

kit = KIT.read_text(encoding='utf-8')
pat = re.compile(r'      <section class="kit-level" id="sections".*?\n      </section>(?=\n    </main>)', re.S)
assert pat.search(kit)
kit = pat.sub(lambda m: level, kit, count=1)
if 'id="nav-sections"' in kit:
    kit = re.sub(r'        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-sections">.*?\n        </div>', lambda m: nav, kit, count=1, flags=re.S)
else:
    old = '        <div class="kit-nav__group">\n          <p class="kit-nav__group-label">Sections</p>\n          <p class="kit-nav__empty">Sin componentes aún</p>\n        </div>'
    assert kit.count(old) == 1
    kit = kit.replace(old, nav)
KIT.write_text(kit, encoding='utf-8', newline='\n')

# ------------------------------------------------------------------ kit.css (solo la primera vez)
css = KITCSS.read_text(encoding='utf-8')
if '/* sections-kit:start */' not in css:
    add = '''
/* sections-kit:start */
/* Demos de Sections: sin relleno ni borde (la sección trae los suyos) y recortadas a la columna. */
.kit-demo--section {
  padding: 0;
  overflow: clip;
  background-color: var(--color-background-default);
}
/* sections-kit:end */
'''
    css = css.replace('/* kit:css-end */', add + '/* kit:css-end */')
    KITCSS.write_text(css, encoding='utf-8', newline='\n')

# ------------------------------------------------------------------ stories.md
def unesc(s): return H.unescape(re.sub(r'</?(code|strong|em)>', lambda m: '`' if m.group(1) == 'code' else ('**' if m.group(1) == 'strong' else '*'), re.sub(r'<a [^>]*>|</a>', '', s)))
os.makedirs(STORIES, exist_ok=True)
for n, a in enumerate(S, 1):
    md = ['# %s' % a['title'], '', '**Nivel:** Section · %02d  ' % n,
          '**Dónde:** markup en `dist/index.html` (entre `<!-- section:%s -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#%s`' % (a['id'], a['id']), '',
          '## Descripción', '', unesc(a['desc_md']), '', '## Snippet', '', '```html', markups[a['id']], '```', '',
          '## Clases y atributos', '', '| Clase o atributo | Efecto |', '|---|---|'] + ['| `%s` | %s |' % (H.unescape(s), unesc(t)) for s, t in a['rows']]
    md += ['', '## Tokens que consume', ''] + ['- `%s`' % t for t in a['tokens']]
    md += ['', '## Accesibilidad', '', unesc(a['a11y_md']), '', '## Decisiones y excepciones', ''] + ['- ' + x for x in a['decisions']] + ['']
    (STORIES / (a['id'] + '.stories.md')).write_text('\n'.join(md), encoding='utf-8', newline='\n')
print('ok:', len(S), 'sections')
