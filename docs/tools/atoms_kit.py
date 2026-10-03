# Genera las fichas de los átomos: dist/kit/index.html + docs/kit/<id>.stories.md (una sola fuente de datos).
import re, os, textwrap, html as H
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # raíz del proyecto (docs/tools/ → design-to-web/)
KIT = str(ROOT / 'dist' / 'kit' / 'index.html')
KITCSS = str(ROOT / 'dist' / 'assets' / 'css' / 'kit.css')
STORIES = str(ROOT / 'docs' / 'kit')

def d(s): return textwrap.dedent(s).strip('\n')
def ic(name): return '<span class="icon icon--%s" aria-hidden="true"></span>' % name
IMG = '../assets/img/'

ICON_NAMES = ['arrow-up-right', 'arrow-right', 'arrow-left', 'arrow-up', 'plus', 'minus', 'play', 'check', 'circle-check', 'circle-check-outline',
              'chevron-down', 'x', 'send', 'message-square', 'layout-grid', 'target', 'trending-up', 'chart-pie', 'users', 'lightbulb', 'rocket', 'gem', 'award', 'hexagon', 'facebook', 'linkedin', 'instagram', 'x-twitter']

# ---------------------------------------------------------------- datos
# block: label, html, surface ('inverse' | None), mods ('row' 'narrow' 'photo'), note
A = []

A.append(dict(id='icons', title='Icons', raw_icons=True,
  desc='Lucide como máscara CSS: la clase <code>.icon</code> hereda el color y el tamaño del contexto (<code>currentColor</code> y <code>1em</code>), así el snippet es una sola línea y no depende de rutas ni de un sprite. Las redes sociales no están en Lucide: son SVG propios del mismo estilo de trazo.',
  desc_md='Lucide como máscara CSS: `.icon` hereda color y tamaño del contexto. Las redes sociales no están en Lucide: son SVG propios del mismo trazo.',
  blocks=[dict(label='Uso', code=d('''
      <span class="icon icon--arrow-up-right" aria-hidden="true"></span>'''), id_suffix='usage')],
  rows=[('.icon', 'Base: cuadrado de 1em que pinta el glifo con el color del texto'),
        ('.icon--{nombre}', 'Elige el glifo (ver lista). Se agrega un modificador por ícono nuevo en main.css'),
        ('aria-hidden="true"', 'Siempre: el ícono es decorativo y el nombre accesible lo da el texto o el aria-label del contenedor')],
  tokens=['--text-body (tamaño heredado)', '--color-text-primary (color heredado)'],
  a11y='Un ícono suelto nunca es el único portador de significado: el botón o enlace que lo contiene lleva texto o <code>aria-label</code>. En modo de colores forzados (Windows alto contraste) el ícono pasa a <code>CanvasText</code>.',
  a11y_md='Un ícono nunca es el único portador de significado: el contenedor lleva texto o `aria-label`. En colores forzados pasa a `CanvasText`.',
  decisions=['Lucide es la única librería de iconos permitida; los glifos de redes (facebook, linkedin, instagram, x-twitter) son propios porque Lucide no incluye logos de marca.',
             '`circle-check` es un círculo relleno con la marca recortada (máscara interna), como el check de las listas de pricing; Lucide solo trae la versión de contorno.',
             '`play` va relleno (el diseño lo muestra sólido).',
             '`badge-check` (Document Required de Service Details) es el sello con la marca; `circle-check-outline`, el círculo con la marca en contorno.']))

A.append(dict(id='button', title='Button',
  desc='Píldora de texto con un círculo de ícono a la derecha. Por defecto va en petróleo sobre fondo claro; <code>--light</code> es la versión para fondos oscuros; <code>--block</code> ocupa el ancho de su card (pricing) y <code>--accent</code> es su relleno amarillo. Funciona como <code>&lt;button&gt;</code> o como <code>&lt;a&gt;</code>.',
  desc_md='Píldora de texto con círculo de ícono. Petróleo sobre fondo claro; `--light` para fondo oscuro; `--block` para el ancho de una card; `--accent` el relleno amarillo. `<button>` o `<a>`.',
  blocks=[
    dict(label='Sobre fondo claro', mods='row', html=d('''
      <button type="button" class="btn">
        Get Started
        <span class="btn__icon">%s</span>
      </button>
      <a href="#button" class="btn">
        Learn More
        <span class="btn__icon">%s</span>
      </a>''' % (ic('arrow-up-right'), ic('arrow-up-right')))),
    dict(label='Sobre fondo oscuro (<code>btn--light</code>)', surface='inverse', mods='row', html=d('''
      <button type="button" class="btn btn--light">
        Get Started
        <span class="btn__icon">%s</span>
      </button>''' % ic('arrow-up-right'))),
    dict(label='Ancho de card (<code>btn--block</code>) y su relleno amarillo (<code>btn--accent</code>)', mods='narrow', html=d('''
      <button type="button" class="btn btn--block">
        Get Started
        %s
      </button>
      <button type="button" class="btn btn--block btn--accent">
        Get Started
        %s
      </button>''' % (ic('arrow-up-right'), ic('arrow-up-right')))),
    dict(label='Relleno amarillo con círculo (<code>btn--accent</code>, Contact)', mods='row', html=d('''
      <button type="button" class="btn btn--accent">
        Submit Now
        <span class="btn__icon">%s</span>
      </button>''' % ic('arrow-up-right'))),
    dict(label='Deshabilitado', mods='row', html=d('''
      <button type="button" class="btn" disabled>
        Get Started
        <span class="btn__icon">%s</span>
      </button>
      <button type="button" class="btn btn--block" disabled>
        Get Started
        %s
      </button>''' % (ic('arrow-up-right'), ic('arrow-up-right')))),
  ],
  rows=[('.btn', 'Píldora petróleo con texto blanco y círculo amarillo'),
        ('.btn__icon', 'Círculo de 40px que envuelve el ícono (solo en el botón con círculo)'),
        ('.btn--light', 'Para fondos oscuros: píldora blanca, círculo petróleo'),
        ('.btn--block', 'Ocupa todo el ancho, texto centrado y flecha en línea, sin círculo'),
        ('.btn--accent', 'Relleno amarillo con texto oscuro y círculo petróleo (Contact); con --block, sin círculo (plan destacado)'),
        ('disabled / aria-disabled="true"', 'Estado deshabilitado; en un &lt;a&gt; usar aria-disabled y quitar el href')],
  tokens=['--color-action-primary(-hover/-active/-disabled)', '--color-action-secondary(-hover)', '--color-action-on-primary', '--color-action-on-secondary', '--color-surface-default', '--color-background-subtle', '--spacing-1 / -5 / -6 / -8', '--radius-full', '--text-body', '--weight-medium', '--ease-fast'],
  a11y='El texto del botón dice qué pasa al activarlo («Get Started», no «Click here»). El ícono es <code>aria-hidden</code>. El foco usa el anillo global (amarillo sobre fondos oscuros). La altura mínima es 48px, muy por encima de los 24px exigidos.',
  a11y_md='Texto descriptivo; ícono `aria-hidden`; foco con el anillo global; altura 48px.',
  decisions=['Altura 48px (círculo de 40px + 4px de aire): el diseño mide ~52px, pero sale de la escala de espaciado y no de estimar la imagen.',
             'Los estados hover, active y disabled no están en el diseño: se derivan de los tokens `action-primary-hover/-active/-disabled` ya definidos.',
             'No hay variante `--light` + `--block`: el diseño solo usa `--block` sobre cards claras y la destacada oscura usa `--accent`.',
             'El círculo de `--accent` es petróleo: con el ámbar por defecto del botón quedaría ámbar sobre ámbar. El «Schedule a call» del header (`--accent` sin `--block`) redefine su propio círculo en blanco (`.site-header--inner .site-header__cta`) y no cambia con este ajuste.']))

A.append(dict(id='icon-button', title='Icon Button',
  desc='Círculo con un solo ícono. Por defecto de contorno sobre fondo claro (flechas del carrusel); <code>--glass</code> va sobre fotos y el amarillo marca hover y estado activo; <code>--sm</code> y <code>--lg</code> cubren el «+» del equipo y el play del video. También es el <strong>Social Icon</strong>: un <code>.icon-btn --sm</code> con el glifo de la red.',
  desc_md='Círculo con un ícono. Contorno sobre fondo claro; `--glass` sobre fotos; `--sm`/`--lg`. También es el Social Icon (`--sm` con glifo de red).',
  blocks=[
    dict(label='Contorno sobre fondo claro (flechas del carrusel)', mods='row', html=d('''
      <button type="button" class="icon-btn" aria-label="Previous service">%s</button>
      <button type="button" class="icon-btn" aria-label="Next service">%s</button>''' % (ic('arrow-left'), ic('arrow-right')))),
    dict(label='Glass sobre foto: «+» del equipo (reposo y activo) y play del video', mods='row photo', html=d('''
      <button type="button" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="Show details for Olivia Bennet" aria-expanded="false">%s</button>
      <button type="button" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="Hide details for Emma Wilson" aria-expanded="true">%s</button>
      <button type="button" class="icon-btn icon-btn--glass icon-btn--lg" aria-label="Play testimonial video">%s</button>''' % (ic('plus'), ic('plus'), ic('play')))),
    dict(label='Social Icon (<code>icon-btn--sm</code> con glifo de red)', mods='row', html=d('''
      <a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="Facebook">%s</a>
      <a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="LinkedIn">%s</a>
      <a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="Instagram">%s</a>
      <a href="#icon-button" class="icon-btn icon-btn--sm" aria-label="X">%s</a>''' % (ic('facebook'), ic('linkedin'), ic('instagram'), ic('x-twitter')))),
  ],
  rows=[('.icon-btn', 'Círculo de 48px con contorno, fondo blanco e ícono de 18px'),
        ('.icon-btn--sm', '40px: «+» del equipo y redes sociales'),
        ('.icon-btn--lg', '64px: play del testimonio en video'),
        ('.icon-btn--glass', 'Velo translúcido con ícono blanco para fotos; hover y estado activo en amarillo'),
        ('aria-expanded / aria-pressed="true"', 'Estado activo del glass (amarillo): el botón de «+» abierto'),
        ('aria-label', 'Obligatorio: el botón no tiene texto visible')],
  tokens=['--color-surface-default', '--color-border-default / -strong', '--color-overlay / --color-overlay-light', '--color-action-secondary', '--color-action-on-secondary', '--color-text-highlight (play)', '--spacing-8 / -9 / -10', '--text-body / -h6 / -h5', '--ease-fast'],
  a11y='Cada botón lleva <code>aria-label</code> que dice la acción y el objeto («Show details for Olivia Bennet»). El «+» comunica su estado con <code>aria-expanded</code>; el amarillo no es el único indicador. Los 40px mínimos superan los 24px exigidos.',
  a11y_md='`aria-label` obligatorio con la acción y el objeto; `aria-expanded`/`aria-pressed` para el estado; 40px mínimo.',
  decisions=['El play del diseño no lleva relleno (solo anillo); aquí comparte el velo del `--glass` para no abrir una variante por un matiz.',
             'El anillo de foco es el global: sobre una foto que no sea `data-surface="inverse"` puede perderse; las cards con foto lo resuelven en Moléculas.']))

A.append(dict(id='link-arrow', title='Link Arrow',
  desc='Enlace de texto con flecha: «Read More ↗» en los posts y «Contact Us ↗» en la card de FAQ. Subraya en hover, así el estado no depende solo del color. <code>--inverse</code> va sobre cards oscuras y <code>--highlight</code> (amarillo) solo sobre fondo oscuro.',
  desc_md='Enlace con flecha («Read More ↗»). Subraya en hover. `--inverse` sobre cards oscuras; `--highlight` amarillo solo sobre fondo oscuro.',
  blocks=[
    dict(label='Sobre fondo claro', mods='row', html=d('''
      <a href="#link-arrow" class="link-arrow">
        Read More
        %s
      </a>''' % ic('arrow-up-right'))),
    dict(label='Sobre fondo oscuro: <code>--inverse</code> y <code>--highlight</code>', surface='inverse', mods='row', html=d('''
      <a href="#link-arrow" class="link-arrow link-arrow--inverse">
        Read More
        %s
      </a>
      <a href="#link-arrow" class="link-arrow link-arrow--highlight">
        Contact Us
        %s
      </a>''' % (ic('arrow-up-right'), ic('arrow-up-right')))),
  ],
  rows=[('.link-arrow', 'Texto en color primario, medium, con flecha; subrayado en hover'),
        ('.link-arrow--inverse', 'Texto blanco, para cards y bloques oscuros'),
        ('.link-arrow--highlight', 'Texto amarillo: solo sobre fondo oscuro (nunca sobre el crema, 1.4:1)')],
  tokens=['--color-text-primary / -inverse / -highlight', '--weight-medium', '--spacing-2', '--ease-fast'],
  a11y='El texto del enlace es descriptivo; cuando varios «Read More» conviven en una página, cada uno añade al enlace un <code>aria-label</code> o texto visualmente oculto con el título del post.',
  a11y_md='Texto descriptivo; varios «Read More» repetidos llevan `aria-label` con el título del post.',
  decisions=['Para que un «Read More» repetido sea distinguible, el post card (Moléculas) añadirá el título como texto accesible.']))

A.append(dict(id='eyebrow', title='Eyebrow',
  desc='Rótulo corto sobre el título de una sección. El cuadrito es un pseudo-elemento decorativo. <code>--center</code> lo marca a ambos lados para encabezados centrados y <code>--inverse</code> lo pasa a amarillo sobre fondo oscuro.',
  desc_md='Rótulo corto sobre el título de sección, con cuadrito decorativo. `--center` a ambos lados; `--inverse` amarillo sobre oscuro.',
  blocks=[
    dict(label='Alineado a la izquierda', html=d('''
      <p class="eyebrow">What We Do</p>''')),
    dict(label='Centrado (<code>--center</code>)', html=d('''
      <p class="eyebrow eyebrow--center">Our Pricing Plan</p>''')),
    dict(label='Sobre fondo oscuro (<code>--center --inverse</code>)', surface='inverse', html=d('''
      <p class="eyebrow eyebrow--center eyebrow--inverse">Client Feedback</p>''')),
  ],
  rows=[('.eyebrow', 'Texto de 16px medium con un cuadrito antes'),
        ('.eyebrow--center', 'Centra el bloque y repite el cuadrito después'),
        ('.eyebrow--inverse', 'Texto y cuadrito amarillos (solo sobre fondo oscuro)')],
  tokens=['--color-text-primary / -highlight', '--text-body', '--weight-medium', '--leading-snug', '--spacing-1 / -2'],
  a11y='Es un <code>&lt;p&gt;</code>, no un encabezado: no altera la jerarquía h1→h2→h3. El cuadrito es CSS puro, sin ruido para lectores de pantalla.',
  a11y_md='`<p>`, no encabezado: no altera la jerarquía. El cuadrito es CSS puro.',
  decisions=['El cuadrito mide 6px (1.5 × `--spacing-1`) porque así lo muestra el diseño; sale de la escala por cálculo.',
             'Texto de 16px (`--text-body`): medido en los PNG a resolución real (Etapa 4, Grupo B), los cuatro eyebrows de la home miden 1,16 veces lo que medían con `--text-sm`, tanto en desktop como en mobile.']))

A.append(dict(id='badge', title='Badge',
  desc='Etiqueta translúcida sobre una foto: el rol de los miembros del equipo y la fecha de los posts. El velo es el <code>--color-overlay</code> del theme (petróleo oscuro al 65%), así el texto blanco se lee sobre cualquier foto. <code>--marker</code> suma el cuadrito amarillo.',
  desc_md='Etiqueta translúcida sobre foto (rol del equipo, fecha del post). Velo `--color-overlay`; `--marker` suma el cuadrito amarillo.',
  blocks=[dict(label='Sobre foto', mods='row photo', html=d('''
      <span class="badge">Financial Advisor</span>
      <span class="badge badge--marker">21 Oct, 2026</span>'''))],
  rows=[('.badge', 'Píldora de 40px con velo oscuro, borde translúcido y texto blanco de 14px'),
        ('.badge--marker', 'Agrega un cuadrito amarillo antes del texto (fechas)')],
  tokens=['--color-overlay / --color-overlay-light', '--color-text-inverse / -highlight', '--text-sm', '--weight-medium', '--spacing-2 / -4 / -8', '--radius-full'],
  a11y='Texto de 14px con el velo sobre foto: el peor caso (foto blanca) da ≈5:1. Una fecha va dentro de <code>&lt;time datetime&gt;</code> cuando la card la usa.',
  a11y_md='Peor caso (foto blanca) ≈5:1. Las fechas van en `<time datetime>`.',
  decisions=['El diseño muestra un vidrio esmerilado; se usa un velo plano (sin `backdrop-filter`) para no romper `position: fixed` de descendientes ni cargar el render.']))

A.append(dict(id='avatar', title='Avatar',
  desc='Retrato circular de 40px; <code>--portrait</code> es el retrato cuadrado de autor del testimonio (80px). <strong>Avatar Stack</strong> solapa avatares con un anillo del color del fondo y cierra con un «+» amarillo.',
  desc_md='Retrato circular de 40px; `--portrait` retrato cuadrado de autor (80px). Avatar Stack solapa avatares y cierra con «+».',
  blocks=[
    dict(label='Avatar y retrato de autor', mods='row', html=d('''
      <img class="avatar" src="%sh1-testimonial-thumb-img-1.webp" alt="" width="40" height="40">
      <img class="avatar avatar--portrait" src="%sh1-testimonial-thumb-img-2.webp" alt="" width="80" height="80">''' % (IMG, IMG))),
    dict(label='Avatar Stack', mods='row', html=d('''
      <div class="avatar-stack">
        <img class="avatar" src="%sh1-testimonial-thumb-img-1.webp" alt="" width="40" height="40">
        <img class="avatar" src="%sh1-testimonial-thumb-img-2.webp" alt="" width="40" height="40">
        <img class="avatar" src="%sh1-testimonial-thumb-img-3.webp" alt="" width="40" height="40">
        <span class="avatar-stack__more">%s</span>
      </div>''' % (IMG, IMG, IMG, ic('plus')))),
  ],
  rows=[('.avatar', 'Imagen circular de 40px con object-fit: cover'),
        ('.avatar--portrait', 'Retrato de autor: 80px con esquinas de 8px'),
        ('.avatar-stack', 'Contenedor que solapa a sus hijos; el anillo es --avatar-ring (por defecto, el fondo de página)'),
        ('.avatar-stack__more', 'Cierre amarillo con «+»'),
        ('--avatar-ring', 'Propiedad: poner el color del fondo donde se use el stack (ej. surface-default en una card)')],
  tokens=['--spacing-8 / -11', '--radius-full / -sm', '--color-background-muted / -default', '--color-action-secondary', '--color-action-on-secondary', '--border-width-md'],
  a11y='Las caras llevan <code>alt=""</code> porque el texto vecino («3M+ People Using Our Platform», el nombre del autor) ya da el sentido; si el avatar fuera el único contenido, llevaría el nombre. <code>width</code> y <code>height</code> explícitos evitan CLS.',
  a11y_md='Caras con `alt=""` (el texto vecino da el sentido); `width`/`height` explícitos.',
  decisions=['El diseño usa una imagen horneada con 3 caras (`h1-about-users.png`); aquí se arma con avatares reales para que el stack sea reutilizable. Las caras de los demos son las de los testimonios, no las del PNG.']))

A.append(dict(id='progress', title='Progress',
  desc='Barra de progreso con la etiqueta a la izquierda y el porcentaje alineado al final del relleno, como el diseño. Usa el elemento nativo <code>&lt;progress&gt;</code>, así el valor y el rol los expone el navegador sin ARIA a mano.',
  desc_md='Barra con etiqueta y porcentaje alineado al final del relleno (`--progress`). Usa `<progress>` nativo.',
  blocks=[dict(label='Tres valores', mods='medium stack', html=d('''
      <div class="progress" style="--progress: 90">
        <div class="progress__head">
          <label for="progress-operational">Operational assessment</label>
          <span aria-hidden="true">90%</span>
        </div>
        <progress class="progress__bar" id="progress-operational" value="90" max="100">90%</progress>
      </div>
      <div class="progress" style="--progress: 76">
        <div class="progress__head">
          <label for="progress-consultation">Consultation &amp; analysis</label>
          <span aria-hidden="true">76%</span>
        </div>
        <progress class="progress__bar" id="progress-consultation" value="76" max="100">76%</progress>
      </div>
      <div class="progress" style="--progress: 85">
        <div class="progress__head">
          <label for="progress-strategic">Strategic interpretation</label>
          <span aria-hidden="true">85%</span>
        </div>
        <progress class="progress__bar" id="progress-strategic" value="85" max="100">85%</progress>
      </div>''')),
    dict(label='--accent: relleno ámbar', mods='medium', html=d('''
      <div class="progress progress--accent" style="--progress: 88">
        <div class="progress__head">
          <label for="progress-demo-accent">Consulting</label>
          <span aria-hidden="true">88%</span>
        </div>
        <progress class="progress__bar" id="progress-demo-accent" value="88" max="100">88%</progress>
      </div>'''))],
  rows=[('.progress', 'Contenedor: cabecera + barra'),
        ('.progress__head', 'Fila con la etiqueta (&lt;label for&gt;) y el porcentaje (aria-hidden)'),
        ('.progress__bar', 'El &lt;progress&gt; nativo: 3px de alto, relleno petróleo sobre pista clara'),
        ('.progress--accent', 'Relleno ámbar (--color-action-secondary); caso de uso: «Consulting» en About Us'),
        ('value / max', 'El avance real (0–100); el relleno lo dibuja el navegador'),
        ('style="--progress: 90"', 'Mismo valor que value: lleva el porcentaje al final del relleno (sin ella, al final de la pista)')],
  tokens=['--color-action-primary / -secondary', '--color-background-muted', '--color-text-primary', '--border-width-sm / -md', '--radius-full', '--ease-slow'],
  a11y='La etiqueta está asociada con <code>&lt;label for&gt;</code> y el navegador anuncia «90%». El porcentaje visible es <code>aria-hidden</code> para no leerlo dos veces. El texto interno de <code>&lt;progress&gt;</code> es el respaldo de navegadores sin soporte.',
  a11y_md='`<label for>` + valor nativo; el % visible es `aria-hidden`.',
  decisions=['El diseño no muestra animación de llenado: el relleno aparece en su valor final. Una animación al entrar al viewport se decide en la Section.',
             'El valor se escribe dos veces (`value` y `--progress`) porque CSS todavía no puede leer `attr(value)` como número en todos los navegadores objetivo; con JS se podría sincronizar, pero se prefirió que funcione sin JS.',
             'Con valores bajos en una fila angosta la etiqueta pasa a dos líneas (el porcentaje no cruza el final del relleno). En el diseño las barras miden 400px y no ocurre.']))

A.append(dict(id='switch', title='Switch',
  desc='Interruptor sobre un <code>&lt;input type="checkbox" role="switch"&gt;</code> nativo. Apagado, la perilla va a la izquierda; encendido, a la derecha. El texto «Monthly / Annually» del pricing se arma en la Section con dos <code>&lt;label&gt;</code>.',
  desc_md='Interruptor sobre `<input type="checkbox" role="switch">`. La posición de la perilla es el estado.',
  blocks=[dict(label='Apagado, encendido y deshabilitado', mods='row', html=d('''
      <input class="switch" type="checkbox" role="switch" id="switch-demo-off">
      <label for="switch-demo-off">Monthly billing</label>
      <input class="switch" type="checkbox" role="switch" id="switch-demo-on" checked>
      <label for="switch-demo-on">Annual billing</label>
      <input class="switch" type="checkbox" role="switch" id="switch-demo-disabled" disabled>
      <label for="switch-demo-disabled">Unavailable</label>'''))],
  rows=[('.switch', 'Pista petróleo de 80×40px con perilla blanca ovalada'),
        ('role="switch"', 'Obligatorio: sin él un lector de pantalla lo anuncia como casilla'),
        ('checked / disabled', 'Estados nativos; la perilla se desplaza con :checked'),
        ('&lt;label for&gt;', 'Obligatorio: el nombre accesible no puede ser solo un placeholder')],
  tokens=['--color-action-primary(-hover/-disabled)', '--color-surface-default', '--spacing-1 / -7 / -8 / -11', '--radius-full', '--ease-fast / --ease-base'],
  a11y='Es un control nativo: Tab para llegar, Espacio para alternar, y el estado lo anuncia el lector («activado/desactivado»). El estado se ve por la <em>posición</em> de la perilla, no por el color de la pista. Con «reducir movimiento» la perilla salta sin animación.',
  a11y_md='Control nativo (Tab/Espacio); el estado lo da la posición de la perilla; sin animación con reducir movimiento.',
  decisions=['El diseño solo muestra el estado apagado: el encendido se deriva (perilla a la derecha, misma pista) en vez de inventar un color nuevo.']))

A.append(dict(id='divider', title='Divider',
  desc='Filete horizontal de 1px sobre un <code>&lt;hr&gt;</code>. <code>--inverse</code> lo adapta a fondos oscuros (divisor de las cards de testimonio y del footer).',
  desc_md='Filete de 1px sobre `<hr>`. `--inverse` para fondos oscuros.',
  blocks=[
    dict(label='Sobre fondo claro', mods='narrow', html=d('''
      <hr class="divider">''')),
    dict(label='Sobre fondo oscuro (<code>divider--inverse</code>)', surface='inverse', mods='narrow', html=d('''
      <hr class="divider divider--inverse">''')),
  ],
  rows=[('.divider', 'Filete de 1px con el color de borde sutil'),
        ('.divider--inverse', 'Filete translúcido blanco para fondos oscuros')],
  tokens=['--color-border-subtle', '--color-overlay-light', '--border-width-sm'],
  a11y='<code>&lt;hr&gt;</code> expone un separador; si el filete es solo decorativo se puede dibujar con <code>border</code> en el componente en vez de usar el átomo.',
  a11y_md='`<hr>` expone un separador; si es puramente decorativo, usar `border` del componente.',
  decisions=['El filete del hero (parcial, blanco al 30%) es propio del Hero y no pasa por este átomo.']))

A.append(dict(id='check-list', title='Check List',
  desc='Lista con el check relleno (<code>icon--circle-check</code>): el ícono en el color del texto fuerte y el texto en secundario. La usan «Mistakes to avoid…» y Key Features en Service Details.',
  desc_md='Lista con `icon--circle-check` relleno: ícono en texto fuerte, texto en secundario (Service Details).',
  blocks=[
    dict(label='Cuatro ítems', mods='medium', html=d('''
      <ul class="check-list" role="list">
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Market research and competitive analysis</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Operational efficiency and process optimization</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Risk assessment and decision-making support</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Strategic business planning and roadmap</li>
      </ul>''')),
  ],
  rows=[('ul.check-list + role="list"', 'La lista; role="list" porque list-style: none la oculta como lista en Safari'),
        ('span.icon.icon--circle-check + aria-hidden="true"', 'Check decorativo, centrado en la primera línea')],
  tokens=['--color-text-primary (ícono)', '--color-text-secondary (texto)', '--spacing-3 / -4'],
  a11y='Es una lista real (<code>role="list"</code> la devuelve a VoiceOver, que la pierde con <code>list-style: none</code>). El check es <code>aria-hidden</code>: no aporta información que no esté en el texto.',
  a11y_md='Lista real con `role="list"` (VoiceOver); check `aria-hidden`.',
  decisions=['La lista de About Us (`about-intro__list`, check en contorno) queda como está: es otro ícono y vive en su Section.',
             'El ícono se centra en la primera línea con `1lh`: los ítems que en mobile ocupan dos líneas no lo desalinean.']))
_i = [a['id'] for a in A].index('divider')
A.insert(_i + 1, A.pop())

A.append(dict(id='dots', title='Pagination Dots',
  desc='Puntos de paginación para carruseles (testimonios, stats en mobile). Cada punto es un botón de 24×24px con el punto dibujado en <code>::before</code>. El inactivo usa <code>border-strong</code> y el activo lleva un halo.',
  desc_md='Puntos de paginación. Cada punto es un botón de 24×24px; el activo lleva halo.',
  blocks=[
    dict(label='Sobre fondo claro', mods='row', html=d('''
      <div class="dots" role="group" aria-label="Choose a story">
        <button type="button" class="dots__dot" aria-label="Show story 1"></button>
        <button type="button" class="dots__dot" aria-label="Show story 2"></button>
        <button type="button" class="dots__dot" aria-label="Show story 3" aria-current="true"></button>
        <button type="button" class="dots__dot" aria-label="Show story 4"></button>
        <button type="button" class="dots__dot" aria-label="Show story 5"></button>
        <button type="button" class="dots__dot" aria-label="Show story 6"></button>
      </div>''')),
    dict(label='Sobre fondo oscuro (<code>dots--inverse</code>)', surface='inverse', mods='row', html=d('''
      <div class="dots dots--inverse" role="group" aria-label="Choose a story">
        <button type="button" class="dots__dot" aria-label="Show story 1"></button>
        <button type="button" class="dots__dot" aria-label="Show story 2"></button>
        <button type="button" class="dots__dot" aria-label="Show story 3" aria-current="true"></button>
        <button type="button" class="dots__dot" aria-label="Show story 4"></button>
        <button type="button" class="dots__dot" aria-label="Show story 5"></button>
        <button type="button" class="dots__dot" aria-label="Show story 6"></button>
      </div>''')),
  ],
  rows=[('.dots', 'Fila de puntos; el color activo es --dots-active'),
        ('.dots--inverse', 'Activo amarillo para fondos oscuros'),
        ('.dots__dot', 'Botón de 24×24px; el punto (12px) se dibuja en ::before'),
        ('aria-current="true"', 'Marca el punto activo; el cambio de slide lo mantiene sincronizado (organismo Carrusel)')],
  tokens=['--color-border-strong (inactivo)', '--color-action-primary / --color-text-highlight (activo)', '--spacing-1 / -3 / -6', '--radius-full', '--ease-base'],
  a11y='Cada botón nombra su destino («Show story 3»); el activo se marca con <code>aria-current</code>, no solo con color. El punto inactivo da ≥3:1 tanto sobre el crema como sobre el fondo oscuro.',
  a11y_md='Cada botón nombra su destino; el activo con `aria-current`; inactivo ≥3:1 sobre claro y oscuro.',
  decisions=['El inactivo del diseño es un gris translúcido más tenue; se usa `border-strong` porque es el único token que llega a 3:1 en ambos fondos.']))

A.append(dict(id='scroll-top', title='Scroll Top', static=True,
  desc='Botón fijo abajo a la derecha que vuelve al inicio. Aparece al pasar media pantalla y el anillo dibuja el avance del scroll. <strong>Está activo en este mismo kit: baja por la página y míralo.</strong>',
  desc_md='Botón fijo que vuelve al inicio. Aparece tras media pantalla; el anillo dibuja el avance del scroll. Vive en el body de la página.',
  blocks=[dict(label='Snippet (va una sola vez, al final del <code>&lt;body&gt;</code>)', code=d('''
      <button type="button" class="scroll-top" aria-label="Back to top">
        <span class="icon icon--arrow-up" aria-hidden="true"></span>
      </button>'''), id_suffix='usage')],
  rows=[('.scroll-top', 'Círculo fijo de 48px; oculto con visibility hasta que main.js agrega .is-visible'),
        ('.is-visible', 'La pone main.js al pasar el 50% del alto del viewport'),
        ('--scroll-progress', 'Propiedad 0–100 que main.js actualiza; llena el anillo con conic-gradient'),
        ('main.js › initScrollTop', 'Sin JS el botón queda oculto: el sitio sigue usable')],
  tokens=['--color-action-primary (anillo)', '--color-border-default (pista)', '--color-surface-default', '--spacing-5 / -9', '--z-sticky', '--ease-base'],
  a11y='Tiene <code>aria-label</code>. Oculto usa <code>visibility: hidden</code>, así sale del orden de tabulación. Al activarlo, el foco pasa al <code>&lt;body&gt;</code> para que Tab arranque desde el inicio y no desde el pie. Con Lenis hace el scroll suave del motor; sin él, <code>scroll-behavior</code> respetando «reducir movimiento».',
  a11y_md='`aria-label`; oculto con `visibility`; al activarlo mueve el foco al `<body>`; respeta reducir movimiento.',
  decisions=['El diseño muestra el botón con su anillo parcialmente lleno pero no dice cuándo aparece: se asume al pasar media pantalla (`SHOW_AFTER = 0.5` en main.js).',
             'En escritorio queda a 48px de los bordes (medido en el diseño); en mobile, a 20px.']))


A.append(dict(id='input', title='Input',
  desc='Campo de texto de una línea con solo el filete inferior: el único caso del diseño es el de la newsletter. Sobre superficies oscuras (<code>data-surface</code>) el filete y el placeholder pasan a blanco al 78% para mantener el contraste de un control (3:1).',
  desc_md='Campo de texto de una línea con filete inferior (caso del diseño: newsletter). Sobre superficies oscuras filete y placeholder pasan a blanco al 78%.',
  blocks=[
    dict(label='Sobre fondo claro', mods='narrow', html=d('''
      <label for="input-demo-light" class="visually-hidden">Email address</label>
      <input class="input" type="email" id="input-demo-light" name="email" placeholder="Enter your email" autocomplete="email">''')),
    dict(label='Sobre fondo oscuro (hereda de <code>data-surface</code>)', surface='inverse', mods='narrow', html=d('''
      <label for="input-demo-dark" class="visually-hidden">Email address</label>
      <input class="input" type="email" id="input-demo-dark" name="email" placeholder="Enter your email" autocomplete="email">''')),
    dict(label='Textarea (misma clase)', mods='narrow', html=d('''
      <label for="input-demo-textarea" class="visually-hidden">Message</label>
      <textarea class="input" id="input-demo-textarea" name="message" placeholder="Write your message"></textarea>''')),
    dict(label='--filled (caja gris)', mods='narrow', html=d('''
      <label for="input-demo-filled" class="visually-hidden">Your name</label>
      <input class="input input--filled" type="text" id="input-demo-filled" name="name" placeholder="Name">''')),
  ],
  rows=[('.input', 'Campo sin caja: solo el filete inferior; ocupa el ancho de su contenedor'),
        ('.input--filled', 'Caja gris con filete inferior fuerte (Quote Form de Service Details)'),
        ('textarea.input', 'Varias líneas: alto mínimo de 96px y redimensionable solo en vertical'),
        ('aria-invalid="true"', 'Estado de error: el filete pasa a color de error (acompañar con un mensaje de texto)'),
        ('&lt;label for&gt;', 'Obligatorio, aunque esté visualmente oculto (<code>visually-hidden</code>): el placeholder no es un nombre accesible'),
        ('type / autocomplete', 'El tipo correcto (email, tel…) abre el teclado adecuado en móvil; autocomplete evita volver a pedir un dato')],
  tokens=['--color-text-primary / -inverse', '--color-border-strong / --color-text-inverse-secondary (filete)', '--color-text-tertiary (placeholder)', '--color-border-error', '--spacing-3', '--text-body', '--ease-fast'],
  a11y='Lleva <code>&lt;label&gt;</code> asociado y el placeholder solo ilustra el formato. El foco usa el anillo global (amarillo sobre superficies oscuras). El filete da ≥3:1 sobre claro y oscuro, como exige WCAG 1.4.11 para el borde de un control.',
  a11y_md='`<label>` asociado (puede ser `visually-hidden`); foco con anillo global; filete ≥3:1.',
  decisions=['Dos estilos: filete (newsletter y Quote Form de About Us) y --filled (Quote Form de Service Details).',
             '--filled: el borde del diseño (≈ 1.2:1) no llega al 3:1 de un control; se mantiene en tres lados y el filete inferior va en `--color-border-strong` (decisión del usuario).',
             'El filete del diseño es translúcido y tenue; aquí es blanco al 78% para cumplir 3:1 como borde de control.']))

_i = [a['id'] for a in A].index('switch')
A.insert(_i + 1, A.pop())

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
    dict(label='--filled y --select: vacío, con valor y con error', mods='narrow stack', html=d('''
      <div class="field field--filled">
        <label class="field__label" for="field-demo-filled-name">Name<span aria-hidden="true">*</span></label>
        <input class="input input--filled field__control" type="text" id="field-demo-filled-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="field-demo-filled-name-error">
        <p class="field__error" id="field-demo-filled-name-error"></p>
      </div>
      <div class="field field--filled field--select">
        <label class="field__label" for="field-demo-filled-service">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="field-demo-filled-service" name="service" required aria-describedby="field-demo-filled-service-error">
          <option value="" hidden selected></option>
          <option>Strategic Planning</option>
          <option>Business Optimization</option>
          <option>IT Consulting</option>
          <option>Change Management</option>
          <option>Leadership</option>
        </select>
        <p class="field__error" id="field-demo-filled-service-error"></p>
      </div>
      <div class="field field--filled field--select">
        <label class="field__label" for="field-demo-filled-service-2">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="field-demo-filled-service-2" name="service" required aria-invalid="true" aria-describedby="field-demo-filled-service-2-error">
          <option value="" hidden selected></option>
          <option>Strategic Planning</option>
          <option>Business Optimization</option>
        </select>
        <p class="field__error" id="field-demo-filled-service-2-error">Choose an option.</p>
      </div>''')),
  ],
  rows=[('.field', 'Envoltura: reserva arriba el lugar del label subido'),
        ('label.field__label + for', 'Nombre visible del campo; flota sobre el filete con foco o con texto'),
        ('.input.field__control + placeholder=" "', 'El campo; el placeholder de un espacio habilita :placeholder-shown (es invisible)'),
        ('&lt;span aria-hidden="true"&gt;*&lt;/span&gt; + required', 'Asterisco visual; lo obligatorio lo anuncia required'),
        ('p.field__error#&lt;id&gt;-error + aria-describedby', 'Mensaje de error enlazado; vacío no ocupa lugar'),
        ('.field--filled', 'Con Input --filled: el label descansa dentro de la caja y sube alineado con su borde'),
        ('.field--select + option[value=""][hidden][selected]', 'Select con chevron; la opción vacía deja el label en reposo'),
        ('aria-invalid="true"', 'Filete en color de error (lo pone main.js al validar)')],
  tokens=['--color-text-secondary (label)', '--color-feedback-error-text', '--text-sm', '--spacing-1 / -3 / -5', '--spacing-4 / -6 (--filled)', '--ease-fast', 'Input (átomo)'],
  a11y='El nombre del campo es un <code>&lt;label&gt;</code> real y visible en los dos estados (cumple «label asociado, no solo placeholder» de <code>accessibility.md</code>). El error se enlaza con <code>aria-describedby</code> y el campo lleva <code>aria-invalid</code>: el lector lee nombre, estado y mensaje. El asterisco es <code>aria-hidden</code> porque <code>required</code> ya anuncia que es obligatorio. Con «reducir movimiento» el label cambia de lugar sin animar.',
  a11y_md='`<label>` real y visible en reposo y con texto; error con `aria-describedby` + `aria-invalid`; asterisco `aria-hidden` (lo anuncia `required`).',
  decisions=['Label flotante (decisión del usuario) en vez del placeholder del diseño: se ve igual en reposo y no desaparece al escribir.',
             'Usa `:has()` para saber si el campo tiene texto; el label puede ir antes del campo en el DOM.',
             'Solo sobre fondo claro: son los casos del diseño (Quote Form de About Us y de Service Details).']))
_i = [a['id'] for a in A].index('input')
A.insert(_i + 1, A.pop())

A.append(dict(id='select', title='Select',
  desc='El <a href="#input">Input</a> sobre un <code>&lt;select&gt;</code> nativo, sin la flecha del sistema: el chevron lo dibuja <a href="#field">Field</a> <code>--select</code>. Va siempre dentro de un Field, que le da el label flotante y el mensaje de error.',
  desc_md='`.input` sobre `<select>` nativo sin flecha del sistema; el chevron y el label flotante los pone Field `--select`.',
  blocks=[
    dict(label='Vacío y con una opción elegida (--filled)', mods='narrow stack', html=d('''
      <div class="field field--filled field--select">
        <label class="field__label" for="select-demo-empty">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="select-demo-empty" name="service" required>
          <option value="" hidden selected></option>
          <option>Strategic Planning</option>
          <option>Business Optimization</option>
          <option>IT Consulting</option>
        </select>
      </div>
      <div class="field field--filled field--select">
        <label class="field__label" for="select-demo-chosen">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="select-demo-chosen" name="service" required>
          <option value="" hidden></option>
          <option>Strategic Planning</option>
          <option selected>Business Optimization</option>
          <option>IT Consulting</option>
        </select>
      </div>''')),
  ],
  rows=[('select.input', 'Sin apariencia nativa; deja lugar al chevron a la derecha'),
        ('option[value=""][hidden][selected]', 'Opción vacía inicial: deja el label en reposo y hace fallar required hasta elegir'),
        ('.field--select', 'Dibuja el chevron y maneja el label (ver Field)'),
        ('required', 'Obligatorio: main.js muestra «Choose an option.» si queda vacío')],
  tokens=['Input (átomo)', 'Field (átomo)', '--color-text-primary (chevron)', '--spacing-5 / -7'],
  a11y='Es un <code>&lt;select&gt;</code> nativo: teclado, lectores y el selector del sistema (móvil) funcionan sin JS. El nombre lo da el <code>&lt;label&gt;</code> del Field; el chevron es decorativo (pseudo-elemento sin texto). La opción vacía está oculta en la lista (<code>hidden</code>), así nadie la vuelve a elegir por error.',
  a11y_md='`<select>` nativo (teclado, lector, selector del sistema); nombre del `<label>`; chevron decorativo; opción vacía `hidden`.',
  decisions=['Nativo antes que un select a medida: el diseño no pide nada que el nativo no haga, y uno a medida necesita JS y ARIA de listbox.',
             'La opción vacía no lleva `disabled`: con `disabled`, Chromium/Windows fuerza el color del texto y obligaría a usar `!important`, que el theme no admite (CLAUDE.md §11).',
             'El chevron repite el data URI de `icon--chevron-down` (un pseudo-elemento no puede usar `.icon`): si cambia uno, cambiar el otro.',
             'Safari no oculta opciones con `hidden`: ahí la lista muestra una fila vacía al principio. Elegirla deja el campo vacío y la validación lo marca.']))
_i = [a['id'] for a in A].index('field')
A.insert(_i + 1, A.pop())

# ---------------------------------------------------------------- render HTML
def indent(txt, n):
    pad = ' ' * n
    return '\n'.join((pad + l) if l.strip() else l for l in txt.split('\n'))

def snippet(sid, code=None):
    inner = '<code data-source="demo"></code>' if code is None else '<code>' + H.escape(code, quote=False) + '</code>'
    return d('''
      <div class="kit-snippet is-collapsed">
        <div class="kit-snippet__bar">
          <button type="button" class="kit-btn" data-kit-toggle aria-expanded="false" aria-controls="%s">Ver código</button>
          <button type="button" class="kit-btn" data-kit-copy>Copiar</button>
        </div>
        <pre id="%s" tabindex="0">%s</pre>
      </div>''' % (sid, sid, inner))

def block(a, i, b):
    sid = 'snippet-%s-%d' % (a['id'], i)
    out = ['          <div class="kit-block">', '            <span class="kit-block__label">%s</span>' % b['label']]
    if 'code' in b:
        out.append(indent(snippet(sid, b['code']), 12))
    else:
        mods = ''.join(' kit-demo--' + m for m in b.get('mods', '').split())
        surf = ' data-surface="%s"' % b['surface'] if b.get('surface') else ''
        out.append('            <div class="kit-demo%s"%s lang="en">' % (mods, surf))
        out.append(indent(b['html'], 14))
        out.append('            </div>')
        out.append(indent(snippet(sid), 12))
    out.append('          </div>')
    return '\n'.join(out)

def icons_block():
    tiles = '\n'.join('              <li class="kit-icon"><span class="icon icon--%s" aria-hidden="true"></span><code>icon--%s</code></li>' % (n, n) for n in ICON_NAMES)
    return ('          <div class="kit-block">\n            <span class="kit-block__label">Set completo (%d)</span>\n'
            '            <ul class="kit-icons">\n%s\n            </ul>\n          </div>' % (len(ICON_NAMES), tiles))

def card(a, n):
    parts = ['        <section class="kit-card" id="%s" aria-labelledby="%s-title">' % (a['id'], a['id']),
             '          <header class="kit-card__header">',
             '            <p class="kit-card__tag">Átomo · %02d</p>' % n,
             '            <h3 id="%s-title">%s</h3>' % (a['id'], a['title']),
             '            <p class="kit-card__desc">%s</p>' % a['desc'], '          </header>']
    if a.get('raw_icons'): parts.append(icons_block())
    for i, b in enumerate(a['blocks'], 1): parts.append(block(a, i, b))
    rows = '\n'.join('                  <tr><th scope="row"><code>%s</code></th><td>%s</td></tr>' % (s, t) for s, t in a['rows'])
    parts.append('''          <div class="kit-block">
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
    parts.append('          <div class="kit-block">\n            <span class="kit-block__label">Tokens que consume</span>\n            <ul class="kit-spec">\n%s\n            </ul>\n          </div>'
                 % '\n'.join('              <li><code>%s</code></li>' % t for t in a['tokens']))
    parts.append('          <p class="kit-note"><strong>Accesibilidad:</strong> %s</p>' % a['a11y'])
    parts.append('        </section>')
    return '\n'.join(parts)

cards = '\n\n'.join(card(a, i) for i, a in enumerate(A, 1))
level = ('      <section class="kit-level" id="atoms" aria-labelledby="atoms-title">\n'
         '        <h2 id="atoms-title">Átomos</h2>\n'
         '        <p class="kit-level__intro">Las piezas mínimas: iconos, botones, enlaces, etiquetas y controles. No dependen de otro componente del kit; solo tokens y HTML/CSS (el único JS es el de Scroll Top).</p>\n'
         + cards + '\n        <!-- kit:atoms-end -->\n      </section>')

nav_items = '\n'.join('            <li><a class="kit-nav__link" href="#%s"><span class="kit-nav__num">%02d</span> %s</a></li>' % (a['id'], i, a['title']) for i, a in enumerate(A, 1))
nav = ('        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-atoms">Átomos</p>\n'
       '          <ul class="kit-nav__list" aria-labelledby="nav-atoms">\n' + nav_items + '\n          </ul>\n        </div>')

page = open(KIT, encoding='utf-8').read()

# nivel Átomos
pat = re.compile(r'      <section class="kit-level" id="atoms".*?(?=\n\n      <section class="kit-level" id="molecules")', re.S)
assert pat.search(page), 'no encuentro la sección atoms'
page = pat.sub(lambda m: level, page, count=1)

# navegación
if 'id="nav-atoms"' in page:
    page = re.sub(r'        <div class="kit-nav__group">\n          <p class="kit-nav__group-label" id="nav-atoms">.*?\n        </div>', lambda m: nav, page, count=1, flags=re.S)
else:
    old = '        <div class="kit-nav__group">\n          <p class="kit-nav__group-label">Átomos</p>\n          <p class="kit-nav__empty">Sin componentes aún</p>\n        </div>'
    assert page.count(old) == 1
    page = page.replace(old, nav)

# Scroll Top vivo en el kit
live = ('  <button type="button" class="scroll-top" aria-label="Back to top" lang="en">\n'
        '    <span class="icon icon--arrow-up" aria-hidden="true"></span>\n  </button>\n\n')
if 'class="scroll-top"' not in page.split('<script src=')[0].split('</main>')[-1]:
    marker = '  <script src="../assets/js/main.js" defer></script>'
    assert page.count(marker) == 1
    page = page.replace(marker, live + marker)

# pares de contraste nuevos
extra = ('                  <tr data-contrast="--color-text-primary|--color-background-subtle" data-min="4.5"><th scope="row">text-primary / background-subtle (btn--block)</th><td data-ratio></td><td>4.5:1</td><td><span class="kit-badge" data-badge></span></td></tr>\n'
         '                  <tr data-contrast="--color-border-strong|--color-background-inverse" data-min="3"><th scope="row">border-strong / background-inverse (dots inactivos)</th><td data-ratio></td><td>3:1</td><td><span class="kit-badge" data-badge></span></td></tr>\n')
if 'btn--block)' not in page:
    anchor = '                </tbody>\n              </table>\n            </div>\n          </div>\n\n          <div class="kit-block">\n            <span class="kit-block__label">Foco y superficie inversa</span>'
    assert page.count(anchor) == 1
    page = page.replace(anchor, extra + anchor)
open(KIT, 'w', encoding='utf-8', newline='\n').write(page)

# ---------------------------------------------------------------- kit.css
css = open(KITCSS, encoding='utf-8').read()
if '/* atoms-kit:start */' not in css:
    css = css.replace('  --kit-table-min: 36rem;\n', '  --kit-table-min: 36rem;\n  --kit-narrow: 22rem;\n  --kit-icon-min: 8.5rem;\n', 1)
    add = '''
/* atoms-kit:start */
/* Demos de átomos: fila, columna angosta (ancho de card) y fondo de foto */
.kit-demo--row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--spacing-5);
}
.kit-demo--narrow {
  display: grid;
  gap: var(--spacing-5);
  max-inline-size: var(--kit-narrow);
}
.kit-demo--photo {
  border-color: transparent;
  background: var(--color-background-inverse) url('../img/h1-team-member-img-1.webp') center / cover;
}
/* Tokens que consume un componente */
.kit-spec {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-2);
  margin: 0;
  padding: 0;
  list-style: none;
}
.kit-spec li {
  padding: var(--spacing-1) var(--spacing-3);
  border-radius: var(--radius-full);
  background-color: var(--color-background-subtle);
}
/* Set de iconos */
.kit-icons {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(var(--kit-icon-min), 1fr));
  gap: var(--spacing-3);
  margin: 0;
  padding: 0;
  list-style: none;
}
.kit-icon {
  display: grid;
  justify-items: center;
  gap: var(--spacing-3);
  padding: var(--spacing-5) var(--spacing-3);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-md);
  font-size: var(--text-h4);
  color: var(--color-text-primary);
}
.kit-icon code {
  font-size: var(--text-xs);
  color: var(--color-text-tertiary);
}
/* atoms-kit:end */
'''
    css = css.replace('/* kit:css-end */', add + '/* kit:css-end */')
    open(KITCSS, 'w', encoding='utf-8', newline='\n').write(css)

# ---------------------------------------------------------------- stories.md
def unesc(s): return H.unescape(re.sub(r'</?(code|strong|em)>', lambda m: '`' if m.group(1) == 'code' else ('**' if m.group(1) == 'strong' else '*'), s))
os.makedirs(STORIES, exist_ok=True)
for n, a in enumerate(A, 1):
    md = ['# %s' % a['title'], '', '**Nivel:** Átomo · %02d  ' % n, '**Dónde:** `dist/assets/css/main.css` (bloque `/* %s */`) · showcase en `dist/kit/index.html#%s`' % (a['title'], a['id']), '',
          '## Descripción', '', unesc(a['desc_md']), '', '## Snippets', '']
    for b in a['blocks']:
        code = b['code'] if 'code' in b else b['html']
        md += ['**%s**' % unesc(b['label']) if b.get('label') else '', '', '```html', H.unescape(code), '```', '']
    md += ['## Clases y atributos', '', '| Clase o atributo | Efecto |', '|---|---|']
    md += ['| `%s` | %s |' % (H.unescape(s), unesc(t)) for s, t in a['rows']]
    md += ['', '## Tokens que consume', ''] + ['- `%s`' % t for t in a['tokens']]
    md += ['', '## Accesibilidad', '', unesc(a['a11y_md']), '', '## Decisiones y excepciones', ''] + ['- ' + x for x in a['decisions']] + ['']
    open(os.path.join(STORIES, a['id'] + '.stories.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(md))
print('ok:', len(A), 'átomos')
