# Logos

**Nivel:** Section · 10  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:logos -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#logos`

## Descripción

Solo mobile. Grilla 2 × 4 con filetes: 7 logos (4 imágenes repetidas) y «Join with Us ↗». Oculta desde lg.

## Snippet

```html
<section class="section logos" id="logos" aria-labelledby="logos-title">
  <div class="container">
    <h2 class="visually-hidden" id="logos-title">Our partners</h2>
    <ul class="logo-grid" role="list">
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-1.png" alt="Logoipsum" width="175" height="34" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-2.png" alt="Logoipsum" width="145" height="35" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-3.png" alt="Logoipsum" width="155" height="28" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-4.png" alt="Logoipsum" width="155" height="31" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-1.png" alt="Logoipsum" width="175" height="34" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-2.png" alt="Logoipsum" width="145" height="35" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal><img src="assets/img/h1-partner-img-3.png" alt="Logoipsum" width="155" height="28" loading="lazy"></li>
      <li class="logo-grid__cell" data-reveal>
        <a href="contact.html" class="link-arrow">
          Join with Us
          <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
        </a>
      </li>
    </ul>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `section.section.logos` | Sin padding superior (el diseño la pega a Team); display: none desde lg |
| `ul.logo-grid` | Grilla de 2 columnas; los filetes son su fondo, que asoma por un gap de 1px |
| `.logo-grid__cell` | Celda de 100px de alto mínimo con el logo centrado |
| `.logos--desktop` | About Us: la grilla también desde lg, en 4 columnas |

## Tokens que consume

- `--color-border-default`
- `--color-background-default`
- `--border-width-sm`
- `--radius-md`
- `--spacing-4 / -5 / -11`
- `Link Arrow (átomo)`

## Accesibilidad

`<h2>` oculto «Our partners»; logos con `alt`; «Join with Us» enlace con texto visible.

## Decisiones y excepciones

- Solo mobile (decisión del equipo); las 4 imágenes de partners se repiten para completar 7 celdas (decisión del equipo).
- Los filetes salen del fondo de la grilla y un gap de 1px: no dependen de cuántas celdas haya.
- Los PNG de partners son casi negros y el diseño los muestra en gris: se usan tal cual, sin filtros.
- «Join with Us» lleva al footer (contacto): el diseño no dice adónde va.
