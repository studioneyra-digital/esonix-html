# Copia las piezas comunes del sitio desde dist/index.html (la única fuente) a las demás páginas de dist/:
#   shared:assets  → las hojas de estilo del <head>
#   shared:header  → skip link + header
#   shared:footer  → footer, off-canvas, Scroll Top y scripts
# En cada página marca con aria-current="page" el enlace del menú que apunta a ella (header y off-canvas)
# y quita la marca que trae la home. Correrlo después de cualquier cambio en esas piezas de index.html.
# Variantes: el marcador de apertura de una página puede llevar modificadores BEM, p. ej.
#   <!-- shared:header site-header--inner -->
# y cada uno se agrega a la clase de su componente (site-header) dentro del bloque copiado. El marcador
# de la página conserva sus modificadores; la fuente no lleva ninguno.
# Uso: python docs/tools/sync_shared.py [--check] [--dist <carpeta>]
#   --check  no escribe; sale con 1 si alguna página está desfasada (sirve antes de commitear)
import argparse, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
BLOCKS = ('assets', 'header', 'footer')
NAV_LINK = r'<a class="(?:site-nav__link|site-nav__sublink|offcanvas__link|offcanvas__sublink)" href="%s"'

def pattern(name):
    return re.compile(r'(?P<open>[ \t]*<!-- shared:%s(?P<mods>(?: [\w-]+)*) -->\n)(?P<body>.*?<!-- /shared:%s -->)' % (name, name), re.S)

def find_block(html, name, where):
    m = pattern(name).search(html)
    if not m:
        sys.exit('falta el bloque shared:%s en %s' % (name, where))
    return m

def mark_current(markup, page_name):
    markup = markup.replace(' aria-current="page"', '')
    return re.sub('(' + NAV_LINK % re.escape(page_name) + ')', r'\1 aria-current="page"', markup)

def apply_mods(markup, mods, where):
    # site-header--inner → se agrega junto a la primera clase site-header del bloque
    for mod in mods:
        base = mod.split('--')[0]
        markup, n = re.subn(r'class="%s(?=[ "])' % re.escape(base), 'class="%s %s' % (base, mod), markup, count=1)
        if not n:
            sys.exit('el modificador %s de %s no tiene un componente %s en el bloque' % (mod, where, base))
    return markup

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--dist', default=str(ROOT / 'dist'))
    args = parser.parse_args()

    dist = Path(args.dist)
    source = (dist / 'index.html').read_text(encoding='utf-8')
    shared = {name: find_block(source, name, 'index.html').group('body') for name in BLOCKS}

    stale = []
    for page in sorted(dist.glob('*.html')):
        if page.name == 'index.html':
            continue
        html = page.read_text(encoding='utf-8')
        new = html
        for name in BLOCKS:
            m = find_block(new, name, page.name)
            body = apply_mods(mark_current(shared[name], page.name), m.group('mods').split(), page.name)
            new = new[:m.start()] + m.group('open') + body + new[m.end():]
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
