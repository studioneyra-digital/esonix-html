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

# ------------------------------------------------------------------ Grupo B: piezas de los demos
# Services: los tres primeros textos son del diseño; Financial Planning y Brand Strategy, placeholder
# (el diseño los muestra cortados en los costados).
SERVICES = [
    ('Marketing Guidance', 'target', 'h1-service-img-2.webp', 'Through expert insights and strategic planning, marketing guidance enables businesses to understand customer.', False),
    ('Process Optimization', 'trending-up', 'h1-service-img-3.webp', 'By analyzing existing operations and implementing effective improvements, process optimization helps business.', True),
    ('Sales Improvement', 'chart-pie', 'h1-service-img-4.webp', 'We support businesses in improving sales performance through training, strategy development.', False),
    ('Financial Planning', 'gem', 'h1-service-img-5.webp', 'Our advisors build budgets, forecasts and funding plans that keep every decision tied to your numbers.', False),
    ('Brand Strategy', 'lightbulb', 'h1-service-img-1.webp', 'We help companies define a clear position and a message that strengthens their market presence.', False),
]
# Testimonials: James, Isabella y David son del diseño; Jonathan aparece cortado (cita completada) y los
# dos últimos son placeholder. Los tres en video usan el único video entregado.
VIDEO_ID = 'RqueNBILfVU'
TESTIMONIALS = [
    ('text', 'h1-testimonial-thumb-img-1.webp', 'James Anderson', 'Entrepreneur, Brand Strategist', 'We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.'),
    ('video', 'h1-testimonial-large-img-2.webp', 'Isabella Harris', 'CEO &amp; Founder', 'Working with this consulting team completely transformed our business operations.'),
    ('text', 'h1-testimonial-thumb-img-2.webp', 'David Thompson', 'Sales Director, HR Consultant', 'Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy.'),
    ('video', 'h1-testimonial-large-img-3.webp', 'Jonathan Walker', 'Operations Manager', 'Their business insights and personalized solutions had a real impact on our growth.'),
    ('text', 'h1-testimonial-thumb-img-3.webp', 'Sophia Martinez', 'Marketing Director', 'From the first workshop, the team understood our goals and turned them into a plan we could actually execute.'),
    ('video', 'h1-testimonial-large-img-1.webp', 'Michael Brooks', 'Founder, Brooks &amp; Co.', 'They stayed committed to every milestone and helped us improve how the whole company works.'),
]
FAQ = [
    (False, 'How can consulting help my business grow?', 'Consulting brings an outside view, proven methods and focused support, so you can find opportunities and act on them faster.'),
    (True, 'What industries do you specialize in?', 'Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.'),
    (False, 'What services do business consultants provide?', 'We offer strategy, process optimization, sales improvement and financial advisory.'),
    (False, 'Can you help improve team productivity?', 'Yes. We review how work moves between people and tools, then set up routines and metrics that remove bottlenecks.'),
]

def service_card(title, icon, img, text, brand):
    return '\n'.join([
        '<article class="card-service"%s>' % (' data-surface="brand"' if brand else ''),
        '  <img class="card-service__media" src="%s%s" alt="" width="1500" height="900" loading="lazy">' % (IMG, img),
        '  <div class="card-service__body">',
        '    <div class="card-service__head">',
        '      %s' % ic(icon, ' card-service__icon'),
        '      <h3 class="card-service__title">%s</h3>' % title,
        '    </div>',
        '    <p>%s</p>' % text,
        '  </div>',
        '</article>'])

def testimonial_card(kind, img, name, role, quote):
    plain = H.unescape(name)
    if kind == 'text':
        return '\n'.join([
            '<figure class="card-testimonial" data-surface="brand">',
            '  <blockquote class="card-testimonial__quote">',
            '    <p>“%s”</p>' % quote,
            '  </blockquote>',
            '  <figcaption class="card-testimonial__footer">',
            '    <hr class="divider divider--inverse">',
            '    <p class="card-testimonial__author">',
            '      <img class="avatar avatar--portrait" src="%s%s" alt="" width="80" height="80" loading="lazy">' % (IMG, img),
            '      <span><span class="card-testimonial__name">%s,</span> %s</span>' % (name, role),
            '    </p>',
            '  </figcaption>',
            '</figure>'])
    return '\n'.join([
        '<figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">',
        '  <img class="card-photo__img" src="%s%s" alt="" width="1048" height="920" loading="lazy">' % (IMG, img),
        '  <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from %s" aria-haspopup="dialog" data-video-id="%s" data-video-title="Video testimonial from %s">%s</button>' % (plain, VIDEO_ID, plain, ic('play')),
        '  <div class="card-testimonial__body">',
        '    <figcaption class="card-testimonial__footer">',
        '      <p class="card-testimonial__author"><span><span class="card-testimonial__name">%s,</span> %s</span></p>' % (name, role),
        '      <hr class="divider divider--inverse">',
        '    </figcaption>',
        '    <blockquote class="card-testimonial__quote">',
        '      <p>“%s”</p>' % quote,
        '    </blockquote>',
        '  </div>',
        '</figure>'])

def carousel(cid, label, slides, dots=None, attrs=''):
    items = '\n'.join('\n'.join(['    <div class="swiper-slide carousel__slide">', textwrap.indent(s, '      '), '    </div>']) for s in slides)
    out = ['<div class="carousel" id="%s" data-carousel%s role="region" aria-roledescription="carousel" aria-label="%s">' % (cid, attrs, label),
           '  <div class="swiper carousel__viewport">',
           '    <div class="swiper-wrapper">',
           textwrap.indent(items, '  '),
           '    </div>',
           '  </div>']
    if dots:
        out.append('  <div class="dots dots--inverse" role="group" aria-label="Choose a story" data-carousel-dots="%s"></div>' % dots)
    out.append('</div>')
    return '\n'.join(out)

def arrows(cid, noun):
    return '\n'.join([
        '<div class="carousel__arrows">',
        '  <button type="button" class="icon-btn" data-carousel-prev aria-controls="%s" aria-label="Previous %s">%s</button>' % (cid, noun, ic('arrow-left')),
        '  <button type="button" class="icon-btn" data-carousel-next aria-controls="%s" aria-label="Next %s">%s</button>' % (cid, noun, ic('arrow-right')),
        '</div>'])

def accordion():
    items = []
    for open_, q, a in FAQ:
        items.append('\n'.join([
            '<details class="accordion-item" name="faq"%s>' % (' open' if open_ else ''),
            '  <summary class="accordion-item__summary">',
            '    <span class="accordion-item__mark" aria-hidden="true">?</span>',
            '    <span class="accordion-item__question">%s</span>' % q,
            '    <span class="accordion-item__toggle" aria-hidden="true">%s%s</span>' % (ic('plus'), ic('minus')),
            '  </summary>',
            '  <div class="accordion-item__panel">',
            '    <p>%s</p>' % a,
            '  </div>',
            '</details>']))
    return '<div class="accordion">\n%s\n</div>' % textwrap.indent('\n'.join(items), '  ')

def video_modal():
    return '\n'.join([
        '<dialog class="video-modal" id="video-dialog" data-video-modal data-surface="inverse" aria-labelledby="video-dialog-title">',
        '  <div class="video-modal__head">',
        '    <h2 class="video-modal__title" id="video-dialog-title">Video</h2>',
        '    <button type="button" class="icon-btn icon-btn--glass icon-btn--sm" data-video-close aria-label="Close video">%s</button>' % ic('x'),
        '  </div>',
        '  <div class="video-modal__frame"></div>',
        '</dialog>'])

O.append(dict(id='carousel', title='Carousel',
  desc='Base de Swiper para los carruseles de la home: loop con el slide activo <strong>centrado</strong>, arrastre con mouse y táctil, teclado (flechas del teclado con el carrusel a la vista) y 1, 2 o 3 slides según el ancho del carrusel (48 y 64rem). Los slides vecinos sangran fuera del carrusel hasta el borde, como el diseño; en la página los recorta la Section. Services usa flechas (pueden ir en el encabezado: se vinculan por <code>aria-controls</code>) y destaca el slide activo (<code>data-carousel-highlight</code>); Testimonials usa dots, que genera <code>main.js</code>. Los testimonios en video abren el <a href="#video-modal">Video Modal</a>.',
  desc_md='Base de Swiper (loop con el activo centrado, arrastre, teclado) con 1/2/3 slides según el ancho del carrusel (48 y 64rem, container). Los vecinos sangran fuera; la Section recorta con `overflow-x: clip`. Flechas vinculadas por `aria-controls` (en cualquier lugar) o dots generados por `main.js`. `data-carousel-highlight` destaca el slide activo; `data-carousel-start` / `-start-wide` eligen el inicial.',
  blocks=[dict(label='Services: flechas y slide activo destacado', mods='bleed bleed-arrows', html=arrows('carousel-services', 'service') + '\n' + carousel('carousel-services', 'Services', [service_card(*s) for s in SERVICES], attrs=' data-carousel-highlight data-carousel-start="0" data-carousel-start-wide="1"')),
          dict(label='Testimonials: dots, sobre fondo oscuro', mods='bleed', surface='inverse', html=carousel('carousel-testimonials', 'Client stories', [testimonial_card(*t) for t in TESTIMONIALS], dots='Show story', attrs=' data-carousel-start="2"'))],
  rows=[('.carousel + data-carousel + id', 'Contenedor (container: carousel); main.js lo inicia al acercarse al viewport'),
        ('role="region" aria-roledescription="carousel" aria-label', 'Región con nombre propio («Services», «Client stories»)'),
        ('.swiper.carousel__viewport / .swiper-wrapper', 'Estructura de Swiper; el viewport deja ver los slides vecinos'),
        ('.swiper-slide.carousel__slide', 'Un slide; iguala la altura de las cards'),
        ('.carousel__arrows', 'Fila de flechas (Icon Button); puede vivir fuera del carrusel'),
        ('data-carousel-prev / data-carousel-next + aria-controls', 'Flechas: aria-controls apunta al id del carrusel'),
        ('.dots + data-carousel-dots="Show story"', 'Contenedor de los dots: main.js crea un botón por slide original con ese prefijo de nombre'),
        ('data-carousel-start="2"', 'Slide inicial (índice desde 0; por defecto 0)'),
        ('data-carousel-start-wide="1"', 'Slide inicial cuando el carrusel mide 64rem o más (3 por vista); si falta, vale data-carousel-start'),
        ('data-carousel-highlight', 'La card del slide activo recibe data-surface="brand" y las demás lo pierden; el markup trae destacada la inicial (estado sin JS)')],
  tokens=['--spacing-5 / -6 (separación)', '--spacing-9', '--ease-slow (velocidad)', 'Icon Button y Pagination Dots (átomos)', 'Card Service y Card Testimonial (moléculas)'],
  a11y='La región tiene <code>aria-roledescription="carousel"</code> y nombre; cada slide es un <code>role="group"</code> «slide» con nombre «3 of 6» (rol del módulo a11y de Swiper; el nombre lo pone <code>main.js</code> sin contar las copias del loop, que van con <code>aria-hidden</code> e <code>inert</code>; Swiper además anuncia el cambio con una región <code>aria-live="polite"</code>). Flechas y dots son <code>&lt;button&gt;</code> con nombre; el dot actual lleva <code>aria-current="true"</code>. Con el foco en un slide que no se ve, Swiper lo trae a la vista. No hay autoplay. La velocidad sale de <code>--ease-slow</code>, que vale 0 con «reducir movimiento». Sin JS, los slides quedan en fila con scroll horizontal nativo.',
  a11y_md='Región con `aria-roledescription="carousel"` y nombre; slides `role="group"` «N of M» (a11y de Swiper, `aria-live="polite"`). Flechas y dots son `<button>`; dot actual con `aria-current`. Sin autoplay; velocidad `--ease-slow` (0 con reduced motion). Sin JS: fila con scroll nativo.',
  decisions=['Slides por vista según el ancho del carrusel (`breakpointsBase: container`), igual que el header: con el container de Bootstrap, 3 slides desde 1200px de viewport y 2 entre 768 y 1199px. El diseño solo muestra 1920 (3) y 480px (1). En la columna del kit a 1440px se ven 2.',
             'Slide activo centrado y destacado (decisión del usuario en la Etapa 4; reemplaza a la card destacada fija): en desktop el diseño muestra la oscura al centro con dos enteras y dos parciales a los costados; en mobile, la oscura es la única visible. Services arranca en Marketing Guidance en mobile y en Process Optimization con 3 por vista, como el diseño; Testimonials, en el tercer slide (el diseño marca el tercer dot).',
             'Copias: con el activo centrado se ven a la vez hasta 5 slides y el loop de Swiper necesita uno de repuesto; con 5 slides, al avanzar quedaba un hueco en el costado derecho que se llenaba de golpe al final de la transición. Si hay menos de 6, `main.js` duplica la tanda completa (no un solo slide, para no repetir uno dentro de la misma vuelta); las copias van con `aria-hidden` e `inert`, y el nombre «N of M», los dots y el destacado cuentan solo los originales. Reemplaza al truco anterior (`loopAdditionalSlides` + `loopFix`).',
             'Testimonios: Jonathan Walker (cortado en el diseño), Sophia Martinez y Michael Brooks son placeholder, igual que dos de los cinco servicios. Los tres videos usan el único video entregado.',
             'Dots: uno por slide original (el diseño muestra 6 para 6 testimonios); el activo es el slide centrado. Con copias, un dot lleva al ejemplar más cercano de ese slide.',
             'Swiper vendorizado (11.2.10) con su CSS `swiper-bundle.min.css`; no se usan sus flechas ni su paginación, sino los átomos del theme.']))

O.append(dict(id='accordion', title='Accordion',
  desc='Grupo de <a href="#accordion-item">Accordion Items</a> para el FAQ. Que quede un solo ítem abierto lo da el mismo <code>name</code> en todos los <code>&lt;details&gt;</code>, sin JS; el grupo suma la animación de altura con <code>::details-content</code>.',
  desc_md='Grupo de Accordion Items (FAQ): un solo ítem abierto por el `name` compartido (sin JS) y animación de altura con `::details-content`.',
  blocks=[dict(label='FAQ con un ítem abierto', mods='narrow-wide', html=accordion())],
  rows=[('.accordion', 'Grupo; activa interpolate-size para animar hasta height: auto'),
        ('.accordion-item + name="faq"', 'Cada pregunta (molécula); el mismo name deja una sola abierta'),
        ('open', 'Ítem abierto al cargar (el diseño abre el segundo)')],
  tokens=['--ease-base', 'Accordion Item (molécula)'],
  a11y='Cada pregunta es un <code>&lt;summary&gt;</code> nativo: se abre con Enter o Espacio y el lector anuncia expandido o contraído. La animación usa <code>--ease-base</code>, que vale 0 con «reducir movimiento»; donde el navegador no soporta <code>::details-content</code> o <code>interpolate-size</code>, abre sin animar.',
  a11y_md='`<summary>` nativo (Enter/Espacio, estado anunciado). Animación con `--ease-base` (0 con reduced motion); sin soporte, abre sin animar.',
  decisions=['Es un organismo mínimo (el comportamiento lo da HTML nativo): existe para fijar el `name` del grupo y la animación en un solo lugar.',
             'La cuarta respuesta («Can you help improve team productivity?») es placeholder: el diseño solo muestra abierta la segunda.',
             'Las preguntas van sin el espacio antes de «?» del diseño (tipografía inglesa).']))

O.append(dict(id='video-modal', title='Video Modal',
  desc='<code>&lt;dialog&gt;</code> nativo que reproduce un video de YouTube. Lo abre cualquier botón con <code>data-video-id</code> (el play de los testimonios en video); el iframe de <code>youtube-nocookie.com</code> se crea recién en ese click y se quita al cerrar. El diseño no lo muestra: está armado con los tokens del theme.',
  desc_md='`<dialog>` nativo para YouTube. Lo abre cualquier botón con `data-video-id`; el iframe (youtube-nocookie) se crea en el click y se quita al cerrar. No está en el diseño: sale de tokens.',
  blocks=[dict(label='Probar', snippet=False, mods='row', html='\n'.join([
            '<button type="button" class="btn" aria-haspopup="dialog" data-video-id="%s" data-video-title="Video testimonial from Isabella Harris">' % VIDEO_ID,
            '  Play video',
            '  <span class="btn__icon">%s</span>' % ic('play'),
            '</button>'])),
          dict(label='Markup', mods='source', html=video_modal())],
  rows=[('dialog.video-modal + data-video-modal + data-surface="inverse"', 'El modal; main.js lo mueve al final de &lt;body&gt;'),
        ('.video-modal__head / __title', 'Barra con el título del video (nombre del diálogo) y «Close»'),
        ('data-video-close', 'Botón que cierra'),
        ('.video-modal__frame', 'Marco 16:9 donde main.js inserta el iframe'),
        ('data-video-id', 'En el botón que abre: ID del video de YouTube'),
        ('data-video-title', 'En el botón que abre: título del video (diálogo e iframe)')],
  tokens=['--color-background-inverse', '--color-overlay (fondo)', '--radius-lg', '--shadow-lg', '--spacing-3 / -4 / -5 / -6 / -8 / -13', '--text-body-lg', '--weight-medium', '--ease-base'],
  a11y='<code>showModal()</code> deja inert el resto de la página y lleva el foco a «Close»; Escape, «Close» o un click en el fondo cierran y el foco vuelve al botón que lo abrió (comportamiento nativo). El diálogo se nombra con su título visible y el iframe lleva <code>title</code>. Los botones que lo abren declaran <code>aria-haspopup="dialog"</code>. El fundido usa <code>--ease-base</code> (0 con «reducir movimiento»).',
  a11y_md='`showModal()`: resto inert, foco en «Close»; Escape/«Close»/fondo cierran y el foco vuelve al botón. Nombre = título visible; iframe con `title`; openers con `aria-haspopup="dialog"`. Fundido con `--ease-base`.',
  decisions=['El diseño no muestra el modal: fondo inverso, velo `--color-overlay` y entrada con fundido y desplazamiento corto.',
             'El iframe no se carga hasta el click (`youtube-nocookie.com`, autoplay): la página no descarga YouTube al abrirse. Lleva `referrerpolicy="strict-origin-when-cross-origin"`, porque YouTube rechaza el embed sin referrer.',
             'Ancho máximo 64rem y nunca más alto que la ventana: el ancho se limita a `(100dvh - 8rem) × 16/9`.']))

# ------------------------------------------------------------------ Grupo C: Word List, Marquee, Footer
WORDS = [
    ('word-finance', 'Finance', '01', 'Corporate Finance Management', 'h1-portfolio-img-3.webp', 1920, 1084, False),
    ('word-advisory', 'Advisory', '02', 'Advisory Services', 'h1-portfolio-img-1.webp', 1920, 1076, False),
    ('word-growth', 'Growth', '03', 'Growth Strategy Planning', 'h1-portfolio-img-2.webp', 1920, 765, True),
    ('word-strategy', 'Strategy', '04', 'Market Strategy Execution', 'h1-portfolio-img-4.webp', 1920, 1076, False),
]

def word_list():
    words = '\n'.join(
        '    <li><span class="word-list__word%s" data-word-for="%s">%s</span></li>' % (' is-active' if active else '', wid, word)
        for wid, word, _, _, _, _, _, active in WORDS)
    cards = '\n'.join('\n'.join([
        '    <article class="card-project word-list__card%s" id="%s">' % (' is-active' if active else '', wid),
        '      <img class="card-project__img" src="%s%s" alt="" width="%d" height="%d" loading="lazy">' % (IMG, img, w, h),
        '      <div class="card-project__caption">',
        '        <span class="card-project__index" aria-hidden="true">// %s</span>',
        '        <h3 class="card-project__title">%s</h3>',
        '      </div>',
        '    </article>']) % (idx, title)
        for wid, _, idx, title, img, w, h, active in WORDS)
    return '\n'.join([
        '<div class="word-list" data-word-list>',
        '  <h2 class="visually-hidden">Works</h2>',
        '  <p class="word-list__watermark" aria-hidden="true">Works</p>',
        '  <ul class="word-list__words" role="list">',
        words,
        '  </ul>',
        '  <div class="word-list__media">',
        cards,
        '  </div>',
        '</div>'])

def marquee():
    def group():
        parts = []
        for _ in range(3):
            parts.append('        <span class="marquee__text">Connect With Us</span>')
            parts.append('        <span class="marquee__text">Let\'s <span class="marquee__accent">Grow</span></span>')
        return '\n'.join(parts)
    g = group()
    return '\n'.join([
        '<div class="marquee" data-surface="inverse">',
        '  <div class="marquee__viewport" aria-hidden="true">',
        '    <div class="marquee__track">',
        '      <div class="marquee__group">',
        g,
        '      </div>',
        '      <div class="marquee__group">',
        g,
        '      </div>',
        '    </div>',
        '  </div>',
        '  <p class="visually-hidden">Connect with us. Let\'s grow.</p>',
        '  <div class="marquee__badge" aria-hidden="true">',
        '    <img class="marquee__badge-logo" src="%sprimary-logo.png" alt="" width="140" height="40">' % IMG,
        '  </div>',
        '</div>'])

UTILITY_LINKS = ['License', 'Style Guide', 'Password Protected', 'Error 404', 'Changelog']
FOLLOW_LINKS = ['Facebook', 'Twitter', 'Instagram', 'Linkedin', 'Youtube']
OFFICES = [
    ('Operations &ndash; China', "Shanghai (China's largest cities)"),
    ('Headquarters &ndash; USA', 'Seattle (major city in Washington)'),
]

def footer_list(title_id, title, items):
    links = '\n'.join('    <li><a href="#">%s</a></li>' % i for i in items)
    return '\n'.join([
        '<nav aria-labelledby="%s">' % title_id,
        '  <h3 class="site-footer__title" id="%s">%s</h3>' % (title_id, title),
        '  <ul class="site-footer__list">',
        links,
        '  </ul>',
        '</nav>'])

def site_footer():
    offices = '\n'.join('\n'.join([
        '          <div>',
        '            <p class="site-footer__office-label">%s</p>' % label,
        '            <p class="site-footer__office-city">%s</p>' % city,
        '          </div>'])
        for label, city in OFFICES)
    return '\n'.join([
        '<footer class="site-footer" data-surface="inverse">',
        '  <div class="container">',
        '    <div class="site-footer__top">',
        '      <form class="newsletter" action="#">',
        '        <label class="newsletter__title" for="footer-newsletter-email">Subscribe our newsletter to get latest updates</label>',
        '        <div class="newsletter__field">',
        '          <input class="input" type="email" id="footer-newsletter-email" name="email" placeholder="Enter your email" autocomplete="email" required>',
        '          <button type="submit" class="newsletter__submit" aria-label="Subscribe">%s</button>' % ic('send'),
        '        </div>',
        '      </form>',
        textwrap.indent(footer_list('footer-utility-title', 'Utility Page', UTILITY_LINKS), '      '),
        textwrap.indent(footer_list('footer-follow-title', 'Follow Us', FOLLOW_LINKS), '      '),
        '      <div class="site-footer__offices-col">',
        '        <h3 class="site-footer__title">Our Offices</h3>',
        '        <div class="site-footer__offices">',
        offices,
        '        </div>',
        '      </div>',
        '    </div>',
        '  </div>',
        '  <div class="site-footer__legal">',
        '    <div class="container site-footer__legal-inner">',
        '      <p>Copyright &copy; 2026 Esonix. All Rights Reserved.</p>',
        '      <p>',
        '        <a href="#">Terms &amp; Condition</a>',
        '        <span aria-hidden="true">|</span>',
        '        <a href="#">Privacy Policy</a>',
        '      </p>',
        '    </div>',
        '  </div>',
        '</footer>'])

O.append(dict(id='word-list', title='Word List',
  desc='Bloque Finance / Advisory / Growth / Strategy. Desde <code>lg</code>: cuatro palabras grandes, nítida la activa y desenfocadas las demás, con una <a href="#card-project">Card Project</a> por palabra superpuesta a la derecha; <code>main.js</code> activa la palabra y la card que cruzan el centro del viewport. Bajo <code>lg</code>, como el diseño mobile: el título «Works» gigante y tenue y las cuatro cards apiladas, sin efecto. Achica la ventana para ver la versión mobile.',
  desc_md='Bloque Finance/Advisory/Growth/Strategy. Desde `lg`: palabras grandes (nítida la activa, desenfocadas las demás) + una Card Project por palabra superpuesta; `main.js` activa la que cruza el centro del viewport (ScrollTrigger, sin pin). Bajo `lg`: «Works» gigante y tenue (decorativo) + cards apiladas, sin efecto.',
  blocks=[dict(label='Growth activa (estado inicial, como el diseño), sobre fondo oscuro', mods='narrow-wide', surface='inverse', html=word_list())],
  rows=[('.word-list + data-word-list', 'Contenedor; main.js lo inicia al acercarse al viewport'),
        ('h2.visually-hidden', 'Título real de la sección, solo para lectores (el diseño no lo muestra)'),
        ('.word-list__watermark + aria-hidden', '«Works» gigante y tenue, decorativo; solo bajo lg'),
        ('.word-list__words / __word', 'Columna de palabras (desde lg): desenfocadas con --blur-text, nítida con .is-active'),
        ('data-word-for', 'En cada palabra: id de su Card Project'),
        ('.word-list__media / __card', 'Cards superpuestas (desde lg, grid-area 1 / 1); bajo lg, apiladas'),
        ('.is-active', 'Lo pone main.js en la palabra y la card activas (el markup trae el estado inicial)')],
  tokens=['--text-display', '--weight-semibold', '--leading-tight', '--tracking-tight', '--color-text-inverse', '--color-background-muted (watermark)', '--blur-text', '--spacing-5 / -6 / -8 / -12', '--ease-slow', 'Card Project (molécula)'],
  a11y='Las palabras son contenido real y quedan en el orden de lectura (el desenfoque es solo visual). El título de la sección es un <code>&lt;h2&gt;</code> oculto; el «Works» visible en mobile es <code>aria-hidden</code> porque su gris tenue no llega a contraste AA. Con <code>prefers-reduced-motion: reduce</code>, <code>main.js</code> no inicia el ScrollTrigger y queda el estado del markup. Sin JS, bajo <code>lg</code> se ven todas las cards apiladas.',
  a11y_md='Palabras como contenido real (desenfoque solo visual). `<h2>` oculto como título; «Works» visible `aria-hidden` (gris tenue, sin AA). Con reduced motion no se inicia el ScrollTrigger. Sin JS, cards apiladas.',
  decisions=['Sin `pin`: las palabras no fijan la sección ni estiran el alto artificialmente (evita los bugs de ScrollTrigger + Lenis con pin que advierte `CLAUDE.md`); el alto de scroll lo dan las propias palabras en `--text-display`.',
             'Activación por cruce del centro del viewport (`ScrollTrigger.create` por palabra, `onEnter`/`onEnterBack`), no por click: el diseño liga el cambio al scroll.',
             'Inactivas desenfocadas con el token nuevo `--blur-text` (4px) y blanco al 80%, como el diseño. Excepción declarada a contraste AA: es texto en segundo plano a propósito; la palabra activa, la que se lee en cada posición de scroll, tiene contraste completo.',
             '«Works» en mobile: el diseño lo muestra gigante en gris tenue sobre crema. Se deja decorativo (`aria-hidden`) y el `<h2>` real va oculto (decisión del equipo).',
             'Solo Finance (Corporate Finance Management) sale del diseño; Advisory, Growth y Strategy son placeholder, con las otras 3 imágenes de portfolio. El export mobile repite «// 01» en todas las cards: no se replica.',
             'Estado inicial Growth activa, igual que el diseño (el PNG es una sola captura de una posición de scroll).']))

O.append(dict(id='marquee', title='Marquee',
  desc='Franja de arriba del footer: «Connect With Us&nbsp;&nbsp;Let\'s Grow» en bucle horizontal infinito, translúcido salvo «Grow», con el badge del logo centrado encima (estático; el diseño no lo muestra en movimiento). El texto que arma el bucle está duplicado y es <code>aria-hidden</code>, con una sola frase para lectores al lado.',
  desc_md='Franja del footer: «Connect With Us  Let\'s Grow» en bucle horizontal (CSS puro), translúcido salvo «Grow», con el badge del logo centrado y estático. Texto duplicado `aria-hidden` + una frase para lectores.',
  blocks=[dict(label='Sobre fondo oscuro', surface='inverse', mods='bleed', html=marquee())],
  rows=[('.marquee', 'Contenedor; recorta el texto que sangra a los costados'),
        ('.marquee__viewport + aria-hidden', 'Capa visual del bucle, oculta para lectores'),
        ('.marquee__track / __group', 'Dos grupos idénticos; la animación mueve -50% (el ancho de uno)'),
        ('.marquee__text', 'Frase del bucle, blanco al 25%'),
        ('.marquee__accent', 'La palabra en blanco pleno («Grow»)'),
        ('.visually-hidden', 'Frase única «Connect with us. Let\'s grow.» para lectores'),
        ('.marquee__badge + aria-hidden / __badge-logo', 'Círculo estático con el logo (primary-logo.png), decorativo')],
  tokens=['--text-hero / -display (piso en mobile)', '--weight-semibold', '--leading-tight', '--tracking-tight', '--color-text-inverse', '--color-background-inverse', '--shadow-lg', '--radius-full', '--border-width-sm', '--spacing-7 / -10'],
  a11y='El texto animado y su duplicado quedan dentro de <code>aria-hidden="true"</code> (si no, un lector repetiría la frase varias veces); al lado hay una frase visualmente oculta con el mismo mensaje, una sola vez. El badge es decorativo: el logo con nombre ya está en el header. La animación se detiene con <code>prefers-reduced-motion: reduce</code>.',
  a11y_md='Texto animado + duplicado en `aria-hidden`, con una frase visualmente oculta al lado. Badge decorativo. Animación detenida con `prefers-reduced-motion: reduce`.',
  decisions=['Texto translúcido (blanco al 25%) con «Grow» en blanco pleno, como el diseño a resolución real; no hay separador visible entre frases (el diseño tapa ese hueco con el badge).',
             'Badge con el logo real (`primary-logo.png`), no un ícono: así lo muestra el diseño. Diámetro medido: 160px a 480 → 250px a 1920.',
             'El diseño no muestra el badge en movimiento: se deja estático (solo el texto de fondo se mueve).',
             'Duración del bucle (30s): no sale del diseño (es una imagen fija); se deriva para que se lea cómodo.',
             '`contain: inline-size` en `.marquee`: sin ella, el ancho del texto repetido (miles de px) estira cualquier ancestro grid o flex con columna automática (pasó en el kit) aunque el marquee tenga `overflow: hidden`.']))

O.append(dict(id='site-footer', title='Site Footer',
  desc='Cierre del sitio: <a href="#newsletter">Newsletter</a>, Utility Page, Follow Us, Our Offices y la barra legal, con el filete a todo el ancho. Siempre sobre fondo inverso. Corrige dos errores del export del diseño: «Pixenium» → <strong>Esonix</strong> y «404 Not Error» → <strong>Error 404</strong>.',
  desc_md='Cierre del sitio: Newsletter, Utility Page, Follow Us, Our Offices y barra legal (filete a todo el ancho), sobre fondo inverso. Corrige dos errores del export del diseño: «Pixenium» → Esonix, «404 Not Error» → Error 404.',
  blocks=[dict(label='Footer completo', surface='inverse', html=site_footer())],
  rows=[('footer.site-footer + data-surface="inverse"', 'Landmark contentinfo; la Section le da el fondo'),
        ('.container', 'Contenedor de Bootstrap para las columnas y, dentro de la barra legal, para su contenido'),
        ('.site-footer__top', '2 columnas bajo lg (newsletter y oficinas a todo el ancho); desde lg, 4 columnas con space-between'),
        ('nav + aria-labelledby', 'Utility Page y Follow Us, nombradas por su propio título'),
        ('.site-footer__title', 'Título de columna (h3)'),
        ('.site-footer__list', 'Lista de enlaces placeholder'),
        ('.site-footer__offices-col / __offices / __office-label / __office-city', 'Columna de oficinas: región en gris y ciudad en blanco'),
        ('.site-footer__legal / __legal-inner', 'Barra inferior: filete a todo el ancho y contenido dentro de un .container')],
  tokens=['--text-h4 / -body-lg', '--weight-semibold', '--color-text-inverse / -inverse-secondary', '--spacing-1 / -3 / -4 / -6 / -7 / -8 / -9 / -12', '--border-width-sm', '--ease-fast', 'Newsletter (molécula)'],
  a11y='Es el landmark <code>contentinfo</code> nativo del <code>&lt;footer&gt;</code> de página. Utility Page y Follow Us son <code>&lt;nav aria-labelledby&gt;</code> nombradas por su <code>&lt;h3&gt;</code>, así un lector las distingue del menú principal. El newsletter reutiliza la molécula (label real, botón con <code>aria-label</code>).',
  a11y_md='Landmark `contentinfo` nativo. Utility Page y Follow Us son `<nav aria-labelledby>` nombradas por su `<h3>`. El newsletter reutiliza la molécula.',
  decisions=['«Pixenium» (marca filtrada en el export) se corrige a «Esonix»; «404 Not Error» a «Error 404» (como en el submenú de Pages), según `plan.md`.',
             'Columnas desde lg: newsletter hasta 24rem y las otras tres a su ancho de contenido con `space-between`, que cae en las posiciones medidas del diseño (300 / 810 / 1093 / 1332 px a 1920).',
             'El footer trae sus `.container` (de Bootstrap) porque el filete legal debe cruzar todo el ancho y su texto alinearse con las columnas.',
             'Teléfono y redes en íconos no se repiten acá: el diseño no los muestra en el footer.',
             'Enlaces de Utility Page, Follow Us y legales son placeholder (`href="#"`): no hay páginas reales todavía.']))

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
/* Carrusel: la demo recorta los slides que sangran fuera del carrusel (en la página lo hace la Section);
   el relleno lateral deja ver los vecinos. --bleed-arrows ubica las flechas arriba a la derecha. */
.kit-demo--bleed {
  overflow: clip;
  padding-inline: var(--spacing-9);
}
.kit-demo--bleed-arrows {
  display: grid;
  gap: var(--spacing-6);
}
.kit-demo--bleed-arrows > .carousel__arrows {
  justify-self: end;
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
