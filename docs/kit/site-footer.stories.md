# Site Footer

**Nivel:** Organismo · 08  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Site Footer */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#site-footer`

## Descripción

Cierre del sitio: Newsletter, Utility Page, Follow Us, Our Offices y barra legal, sobre fondo inverso. Corrige dos errores del export del diseño: «Pixenium» → Esonix, «404 Not Error» → Error 404.

## Snippets

**Footer completo**

```html
<footer class="site-footer" id="site-footer" data-surface="inverse">
  <div class="site-footer__top">
    <form class="newsletter" action="#">
      <label class="newsletter__title" for="footer-newsletter-email">Subscribe our newsletter to get latest updates</label>
      <div class="newsletter__field">
        <input class="input" type="email" id="footer-newsletter-email" name="email" placeholder="Enter your email" autocomplete="email" required>
        <button type="submit" class="newsletter__submit" aria-label="Subscribe"><span class="icon icon--send" aria-hidden="true"></span></button>
      </div>
    </form>
    <nav class="site-footer__col" aria-labelledby="footer-utility-title">
      <h3 class="site-footer__title" id="footer-utility-title">Utility Page</h3>
      <ul class="site-footer__list">
        <li><a href="#site-footer">License</a></li>
        <li><a href="#site-footer">Style Guide</a></li>
        <li><a href="#site-footer">Password Protected</a></li>
        <li><a href="#site-footer">Error 404</a></li>
        <li><a href="#site-footer">Changelog</a></li>
      </ul>
    </nav>
    <nav class="site-footer__col" aria-labelledby="footer-follow-title">
      <h3 class="site-footer__title" id="footer-follow-title">Follow Us</h3>
      <ul class="site-footer__list">
        <li><a href="#site-footer">Facebook</a></li>
        <li><a href="#site-footer">Twitter</a></li>
        <li><a href="#site-footer">Instagram</a></li>
        <li><a href="#site-footer">Linkedin</a></li>
        <li><a href="#site-footer">Youtube</a></li>
      </ul>
    </nav>
    <div class="site-footer__col">
      <h3 class="site-footer__title">Our Offices</h3>
      <div class="site-footer__offices">
      <div class="site-footer__office">
        <p class="site-footer__office-label">Operations – China</p>
        <p class="site-footer__office-city">Shanghai <span>(China's largest cities)</span></p>
      </div>
      <div class="site-footer__office">
        <p class="site-footer__office-label">Headquarters – USA</p>
        <p class="site-footer__office-city">Seattle <span>(major city in the state Washington)</span></p>
      </div>
      </div>
    </div>
  </div>
  <div class="site-footer__legal">
    <p>Copyright © 2026 Esonix. All Rights Reserved.</p>
    <p>
      <a href="#site-footer">Terms & Condition</a>
      <span aria-hidden="true">|</span>
      <a href="#site-footer">Privacy Policy</a>
    </p>
  </div>
</footer>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.site-footer + data-surface="inverse"` | Landmark contentinfo; la Section le da el fondo oscuro |
| `.site-footer__top` | Grilla de 4 columnas desde lg: Newsletter, Utility Page, Follow Us, Our Offices |
| `.site-footer__col + nav + aria-labelledby` | Columna de enlaces con su título como nombre accesible |
| `.site-footer__title` | Título de columna (h3) |
| `.site-footer__list` | Lista de enlaces placeholder |
| `.site-footer__offices / __office-label / __office-city` | Par región/ciudad de cada oficina |
| `.site-footer__legal` | Barra inferior: copyright y enlaces legales, con filete superior |

## Tokens que consume

- `--text-h6 / -sm`
- `--weight-semibold / -regular`
- `--color-text-inverse / -inverse-secondary`
- `--spacing-1 / -3 / -5 / -6 / -9`
- `--ease-fast`
- `Newsletter (molécula)`

## Accesibilidad

Landmark `contentinfo` nativo. Utility Page y Follow Us son `<nav aria-labelledby>` nombradas por su `<h3>`. El newsletter reutiliza la molécula (label real, botón con `aria-label`).

## Decisiones y excepciones

- «Pixenium» (nombre de otra marca filtrado en el export) se corrige a «Esonix»; «404 Not Error» se corrige a «Error 404» (ya usado en el submenú de Pages del header), según `plan.md`.
- Teléfono y redes no se repiten en el footer: ya están en el header y el off-canvas; el diseño tampoco los muestra acá.
- Enlaces de Utility Page, Follow Us y legales son placeholder (<code>href="#site-footer"</code>): no hay páginas reales todavía.
