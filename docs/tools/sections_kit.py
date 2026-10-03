# Genera las fichas de las Sections: dist/kit/index.html (nivel «Sections») + docs/kit/<id>.stories.md
# A diferencia de los otros niveles, el markup NO vive en este script: se extrae de la página que declara
# cada sección (clave page, por defecto dist/index.html), entre los marcadores <!-- section:<id> --> y
# <!-- /section:<id> -->. Una sección reutilizada en otra página (con un modificador) no repite la ficha:
# solo la página fuente lleva marcadores. Acá solo van los metadatos de cada ficha (descripción, clases,
# tokens, accesibilidad, decisiones). El CSS es el bloque sections: de main.css, escrito a mano.
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

def for_kit(markup):
    # Rutas relativas a /kit y ids con sufijo: el kit ya tiene demos con los mismos ids (p. ej. Progress)
    out = re.sub(r'\b(src|srcset)="assets/', r'\1="../assets/', markup)
    ids = re.findall(r'\bid="([^"]+)"', out)
    for i in ids:
        out = re.sub(r'(\b(?:id|for|aria-labelledby|aria-controls|aria-describedby|data-word-for)=")%s"' % re.escape(i), r'\g<1>%s-section"' % i, out)
        out = out.replace('href="#%s"' % i, 'href="#%s-section"' % i)
    # El formulario de la página no se activa en el kit (nunca envía correos reales): sin data-quote-form
    # y sin destino. La ficha de la molécula Quote Form ya tiene un demo en vivo.
    out = out.replace(' data-quote-form', '')
    out = re.sub(r'action="https://formsubmit\.co/[^"]*"', 'action="#"', out)
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

S.append(dict(id='services', title='Services',
  desc='Section Head partido (título, texto y las flechas del carrusel en una fila desde xl; apilado antes) y, debajo, el <a href="#carousel">Carousel</a> de <a href="#card-service">Card Service</a> en el contenedor ancho: el slide activo va centrado y destacado (<code>data-carousel-highlight</code>), con los vecinos sangrando hasta el borde de la ventana. La sección los recorta con <code>overflow-x: clip</code>.',
  desc_md='Section Head `--split` (desde xl) con las flechas + Carousel de Card Service en `.container-wide`: activo centrado y destacado, vecinos sangrando hasta el borde; la sección recorta con `overflow-x: clip`.',
  mods='section',
  rows=[('section.section.services', 'Recorta en horizontal los slides que sangran'),
        ('.section-head', 'Encabezado de sección: __main (eyebrow + h2), __text y __actions, apilados'),
        ('.section-head--split', 'Desde xl: título | texto | flechas en una fila; el texto y las flechas se alinean con la primera línea del h2'),
        ('.section-head__title', 'h2 acotado a 38rem para cortar donde el diseño'),
        ('.carousel__arrows.section-head__actions', 'Flechas del carrusel (aria-controls = id del carrusel)'),
        ('data-carousel-highlight data-carousel-start="0" data-carousel-start-wide="1"', 'Destaca el slide activo; arranca en Marketing Guidance (1 o 2 por vista) y en Process Optimization (3 por vista)')],
  tokens=['--text-h1 (section-title)', '--spacing-3 / -5 / -8 / -10', 'Eyebrow, Icon Button (átomos)', 'Card Service (molécula)', 'Carousel (organismo)'],
  a11y='El carrusel es una región con nombre («Services») y cada slide un grupo «N of 5»; las copias que agrega <code>main.js</code> para el loop van con <code>aria-hidden</code> e <code>inert</code>. Las flechas están antes del carrusel en el orden de lectura y lo controlan por <code>aria-controls</code>. El destacado es solo visual: no cambia el contenido que se anuncia.',
  a11y_md='Región «Services», slides «N of 5»; copias del loop con `aria-hidden` + `inert`. Flechas antes del carrusel, con `aria-controls`. El destacado es solo visual.',
  decisions=['Se destaca el slide activo (decisión del usuario): en desktop la card oscura queda al centro, como el diseño; en mobile, es la única visible.',
             'Section Head partido recién desde xl (1280px): a 1024px el título tenía 370px y cortaba en 4 líneas. Antes, apilado como en mobile.',
             'Financial Planning y Brand Strategy son placeholder (el diseño los muestra cortados en los costados). Los íconos son Lucide equivalentes a los glifos propios del diseño.',
             'Hueco entre secciones de 192px (96 + 96) contra ≈170px del diseño: se mantiene el ritmo del theme (`.section`).']))

S.append(dict(id='why-choose-us', title='Why Choose Us',
  desc='Texto a la izquierda, foto a la derecha y, montada sobre el borde inferior de la foto, la <strong>Feature Strip</strong>: un contenedor blanco que junta tres <a href="#card-feature">Card Feature</a> (la del medio, destacada con foto). Desde lg el texto arranca en el borde del <code>.container</code> y la foto llega al del <code>.container-wide</code>. En mobile: texto, foto y la franja apilada, montada 92px sobre la foto.',
  desc_md='Texto + foto, con la Feature Strip (tres Card Feature en un contenedor blanco) montada sobre el borde inferior de la foto. Desde lg el texto se alinea con `.container` y la foto llega al borde de `.container-wide`. Mobile: apilado, la franja 92px sobre la foto.',
  mods='section',
  rows=[('.container-wide.why-choose__grid', 'Grilla: --why-indent | texto 54fr | foto 46fr | --why-indent (columna central única bajo lg)'),
        ('--why-container / --why-indent', 'Ancho de contenido del .container en cada breakpoint y la sangría que resulta; alinea el texto con las otras secciones'),
        ('.why-choose__intro / __title / __text', 'Eyebrow, h2 (corta en 36rem, como el diseño) y párrafo'),
        ('.why-choose__media', 'Foto 1125:1095 que ocupa las dos filas; se estira si el texto es más alto'),
        ('.feature-strip.why-choose__strip', 'Franja blanca con borde: en fila desde lg, apilada antes; montada sobre la foto'),
        ('.feature-strip .card-feature', 'Cards normales sin fondo ni sombra; alto mínimo 18rem (20rem desde lg)')],
  tokens=['--container-width', '--color-surface-default', '--color-border-subtle', '--radius-lg', '--shadow-sm', '--border-width-sm', '--spacing-3 / -4 / -5 / -9 / -10 / -11', 'Eyebrow (átomo)', 'Card Feature (molécula)'],
  a11y='Orden del DOM = orden de lectura: texto, foto y las tres cards. La foto lleva <code>alt</code> descriptivo; el fondo de la card destacada es decorativo. El «Read More» de la card 02 tiene nombre completo («Read More about results-focused strategies») con texto oculto.',
  a11y_md='Orden del DOM = lectura (texto, foto, cards). Foto con `alt`; fondo de la card destacada decorativo. «Read More» con nombre completo por texto oculto.',
  decisions=['El «Read More» de la card 02 se mantiene también en mobile (decisión del usuario): el export mobile lo omite, se trata como omisión del export.',
             'Las columnas de la sangría (`--why-container`) usan los breakpoints de Bootstrap porque replican el ancho de su `.container`; excepción escrita en `design-tokens.md`.',
             'La Feature Strip vive en el bloque de Sections (no es una molécula del kit): solo la usa esta sección.',
             'Excepción declarada a anti-patrones #4 (card dentro de card): la Card Feature destacada vive dentro del contenedor blanco de la franja, como el diseño; las otras dos pierden fondo y sombra y se leen como columnas de la franja.',
             '«Read More» lleva a Services: el diseño no dice adónde va.']))

S.append(dict(id='finance', title='Finance',
  desc='El <a href="#word-list">Word List</a> como sección. Desde lg, un bloque a todo el ancho con radio de 40px, la foto desenfocada <strong>fija</strong> detrás (no se desplaza con la página) y el contenido centrado en vertical; la Card Project activa queda a la derecha con 524px. Bajo lg no hay bloque: «Works» tenue y las cards apiladas sobre el crema.',
  desc_md='Word List como sección. Desde lg: bloque a todo el ancho (radio 40px) con foto desenfocada fija detrás, contenido centrado y la Card Project de 524px a la derecha. Bajo lg: «Works» tenue y cards apiladas.',
  mods='section',
  rows=[('section.section.finance + aria-labelledby="works-title"', 'Desde lg: bloque de 59rem de alto mínimo con clip-path redondeado'),
        ('.finance__media', 'Capa position: fixed con la foto (filter: blur(--blur-photo)) y el velo; el clip-path de la sección la recorta'),
        ('.finance .word-list__media', 'Columna de cards acotada a 524px, alineada a la derecha con 20px de margen'),
        ('h2#works-title.visually-hidden', 'Nombre de la sección (el diseño no muestra título en desktop)')],
  tokens=['--blur-photo (nuevo)', '--radius-xl', '--color-overlay', '--color-background-inverse', '--spacing-5', 'Word List (organismo)', 'Card Project (molécula)'],
  a11y='La sección se nombra con el <code>&lt;h2&gt;</code> oculto «Works». La foto de fondo es decorativa (<code>alt=""</code>) y no se carga bajo lg (está en una capa con <code>display: none</code> y <code>loading="lazy"</code>). El velo mantiene el contraste de la palabra activa en blanco. Con «reducir movimiento» el Word List queda en su estado inicial (Growth activa).',
  a11y_md='Nombrada por el `<h2>` oculto «Works». Foto decorativa que no se carga bajo lg. El velo da contraste a la palabra activa. Reduced motion: queda Growth activa.',
  decisions=['Foto fija sin `background-attachment: fixed` (iOS lo ignora y un `filter` en el mismo elemento lo rompe): es una capa `position: fixed` dentro de la sección, recortada por su `clip-path` (que, a diferencia de `overflow`, sí recorta descendientes fijos). Se agranda el doble del desenfoque por lado para que el borde difuminado no se vea.',
             'Token nuevo `--blur-photo` (12px) junto a `--blur-text` y `--blur-backdrop`; va en `filter` sobre la imagen, nunca en `backdrop-filter`.',
             'Velo `--color-overlay` (65%), algo más denso que el diseño: la palabra activa en blanco pasa sobre la zona clara de la foto.',
             'El bloque mide 1905px de ancho en el PNG (artefacto del export): se trata como 100%.']))

S.append(dict(id='pricing', title='Pricing',
  desc='Section Head centrado, el switch mensual / anual y las tres <a href="#card-pricing">Card Pricing</a> (en 3 columnas desde xl; antes, una columna centrada). <code>main.js</code> cambia los precios al mover el <a href="#switch">Switch</a> y lo anuncia en una región <code>role="status"</code>.',
  desc_md='Section Head `--center`, Switch mensual/anual y tres Card Pricing (3 columnas desde xl, una centrada antes). `main.js` cambia los precios y lo anuncia en `role="status"`.',
  mods='section',
  rows=[('.section-head--center', 'Eyebrow --center y h2 centrados'),
        ('.pricing__billing + data-pricing', 'Fila del switch: «Monthly» (aria-hidden), el switch y su &lt;label&gt;; 18px en mobile y 24px desde lg'),
        ('input.switch[role="switch"]#pricing-annual', 'Encendido = precios anuales; su nombre es «Annually Save 30%»'),
        ('[data-pricing-status][role="status"]', 'Región oculta que anuncia el cambio (solo al mover el switch)'),
        ('[data-price-monthly][data-price-annual]', 'Importe que main.js reemplaza; sin JS queda el mensual'),
        ('.pricing__grid', 'Una columna de hasta 32rem; tres columnas desde xl')],
  tokens=['--text-h6 / -h4', '--color-text-primary', '--spacing-5 / -6 / -8 / -9 / -10', 'Eyebrow, Switch, Button (átomos)', 'Card Pricing (molécula)'],
  a11y='El switch es un <code>&lt;input type="checkbox" role="switch"&gt;</code> nativo con <code>&lt;label for&gt;</code> («Annually Save 30%»): se opera con Espacio y el lector anuncia encendido o apagado. «Monthly» es un rótulo visual oculto al lector, para no duplicar el nombre. Al moverlo, la región <code>role="status"</code> anuncia «Showing annual prices, 30% off.» (o el mensual); al cargar no anuncia nada. Cada «Get Started» lleva el nombre del plan en texto oculto.',
  a11y_md='Switch nativo (`role="switch"`) con `<label>` «Annually Save 30%»; «Monthly» con `aria-hidden`. `role="status"` anuncia el cambio solo al moverlo. «Get Started» con el nombre del plan oculto.',
  decisions=['Precios anuales con el 30% de descuento redondeado como el diseño: 39.9 → 27.9, 49.9 → 34.9, 59.9 → 41.9. «/ Month» no cambia (precio mensual equivalente).',
             'Tres columnas recién desde xl: a 1024px quedaban de 296px y cortaban nombres y beneficios en varias líneas.',
             'El export mobile repite «Long-Term Success Planning» en Premium Features: no se replica.',
             'Los «Get Started» llevan al footer (contacto): el diseño no dice adónde van.']))

S.append(dict(id='stats', title='Stats',
  desc='Solo mobile (el diseño desktop no la tiene; se oculta desde lg). La pastilla «4,000+ Clients Trust Our Expertise» sobre un filete a todo el ancho, el título «Facts prove the outcome» y tres <a href="#stat">Stat</a> centrados, separados por filetes, cada uno con un indicador de tres cuadritos (1, 2 y 3 encendidos). <strong>Achica la ventana por debajo de 1024px para verla.</strong>',
  desc_md='Solo mobile. Pastilla sobre filete a todo el ancho, título y tres Stat centrados entre filetes, con indicador de 3 cuadritos (1/2/3 encendidos, decorativo). Oculta desde lg.',
  mods='section',
  rows=[('section.section.stats', 'display: none desde lg'),
        ('.stats__pill', 'Pastilla centrada; los filetes a los costados son ::before / ::after'),
        ('h2.stats__title', 'Título de la sección, 22px centrado (corta en 12rem, como el diseño)'),
        ('ul.stats__list / .stats__item', 'Lista de cifras entre filetes'),
        ('.stats__level + aria-hidden / .is-on', 'Indicador decorativo de tres cuadritos'),
        ('.stats--strip + .stats__grid', 'About Us: sin pastilla y visible en todos los breakpoints; desde lg, título a la izquierda y las cifras en 3 columnas con filetes verticales')],
  tokens=['--color-border-default', '--color-action-primary', '--radius-full', '--text-h5', '--weight-medium', '--spacing-2 / -5 / -7 / -8', 'Stat --center (molécula)'],
  a11y='Las cifras son una lista con un <code>&lt;h2&gt;</code> que la nombra. El indicador de cuadritos es <code>aria-hidden</code>: no tiene significado que leer. Desde lg la sección no existe para nadie (<code>display: none</code>), sin duplicar contenido.',
  a11y_md='Lista nombrada por su `<h2>`; indicador `aria-hidden`. Desde lg, `display: none` (sin duplicar contenido).',
  decisions=['Solo mobile, decisión del equipo (el diseño desktop no la muestra).',
             '«Years of Consulting Experience» es placeholder (decisión del equipo): el diseño muestra «30+» sin etiqueta.',
             'El indicador de cuadritos no tiene equivalente en el kit y solo lo usa esta sección: vive en el bloque de Sections, no como átomo.',
             'Las cifras usan `--text-h1` (36px en mobile); el diseño mide ≈ 42px. Se mantiene el token.']))

S.append(dict(id='testimonials', title='Testimonials',
  desc='Bloque oscuro con la foto de fondo desenfocada bajo un velo denso, encabezado centrado y el <a href="#carousel">Carousel</a> de <a href="#card-testimonial">Card Testimonial</a> con dots, en el contenedor ancho: el activo va centrado y los vecinos sangran. Arranca en Isabella (tercer testimonio, tercer dot), como el diseño. Las cards en video abren el <a href="#video-modal">Video Modal</a>.',
  desc_md='Bloque oscuro (foto desenfocada + velo), encabezado centrado y Carousel con dots en `.container-wide`; arranca en el tercer slide (Isabella). Radio en las 4 esquinas en mobile y solo arriba desde lg.',
  mods='section',
  rows=[('section.section.testimonials + data-surface="inverse"', 'Fondo oscuro; recorta los slides que sangran y la foto al radio'),
        ('.section-bg', 'Capa de la foto (filter: blur(--blur-photo)) con el velo en ::after; patrón compartido con Feedback (About Us)'),
        ('.section-head--center + .eyebrow--inverse', 'Encabezado centrado, eyebrow amarillo'),
        ('data-carousel-start="2"', 'Arranca en el tercer testimonio, como el diseño')],
  tokens=['--blur-photo', '--color-background-inverse', '--radius-xl', '--spacing-9 / -10 / -11 / -12 / -13', 'Eyebrow --inverse, Pagination Dots (átomos)', 'Card Testimonial (molécula)', 'Carousel, Video Modal (organismos)'],
  a11y='El carrusel es una región «Client stories» con dots nombrados («Show story 3», el actual con <code>aria-current</code>). Los botones de play declaran <code>aria-haspopup="dialog"</code> y el nombre de la persona. La foto de fondo es decorativa; el velo da contraste al texto blanco.',
  a11y_md='Región «Client stories» con dots nombrados y `aria-current`. Play con `aria-haspopup="dialog"`. Foto decorativa con velo.',
  decisions=['Orden de los testimonios tomado del diseño: el parcial de la izquierda es un testimonio en video y Isabella (activa, tercer dot) es la tercera; Michael Brooks y Sophia Martinez son placeholder.',
             'Radio en las cuatro esquinas en mobile y solo arriba desde lg: así lo muestra cada PNG.',
             'Foto de fondo `h1-testimonial-bg-img` con `--blur-photo` y velo inverso al 85%, para que el texto blanco tenga contraste sobre la foto clara.']))

S.append(dict(id='team', title='Team',
  desc='Section Head partido (título y texto, desde xl; el texto queda contra el borde derecho porque no hay acciones) y tres <a href="#card-team">Card Team</a>: apiladas en mobile, en 3 columnas desde lg con Emma Wilson elevada 20px arriba y abajo.',
  desc_md='Section Head `--split` sin acciones (texto contra el borde derecho) y tres Card Team; desde lg en 3 columnas con la central elevada 20px.',
  mods='section',
  rows=[('.section-head--split', 'Título | texto; sin __actions no hay tercera columna'),
        ('.team__grid', 'Una columna en mobile; 3 desde lg, con padding que reserva la elevación'),
        ('.card-team--elevated', 'La central, 20px más alta arriba y abajo (desde lg)')],
  tokens=['--spacing-5 / -6', 'Badge, Icon Button (átomos)', 'Card Team (molécula)'],
  a11y='Cada card es un <code>&lt;article&gt;</code> con el nombre en <code>&lt;h3&gt;</code>; el botón «+» se nombra «View profile of …». Las fotos son decorativas (el nombre y el rol están en texto).',
  a11y_md='`<article>` con `<h3>`; «+» nombrado «View profile of …». Fotos decorativas.',
  decisions=['La grilla reserva con su padding (20px) el espacio de la card elevada: así no invade el encabezado. Medido a 1920: 84px del título a las cards laterales y 64px a la elevada.',
             'Los «+» llevan a `#`: no hay páginas de perfil todavía.']))

S.append(dict(id='logos', title='Logos',
  desc='Solo mobile. Grilla de 2 columnas con filetes entre celdas: siete logos de partners (las 4 imágenes repetidas) y la celda «Join with Us ↗». <strong>Achica la ventana por debajo de 1024px para verla.</strong>',
  desc_md='Solo mobile. Grilla 2 × 4 con filetes: 7 logos (4 imágenes repetidas) y «Join with Us ↗». Oculta desde lg.',
  mods='section',
  rows=[('section.section.logos', 'Sin padding superior (el diseño la pega a Team); display: none desde lg'),
        ('ul.logo-grid', 'Grilla de 2 columnas; los filetes son su fondo, que asoma por un gap de 1px'),
        ('.logo-grid__cell', 'Celda de 100px de alto mínimo con el logo centrado'),
        ('.logos--desktop', 'About Us: la grilla también desde lg, en 4 columnas')],
  tokens=['--color-border-default', '--color-background-default', '--border-width-sm', '--radius-md', '--spacing-4 / -5 / -11', 'Link Arrow (átomo)'],
  a11y='La sección se nombra con un <code>&lt;h2&gt;</code> oculto («Our partners»); cada logo lleva su nombre como <code>alt</code>. «Join with Us» es un enlace con texto visible.',
  a11y_md='`<h2>` oculto «Our partners»; logos con `alt`; «Join with Us» enlace con texto visible.',
  decisions=['Solo mobile (decisión del equipo); las 4 imágenes de partners se repiten para completar 7 celdas (decisión del equipo).',
             'Los filetes salen del fondo de la grilla y un gap de 1px: no dependen de cuántas celdas haya.',
             'Los PNG de partners son casi negros y el diseño los muestra en gris: se usan tal cual, sin filtros.',
             '«Join with Us» lleva al footer (contacto): el diseño no dice adónde va.']))

S.append(dict(id='faq', title='FAQ',
  desc='A la izquierda el encabezado y la <a href="#card-cta">Card CTA</a> abajo; a la derecha el <a href="#accordion">Accordion</a> (un solo ítem abierto por el <code>name</code> compartido). En mobile, apilados.',
  desc_md='Encabezado + Card CTA a la izquierda (columnas de 525 y 720px a 1920) y Accordion a la derecha; apilados en mobile.',
  mods='section',
  rows=[('.faq__grid', 'Una columna en mobile; desde lg, 33rem | 45rem repartidas a los extremos'),
        ('.faq__intro', 'Encabezado y Card CTA; desde lg, el CTA baja al final de la columna'),
        ('.accordion + details[name="faq"]', 'Acordeón: un solo ítem abierto (el segundo, como el diseño)'),
        ('.faq--centered', 'About Us: encabezado centrado arriba; Accordion --boxed (800px) y Card CTA --stacked (448px) en columnas, sobre --color-background-subtle')],
  tokens=['--spacing-8 / -10', 'Eyebrow (átomo)', 'Card CTA, Accordion Item (moléculas)', 'Accordion (organismo)'],
  a11y='Cada pregunta es un <code>&lt;summary&gt;</code> nativo (Enter / Espacio). El «?» y el +/− son <code>aria-hidden</code>. «Contact Us» lleva al footer.',
  a11y_md='`<summary>` nativo; «?» y +/− `aria-hidden`. «Contact Us» lleva al footer.',
  decisions=['El acordeón termina ~50px antes que la Card CTA (en el diseño, a ras): sus ítems miden 105px cerrados y 206px abierto contra 113 y 224px del diseño; igualarlos exigiría paddings fuera de la escala.',
             'Las preguntas van sin el espacio antes de «?» del diseño (tipografía inglesa).']))

S.append(dict(id='blog', title='Blog',
  desc='Section Head centrado, tres <a href="#card-post">Card Post</a> en el contenedor ancho (3 columnas desde lg) y el botón «View All Blog» centrado debajo.',
  desc_md='Section Head `--center`, tres Card Post en `.container-wide` (3 columnas desde lg) y «View All Blog» centrado.',
  mods='section',
  rows=[('.blog__grid', 'Una columna en mobile; 3 columnas desde lg (524px a 1920)'),
        ('.blog__actions', 'Fila centrada del botón'),
        ('&amp;&amp;nbsp;Expert', 'Espacio duro: el título corta antes de «&amp; Expert Advice», como el diseño')],
  tokens=['--spacing-6 / -9 / -10', 'Eyebrow, Button, Badge, Link Arrow (átomos)', 'Card Post (molécula)'],
  a11y='Cada «Read More» lleva el título del post en texto oculto; las fechas son <code>&lt;time datetime&gt;</code>. Las fotos son decorativas.',
  a11y_md='«Read More» con el título oculto; fechas con `<time datetime>`; fotos decorativas.',
  decisions=['El export desktop repite el encabezado del Blog (uno cortado encima del otro): se trata como artefacto y va uno solo.',
             'Los «Read More» y «View All Blog» llevan a `#`: no hay páginas de blog todavía.']))

S.append(dict(id='page-hero', title='Page Hero', page='about-us.html',
  desc='Cabecera de las páginas interiores: foto a sangre con velo, el <strong>breadcrumb</strong> en píldora translúcida y el único <code>&lt;h1&gt;</code> de la página abajo a la izquierda, alineado con el <code>.container</code>. Reserva el alto del <a href="#site-header">header fijo</a> (variante <code>--inner</code> en estas páginas). 750px de alto en desktop y 420px en mobile, como el diseño.',
  desc_md='Cabecera de páginas interiores: foto con velo, breadcrumb en píldora y `<h1>` abajo a la izquierda en el `.container`. 750px (desktop) / 420px (mobile). Reserva el alto del header fijo.',
  mods='section',
  rows=[('section.page-hero + data-surface="inverse"', 'Foto de fondo y texto blanco; la superficie inversa da el foco claro sobre la foto'),
        ('.page-hero__media', 'Capa de la foto (object-fit: cover) con el velo en ::after (izquierda y abajo)'),
        ('.container.page-hero__content', 'Breadcrumb y h1 apilados, alineados con el contenido de las secciones'),
        ('nav.breadcrumb[aria-label="Breadcrumb"] &gt; ol.breadcrumb__list', 'Píldora translúcida; el guion entre ítems es contenido generado sin texto alternativo'),
        ('span[aria-current="page"]', 'La página actual, sin enlace'),
        ('h1.page-hero__title', 'Título de la página con --text-h1; corta en 45rem')],
  tokens=['--text-h1', '--color-overlay / -overlay-light', '--color-text-inverse', '--header-offset', '--radius-full', '--spacing-1 / -2 / -5 / -6 / -7 / -10 / -11'],
  a11y='Único <code>&lt;h1&gt;</code> de la página. El breadcrumb es un <code>&lt;nav&gt;</code> nombrado «Breadcrumb» con una lista ordenada; la página actual lleva <code>aria-current="page"</code> y el separador no se lee. La foto es decorativa (<code>alt=""</code>) y se precarga con prioridad alta (LCP). <code>data-surface="inverse"</code> pasa el anillo de foco a su versión clara sobre la foto.',
  a11y_md='Único `<h1>`. Breadcrumb: `<nav aria-label="Breadcrumb">` + `<ol>`, actual con `aria-current="page"`, separador sin texto. Foto decorativa precargada (LCP). `data-surface="inverse"`: foco claro.',
  decisions=['`--text-h1` (48/36px) en lugar de los ≈ 62/41px que mide el diseño: decisión del usuario, sin token nuevo.',
             'Reutilizable en las 7 páginas interiores: cambia la foto, el último ítem del breadcrumb y el h1.',
             'La foto es `about-page-header-bg.webp` (1920×750, el recorte exacto del diseño); en mobile se encuadra con `object-position`.']))

S.append(dict(id='about-intro', title='About Intro', page='about-us.html',
  desc='«What We Do» de About Us. Desde lg, dos columnas medidas en el diseño: a la izquierda eyebrow, h2, una lista con checks y «More about us»; a la derecha la historia: foto con marco (<code>photo-frame</code>, 5:4), «Who we are» con dos párrafos, un filete y la cita con comillas y firma. En mobile, apilado en el mismo orden.',
  desc_md='«What We Do» de About Us: eyebrow, h2, checks y botón a la izquierda; foto con marco, «Who we are», filete y cita con firma a la derecha. Mobile: apilado.',
  mods='section',
  rows=[('.about-intro__grid', 'Una columna en mobile; desde lg 30rem | 42.5rem (480 y 680px a 1920) a los extremos'),
        ('.about-intro__lead / __list', 'Eyebrow, h2, lista con icon--circle-check-outline y botón'),
        ('.about-intro__story', 'Foto con marco, texto, filete y cita'),
        ('.photo-frame.about-intro__photo', 'Foto 5:4 con marco blanco de 8px'),
        ('h3.about-intro__subtitle', '«Who we are», 24px'),
        ('figure.about-intro__quote', 'Comillas decorativas (::before) a la izquierda de la cita y la firma')],
  tokens=['--text-h1 (section-title) / -h4 / -h5 / -display', '--color-text-primary', '--weight-regular / -medium / -semibold', '--spacing-3 / -4 / -5 / -7 / -10', 'Eyebrow, Button, Divider, Icon (átomos)'],
  a11y='La cita es un <code>&lt;figure&gt;</code> con <code>&lt;blockquote&gt;</code> y la firma en el <code>&lt;figcaption&gt;</code> como imagen con <code>alt</code> («Signature of Michel Jhon»). Las comillas grandes son contenido generado sin texto alternativo. La foto lleva <code>alt</code> descriptivo; los checks son <code>aria-hidden</code>.',
  a11y_md='Cita en `<figure>` + `<blockquote>`; firma en `<figcaption>` con `alt`. Comillas generadas sin texto alternativo. Foto con `alt`; checks `aria-hidden`.',
  decisions=['«More about us» lleva al equipo (`#team-profiles`): el diseño no dice adónde va.',
             'Ícono nuevo `circle-check-outline` (el `circle-check` del theme es relleno, el de Pricing; esta lista lo muestra en contorno).',
             '«From Vision to Success» va en `<strong>` con peso normal: el diseño solo lo distingue por color.',
             'Excepción declarada a anti-patrones #13: los párrafos de «Who we are» llegan a ~85 caracteres por línea en la columna de 680px, como el diseño.']))

S.append(dict(id='team-profiles', title='Team Profiles', page='about-us.html',
  desc='El equipo en About Us: Section Head centrado y tres <a href="#card-team">Card Team</a> <code>--profile</code> (card blanca con foto, nombre, cargo y redes), apiladas en mobile y en 3 columnas desde lg, la central con <code>--reverse</code> (texto arriba).',
  desc_md='Section Head centrado + tres Card Team `--profile`, 3 columnas desde lg; la central `--reverse`.',
  mods='section',
  rows=[('.section-head--center', 'Eyebrow y h2 centrados'),
        ('.team-profiles__grid', 'Una columna en mobile; 3 columnas (424px a 1920) desde lg'),
        ('.card-team--profile.card-team--reverse', 'La card central: texto arriba y foto abajo desde lg')],
  tokens=['--spacing-6', 'Eyebrow (átomo)', 'Card Team --profile (molécula)'],
  a11y='Cada card es un <code>&lt;article&gt;</code> con el nombre en <code>&lt;h3&gt;</code>; cada red se nombra con la persona («Olivia Bennet on LinkedIn»). Las fotos son decorativas: nombre y cargo están en texto. El orden del DOM no cambia con <code>--reverse</code> (foto primero), así el lector de pantalla oye siempre lo mismo.',
  a11y_md='`<article>` + `<h3>`; redes nombradas con la persona; fotos decorativas; `--reverse` no cambia el orden del DOM.',
  decisions=['Las redes llevan a `#`: no hay perfiles todavía.',
             'El id `team-profiles` es el destino de «More about us».']))

S.append(dict(id='feedback', title='Feedback', page='about-us.html',
  desc='Client Feedback de About Us: bloque oscuro con la foto desenfocada (<code>.section-bg</code>, el mismo patrón que Testimonials), encabezado centrado y el <a href="#carousel">Carousel</a> <code>--fade</code> con tres citas y dots. Radio abajo en desktop y arriba en mobile, como cada PNG. Su padding inferior reserva lo que sube el formulario de Why Trust.',
  desc_md='Bloque oscuro con `.section-bg`, encabezado centrado y Carousel `--fade` de 3 citas con dots. Radio abajo (desktop) / arriba (mobile). Reserva `--quote-form-overlap` abajo.',
  mods='section',
  rows=[('section.section.feedback + data-surface="inverse"', 'Fondo oscuro; recorta la foto al radio'),
        ('.section-bg', 'Capa de la foto desenfocada con el velo inverso al 85%'),
        ('.carousel.carousel--fade + data-carousel-fade', 'Una cita por vez con fundido; dots generados por main.js'),
        ('figure.feedback__quote / .feedback__text / .feedback__author', 'Comillas ámbar (::before), cita de 18/24px y autor'),
        ('--quote-form-overlap', 'Lo que el Quote Form sube sobre el bloque: 80px en mobile, 96px desde lg')],
  tokens=['--blur-photo', '--color-background-inverse', '--color-text-highlight', '--text-h4 / -h6 / -display', '--radius-xl', '--spacing-6 / -7 / -10 / -11 / -12 / -13', 'Eyebrow --inverse, Pagination Dots (átomos)', 'Carousel (organismo)'],
  a11y='Región «Client quotes» con dots nombrados («Show quote 2», el actual con <code>aria-current</code>). Cada cita es un <code>&lt;figure&gt;</code> con <code>&lt;blockquote&gt;</code> y autor en <code>&lt;figcaption&gt;</code>. Sin autoplay (no hace falta botón de pausa, WCAG 2.2.2); con «reducir movimiento» el cambio es instantáneo. La foto de fondo es decorativa.',
  a11y_md='Región «Client quotes», dots nombrados con `aria-current`; `<figure>` + `<blockquote>` + `<figcaption>`. Sin autoplay (WCAG 2.2.2); reduced motion: instantáneo.',
  decisions=['Tres citas: David Thompson (diseño) y las de James Anderson e Isabella Harris, con su texto de la Home (decisión del usuario).',
             'El diseño desktop marca activo el segundo dot y el mobile el primero; se arranca en David Thompson (primer dot).',
             'Fondo: `about-video-bg.webp` con el tratamiento de Testimonials, extraído al patrón `.section-bg` (Testimonials migró a él sin cambios visuales).']))

S.append(dict(id='why-trust', title='Why Trust', page='about-us.html',
  desc='Why Choose Us de About Us: el <a href="#quote-form">Quote Form</a> sube sobre el bloque Feedback (margen negativo, <code>--quote-form-overlap</code>) y, a su lado, eyebrow, h2, dos barras de <a href="#progress">Progress</a> (Consulting en ámbar) y «Contact With Us ↗». En mobile, el formulario primero y el texto debajo.',
  desc_md='Quote Form montado sobre Feedback + eyebrow, h2, dos Progress (una `--accent`) y Link Arrow. Mobile: formulario primero.',
  mods='section',
  rows=[('.why-trust__grid', 'Una columna en mobile; desde lg 37.5rem | 35rem (600 y 560px a 1920), alineadas abajo'),
        ('form.quote-form.why-trust__form', 'Primero en el DOM; sube --quote-form-overlap sobre Feedback; desde lg en la columna derecha'),
        ('.why-trust__intro / __bars', 'Eyebrow, h2, barras y enlace'),
        ('.progress--accent', 'La barra «Consulting» en ámbar')],
  tokens=['--quote-form-overlap', '--spacing-5 / -6 / -10', 'Eyebrow, Progress, Link Arrow, Field (átomos)', 'Quote Form (molécula)'],
  a11y='El formulario va antes en el DOM: en mobile es lo que se ve primero y en desktop queda a la derecha, así el orden de Tab es formulario → texto. Cada barra es un <code>&lt;progress&gt;</code> con <code>&lt;label for&gt;</code>. En el kit, el formulario se muestra sin <code>data-quote-form</code> y con <code>action="#"</code>: no envía nada.',
  a11y_md='Formulario primero en el DOM (Tab: formulario → texto). `<progress>` + `<label for>`. En el kit, formulario neutralizado (no envía).',
  decisions=['El formulario envía por FormSubmit a studioneyra@gmail.com (decisión del usuario); el primer envío real dispara un correo de activación.',
             '«Contact With Us» lleva al formulario de la misma sección.',
             'El título del formulario es un `<h2>` (no `<h3>`): el formulario va antes que el h2 de la sección en el DOM, y como h3 quedaba colgando del h2 de Feedback en el esquema de títulos.',
             'El formulario mide 571px contra 585 del diseño: los campos quedan a 83px (el diseño, 75) porque el label flotante necesita reservar su lugar arriba.']))

S.append(dict(id='footer', title='Footer',
  desc='El <a href="#site-footer">Site Footer</a> con el <a href="#marquee">Marquee</a> arriba y la foto <code>h1-footer-bg</code> muy desenfocada bajo un velo denso detrás de los dos. Está fuera de <code>&lt;main&gt;</code>.',
  desc_md='Site Footer + Marquee arriba, con la foto desenfocada (`--blur-photo`) y velo detrás. Fuera de `<main>`.',
  mods='section',
  rows=[('footer.site-footer.page-footer + data-surface="inverse"', 'Footer de la página; recorta la foto'),
        ('.page-footer__media', 'Capa de la foto (filter: blur(--blur-photo)) con el velo en ::after'),
        ('.marquee (sin data-surface)', 'Toma la superficie del footer y deja ver la foto'),
        ('.page-footer > .container', 'Aire entre el Marquee y las columnas, medido en el diseño')],
  tokens=['--blur-photo', '--color-background-inverse', '--spacing-9 / -10 / -11 / -12', 'Newsletter (molécula)', 'Marquee, Site Footer (organismos)'],
  a11y='<code>&lt;footer&gt;</code> fuera de <code>&lt;main&gt;</code> (landmark contentinfo). Sus títulos son <code>&lt;h2&gt;</code> y cada lista de enlaces es un <code>&lt;nav&gt;</code> nombrado por su título. El texto del Marquee es <code>aria-hidden</code> con una frase única para lectores.',
  a11y_md='`<footer>` fuera de `<main>`; títulos `<h2>`; `<nav>` nombrados. Marquee `aria-hidden` + frase única.',
  decisions=['Los títulos son `<h2>` en la página (el footer cuelga del `<body>`); en la ficha del organismo son `<h3>` porque viven dentro de una sección del kit.',
             'Marquee sin su propio `data-surface`: con él, su fondo inverso tapaba la foto.']))

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
         '            <p class="kit-card__desc">%s Fuente: <code>dist/%s</code> (<a href="../%s#%s">ver en la página</a>).</p>' % (a['desc'], page_of(a), page_of(a), a['id']), '          </header>',
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

markups = {a['id']: extract(a['id'], page_of(a)) for a in S}
cards = '\n\n'.join(card(a, i, markups[a['id']]) for i, a in enumerate(S, 1))
level = ('      <section class="kit-level" id="sections" aria-labelledby="sections-title">\n        <h2 id="sections-title">Sections</h2>\n'
         '        <p class="kit-level__intro">Bloques de página completa. A diferencia de los otros niveles, su fuente es la página donde vive cada sección (<code>dist/*.html</code>): cada ficha se arma con lo que hay entre los marcadores <code>&lt;!-- section:id --&gt;</code> de esa página, así el kit y el sitio no se desfasan. Los demos se ven con el ancho de esta columna; los breakpoints responden a la ventana.</p>\n'
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
          '**Dónde:** markup en `dist/%s` (entre `<!-- section:%s -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#%s`' % (page_of(a), a['id'], a['id']), '',
          '## Descripción', '', unesc(a['desc_md']), '', '## Snippet', '', '```html', markups[a['id']], '```', '',
          '## Clases y atributos', '', '| Clase o atributo | Efecto |', '|---|---|'] + ['| `%s` | %s |' % (H.unescape(s), unesc(t)) for s, t in a['rows']]
    md += ['', '## Tokens que consume', ''] + ['- `%s`' % t for t in a['tokens']]
    md += ['', '## Accesibilidad', '', unesc(a['a11y_md']), '', '## Decisiones y excepciones', ''] + ['- ' + x for x in a['decisions']] + ['']
    (STORIES / (a['id'] + '.stories.md')).write_text('\n'.join(md), encoding='utf-8', newline='\n')
print('ok:', len(S), 'sections')
