# Off-canvas

**Nivel:** Organismo · 02  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Off-canvas */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#offcanvas`

## Descripción

Menú mobile: panel crema desde la derecha sobre la página desenfocada; submenús como `<details>`, Location, Contact y redes. Lo abre cualquier botón con `data-offcanvas-open` y `aria-controls`; el resto de la página queda `inert`.

## Snippets

**Markup**

```html
<div class="offcanvas" id="offcanvas-menu" data-offcanvas>
  <div class="offcanvas__backdrop" data-offcanvas-close></div>
  <div class="offcanvas__panel" role="dialog" aria-modal="true" aria-label="Menu" data-lenis-prevent>
    <div class="offcanvas__head">
      <a class="offcanvas__brand" href="#offcanvas">
        <img class="brand-logo" src="../assets/img/secondary-logo.png" alt="Esonix" width="140" height="40">
      </a>
      <button type="button" class="offcanvas__close" data-offcanvas-close>
        Close
        <span class="icon icon--x" aria-hidden="true"></span>
      </button>
    </div>
    <nav aria-label="Main">
      <ul class="offcanvas__list">
        <li>
          <details class="offcanvas__group" name="offcanvas-nav">
            <summary class="offcanvas__link">Home <span class="icon icon--chevron-down" aria-hidden="true"></span></summary>
            <ul class="offcanvas__sub">
              <li><a class="offcanvas__sublink" href="#offcanvas">Home Version 01</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Home Version 02</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Home Version 03</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details class="offcanvas__group" name="offcanvas-nav">
            <summary class="offcanvas__link">Services <span class="icon icon--chevron-down" aria-hidden="true"></span></summary>
            <ul class="offcanvas__sub">
              <li><a class="offcanvas__sublink" href="#offcanvas">Marketing Guidance</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Process Optimization</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Sales Improvement</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Service Details</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details class="offcanvas__group" name="offcanvas-nav">
            <summary class="offcanvas__link">Pages <span class="icon icon--chevron-down" aria-hidden="true"></span></summary>
            <ul class="offcanvas__sub">
              <li><a class="offcanvas__sublink" href="#offcanvas">About Us</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Portfolios</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Portfolio Details</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Team Members</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Pricing Page</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">FAQ Page</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Error 404</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Coming Soon</a></li>
            </ul>
          </details>
        </li>
        <li>
          <details class="offcanvas__group" name="offcanvas-nav">
            <summary class="offcanvas__link">Blog <span class="icon icon--chevron-down" aria-hidden="true"></span></summary>
            <ul class="offcanvas__sub">
              <li><a class="offcanvas__sublink" href="#offcanvas">Blog Grid</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Blog Standard</a></li>
              <li><a class="offcanvas__sublink" href="#offcanvas">Blog Details</a></li>
            </ul>
          </details>
        </li>
        <li><a class="offcanvas__link" href="#offcanvas">Contact</a></li>
      </ul>
    </nav>
    <div class="offcanvas__info">
      <div>
        <h2 class="offcanvas__title">Location</h2>
        <p>Seattle (major city in the state Washington).</p>
      </div>
      <div>
        <h2 class="offcanvas__title">Contact</h2>
        <p class="offcanvas__contact">
          <a href="tel:+880123456789">+880 (123) 456 789</a>
          <a href="mailto:support@esonix.com">support@esonix.com</a>
        </p>
      </div>
      <ul class="offcanvas__socials" aria-label="Social media">
        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
        <li><a class="icon-btn icon-btn--sm" href="#offcanvas" aria-label="X (Twitter)"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
      </ul>
    </div>
  </div>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.offcanvas + data-offcanvas + id` | Capa fija a pantalla completa; main.js la mueve al final de <body> |
| `.offcanvas.is-open` | Estado abierto (lo pone main.js): panel visible y fondo desenfocado |
| `.offcanvas__backdrop + data-offcanvas-close` | Fondo con velo y desenfoque; un click cierra |
| `.offcanvas__panel + role="dialog" aria-modal="true"` | Panel crema que entra desde la derecha; scrollea por dentro (data-lenis-prevent) |
| `.offcanvas__head / __brand / __close` | Logo (secondary-logo.png) y botón «Close» con el filete inferior |
| `.offcanvas__group + name` | <details> de cada submenú; el mismo name deja uno abierto a la vez |
| `.offcanvas__link` | Ítem principal en mayúsculas (summary o enlace) |
| `.offcanvas__sub / __sublink` | Lista y enlaces del submenú |
| `.offcanvas__info / __title / __contact` | Location y Contact |
| `.offcanvas__socials` | Icon Button --sm con el contorno fuerte del diseño |

## Tokens que consume

- `--color-background-default`
- `--color-overlay-light`
- `--blur-backdrop`
- `--color-text-primary / -secondary`
- `--color-action-primary`
- `--color-border-default / -strong`
- `--text-h4 / -h5 / -body`
- `--spacing-1 / -2 / -3 / -4 / -7 / -9 / -12 / -13`
- `--radius-sm / -xs`
- `--shadow-lg`
- `--z-modal`
- `--ease-fast / -base / -slow`

## Accesibilidad

`role="dialog"` + `aria-modal="true"`, nombre «Menu». Abierto: resto de `<body>` `inert`, foco en «Close», `aria-expanded="true"` en el botón. Escape/fondo/«Close» cierran y devuelven el foco. Cerrado: `visibility: hidden`. Submenús con `<details>` nativo. Animación con `--ease-slow` (0 ms con reduced motion).

## Decisiones y excepciones

- Submenús exclusivos (un `<details>` abierto a la vez, por `name`): el diseño los muestra todos cerrados.
- Fondo desenfocado sin oscurecer, como el diseño: nuevo token `--blur-backdrop` (6px) en `shadow.css`.
- Ancho del panel `clamp(16rem, 100% - 8rem, 24rem)`: deja ver una franja de página como el diseño (350 de 480 px).
- Se cierra solo si el botón que lo abrió deja de verse (la barra se ensanchó y apareció el menú), sin devolverle el foco.
