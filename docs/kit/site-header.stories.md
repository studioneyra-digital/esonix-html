# Site Header

**Nivel:** Organismo · 01  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Site Header */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#site-header`

## Descripción

Barra del sitio sobre la foto del hero: logo, menú en píldora blanca con submenús (disclosure), redes en texto y teléfono. Responde al ancho de su contenedor (container query `site-header`): < 48rem logo + «Menu» (abre el Off-canvas); ≥ 48rem menú y círculo del chat; ≥ 64rem número de teléfono; ≥ 80rem redes.

## Snippets

**Barra completa (80rem de ancho), a escala**

```html
<header class="site-header">
  <div class="site-header__bar">
    <a class="site-header__brand" href="#site-header">
      <img class="brand-logo" src="../assets/img/primary-logo.png" alt="Esonix" width="140" height="40">
    </a>
    <nav class="site-header__nav" aria-label="Main">
      <ul class="site-nav__list">
        <li class="site-nav__item">
          <button type="button" class="site-nav__link site-nav__trigger" aria-expanded="false" aria-controls="submenu-home">
            Home
            <span class="icon icon--chevron-down site-nav__chevron" aria-hidden="true"></span>
          </button>
          <ul class="site-nav__submenu" id="submenu-home" data-surface="brand">
            <li><a class="site-nav__sublink" href="#site-header">Home Version 01</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Home Version 02</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Home Version 03</a></li>
          </ul>
        </li>
        <li class="site-nav__item">
          <button type="button" class="site-nav__link site-nav__trigger" aria-expanded="false" aria-controls="submenu-services">
            Services
            <span class="icon icon--chevron-down site-nav__chevron" aria-hidden="true"></span>
          </button>
          <ul class="site-nav__submenu" id="submenu-services" data-surface="brand">
            <li><a class="site-nav__sublink" href="#site-header">Marketing Guidance</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Process Optimization</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Sales Improvement</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Service Details</a></li>
          </ul>
        </li>
        <li class="site-nav__item">
          <button type="button" class="site-nav__link site-nav__trigger" aria-expanded="false" aria-controls="submenu-pages">
            Pages
            <span class="icon icon--chevron-down site-nav__chevron" aria-hidden="true"></span>
          </button>
          <ul class="site-nav__submenu" id="submenu-pages" data-surface="brand">
            <li><a class="site-nav__sublink" href="#site-header">About Us</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Portfolios</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Portfolio Details</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Team Members</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Pricing Page</a></li>
            <li><a class="site-nav__sublink" href="#site-header">FAQ Page</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Error 404</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Coming Soon</a></li>
          </ul>
        </li>
        <li class="site-nav__item">
          <button type="button" class="site-nav__link site-nav__trigger" aria-expanded="false" aria-controls="submenu-blog">
            Blog
            <span class="icon icon--chevron-down site-nav__chevron" aria-hidden="true"></span>
          </button>
          <ul class="site-nav__submenu" id="submenu-blog" data-surface="brand">
            <li><a class="site-nav__sublink" href="#site-header">Blog Grid</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Blog Standard</a></li>
            <li><a class="site-nav__sublink" href="#site-header">Blog Details</a></li>
          </ul>
        </li>
        <li class="site-nav__item"><a class="site-nav__link" href="#site-header">Contact</a></li>
      </ul>
    </nav>
    <ul class="site-header__socials" aria-label="Social media">
      <li><a class="site-header__social" href="#site-header">FB<span class="visually-hidden"> Facebook</span></a></li>
      <li><a class="site-header__social" href="#site-header">TW<span class="visually-hidden"> Twitter</span></a></li>
      <li><a class="site-header__social" href="#site-header">LI<span class="visually-hidden"> LinkedIn</span></a></li>
      <li><a class="site-header__social" href="#site-header">IG<span class="visually-hidden"> Instagram</span></a></li>
    </ul>
    <a class="site-header__phone" href="tel:+880123456789">
      <span class="site-header__phone-number">+880 (123) 456 789</span>
      <span class="site-header__phone-icon"><span class="icon icon--message-square" aria-hidden="true"></span></span>
    </a>
    <button type="button" class="site-header__toggle" data-offcanvas-open aria-controls="offcanvas-menu" aria-expanded="false">
      Menu
      <span class="icon icon--layout-grid" aria-hidden="true"></span>
    </button>
  </div>
</header>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.site-header` | Contenedor de consulta (container: site-header); texto blanco y foco amarillo |
| `.site-header__bar` | Barra en píldora con velo blanco al 10% y borde blanco al 30%; reparte los grupos con space-between |
| `.site-header__brand` | Enlace del logo (primary-logo.png, sobre oscuro) |
| `.site-header--fixed` | Variante fija arriba (position: fixed, z-sticky), centrada hasta --site-header-max; el margen alrededor de la barra no captura clics |
| `.site-header--fixed.is-scrolled` | Lo agrega main.js al pasar el 10% del alto de la ventana: la barra pasa a fondo inverso para leerse sobre las secciones claras |
| `.site-header__nav` | Contenedor <nav> del menú; visible desde 48rem de barra |
| `.site-nav__list / __item / __link` | Píldora blanca, ítem posicionado y enlace o botón del menú |
| `.site-nav__trigger + aria-expanded / aria-controls` | Botón que abre su submenú; el chevron gira con aria-expanded="true" |
| `.site-nav__submenu + data-surface="brand"` | Panel petróleo bajo la píldora, con un puente invisible para el hover |
| `.site-nav__sublink / aria-current="page"` | Enlace del submenú; amarillo en hover y en la página actual |
| `.site-header__socials / __social` | Redes en texto («FB - TW - LI - IG»), desde 80rem de barra |
| `.site-header__phone / __phone-number / __phone-icon` | Enlace tel: con el círculo amarillo; bajo 64rem de barra el número es solo para lectores |
| `.site-header__toggle + data-offcanvas-open` | Botón «Menu» (bajo 48rem de barra); aria-controls apunta al id del Off-canvas |

## Tokens que consume

- `--color-overlay-light`
- `--color-text-inverse / -highlight / -primary`
- `--color-surface-default`
- `--color-action-primary / -secondary / -secondary-hover / -on-secondary`
- `--color-border-focus-inverse`
- `--text-body-lg / -body`
- `--weight-medium / -semibold`
- `--spacing-2 / -3 / -4 / -5 / -6 / -7 / -8 / -12 / -13`
- `--radius-full / -sm / -xs`
- `--shadow-lg`
- `--color-background-inverse`
- `--z-dropdown / -sticky`
- `--ease-fast / -base`

## Accesibilidad

Los ítems con submenú son `<button>` con `aria-expanded`/`aria-controls` (divulgación, no `role="menu"`); Escape cierra y devuelve el foco. Submenús cerrados en `visibility: hidden`. Redes con nombre «FB Facebook» (WCAG 2.5.3); guiones sin anunciar. Foco amarillo sobre la foto y petróleo en la píldora. El `<header>` no va dentro de `<main>` ni de `<section>` (landmark `banner`).

## Decisiones y excepciones

- Submenús de Home, Services y Blog con placeholder: el diseño solo muestra el de Pages.
- Hover de los enlaces de la píldora en petróleo y submenú abierto con el chevron girado: el diseño no muestra el hover.
- Container query en vez de `@media`: la barra completa necesita ~1150px y el header no sabe en qué columna vive (con el container de Bootstrap, 1140px a 1280px de viewport, ya se desbordaba). Los umbrales son los breakpoints del theme (48/64/80rem) medidos sobre el ancho del header. Con el container de Bootstrap el menú aparece desde 992px de viewport (el plan decía `lg`, 1024px).
- Bajo 80rem de barra se ocultan las redes (están en el footer y en el off-canvas) y bajo 64rem el número queda solo para lectores. El diseño solo muestra 1920 y 480px.
- El header lleva `container-type`, que crea un contexto de apilamiento: la Section que lo superponga al hero le da su `z-index`.
- El círculo del chat es un adorno (confirmado por el equipo): va dentro del enlace del teléfono, que es el único elemento interactivo.
- Header fijo «por el momento» (decisión del equipo): variante `--fixed`. El diseño no muestra el estado con scroll; se deriva de tokens: la barra pasa a `--color-background-inverse` con `is-scrolled`, porque el texto blanco no se lee con el velo sobre las secciones crema. La demo del kit no es fija (taparía el kit): para verla, agregar la clase al header de una página. La Section reserva el espacio superior y define `scroll-padding-top` para los anclajes.
- Teléfono real confirmado: +880 (123) 456 789, en el header y en el off-canvas. El número de relleno del diseño (+ 123 (456) - 789) se descarta.
- La barra no lleva `backdrop-filter`: el velo es plano, como el badge (un filtro en el header recortaría cualquier descendiente fijo).
