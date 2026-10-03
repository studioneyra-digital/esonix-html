# Genera las fichas de las moléculas: dist/kit/index.html + docs/kit/<id>.stories.md
import re, os, textwrap, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
KIT = str(ROOT / 'dist' / 'kit' / 'index.html')
KITCSS = str(ROOT / 'dist' / 'assets' / 'css' / 'kit.css')
STORIES = str(ROOT / 'docs' / 'kit')
IMG = '../assets/img/'

def d(s): return textwrap.dedent(s).strip('\n')
def ic(name, extra=''): return '<span class="icon icon--%s%s" aria-hidden="true"></span>' % (name, extra)
def lis(items): return '\n'.join(items)

# ------------------------------------------------------------------ piezas reutilizadas por los demos
def service(title, text, icon, img, brand=False):
    return d('''
      <article class="card-service"%s>
        <img class="card-service__media" src="%s%s" alt="" width="1500" height="900" loading="lazy">
        <div class="card-service__body">
          <div class="card-service__head">
            %s
            <h3 class="card-service__title">%s</h3>
          </div>
          <p>%s</p>
        </div>
      </article>''' % (' data-surface="brand"' if brand else '', IMG, img, ic(icon, ' card-service__icon'), title, text))

def pricing(name, tagline, icon, price, items, brand=False):
    li = []
    for i, t in enumerate(items):
        cls = 'card-pricing__item is-muted' if i == len(items) - 1 else 'card-pricing__item'
        li.append('          <li class="%s">%s %s</li>' % (cls, ic('circle-check'), t))
    return d('''
      <article class="card-pricing"%s>
        <header class="card-pricing__head">
          <span class="card-pricing__icon">%s</span>
          <div>
            <h3 class="card-pricing__name">%s</h3>
            <p>%s</p>
          </div>
        </header>
        <p class="card-pricing__price"><span class="card-pricing__amount">%s</span> <span>/ Month</span></p>
        <a href="#card-pricing" class="btn btn--block%s">
          Get Started
          %s
        </a>
        <ul class="card-pricing__list">
%s
        </ul>
      </article>''' % (' data-surface="brand"' if brand else '', ic(icon), name, tagline, price, ' btn--accent' if brand else '', ic('arrow-up-right'), chr(10).join(li)))

def team(img, role, name, elevated=False):
    return d('''
      <article class="card-photo card-team%s" data-surface="inverse">
        <img class="card-photo__img" src="%s%s" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__body">
          <div class="card-team__top">
            <span class="badge">%s</span>
            <a href="#card-team" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of %s">%s</a>
          </div>
          <h3 class="card-team__name">%s</h3>
        </div>
      </article>''' % (' card-team--elevated' if elevated else '', IMG, img, role, name, ic('plus'), name))

SOCIALS = [('facebook', 'Facebook'), ('x-twitter', 'X'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn')]

def profile(img, role, name, reverse=False):
    socials = '\n'.join('            <li><a href="#card-team" class="card-team__social" aria-label="%s on %s">%s</a></li>' % (name, net, ic(icon)) for icon, net in SOCIALS)
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

def post(img, date_iso, date_txt, title, text, hidden):
    return d('''
      <article class="card-post">
        <div class="card-post__media">
          <img class="card-post__img" src="%s%s" alt="" width="1308" height="600" loading="lazy">
          <span class="badge badge--marker card-post__date"><time datetime="%s">%s</time></span>
        </div>
        <div class="card-post__body">
          <h3 class="card-post__title">%s</h3>
          <p>%s</p>
          <a href="#card-post" class="link-arrow">
            Read More<span class="visually-hidden"> about %s</span>
            %s
          </a>
        </div>
      </article>''' % (IMG, img, date_iso, date_txt, title, text, hidden, ic('arrow-up-right')))

def testi_text(thumb, name, role, quote):
    return d('''
      <figure class="card-testimonial" data-surface="brand">
        <blockquote class="card-testimonial__quote">
          <p>“%s”</p>
        </blockquote>
        <figcaption class="card-testimonial__footer">
          <hr class="divider divider--inverse">
          <p class="card-testimonial__author">
            <img class="avatar avatar--portrait" src="%s%s" alt="" width="80" height="80" loading="lazy">
            <span><span class="card-testimonial__name">%s,</span> %s</span>
          </p>
        </figcaption>
      </figure>''' % (quote, IMG, thumb, name, role))

def faq(open_, q, a):
    return d('''
      <details class="accordion-item" name="faq-demo"%s>
        <summary class="accordion-item__summary">
          <span class="accordion-item__mark" aria-hidden="true">?</span>
          <span class="accordion-item__question">%s</span>
          <span class="accordion-item__toggle" aria-hidden="true">%s%s</span>
        </summary>
        <div class="accordion-item__panel">
          <p>%s</p>
        </div>
      </details>''' % (' open' if open_ else '', q, ic('plus'), ic('minus'), a))

M = []

M.append(dict(id='card-service', title='Card Service',
  desc='Card de un servicio: foto, ícono Lucide, título y texto. Con <code>data-surface="brand"</code> pasa a la versión destacada (petróleo, ícono amarillo). Vive dentro del carrusel de Services y ocupa la altura de su slide.',
  desc_md='Card de servicio: foto, ícono, título y texto. `data-surface="brand"` la destaca (petróleo, ícono amarillo).',
  blocks=[dict(label='Normal y destacada', mods='cards', html=service('Marketing Guidance', 'Through expert insights and strategic planning, marketing guidance enables businesses to understand customer.', 'target', 'h1-service-img-2.webp')
        + '\n' + service('Process Optimization', 'By analyzing existing operations and implementing effective improvements, process optimization helps business.', 'trending-up', 'h1-service-img-3.webp', True))],
  rows=[('.card-service', 'Card blanca con sombra suave; ocupa el alto de su contenedor'),
        ('.card-service__media', 'Foto 5:3 con esquinas redondeadas (la fuente es 1500×900)'),
        ('.card-service__head / __icon / __title', 'Ícono de 40px y título (h3); __head se disuelve en la grilla de __body y el párrafo queda sangrado bajo el título'),
        ('data-surface="brand"', 'Versión destacada: fondo petróleo, texto claro, ícono amarillo y foco amarillo')],
  tokens=['--color-surface-default', '--shadow-sm', '--radius-lg / -md', '--spacing-3 / -4 / -5 / -7', '--text-h4', '--weight-medium', '--color-text-secondary / -inverse-secondary / -highlight'],
  a11y='La foto es decorativa (<code>alt=""</code>); el título es un <code>&lt;h3&gt;</code> bajo el <code>&lt;h2&gt;</code> de la sección. El ícono es <code>aria-hidden</code>. La card no es un enlace: si el servicio tiene página, el enlace va dentro con texto descriptivo.',
  a11y_md='Foto decorativa; título `h3`; ícono `aria-hidden`; la card no es un enlace.',
  decisions=['Texto sangrado bajo el título e ícono de 40px, medidos en el PNG a resolución real (Etapa 4, Grupo B); antes el párrafo arrancaba bajo el ícono.',
             'Los iconos del diseño son glifos propios de cada servicio; aquí se usan Lucide equivalentes (target, trending-up, chart-pie, users, lightbulb) hasta tener los del cliente.',
             'Las cards del diseño tienen esquinas de ~20px: se usa `--radius-lg` (24px) para cards y `--radius-md` (16px) para sus fotos.']))

M.append(dict(id='card-feature', title='Card Feature',
  desc='Card de un argumento de venta: número decorativo arriba, título y texto abajo. Con <code>data-surface="brand"</code> lleva foto de fondo bajo un velo petróleo, el número en amarillo y un «Read More». En la home las tres van pegadas en una franja.',
  desc_md='Card de argumento: número decorativo, título y texto. `data-surface="brand"` suma foto de fondo con velo petróleo y «Read More».',
  blocks=[dict(label='Normal, destacada y normal', mods='cards', html=d('''
      <article class="card-feature">
        <p class="card-feature__number" aria-hidden="true">01</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Tailored business solutions</h3>
          <p>We provide tailored business solution designed to match your unique goals</p>
        </div>
      </article>
      <article class="card-feature" data-surface="brand">
        <img class="card-feature__bg" src="%sh1-feature-bg-image.webp" alt="" width="1320" height="960" loading="lazy">
        <p class="card-feature__number" aria-hidden="true">02</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Results-focused strategies</h3>
          <p>Our results-focused strategies are designed to deliver measurable business growth</p>
          <a href="#card-feature" class="link-arrow link-arrow--inverse">
            Read More<span class="visually-hidden"> about results-focused strategies</span>
            %s
          </a>
        </div>
      </article>
      <article class="card-feature">
        <p class="card-feature__number" aria-hidden="true">03</p>
        <div class="card-feature__body">
          <h3 class="card-feature__title">Proven success methods</h3>
          <p>With a focus on practical results, we create strategies that deliver lasting value</p>
        </div>
      </article>''' % (IMG, ic('arrow-up-right'))))],
  rows=[('.card-feature', 'Card blanca; número arriba y texto abajo (justify space-between)'),
        ('.card-feature__number', 'Número decorativo en gris claro (aria-hidden)'),
        ('.card-feature__bg', 'Foto de fondo (solo en la destacada); queda bajo el velo'),
        ('data-surface="brand"', 'Destacada: velo petróleo al 85% sobre la foto, número amarillo y texto claro')],
  tokens=['--color-surface-default', '--color-border-default (número)', '--color-action-primary (velo)', '--color-text-highlight', '--radius-lg', '--spacing-3 / -7 / -10', '--text-h4 / -h5'],
  a11y='El número es <code>aria-hidden</code>: las tres cards no son una secuencia, así que la numeración es solo visual. «Read More» agrega con <code>visually-hidden</code> el tema del que habla, para no repetir un enlace ambiguo.',
  a11y_md='Número `aria-hidden` (no es una secuencia); «Read More» con texto oculto que dice de qué habla.',
  decisions=['El diseño pega las tres cards en una franja con un contenedor blanco redondeado; ese contenedor (y el recorte de las esquinas) es de la Section, no de la card.',
             'El velo petróleo del diseño deja ver la foto con tinte verde; se resuelve con `color-mix()` del token de acción al 85%.']))

M.append(dict(id='card-pricing', title='Card Pricing',
  desc='Plan de precios: ícono, nombre, precio mensual, botón y lista de beneficios. Con <code>data-surface="brand"</code> se destaca (petróleo y botón amarillo). El último beneficio va atenuado, como en el diseño. El cambio Monthly / Annually lo maneja la Section.',
  desc_md='Plan de precios: ícono, nombre, precio, botón y lista. `data-surface="brand"` lo destaca (petróleo, botón amarillo). El último beneficio va atenuado.',
  blocks=[dict(label='Starter, Enterprise (destacado) y Premium', mods='cards', html=
        pricing('Starter Plan', 'Core strategies for business success', 'rocket', '$39.9', ['Growth Recommendations', 'Monthly Strategy Consultation', 'Basic Market Analysis', 'Email support'])
        + '\n' + pricing('Enterprise Plan', 'Drive innovation &amp; long-term success', 'award', '$49.9', ['Customized Business Strategy', 'Advanced Market Research', 'Ongoing Performance Monitoring', 'Priority Support &amp; Advisory'], True)
        + '\n' + pricing('Premium Features', 'Unlock greater efficiency and growth', 'gem', '$59.9', ['Long-Term Success Planning', 'Actionable Growth Strategies', 'Industry Expert Guidance', 'Dedicated Business Support']))],
  rows=[('.card-pricing', 'Card blanca en grilla; ícono + nombre arriba, precio, botón y lista'),
        ('.card-pricing__price / __amount', 'Precio en Mona Sans semibold del tamaño de h1; «/ Month» va atenuado'),
        ('.card-pricing__list / __item', 'Panel con borde que contiene los beneficios con check relleno'),
        ('.is-muted', 'Beneficio atenuado (solo énfasis visual, no cambia el significado)'),
        ('data-surface="brand"', 'Plan destacado: petróleo, lista en panel claro translúcido; usa btn--accent en el botón')],
  tokens=['--color-surface-default / -background-subtle', '--shadow-sm', '--radius-lg / -md', '--text-h1 / -h4', '--color-action-primary', '--color-overlay-light (panel destacado)', '--color-text-tertiary / -inverse-secondary (atenuado)', '--spacing-3 / -5 / -6 / -9'],
  a11y='El nombre del plan es un <code>&lt;h3&gt;</code>; los beneficios son una <code>&lt;ul&gt;</code> y el check es <code>aria-hidden</code>. El texto atenuado cumple AA (5.1:1 sobre blanco; 4.8:1 sobre el panel de la card destacada). «Get Started» se repite en cada plan: si hace falta distinguirlos, añadir texto <code>visually-hidden</code> con el plan.',
  a11y_md='Nombre `h3`; beneficios en `<ul>`; check `aria-hidden`; atenuado ≥ AA; «Get Started» repetido puede llevar texto oculto con el plan.',
  decisions=['**Excepción a anti-patrones #4 (card anidada):** la lista de beneficios es un panel con borde dentro de la card porque el diseño lo muestra así. Se declara aquí en lugar de ignorarla.',
             'El último beneficio atenuado no se marca como «no incluido»: el diseño solo lo muestra tenue y no dice qué significa. Pendiente de confirmar.',
             'Los iconos de plan (rocket, award, gem) son Lucide equivalentes a los del diseño.']))

M.append(dict(id='card-testimonial', title='Card Testimonial',
  desc='Reseña de un cliente dentro de un <code>&lt;figure&gt;</code>: cita y autor. La de texto va en petróleo (<code>data-surface="brand"</code>); <code>--video</code> es una foto con botón de play y el autor sobre la cita. El play abre el modal de video de la Etapa 3 (aquí lleva <code>data-video-id</code>).',
  desc_md='Reseña en `<figure>`: cita y autor. La de texto va en petróleo; `--video` es una foto con botón de play (`data-video-id`).',
  blocks=[
    dict(label='De texto', surface='inverse', mods='cards', html=testi_text('h1-testimonial-thumb-img-1.webp', 'James Anderson', 'Entrepreneur, Brand Strategist', 'We were struggling with operational challenges before partnering with this consulting firm. Their expertise and hands-on support.')
        + '\n' + testi_text('h1-testimonial-thumb-img-2.webp', 'David Thompson', 'Sales Director, HR Consultant', 'Their professional guidance gave us a clear direction for expanding our business. From financial planning to market strategy.')),
    dict(label='En video (<code>--video</code>)', surface='inverse', mods='medium', html=d('''
      <figure class="card-photo card-testimonial card-testimonial--video" data-surface="inverse">
        <img class="card-photo__img" src="%sh1-testimonial-large-img-2.webp" alt="" width="1048" height="920" loading="lazy">
        <button type="button" class="icon-btn icon-btn--glass icon-btn--lg card-testimonial__play" aria-label="Play video testimonial from Isabella Harris" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Video testimonial from Isabella Harris">%s</button>
        <div class="card-testimonial__body">
          <figcaption class="card-testimonial__footer">
            <p class="card-testimonial__author"><span><span class="card-testimonial__name">Isabella Harris,</span> CEO &amp; Founder</span></p>
            <hr class="divider divider--inverse">
          </figcaption>
          <blockquote class="card-testimonial__quote">
            <p>“Working with this consulting team completely transformed our business operations.”</p>
          </blockquote>
        </div>
      </figure>''' % (IMG, ic('play')))),
  ],
  rows=[('.card-testimonial', 'Contenedor del testimonio (figure); en la de texto, cita arriba y autor abajo'),
        ('.card-testimonial__quote', 'La cita en 24px medium; es un blockquote'),
        ('.card-testimonial__footer', 'Divisor + autor (figcaption)'),
        ('.card-testimonial__name', 'Nombre del autor en amarillo; el cargo va en blanco a continuación'),
        ('.card-testimonial--video', 'Versión en foto (con card-photo): play centrado y autor sobre la cita'),
        ('data-video-id / data-video-title', 'ID y título del video de YouTube: el botón abre el Video Modal (organismo)')],
  tokens=['--color-action-primary (via data-surface="brand")', '--color-text-inverse / -highlight', '--color-overlay-light (divisor)', '--text-h4', '--leading-normal', '--radius-lg', '--spacing-4 / -5 / -6 / -8', '--scrim (card-photo)'],
  a11y='Cita y autor usan la semántica de <code>figure</code>, <code>blockquote</code> y <code>figcaption</code>. El botón de play lleva un <code>aria-label</code> con el nombre del autor. El texto sobre la foto va sobre un velo del 92% abajo, así que el contraste no depende de la imagen.',
  a11y_md='`figure`/`blockquote`/`figcaption`; play con `aria-label`; texto sobre velo de 92%.',
  decisions=['El video del diseño es el de YouTube indicado por el equipo (`RqueNBILfVU`); lo reproduce el organismo Video Modal.',
             'En el diseño el avatar del autor de texto es un retrato cuadrado de 75px; aquí usa el átomo `avatar--portrait` (80px).']))

M.append(dict(id='card-team', title='Card Team',
  desc='Foto de un miembro del equipo con su rol arriba a la izquierda, una acción arriba a la derecha y el nombre abajo. <code>--elevated</code> sube la card 20px por encima y por debajo de sus vecinas desde <code>lg</code> (la card central del diseño, siempre destacada). <code>--profile</code> es la variante clara de About Us: card blanca con la foto arriba y, debajo, nombre, cargo y redes (<code>--reverse</code> invierte el orden desde <code>lg</code>).',
  desc_md='Foto con rol (badge), acción («+») y nombre. `--elevated` sube la card 20px desde lg.',
  blocks=[dict(label='Tres cards, la central elevada', mods='cards', html=
        team('h1-team-member-img-1.webp', 'Financial Advisor', 'Olivia Bennet')
        + '\n' + team('h1-team-member-img-2.webp', 'Business Analyst', 'Emma Wilson', True)
        + '\n' + team('h1-team-member-img-3.webp', 'Corporate Trainer', 'Michael Turner')),
          dict(label='--profile (About Us), la central con --reverse', mods='cards', html=
        profile('h1-team-member-img-1.webp', 'Financial Advisor', 'Olivia Bennet')
        + '\n' + profile('h1-team-member-img-2.webp', 'Business Analyst', 'Emma Wilson', True)
        + '\n' + profile('h1-team-member-img-3.webp', 'Corporate Trainer', 'Michael Turner'))],
  rows=[('.card-photo', 'Patrón base: foto + velo + contenido en la misma celda (con data-surface="inverse")'),
        ('.card-team--profile', 'Variante clara: card blanca con marco de 12px, foto arriba, nombre, cargo y redes'),
        ('.card-team--reverse', 'Con --profile: texto arriba y foto abajo desde lg'),
        ('a.card-team__social + aria-label', 'Red social con área de 32px; el nombre dice persona y red («Olivia Bennet on LinkedIn»)'),
        ('.card-team__top', 'Fila superior: badge de rol y botón «+»'),
        ('.card-team__name', 'Nombre (h3) centrado abajo'),
        ('.card-team--elevated', 'Margen negativo de 20px desde lg y botón «+» amarillo')],
  tokens=['--radius-lg', '--scrim (degradé inferior)', '--color-background-inverse', '--spacing-3 / -5', '--text-h4', '--weight-medium'],
  a11y='El «+» es un enlace al perfil con <code>aria-label</code> que nombra a la persona («View profile of Olivia Bennet»). La foto es decorativa porque el nombre ya está en el <code>&lt;h3&gt;</code>. El anillo de foco es amarillo gracias a <code>data-surface="inverse"</code>. En <code>--profile</code> cada red es un enlace nombrado con la persona y la red («Olivia Bennet on LinkedIn») y mide 32px, por encima del mínimo de 24px de WCAG 2.5.8.',
  a11y_md='«+» como enlace con `aria-label` que nombra a la persona; foto decorativa; foco amarillo.',
  decisions=['El diseño no dice qué hace el «+»: se implementa como enlace al perfil (el menú Pages incluye «Team Members»). Pendiente de confirmar.',
             'La elevación es margen negativo, no `transform`, para que la card crezca y no se solape con las vecinas; la Section reserva el espacio.']))

M.append(dict(id='card-post', title='Card Post',
  desc='Entrada del blog: foto con la fecha encima, título, extracto y «Read More». El texto lleva sangría respecto a la foto. El enlace agrega, oculto, el título del post para distinguirlo de los otros «Read More».',
  desc_md='Entrada del blog: foto con fecha, título, extracto y «Read More» (con el título oculto para lectores).',
  blocks=[dict(label='Dos posts', mods='cards', html=
        post('h1-blog-img-1.webp', '2026-10-21', '21 Oct, 2026', 'How Consulting Improves Business Performance', 'With expert advice &amp; customized solutions, businesses can strengthen their competitive position', 'how consulting improves business performance')
        + '\n' + post('h1-blog-img-2.webp', '2026-10-18', '18 Oct, 2026', 'Effective Financial Planning for Sustainable Growth', 'Strong financial planning also supports investment in innovation, team development.', 'effective financial planning for sustainable growth'))],
  rows=[('.card-post__media', 'Foto 4:3 con esquinas redondeadas (la fuente es 1308×600; se recorta con cover)'),
        ('.card-post__date', 'Posiciona el badge de fecha sobre la foto (usa badge--marker)'),
        ('.card-post__body', 'Título (h3), extracto y enlace; sangría lateral de 20px')],
  tokens=['--radius-lg', '--spacing-3 / -4 / -5', '--text-h4', '--weight-medium'],
  a11y='La fecha está en <code>&lt;time datetime&gt;</code>. El «Read More» incluye texto <code>visually-hidden</code> con el título, así un lector de pantalla oye «Read More about how consulting improves…».',
  a11y_md='Fecha en `<time datetime>`; «Read More» con título oculto.',
  decisions=['El diseño recorta la foto a ~1.38:1; se usa 4:3 (estándar) en vez de un número suelto.']))

M.append(dict(id='card-project', title='Card Project',
  desc='Proyecto del bloque Finance / Advisory / Growth / Strategy: foto con marco blanco y, debajo, un número decorativo («// 01») y el título. La Section cambia de card al hacer scroll (Etapa 3).',
  desc_md='Proyecto del bloque Finance: foto con marco blanco, número decorativo y título.',
  blocks=[dict(label='Dos proyectos', mods='cards', html=d('''
      <article class="card-project">
        <img class="card-project__img" src="%sh1-portfolio-img-3.webp" alt="" width="1920" height="1084" loading="lazy">
        <div class="card-project__caption">
          <span class="card-project__index" aria-hidden="true">// 01</span>
          <h3 class="card-project__title">Corporate Finance Management</h3>
        </div>
      </article>
      <article class="card-project">
        <img class="card-project__img" src="%sh1-portfolio-img-1.webp" alt="" width="1920" height="1076" loading="lazy">
        <div class="card-project__caption">
          <span class="card-project__index" aria-hidden="true">// 02</span>
          <h3 class="card-project__title">Advisory Services</h3>
        </div>
      </article>''' % (IMG, IMG)))],
  rows=[('.card-project', 'Card blanca con marco de 12px alrededor de la foto'),
        ('.card-project__img', 'Foto 10:7 con esquinas redondeadas'),
        ('.card-project__index', 'Número decorativo («// 01»), aria-hidden'),
        ('.card-project__title', 'Título del proyecto (h3)')],
  tokens=['--color-surface-default', '--shadow-sm', '--radius-lg / -md', '--spacing-3 / -4 / -5', '--text-sm / -h4', '--color-text-tertiary'],
  a11y='El número es decorativo (<code>aria-hidden</code>); el título es un <code>&lt;h3&gt;</code>. La foto es decorativa.',
  a11y_md='Número `aria-hidden`; título `h3`; foto decorativa.',
  decisions=['En mobile el diseño muestra el título de una card en amarillo sobre claro (1.4:1): no se replica, no pasa contraste.',
             'Solo hay una foto de proyecto fiel al diseño (la de las notas adhesivas); las demás son placeholders del set de portfolio.']))

M.append(dict(id='card-cta', title='Card CTA',
  desc='Card con foto de fondo y una invitación a contactar: ícono arriba y, abajo, título, texto y enlace amarillo. Se usa en la FAQ («Still have questions?»). <code>--stacked</code> es la variante clara de About Us: card blanca con la foto arriba y el enlace en el color normal.',
  desc_md='Card con foto: ícono arriba; título, texto y enlace amarillo abajo (FAQ).',
  blocks=[dict(label='Sobre foto', mods='narrow', html=d('''
      <article class="card-photo card-cta" data-surface="inverse">
        <img class="card-photo__img" src="%sh1-cta-img.webp" alt="" width="1040" height="700" loading="lazy">
        <div class="card-cta__body">
          <span class="card-cta__icon">%s</span>
          <div class="card-cta__text">
            <h3 class="card-cta__title">Still have questions?</h3>
            <p>Our results-focused strategies are designed to deliver measurable business growth</p>
            <a href="#card-cta" class="link-arrow link-arrow--highlight">
              Contact Us
              %s
            </a>
          </div>
        </div>
      </article>''' % (IMG, ic('hexagon'), ic('arrow-up-right')))),
          dict(label='--stacked (FAQ de About Us)', mods='narrow', html=d('''
      <article class="card-cta card-cta--stacked">
        <img class="card-cta__photo" src="%sh2-cta-img.webp" alt="" width="848" height="740" loading="lazy">
        <div class="card-cta__text">
          <h3 class="card-cta__title">Still have questions?</h3>
          <p>Our results-focused strategies are designed to deliver measurable business growth</p>
          <a href="#card-cta" class="link-arrow">
            Contact Us
            %s
          </a>
        </div>
      </article>''' % (IMG, ic('arrow-up-right'))))],
  rows=[('.card-photo', 'Patrón base con foto, velo y contenido (con data-surface="inverse")'),
        ('.card-cta--stacked + img.card-cta__photo', 'Variante clara: foto arriba en el flujo, sin ícono; enlace en el color normal'),
        ('.card-cta__icon', 'Círculo translúcido con ícono'),
        ('.card-cta__text', 'Título (h3), texto y enlace amarillo')],
  tokens=['--radius-lg', '--scrim (velo del 45% al 90%)', '--color-overlay-light', '--color-text-highlight (enlace)', '--text-h4', '--spacing-3 / -6 / -8 / -9'],
  a11y='El texto va sobre un velo de entre el 45% y el 90% del fondo oscuro; abajo, donde está el texto, es el más opaco. El enlace amarillo se usa solo porque el fondo es oscuro (9:1).',
  a11y_md='Texto sobre velo del 45–90%; enlace amarillo solo sobre oscuro.',
  decisions=['El ícono del diseño (poliedro) es un Lucide `hexagon` equivalente.']))

M.append(dict(id='card-hero', title='Card Hero',
  desc='Tarjeta translúcida sobre la foto del hero con una miniatura, un número y el título. Es estática (no enlaza): así lo indicó el equipo.',
  desc_md='Tarjeta translúcida del hero: miniatura, número y título. Estática, no enlaza.',
  blocks=[dict(label='Sobre foto', mods='narrow photo', html=d('''
      <div class="card-hero">
        <img class="card-hero__media" src="%sh1-hero-thumb-img.webp" alt="" width="160" height="182" loading="lazy">
        <div class="card-hero__body">
          <span class="card-hero__index">01</span>
          <p class="card-hero__title">Creative Business Insights</p>
        </div>
      </div>''' % IMG))],
  rows=[('.card-hero', 'Fila con miniatura y texto sobre el velo oscuro del theme (--color-overlay) con borde translúcido'),
        ('.card-hero__media', 'Miniatura de 160px de ancho'),
        ('.card-hero__index', 'Número en amarillo'),
        ('.card-hero__title', 'Título en 24px medium; es un párrafo, no un encabezado')],
  tokens=['--color-overlay / --color-overlay-light (borde)', '--color-text-inverse / -highlight', '--radius-md / -sm', '--spacing-2 / -3 / -4 / -11', '--text-h4'],
  a11y='Es un contenedor sin interacción; el título es un <code>&lt;p&gt;</code> para no competir con el <code>&lt;h1&gt;</code> del hero. El velo del 65% da ≥5:1 al texto blanco sobre cualquier foto, así que no depende del hero.',
  a11y_md='Sin interacción; título `p` (no compite con el `h1`); el hero aporta el velo.',
  decisions=['El diseño muestra la tarjeta con un velo teñido de petróleo; se usa el `--color-overlay` del theme (el mismo de los badges) en vez de un blanco al 10%, que no daba lectura sobre fotos claras.']))

M.append(dict(id='stat', title='Stat',
  desc='Cifra grande con su etiqueta. El sufijo («+») va atenuado. Alineada a la izquierda en «What We Do» y con <code>--center</code> en la sección de números de mobile.',
  desc_md='Cifra grande con etiqueta; el sufijo va atenuado. `--center` para la versión centrada.',
  blocks=[
    dict(label='A la izquierda', html=d('''
      <div class="stat">
        <p class="stat__value">3M<span class="stat__suffix">+</span></p>
        <p>People Using Our Platform</p>
      </div>''')),
    dict(label='Centrada (<code>--center</code>)', mods='narrow', html=d('''
      <div class="stat stat--center">
        <p class="stat__value">98%</p>
        <p>Excellence in Customer Satisfaction</p>
      </div>
      <div class="stat stat--center">
        <p class="stat__value">12K<span class="stat__suffix">+</span></p>
        <p>Projects Successfully Finished</p>
      </div>''')),
  ],
  rows=[('.stat', 'Cifra arriba y etiqueta abajo'),
        ('.stat__value', 'La cifra en Mona Sans semibold del tamaño de h1'),
        ('.stat__suffix', 'Sufijo atenuado (tertiary); sigue siendo texto: el lector lo lee'),
        ('.stat--center', 'Centra el texto')],
  tokens=['--text-h1', '--weight-semibold', '--color-text-primary / -tertiary / -secondary', '--spacing-2'],
  a11y='La cifra y la etiqueta son texto real. El sufijo atenuado (5.1:1) cumple AA; no se oculta ni se dibuja con CSS, así «3M+» se lee completo.',
  a11y_md='Texto real; sufijo atenuado cumple AA.',
  decisions=['Las etiquetas «Excellence in Customer Satisfaction» y «Projects Successfully Finished» están cortadas en el diseño de mobile; se completaron como placeholder.']))

M.append(dict(id='accordion-item', title='Accordion Item',
  desc='Pregunta de la FAQ sobre un <code>&lt;details&gt;</code> nativo: abre con Enter o Espacio sin JavaScript y, si los ítems comparten el atributo <code>name</code>, solo uno queda abierto. El «?» y el +/− son decorativos.',
  desc_md='Pregunta de la FAQ sobre `<details>` nativo; con el mismo `name` solo uno queda abierto. Sin JS.',
  blocks=[dict(label='Grupo de tres (el segundo abierto)', mods='narrow-wide', html=
        faq(False, 'How can consulting help my business grow?', 'Consulting brings an outside view, proven methods and focused support, so you can find opportunities and act on them faster.')
        + '\n' + faq(True, 'What industries do you specialize in?', 'Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.')
        + '\n' + faq(False, 'What services do business consultants provide?', 'We offer strategy, process optimization, sales improvement and financial advisory.'))],
  rows=[('.accordion-item', '&lt;details&gt; con un filete inferior'),
        ('.accordion-item__summary', '&lt;summary&gt;: fila con «?», la pregunta y el +/−'),
        ('.accordion-item__mark', 'Círculo con «?»: gris cerrado, amarillo abierto'),
        ('.accordion-item__toggle', 'Muestra «+» cerrado y «−» abierto (CSS puro)'),
        ('.accordion-item__panel', 'Respuesta, alineada bajo el texto de la pregunta'),
        ('name="…" / open', 'Mismo name en varios ítems = acordeón exclusivo; open abre uno por defecto')],
  tokens=['--color-border-subtle', '--color-background-subtle', '--color-action-secondary / -on-secondary', '--text-h5', '--weight-medium', '--spacing-5 / -6 / -8', '--ease-base'],
  a11y='El <code>&lt;summary&gt;</code> es el botón: se llega con Tab y el navegador anuncia «expandido/contraído» sin ARIA. La fila entera es el área de clic (más de 48px de alto). El «?» y el +/− son <code>aria-hidden</code>. El estado no depende solo del amarillo: cambia también el ícono.',
  a11y_md='`<summary>` nativo: Tab, Enter/Espacio y estado anunciado sin ARIA; fila de 48px+; +/− cambia con el estado.',
  decisions=['Pregunta semibold de 24px desde lg y 18px en mobile (el diseño mide ~20px; con 18 los cortes de línea coinciden), con 32px de separación del «?» (20px en mobile): medido en los PNG a resolución real (Etapa 4, Grupo C); antes, 22px medium en todos los anchos.',
             'Se usa `<details name>` nativo en lugar del `<button aria-expanded>` con JS que planteaba el plan: es exclusivo, accesible y no necesita script. Si hace falta animar la altura, se agrega después con `::details-content`.',
             'La copia del diseño escribe «in ?»; se normalizó a «in?».']))

M.append(dict(id='newsletter', title='Newsletter',
  desc='Formulario de suscripción: la frase es el <code>&lt;label&gt;</code> del campo y el botón de envío va dentro del filete. Está pensado para el footer oscuro (<code>data-surface="inverse"</code>).',
  desc_md='Formulario de suscripción: la frase es el `<label>` del campo; el botón de envío va dentro del filete.',
  blocks=[dict(label='Sobre fondo oscuro', surface='inverse', mods='narrow', html=d('''
      <form class="newsletter" action="#">
        <label class="newsletter__title" for="newsletter-email">Subscribe our newsletter to get latest updates</label>
        <div class="newsletter__field">
          <input class="input" type="email" id="newsletter-email" name="email" placeholder="Enter your email" autocomplete="email" required>
          <button type="submit" class="newsletter__submit" aria-label="Subscribe">%s</button>
        </div>
      </form>''' % ic('send')))],
  rows=[('.newsletter', 'Formulario: frase arriba, campo abajo'),
        ('.newsletter__title', 'El label del campo, con aspecto de título de 24px'),
        ('.newsletter__field', 'Posiciona el botón dentro del filete del input'),
        ('.newsletter__submit', 'Botón de envío sin caja; se pone amarillo en hover')],
  tokens=['--color-text-inverse / -inverse-secondary / -highlight', '--text-h4 / -h6', '--weight-medium', '--spacing-5 / -8 / -9', '--ease-fast'],
  a11y='La frase es el <code>&lt;label for&gt;</code> del campo, así el nombre accesible es visible. El botón tiene <code>aria-label</code> y 40px de lado. Falta definir el aviso de éxito o error: cuando exista backend, se anuncia con <code>role="status"</code> sin robar el foco.',
  a11y_md='La frase es el `<label for>`; botón con `aria-label`; el aviso de resultado va con `role="status"`.',
  decisions=['`align-content: start`: en la fila del footer (más alta que el formulario) el campo quedaba separado del título (Etapa 4, Grupo C).',
             'El sitio es estático y sin backend: el `action` queda en `#` y el envío se conecta por proyecto (servicio de formularios o email).']))

SERVICES = ['Strategic Planning', 'Business Optimization', 'IT Consulting', 'Change Management', 'Leadership']

def quote_form(fid, action, live=False, state='', outline=False):
    # state: '' | 'error' | 'sending' | 'sent' | 'failed' — solo para mostrar estados estáticos en el kit
    # outline: variante de Service Details (campos --filled, campo Service, textos del aside)
    err = state == 'error'
    filled = state in ('sending', 'failed')

    def field(name, label, kind, auto, value='', error=''):
        inv = ' aria-invalid="true"' if error else ''
        attrs = 'id="%s-%s" name="%s" placeholder=" " required aria-describedby="%s-%s-error"%s' % (fid, name, name, fid, name, inv)
        wrap = 'field field--filled' if outline else 'field'
        cls = 'input input--filled field__control' if outline else 'input field__control'
        if kind == 'textarea':
            control = '<textarea class="%s" %s>%s</textarea>' % (cls, attrs, value)
        else:
            val = ' value="%s"' % value if value else ''
            extra = ' pattern="[\\d\\s+\\(\\)\\-]{6,}"' if kind == 'tel' else ''
            control = '<input class="%s" type="%s" %s autocomplete="%s"%s%s>' % (cls, kind, attrs, auto, extra, val)
        return '\n'.join(['  <div class="%s">' % wrap,
                          '    <label class="field__label" for="%s-%s">%s<span aria-hidden="true">*</span></label>' % (fid, name, label),
                          '    ' + control,
                          '    <p class="field__error" id="%s-%s-error">%s</p>' % (fid, name, error),
                          '  </div>'])

    def service_field():
        options = '\n'.join('      <option%s>%s</option>' % (' selected' if filled and s == 'Business Optimization' else '', s) for s in SERVICES)
        inv = ' aria-invalid="true"' if err else ''
        return '\n'.join(['  <div class="field field--filled field--select">',
                          '    <label class="field__label" for="%s-service">Service<span aria-hidden="true">*</span></label>' % fid,
                          '    <select class="input input--filled field__control" id="%s-service" name="service" required aria-describedby="%s-service-error"%s>' % (fid, fid, inv),
                          '      <option value="" hidden%s></option>' % ('' if filled else ' selected'),
                          options,
                          '    </select>',
                          '    <p class="field__error" id="%s-service-error">%s</p>' % (fid, 'Choose an option.' if err else ''),
                          '  </div>'])

    busy = ' aria-disabled="true"' if state == 'sending' else ''
    title = 'Get a Quote' if outline else 'Get a free Quote'
    label = 'Sending…' if state == 'sending' else ('Submit Now' if outline else 'Get Started')
    # Cada formulario con nombre es un landmark: en el kit, los demos de estado llevan un nombre propio
    # para no repetir el del demo en vivo (axe: landmark-unique). En la página va aria-labelledby al título.
    examples = {'error': 'validation error', 'sending': 'sending', 'sent': 'sent', 'failed': 'send error'}
    name = ' aria-label="%s, %s example"' % (title, examples[state]) if state else ' aria-labelledby="%s-title"' % fid
    lines = [
        '<form class="quote-form%s" id="%s-form"%s action="%s" method="post" novalidate%s>' % (' quote-form--outline' if outline else '', fid, ' data-quote-form' if live else '', action, name),
        '  <h3 class="quote-form__title" id="%s-title">%s</h3>' % (fid, title),
        '  <input type="hidden" name="_subject" value="New quote request from esonix.example">',
        '  <div hidden><label for="%s-honey">Leave this field empty</label><input type="text" id="%s-honey" name="_honey" tabindex="-1" autocomplete="off"></div>' % (fid, fid),
        field('name', 'Name' if outline else 'Your name', 'text', 'name', 'Emma Wilson' if filled else '', 'This field is required.' if err else ''),
        field('email', 'Email' if outline else 'Your email', 'email', 'email', 'emma@company.com' if filled else ('emma@' if err else ''), 'Enter a valid email address.' if err else ''),
        field('phone', 'Phone' if outline else 'Phone number', 'tel', 'tel', '+1 (555) 123 4567' if filled else ''),
    ]
    if outline:
        lines.append(service_field())
    lines += [
        field('message', 'Message', 'textarea', '', 'We need help with our pricing strategy.' if filled else ''),
        '  <button type="submit" class="btn quote-form__submit"%s>' % busy,
        '    <span data-submit-label>%s</span>' % label,
        '    <span class="btn__icon">%s</span>' % ic('arrow-up-right'),
        '  </button>',
        '  <div class="quote-form__messages">',
        '    <p class="quote-form__status" role="status" data-form-status>%s</p>' % ('Thanks! Your message was sent. We will get back to you soon.' if state == 'sent' else ''),
        '    <p class="quote-form__alert" role="alert" data-form-alert>%s</p>' % ('Your message could not be sent. Please check your connection and try again.' if state == 'failed' else ''),
        '  </div>',
        '</form>']
    return '\n'.join(lines)

M.append(dict(id='quote-form', title='Quote Form',
  desc='Formulario «Get a free Quote» de About Us: card blanca con cuatro <a href="#field">Field</a> y el botón. Funciona sin JS (envío normal a FormSubmit); con JS, <code>main.js</code> valida, envía por <code>fetch</code> sin salir de la página y muestra los estados. El destino es el <code>action</code> del HTML.',
  desc_md='Card con 4 Field y botón. Sin JS envía normal a FormSubmit; con JS valida, envía por fetch y muestra estados. Destino = `action`.',
  blocks=[
    dict(label='En vivo: la validación es real; sin destino, el envío termina en el estado de error', mods='narrow', html=quote_form('quote-demo', '#kit-demo', live=True)),
    dict(label='Error de validación', mods='narrow', html=quote_form('quote-error', '#', state='error')),
    dict(label='Enviando', mods='narrow', html=quote_form('quote-sending', '#', state='sending')),
    dict(label='Enviado', mods='narrow', html=quote_form('quote-sent', '#', state='sent')),
    dict(label='Error de envío', mods='narrow', html=quote_form('quote-failed', '#', state='failed')),
    dict(label='--outline con campos --filled y Select (Service Details)', mods='narrow', html=quote_form('quote-outline', '#', state='error', outline=True)),
  ],
  rows=[('form.quote-form[data-quote-form]', 'Activa el envío por fetch y la validación de main.js'),
        ('action="https://formsubmit.co/&lt;destino&gt;" method="post" novalidate', 'Destino (sin JS, envío normal); novalidate deja la validación a main.js'),
        ('.quote-form--outline', 'Card con borde, sin fondo ni sombra; título de 24px (aside de Service Details)'),
        ('.field--filled / .field--select', 'Campos en caja gris y el Select «Service» (ver Field y Select)'),
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
             'El teléfono acepta dígitos, espacios, `+`, paréntesis y guiones (mínimo 6).',
             '--outline usa campos --filled: el diseño de Service Details los muestra en caja gris, con el filete inferior fuerte por contraste (decisión del usuario).']))

M.append(dict(id='service-nav', title='Service Nav',
  desc='«Exclusive Services» de Service Details: card con borde, título y la lista de servicios en píldoras con un cuadrado de flecha. La página actual va marcada con <code>aria-current="page"</code> (petróleo con el cuadrado ámbar).',
  desc_md='Card con la lista de servicios en píldoras; la actual con `aria-current="page"` (petróleo, cuadrado ámbar).',
  blocks=[
    dict(label='Con el servicio actual marcado', mods='narrow', html=d('''
      <nav class="service-nav" aria-labelledby="service-nav-demo-title">
        <h3 class="service-nav__title" id="service-nav-demo-title">Exclusive Services</h3>
        <ul class="service-nav__list" role="list">
          <li><a class="service-nav__link" href="#">Strategic Planning<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#" aria-current="page">Business Optimization<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">IT Consulting<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Change Management<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Leadership<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
        </ul>
      </nav>''')),
  ],
  rows=[('nav.service-nav + aria-labelledby', 'Landmark de navegación nombrado por su título'),
        ('.service-nav__title', 'Título de 24px; h2 en la página (aside), h3 en el kit'),
        ('ul.service-nav__list + role="list"', 'La lista de servicios'),
        ('a.service-nav__link', 'Píldora gris con el texto y el cuadrado de flecha'),
        ('aria-current="page"', 'Servicio de la página actual: petróleo y cuadrado ámbar'),
        ('.service-nav__icon', 'Cuadrado blanco con icon--arrow-right; ámbar en hover y en el actual')],
  tokens=['--color-border-default / -subtle', '--color-background-subtle', '--color-action-primary / -on-primary', '--color-action-secondary / -on-secondary', '--color-surface-default', '--radius-md / -sm / -xs', '--text-h4', '--weight-medium / -semibold', '--spacing-2 / -4 / -5 / -6 / -8', '--ease-fast'],
  a11y='Es un <code>&lt;nav&gt;</code> nombrado por su título, distinto del menú principal. El servicio actual se anuncia con <code>aria-current="page"</code>, no solo por color. Las flechas son decorativas. El texto blanco sobre petróleo pasa AA; el foco usa el anillo del theme por fuera de la píldora (visible también sobre la activa).',
  a11y_md='`<nav>` nombrado por su título; actual con `aria-current="page"`; flechas `aria-hidden`; foco del theme por fuera de la píldora.',
  decisions=['El diseño no muestra el hover: el cuadrado toma el ámbar del activo, sin cambiar el fondo de la píldora.',
             'En la página, los servicios que todavía no tienen página enlazan a `#`; Business Optimization enlaza a `service-details.html`.']))

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
    return '\n'.join(['          <div class="kit-block">', '            <span class="kit-block__label">%s</span>' % b['label'],
                      '            <div class="kit-demo%s"%s lang="en">' % (mods, surf), indent(b['html'], 14), '            </div>',
                      indent(snippet(sid), 12), '          </div>'])

def card(a, n):
    p = ['        <section class="kit-card" id="%s" aria-labelledby="%s-title">' % (a['id'], a['id']), '          <header class="kit-card__header">',
         '            <p class="kit-card__tag">Molécula · %02d</p>' % n, '            <h3 id="%s-title">%s</h3>' % (a['id'], a['title']),
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

cards = '\n\n'.join(card(a, i) for i, a in enumerate(M, 1))
level = ('      <section class="kit-level" id="molecules" aria-labelledby="molecules-title">\n        <h2 id="molecules-title">Moléculas</h2>\n'
         '        <p class="kit-level__intro">Componen dos a cuatro átomos y no conocen el contexto de página: no hacen fetch ni asumen un layout. Las cards destacadas usan <code>data-surface="brand"</code>; las que van sobre foto usan el patrón <code>card-photo</code> con <code>data-surface="inverse"</code>.</p>\n'
         + cards + '\n        <!-- kit:molecules-end -->\n      </section>')
nav_items = '\n'.join('            <li><a class="kit-nav__link" href="#%s"><span class="kit-nav__num">%02d</span> %s</a></li>' % (a['id'], i, a['title']) for i, a in enumerate(M, 1))
nav = ('        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-molecules">Moléculas</p>\n'
       '          <ul class="kit-nav__list" aria-labelledby="nav-molecules">\n' + nav_items + '\n          </ul>\n        </div>')

page = open(KIT, encoding='utf-8').read()
pat = re.compile(r'      <section class="kit-level" id="molecules".*?(?=\n\n      <section class="kit-level" id="organisms")', re.S)
assert pat.search(page)
page = pat.sub(lambda m: level, page, count=1)
if 'id="nav-molecules"' in page:
    page = re.sub(r'        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-molecules">.*?\n        </div>', lambda m: nav, page, count=1, flags=re.S)
else:
    old = '        <div class="kit-nav__group">\n          <p class="kit-nav__group-label">Moléculas</p>\n          <p class="kit-nav__empty">Sin componentes aún</p>\n        </div>'
    assert page.count(old) == 1
    page = page.replace(old, nav)

# Foundations › Colors: la superficie brand
if 'data-surface="brand"</code> es el petróleo' not in page:
    anchor = '            <p class="kit-note">El gris de párrafos del diseño'
    assert page.count(anchor) == 1
    note = ('            <p class="kit-note"><code>data-surface="inverse"</code> (fondo <code>--color-background-inverse</code>) es para bloques oscuros full-bleed y '
            '<code>data-surface="brand"</code> es el petróleo de las cards destacadas (<code>--color-action-primary</code>). Las dos reasignan el foco a amarillo y '
            'dan lectura a titulares y enlaces de todo su árbol.</p>\n')
    page = page.replace(anchor, note + anchor)
    page = page.replace('<span class="kit-block__label">Foco y superficie inversa</span>', '<span class="kit-block__label">Foco y superficies oscuras (inverse y brand)</span>')
open(KIT, 'w', encoding='utf-8', newline='\n').write(page)

# ------------------------------------------------------------------ kit.css
css = open(KITCSS, encoding='utf-8').read()
if '/* molecules-kit:start */' not in css:
    css = css.replace('  --kit-icon-min: 8.5rem;\n', '  --kit-icon-min: 8.5rem;\n  --kit-card-min: 17rem;\n  --kit-wide: 44rem;\n  --kit-medium: 33rem;\n', 1)
    add = '''
/* molecules-kit:start */
/* Demos de moléculas: grilla de cards y columna ancha para el acordeón */
.kit-demo--cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--kit-card-min)), 1fr));
  gap: var(--spacing-5);
  align-items: stretch;
}
.kit-demo--narrow-wide {
  max-inline-size: var(--kit-wide);
}
.kit-demo--medium {
  max-inline-size: var(--kit-medium);
}
/* molecules-kit:end */
'''
    css = css.replace('/* kit:css-end */', add + '/* kit:css-end */')
    open(KITCSS, 'w', encoding='utf-8', newline='\n').write(css)

# ------------------------------------------------------------------ stories.md
def unesc(s): return H.unescape(re.sub(r'</?(code|strong|em)>', lambda m: '`' if m.group(1) == 'code' else ('**' if m.group(1) == 'strong' else '*'), s))
os.makedirs(STORIES, exist_ok=True)
for n, a in enumerate(M, 1):
    md = ['# %s' % a['title'], '', '**Nivel:** Molécula · %02d  ' % n, '**Dónde:** `dist/assets/css/main.css` (bloque `/* %s */`) · showcase en `dist/kit/index.html#%s`' % (a['title'], a['id']), '',
          '## Descripción', '', unesc(a['desc_md']), '', '## Snippets', '']
    for b in a['blocks']:
        md += ['**%s**' % unesc(b['label']), '', '```html', H.unescape(b['html']), '```', '']
    md += ['## Clases y atributos', '', '| Clase o atributo | Efecto |', '|---|---|'] + ['| `%s` | %s |' % (H.unescape(s), unesc(t)) for s, t in a['rows']]
    md += ['', '## Tokens que consume', ''] + ['- `%s`' % t for t in a['tokens']]
    md += ['', '## Accesibilidad', '', unesc(a['a11y_md']), '', '## Decisiones y excepciones', ''] + ['- ' + x for x in a['decisions']] + ['']
    open(os.path.join(STORIES, a['id'] + '.stories.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(md))
print('ok:', len(M), 'moléculas')
