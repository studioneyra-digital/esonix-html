# Site Footer

**Nivel:** Organismo · 08  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Site Footer */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#site-footer`

## Descripción

Cierre del sitio: Newsletter, Utility Page, Follow Us, Our Offices y barra legal (filete a todo el ancho), sobre fondo inverso. Corrige dos errores del export del diseño: «Pixenium» → Esonix, «404 Not Error» → Error 404.

## Snippets

**Footer completo**

```html
<footer class="site-footer" data-surface="inverse">
  <div class="container">
    <div class="site-footer__top">
      <form class="newsletter" action="#">
        <label class="newsletter__title" for="footer-newsletter-email">Subscribe our newsletter to get latest updates</label>
        <div class="newsletter__field">
          <input class="input" type="email" id="footer-newsletter-email" name="email" placeholder="Enter your email" autocomplete="email" required>
          <button type="submit" class="newsletter__submit" aria-label="Subscribe"><span class="icon icon--send" aria-hidden="true"></span></button>
        </div>
      </form>
      <nav aria-labelledby="footer-utility-title">
        <h3 class="site-footer__title" id="footer-utility-title">Utility Page</h3>
        <ul class="site-footer__list">
          <li><a href="#">License</a></li>
          <li><a href="#">Style Guide</a></li>
          <li><a href="#">Password Protected</a></li>
          <li><a href="#">Error 404</a></li>
          <li><a href="#">Changelog</a></li>
        </ul>
      </nav>
      <nav aria-labelledby="footer-follow-title">
        <h3 class="site-footer__title" id="footer-follow-title">Follow Us</h3>
        <ul class="site-footer__list">
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
          <li><a href="#">Instagram</a></li>
          <li><a href="#">Linkedin</a></li>
          <li><a href="#">Youtube</a></li>
        </ul>
      </nav>
      <div class="site-footer__offices-col">
        <h3 class="site-footer__title">Our Offices</h3>
        <div class="site-footer__offices">
          <div>
            <p class="site-footer__office-label">Operations – China</p>
            <p class="site-footer__office-city">Shanghai (China's largest cities)</p>
          </div>
          <div>
            <p class="site-footer__office-label">Headquarters – USA</p>
            <p class="site-footer__office-city">Seattle (major city in Washington)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="site-footer__legal">
    <div class="container site-footer__legal-inner">
      <p>Copyright © 2026 Esonix. All Rights Reserved.</p>
      <p>
        <a href="#">Terms & Condition</a>
        <span aria-hidden="true">|</span>
        <a href="#">Privacy Policy</a>
      </p>
    </div>
  </div>
</footer>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `footer.site-footer + data-surface="inverse"` | Landmark contentinfo; la Section le da el fondo |
| `.container` | Contenedor de Bootstrap para las columnas y, dentro de la barra legal, para su contenido |
| `.site-footer__top` | 2 columnas bajo lg (newsletter y oficinas a todo el ancho); desde lg, 4 columnas con space-between |
| `nav + aria-labelledby` | Utility Page y Follow Us, nombradas por su propio título |
| `.site-footer__title` | Título de columna (h3) |
| `.site-footer__list` | Lista de enlaces placeholder |
| `.site-footer__offices-col / __offices / __office-label / __office-city` | Columna de oficinas: región en gris y ciudad en blanco |
| `.site-footer__legal / __legal-inner` | Barra inferior: filete a todo el ancho y contenido dentro de un .container |

## Tokens que consume

- `--text-h4 / -body-lg`
- `--weight-semibold`
- `--color-text-inverse / -inverse-secondary`
- `--spacing-1 / -3 / -4 / -6 / -7 / -8 / -9 / -12`
- `--border-width-sm`
- `--ease-fast`
- `Newsletter (molécula)`

## Accesibilidad

Landmark `contentinfo` nativo. Utility Page y Follow Us son `<nav aria-labelledby>` nombradas por su `<h3>`. El newsletter reutiliza la molécula.

## Decisiones y excepciones

- «Pixenium» (marca filtrada en el export) se corrige a «Esonix»; «404 Not Error» a «Error 404» (como en el submenú de Pages), según `plan.md`.
- Columnas desde lg: newsletter hasta 24rem y las otras tres a su ancho de contenido con `space-between`, que cae en las posiciones medidas del diseño (300 / 810 / 1093 / 1332 px a 1920).
- El footer trae sus `.container` (de Bootstrap) porque el filete legal debe cruzar todo el ancho y su texto alinearse con las columnas.
- Teléfono y redes en íconos no se repiten acá: el diseño no los muestra en el footer.
- Enlaces de Utility Page, Follow Us y legales son placeholder (`href="#"`): no hay páginas reales todavía.
