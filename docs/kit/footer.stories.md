# Footer

**Nivel:** Section · 13  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:footer -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#footer`

## Descripción

Site Footer + Marquee arriba, con la foto desenfocada (`--blur-photo`) y velo detrás. Fuera de `<main>`.

## Snippet

```html
<footer class="site-footer page-footer" id="site-footer" data-surface="inverse">
  <div class="page-footer__media">
    <img src="assets/img/h1-footer-bg.webp" alt="" width="1920" height="880" loading="lazy">
  </div>
  <div class="marquee">
    <div class="marquee__viewport" aria-hidden="true">
      <div class="marquee__track">
        <div class="marquee__group">
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        </div>
        <div class="marquee__group">
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
          <span class="marquee__text">Connect With Us</span>
          <span class="marquee__text">Let's <span class="marquee__accent">Grow</span></span>
        </div>
      </div>
    </div>
    <p class="visually-hidden">Connect with us. Let's grow.</p>
    <div class="marquee__badge" aria-hidden="true">
      <img class="marquee__badge-logo" src="assets/img/primary-logo.png" alt="" width="140" height="40">
    </div>
  </div>
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
        <h2 class="site-footer__title" id="footer-utility-title">Utility Page</h2>
        <ul class="site-footer__list">
          <li><a href="#">License</a></li>
          <li><a href="#">Style Guide</a></li>
          <li><a href="#">Password Protected</a></li>
          <li><a href="#">Error 404</a></li>
          <li><a href="#">Changelog</a></li>
        </ul>
      </nav>
      <nav aria-labelledby="footer-follow-title">
        <h2 class="site-footer__title" id="footer-follow-title">Follow Us</h2>
        <ul class="site-footer__list">
          <li><a href="#">Facebook</a></li>
          <li><a href="#">Twitter</a></li>
          <li><a href="#">Instagram</a></li>
          <li><a href="#">Linkedin</a></li>
          <li><a href="#">Youtube</a></li>
        </ul>
      </nav>
      <div class="site-footer__offices-col">
        <h2 class="site-footer__title">Our Offices</h2>
        <div class="site-footer__offices">
          <div>
            <p class="site-footer__office-label">Operations &ndash; China</p>
            <p class="site-footer__office-city">Shanghai (China's largest cities)</p>
          </div>
          <div>
            <p class="site-footer__office-label">Headquarters &ndash; USA</p>
            <p class="site-footer__office-city">Seattle (major city in Washington)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="site-footer__legal">
    <div class="container site-footer__legal-inner">
      <p>Copyright &copy; 2026 Esonix. All Rights Reserved.</p>
      <p>
        <a href="#">Terms &amp; Condition</a>
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
| `footer.site-footer.page-footer + data-surface="inverse"` | Footer de la página; recorta la foto |
| `.page-footer__media` | Capa de la foto (filter: blur(--blur-photo)) con el velo en ::after |
| `.marquee (sin data-surface)` | Toma la superficie del footer y deja ver la foto |
| `.page-footer > .container` | Aire entre el Marquee y las columnas, medido en el diseño |

## Tokens que consume

- `--blur-photo`
- `--color-background-inverse`
- `--spacing-9 / -10 / -11 / -12`
- `Newsletter (molécula)`
- `Marquee, Site Footer (organismos)`

## Accesibilidad

`<footer>` fuera de `<main>`; títulos `<h2>`; `<nav>` nombrados. Marquee `aria-hidden` + frase única.

## Decisiones y excepciones

- Los títulos son `<h2>` en la página (el footer cuelga del `<body>`); en la ficha del organismo son `<h3>` porque viven dentro de una sección del kit.
- Marquee sin su propio `data-surface`: con él, su fondo inverso tapaba la foto.
