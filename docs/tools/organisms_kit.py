# Genera las fichas de los organismos: dist/kit/index.html + docs/kit/<id>.stories.md
# Igual que molecules_kit.py, con dos extras por bloque: snippet=False (bloque de prueba sin código)
# y el mod «source» (kit.css lo oculta: el organismo vive fuera de flujo, p. ej. el off-canvas).
import re, os, textwrap, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
KIT = str(ROOT / 'dist' / 'kit' / 'index.html')
KITCSS = str(ROOT / 'dist' / 'assets' / 'css' / 'kit.css')
STORIES = str(ROOT / 'docs' / 'kit')
IMG = '../assets/img/'

def d(s): return textwrap.dedent(s).strip('\n')
def ic(name, extra=''): return '<span class="icon icon--%s%s" aria-hidden="true"></span>' % (name, extra)

# ------------------------------------------------------------------ contenido del menú (compartido)
# Pages es el contenido real del diseño; Home, Services y Blog son placeholder (el diseño no los muestra).
MENU = [
    ('Home', 'home', ['Home Version 01', 'Home Version 02', 'Home Version 03']),
    ('Services', 'services', ['Marketing Guidance', 'Process Optimization', 'Sales Improvement', 'Service Details']),
    ('Pages', 'pages', ['About Us', 'Portfolios', 'Portfolio Details', 'Team Members', 'Pricing Page', 'FAQ Page', 'Error 404', 'Coming Soon']),
    ('Blog', 'blog', ['Blog Grid', 'Blog Standard', 'Blog Details']),
]
SOCIALS = [('FB', 'Facebook', 'facebook'), ('TW', 'Twitter', 'x-twitter'), ('LI', 'LinkedIn', 'linkedin'), ('IG', 'Instagram', 'instagram')]

def header(sfx=''):
    # sfx: sufijo de ids para repetir el header en otra demo del kit sin ids duplicados
    items = []
    for label, key, subs in MENU:
        links = '\n'.join('    <li><a class="site-nav__sublink" href="#site-header">%s</a></li>' % s for s in subs)
        items.append('\n'.join([
            '<li class="site-nav__item">',
            '  <button type="button" class="site-nav__link site-nav__trigger" aria-expanded="false" aria-controls="submenu-%s%s">' % (key, sfx),
            '    %s' % label,
            '    %s' % ic('chevron-down', ' site-nav__chevron'),
            '  </button>',
            '  <ul class="site-nav__submenu" id="submenu-%s%s" data-surface="brand">' % (key, sfx),
            links,
            '  </ul>',
            '</li>']))
    items.append('<li class="site-nav__item"><a class="site-nav__link" href="#site-header">Contact</a></li>')
    socials = '\n'.join('  <li><a class="site-header__social" href="#site-header">%s<span class="visually-hidden"> %s</span></a></li>' % (a, n) for a, n, _ in SOCIALS)
    body = '\n'.join([
        '<a class="site-header__brand" href="#site-header">',
        '  <img class="brand-logo" src="%sprimary-logo.png" alt="Esonix" width="140" height="40">' % IMG,
        '</a>',
        '<nav class="site-header__nav" aria-label="Main">',
        '  <ul class="site-nav__list">',
        textwrap.indent('\n'.join(items), '    '),
        '  </ul>',
        '</nav>',
        '<ul class="site-header__socials" aria-label="Social media">',
        socials,
        '</ul>',
        '<a class="site-header__phone" href="tel:+880123456789">',
        '  <span class="site-header__phone-number">+880 (123) 456 789</span>',
        '  <span class="site-header__phone-icon">%s</span>' % ic('message-square'),
        '</a>',
        '<button type="button" class="site-header__toggle" data-offcanvas-open aria-controls="offcanvas-menu" aria-expanded="false">',
        '  Menu',
        '  %s' % ic('layout-grid'),
        '</button>'])
    return '<header class="site-header">\n  <div class="site-header__bar">\n%s\n  </div>\n</header>' % textwrap.indent(body, '    ')

def offcanvas():
    groups = []
    for label, key, subs in MENU:
        links = '\n'.join('      <li><a class="offcanvas__sublink" href="#offcanvas">%s</a></li>' % s for s in subs)
        groups.append('\n'.join([
            '<li>',
            '  <details class="offcanvas__group" name="offcanvas-nav">',
            '    <summary class="offcanvas__link">%s %s</summary>' % (label, ic('chevron-down')),
            '    <ul class="offcanvas__sub">',
            links,
            '    </ul>',
            '  </details>',
            '</li>']))
    groups.append('<li><a class="offcanvas__link" href="#offcanvas">Contact</a></li>')
    socials = '\n'.join('        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="%s">%s</a></li>' % (n, ic(i)) for _, n, i in SOCIALS if i != 'x-twitter')
    socials += '\n        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="X (Twitter)">%s</a></li>' % ic('x-twitter')
    return '\n'.join([
        '<div class="offcanvas" id="offcanvas-menu" data-offcanvas>',
        '  <div class="offcanvas__backdrop" data-offcanvas-close></div>',
        '  <div class="offcanvas__panel" role="dialog" aria-modal="true" aria-label="Menu" data-lenis-prevent>',
        '    <div class="offcanvas__head">',
        '      <a class="offcanvas__brand" href="#offcanvas">',
        '        <img class="brand-logo" src="%ssecondary-logo.png" alt="Esonix" width="140" height="40">' % IMG,
        '      </a>',
        '      <button type="button" class="offcanvas__close" data-offcanvas-close>',
        '        Close',
        '        %s' % ic('x'),
        '      </button>',
        '    </div>',
        '    <nav aria-label="Main">',
        '      <ul class="offcanvas__list">',
        textwrap.indent('\n'.join(groups), '        '),
        '      </ul>',
        '    </nav>',
        '    <div class="offcanvas__info">',
        '      <div>',
        '        <h2 class="offcanvas__title">Location</h2>',
        '        <p>Seattle (major city in the state Washington).</p>',
        '      </div>',
        '      <div>',
        '        <h2 class="offcanvas__title">Contact</h2>',
        '        <p class="offcanvas__contact">',
        '          <a href="tel:+880123456789">+880 (123) 456 789</a>',
        '          <a href="mailto:support@esonix.com">support@esonix.com</a>',
        '        </p>',
        '      </div>',
        '      <ul class="offcanvas__socials" aria-label="Social media">',
        socials,
        '      </ul>',
        '    </div>',
        '  </div>',
        '</div>'])

O = []

O.append(dict(id='site-header', title='Site Header',
  desc='Barra del sitio sobre la foto del hero: logo, menú en píldora blanca con submenús, redes en texto y teléfono con el círculo del chat. Responde al ancho de su contenedor (container query), no al del viewport: con menos de 48rem quedan el logo y <strong>Menu</strong>, que abre el <a href="#offcanvas">Off-canvas</a>; desde 48rem aparece el menú, desde 64rem el número de teléfono y desde 80rem las redes. Pasa el mouse o haz click en Home, Services, Pages o Blog para ver los submenús.',
  desc_md='Barra del sitio sobre la foto del hero: logo, menú en píldora blanca con submenús (disclosure), redes en texto y teléfono. Responde al ancho de su contenedor (container query `site-header`): < 48rem logo + «Menu» (abre el Off-canvas); ≥ 48rem menú y círculo del chat; ≥ 64rem número de teléfono; ≥ 80rem redes.',
  blocks=[dict(label='Barra completa (80rem de ancho), a escala', mods='hero hero-full', html=header()),
          dict(label='Al ancho de esta columna: achica la ventana para ver cómo se adapta', mods='hero', snippet=False, html=header('-col')),
          dict(label='Mobile (barra de menos de 48rem): logo y Menu', mods='hero hero-mobile', snippet=False, html=header('-sm'))],
  rows=[('.site-header', 'Contenedor de consulta (container: site-header); texto blanco y foco amarillo'),
        ('.site-header__bar', 'Barra en píldora con velo blanco al 10% y borde blanco al 30%; reparte los grupos con space-between'),
        ('.site-header__brand', 'Enlace del logo (primary-logo.png, sobre oscuro)'),
        ('.site-header--fixed', 'Variante fija arriba (position: fixed, z-sticky), centrada hasta --site-header-max; el margen alrededor de la barra no captura clics'),
        ('.site-header--fixed.is-scrolled', 'Lo agrega main.js al pasar el 10% del alto de la ventana: la barra pasa a fondo inverso para leerse sobre las secciones claras'),
        ('.site-header__nav', 'Contenedor &lt;nav&gt; del menú; visible desde 48rem de barra'),
        ('.site-nav__list / __item / __link', 'Píldora blanca, ítem posicionado y enlace o botón del menú'),
        ('.site-nav__trigger + aria-expanded / aria-controls', 'Botón que abre su submenú; el chevron gira con aria-expanded="true"'),
        ('.site-nav__submenu + data-surface="brand"', 'Panel petróleo bajo la píldora, con un puente invisible para el hover'),
        ('.site-nav__sublink / aria-current="page"', 'Enlace del submenú; amarillo en hover y en la página actual'),
        ('.site-header__socials / __social', 'Redes en texto («FB - TW - LI - IG»), desde 80rem de barra'),
        ('.site-header__phone / __phone-number / __phone-icon', 'Enlace tel: con el círculo amarillo; bajo 64rem de barra el número es solo para lectores'),
        ('.site-header__toggle + data-offcanvas-open', 'Botón «Menu» (bajo 48rem de barra); aria-controls apunta al id del Off-canvas')],
  tokens=['--color-overlay-light', '--color-text-inverse / -highlight / -primary', '--color-surface-default', '--color-action-primary / -secondary / -secondary-hover / -on-secondary', '--color-border-focus-inverse', '--text-body-lg / -body', '--weight-medium / -semibold', '--spacing-2 / -3 / -4 / -5 / -6 / -7 / -8 / -12 / -13', '--radius-full / -sm / -xs', '--shadow-lg', '--color-background-inverse', '--z-dropdown / -sticky', '--ease-fast / -base'],
  a11y='Home, Services, Pages y Blog no tienen página propia: son <code>&lt;button&gt;</code> con <code>aria-expanded</code> y <code>aria-controls</code> (patrón de divulgación, no <code>role="menu"</code>), se abren con Enter o Espacio y se cierran con Escape devolviendo el foco. Cerrados, los submenús quedan en <code>visibility: hidden</code> y salen del orden de tabulación. Las abreviaturas de redes completan su nombre con texto oculto («FB Facebook»: el nombre contiene lo visible, WCAG 2.5.3) y los guiones no se anuncian. El foco es amarillo sobre la foto y petróleo dentro de la píldora blanca. Para conservar el landmark <code>banner</code>, el <code>&lt;header&gt;</code> no debe quedar dentro de <code>&lt;main&gt;</code> ni de una <code>&lt;section&gt;</code>.',
  a11y_md='Los ítems con submenú son `<button>` con `aria-expanded`/`aria-controls` (divulgación, no `role="menu"`); Escape cierra y devuelve el foco. Submenús cerrados en `visibility: hidden`. Redes con nombre «FB Facebook» (WCAG 2.5.3); guiones sin anunciar. Foco amarillo sobre la foto y petróleo en la píldora. El `<header>` no va dentro de `<main>` ni de `<section>` (landmark `banner`).',
  decisions=['Submenús de Home, Services y Blog con placeholder: el diseño solo muestra el de Pages.',
             'Hover de los enlaces de la píldora en petróleo y submenú abierto con el chevron girado: el diseño no muestra el hover.',
             'Container query en vez de `@media`: la barra completa necesita ~1150px y el header no sabe en qué columna vive (con el container de Bootstrap, 1140px a 1280px de viewport, ya se desbordaba). Los umbrales son los breakpoints del theme (48/64/80rem) medidos sobre el ancho del header. Con el container de Bootstrap el menú aparece desde 992px de viewport (el plan decía `lg`, 1024px).',
             'Bajo 80rem de barra se ocultan las redes (están en el footer y en el off-canvas) y bajo 64rem el número queda solo para lectores. El diseño solo muestra 1920 y 480px.',
             'El header lleva `container-type`, que crea un contexto de apilamiento: la Section que lo superponga al hero le da su `z-index`.',
             'El círculo del chat es un adorno (confirmado por el equipo): va dentro del enlace del teléfono, que es el único elemento interactivo.',
             'Header fijo «por el momento» (decisión del equipo): variante `--fixed`. El diseño no muestra el estado con scroll; se deriva de tokens: la barra pasa a `--color-background-inverse` con `is-scrolled`, porque el texto blanco no se lee con el velo sobre las secciones crema. La demo del kit no es fija (taparía el kit): para verla, agregar la clase al header de una página. La Section reserva el espacio superior y define `scroll-padding-top` para los anclajes.',
             'Teléfono real confirmado: +880 (123) 456 789, en el header y en el off-canvas. El número de relleno del diseño (+ 123 (456) - 789) se descarta.',
             'La barra no lleva `backdrop-filter`: el velo es plano, como el badge (un filtro en el header recortaría cualquier descendiente fijo).']))

O.append(dict(id='offcanvas', title='Off-canvas',
  desc='Menú mobile: panel crema que entra desde la derecha sobre la página desenfocada, con los submenús como acordeones, Location, Contact y redes. Lo abre el botón <strong>Menu</strong> del <a href="#site-header">Site Header</a> (o cualquier botón con <code>data-offcanvas-open</code> y <code>aria-controls</code>). Abierto, el resto de la página queda <code>inert</code>.',
  desc_md='Menú mobile: panel crema desde la derecha sobre la página desenfocada; submenús como `<details>`, Location, Contact y redes. Lo abre cualquier botón con `data-offcanvas-open` y `aria-controls`; el resto de la página queda `inert`.',
  blocks=[dict(label='Probar y vista estática', snippet=False, mods='offcanvas-try', html='\n'.join([
            '<button type="button" class="btn" data-offcanvas-open aria-controls="offcanvas-menu" aria-expanded="false">',
            '  Open menu',
            '  <span class="btn__icon">%s</span>' % ic('layout-grid'),
            '</button>',
            '<div class="kit-offcanvas-preview" data-kit-clone="offcanvas-menu" data-kit-open="2"></div>'])),
          dict(label='Markup', mods='source', html=offcanvas())],
  rows=[('.offcanvas + data-offcanvas + id', 'Capa fija a pantalla completa; main.js la mueve al final de &lt;body&gt;'),
        ('.offcanvas.is-open', 'Estado abierto (lo pone main.js): panel visible y fondo desenfocado'),
        ('.offcanvas__backdrop + data-offcanvas-close', 'Fondo con velo y desenfoque; un click cierra'),
        ('.offcanvas__panel + role="dialog" aria-modal="true"', 'Panel crema que entra desde la derecha; scrollea por dentro (data-lenis-prevent)'),
        ('.offcanvas__head / __brand / __close', 'Logo (secondary-logo.png) y botón «Close» con el filete inferior'),
        ('.offcanvas__group + name', '&lt;details&gt; de cada submenú; el mismo name deja uno abierto a la vez'),
        ('.offcanvas__link', 'Ítem principal en mayúsculas (summary o enlace)'),
        ('.offcanvas__sub / __sublink', 'Lista y enlaces del submenú'),
        ('.offcanvas__info / __title / __contact', 'Location y Contact'),
        ('.offcanvas__socials', 'Icon Button --sm con el contorno fuerte del diseño')],
  tokens=['--color-background-default', '--color-overlay-light', '--blur-backdrop', '--color-text-primary / -secondary', '--color-action-primary', '--color-border-default / -strong', '--text-h4 / -h5 / -body', '--spacing-1 / -2 / -3 / -4 / -7 / -9 / -12 / -13', '--radius-sm / -xs', '--shadow-lg', '--z-modal', '--ease-fast / -base / -slow'],
  a11y='El panel es <code>role="dialog"</code> con <code>aria-modal="true"</code> y nombre «Menu». Al abrir, el resto de <code>&lt;body&gt;</code> queda <code>inert</code> (el foco no puede salir), el foco va a «Close» y el botón que lo abrió pasa a <code>aria-expanded="true"</code>; Escape, el fondo o «Close» lo cierran y devuelven el foco a ese botón. Cerrado queda en <code>visibility: hidden</code>, fuera del árbol de accesibilidad. Los submenús son <code>&lt;details&gt;</code> nativos: funcionan con teclado y sin JS. La animación usa <code>--ease-slow</code>, que vale 0 ms con «reducir movimiento».',
  a11y_md='`role="dialog"` + `aria-modal="true"`, nombre «Menu». Abierto: resto de `<body>` `inert`, foco en «Close», `aria-expanded="true"` en el botón. Escape/fondo/«Close» cierran y devuelven el foco. Cerrado: `visibility: hidden`. Submenús con `<details>` nativo. Animación con `--ease-slow` (0 ms con reduced motion).',
  decisions=['Submenús exclusivos (un `<details>` abierto a la vez, por `name`): el diseño los muestra todos cerrados.',
             'Fondo desenfocado sin oscurecer, como el diseño: nuevo token `--blur-backdrop` (6px) en `shadow.css`.',
             'Ancho del panel `clamp(16rem, 100% - 8rem, 24rem)`: deja ver una franja de página como el diseño (350 de 480 px).',
             'Se cierra solo si el botón que lo abrió deja de verse (la barra se ensanchó y apareció el menú), sin devolverle el foco.']))

# ------------------------------------------------------------------ render
def indent(txt, n):
    pad = ' ' * n
    return '\n'.join((pad + l) if l.strip() else l for l in txt.split('\n'))

def snippet(sid):
    return d('''
      <div class="kit-snippet is-collapsed">
        <div class="kit-snippet__bar">
          <button type="button" class="kit-btn" data-kit-toggle aria-expanded="false" aria-controls="%s">Ver código</button>
          <button type="button" class="kit-btn" data-kit-copy>Copiar</button>
        </div>
        <pre id="%s" tabindex="0"><code data-source="demo"></code></pre>
      </div>''' % (sid, sid))

def block(a, i, b):
    sid = 'snippet-%s-%d' % (a['id'], i)
    mods = ''.join(' kit-demo--' + m for m in b.get('mods', '').split())
    surf = ' data-surface="%s"' % b['surface'] if b.get('surface') else ''
    out = ['          <div class="kit-block">', '            <span class="kit-block__label">%s</span>' % b['label'],
           '            <div class="kit-demo%s"%s lang="en">' % (mods, surf), indent(b['html'], 14), '            </div>']
    if b.get('snippet', True):
        out.append(indent(snippet(sid), 12))
    out.append('          </div>')
    return '\n'.join(out)

def card(a, n):
    p = ['        <section class="kit-card" id="%s" aria-labelledby="%s-title">' % (a['id'], a['id']), '          <header class="kit-card__header">',
         '            <p class="kit-card__tag">Organismo · %02d</p>' % n, '            <h3 id="%s-title">%s</h3>' % (a['id'], a['title']),
         '            <p class="kit-card__desc">%s</p>' % a['desc'], '          </header>']
    p += [block(a, i, b) for i, b in enumerate(a['blocks'], 1)]
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

cards = '\n\n'.join(card(a, i) for i, a in enumerate(O, 1))
level = ('      <section class="kit-level" id="organisms" aria-labelledby="organisms-title">\n        <h2 id="organisms-title">Organismos</h2>\n'
         '        <p class="kit-level__intro">Orquestan estado y varias moléculas o átomos. Su comportamiento vive en <code>main.js</code>, un bloque comentado por organismo; se copian como markup y se configuran con atributos <code>data-*</code> y ARIA, sin fetch propio.</p>\n'
         + cards + '\n        <!-- kit:organisms-end -->\n      </section>')
nav_items = '\n'.join('            <li><a class="kit-nav__link" href="#%s"><span class="kit-nav__num">%02d</span> %s</a></li>' % (a['id'], i, a['title']) for i, a in enumerate(O, 1))
nav = ('        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-organisms">Organismos</p>\n'
       '          <ul class="kit-nav__list" aria-labelledby="nav-organisms">\n' + nav_items + '\n          </ul>\n        </div>')

page = open(KIT, encoding='utf-8').read()
pat = re.compile(r'      <section class="kit-level" id="organisms".*?(?=\n\n      <section class="kit-level" id="sections")', re.S)
assert pat.search(page)
page = pat.sub(lambda m: level, page, count=1)
if 'id="nav-organisms"' in page:
    page = re.sub(r'        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-organisms">.*?\n        </div>', lambda m: nav, page, count=1, flags=re.S)
else:
    old = '        <div class="kit-nav__group">\n          <p class="kit-nav__group-label">Organismos</p>\n          <p class="kit-nav__empty">Sin componentes aún</p>\n        </div>'
    assert page.count(old) == 1
    page = page.replace(old, nav)
open(KIT, 'w', encoding='utf-8', newline='\n').write(page)

# ------------------------------------------------------------------ kit.css
css = open(KITCSS, encoding='utf-8').read()
if '/* organisms-kit:start */' not in css:
    css = css.replace('  --kit-medium: 33rem;\n', '  --kit-medium: 33rem;\n  --kit-hero-min: 34rem;\n  --kit-phone: 30rem;\n  --kit-zoom: 0.72;\n', 1)
    add = '''
/* organisms-kit:start */
/* Demos de organismos: el header sobre la foto del hero (con alto para que entre el submenú abierto),
   el bloque fuente oculto (el off-canvas vive fuera de flujo) y la vista estática del panel. */
.kit-demo--hero {
  min-block-size: var(--kit-hero-min);
  padding: var(--spacing-5);
  border-color: transparent;
  /* El velo superior es el que pondrá la Section del hero: da al texto blanco el contraste real */
  background: linear-gradient(var(--color-overlay), transparent 50%), var(--color-background-inverse) url('../img/h1-hero-img.webp') center top / cover;
}
/* Barra completa a escala: el demo mide 80rem de contenido (el header ve 80rem en su container query)
   y zoom lo achica para que entre en la columna; si igual no entra, el bloque scrollea. */
.kit-block:has(> .kit-demo--hero-full) {
  overflow-x: auto;
  contain: inline-size; /* sin esto, los 80rem del demo ensanchan la card y la página en mobile */
}
.kit-demo--hero-full {
  box-sizing: content-box;
  inline-size: 80rem;
  zoom: var(--kit-zoom);
}
.kit-demo--hero-mobile {
  max-inline-size: var(--kit-phone);
}
.kit-demo--source {
  display: none;
}
.kit-demo--offcanvas-try {
  display: grid;
  justify-items: start;
  gap: var(--spacing-6);
}
.kit-offcanvas-preview {
  display: flex;
  justify-content: flex-end;
  inline-size: min(100%, var(--kit-phone));
  border-radius: var(--radius-md);
  overflow: hidden;
  background: var(--color-background-inverse) url('../img/h1-hero-img.webp') left top / cover;
}
.kit-offcanvas-preview .offcanvas__panel {
  position: static;
  transform: none;
}
/* organisms-kit:end */
'''
    css = css.replace('/* kit:css-end */', add + '/* kit:css-end */')
    open(KITCSS, 'w', encoding='utf-8', newline='\n').write(css)

# ------------------------------------------------------------------ stories.md
def unesc(s): return H.unescape(re.sub(r'</?(code|strong|em)>', lambda m: '`' if m.group(1) == 'code' else ('**' if m.group(1) == 'strong' else '*'), s))
os.makedirs(STORIES, exist_ok=True)
for n, a in enumerate(O, 1):
    md = ['# %s' % a['title'], '', '**Nivel:** Organismo · %02d  ' % n, '**Dónde:** `dist/assets/css/main.css` (bloque `/* %s */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#%s`' % (a['title'], a['id']), '',
          '## Descripción', '', unesc(a['desc_md']), '', '## Snippets', '']
    for b in a['blocks']:
        if not b.get('snippet', True):
            continue
        md += ['**%s**' % unesc(b['label']), '', '```html', H.unescape(b['html']), '```', '']
    md += ['## Clases y atributos', '', '| Clase o atributo | Efecto |', '|---|---|'] + ['| `%s` | %s |' % (H.unescape(s), unesc(t)) for s, t in a['rows']]
    md += ['', '## Tokens que consume', ''] + ['- `%s`' % t for t in a['tokens']]
    md += ['', '## Accesibilidad', '', unesc(a['a11y_md']), '', '## Decisiones y excepciones', ''] + ['- ' + x for x in a['decisions']] + ['']
    open(os.path.join(STORIES, a['id'] + '.stories.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(md))
print('ok:', len(O), 'organismos')
