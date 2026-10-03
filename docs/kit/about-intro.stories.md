# About Intro

**Nivel:** Section · 14  
**Dónde:** markup en `dist/about-us.html` (entre `<!-- section:about-intro -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#about-intro`

## Descripción

«What We Do» de About Us: eyebrow, h2, checks y botón a la izquierda; foto con marco, «Who we are», filete y cita con firma a la derecha. Mobile: apilado.

## Snippet

```html
<section class="section about-intro" aria-labelledby="about-intro-title">
  <div class="container about-intro__grid">
    <div class="about-intro__lead" data-reveal>
      <p class="eyebrow">What We Do</p>
      <h2 class="section-title" id="about-intro-title">Unlocking Business Potential with Tailored Solutions</h2>
      <ul class="about-intro__list" role="list">
        <li><span class="icon icon--circle-check-outline" aria-hidden="true"></span>Client-Focused Consulting</li>
        <li><span class="icon icon--circle-check-outline" aria-hidden="true"></span>Business Performance Improvement</li>
        <li><span class="icon icon--circle-check-outline" aria-hidden="true"></span>Innovative Business Solutions</li>
      </ul>
      <a href="#team-profiles" class="btn">
        More about us
        <span class="btn__icon"><span class="icon icon--arrow-up-right" aria-hidden="true"></span></span>
      </a>
    </div>
    <div class="about-intro__story">
      <div class="photo-frame about-intro__photo" data-reveal="mask">
        <img src="assets/img/h3-about-img.webp" alt="A consultant smiling as she shakes hands with a client" width="1200" height="1200" loading="lazy">
      </div>
      <div class="about-intro__text" data-reveal>
        <h3 class="about-intro__subtitle">Who we are</h3>
        <p>Our mission is to help businesses make smarter decisions &amp; achieve lasting success. By combining industry expertise, strategic insight</p>
        <p>With years of industry experience, we empower businesses to overcome challenges and unlock new opportunities. From business strategy and market analysis to operational improvement</p>
      </div>
      <hr class="divider">
      <figure class="about-intro__quote" data-reveal>
        <blockquote>
          <p><strong>From Vision to Success</strong> — Providing Expert Business Consulting that Delivers Real Impact. By combining industry expertise, data-driven insights, &amp; a client-focused approach</p>
        </blockquote>
        <figcaption><img src="assets/img/signature-2.png" alt="Signature of Michel Jhon" width="108" height="46" loading="lazy"></figcaption>
      </figure>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.about-intro__grid` | Una columna en mobile; desde lg 30rem | 42.5rem (480 y 680px a 1920) a los extremos |
| `.about-intro__lead / __list` | Eyebrow, h2, lista con icon--circle-check-outline y botón |
| `.about-intro__story` | Foto con marco, texto, filete y cita |
| `.photo-frame.about-intro__photo` | Foto 5:4 con marco blanco de 8px |
| `h3.about-intro__subtitle` | «Who we are», 24px |
| `figure.about-intro__quote` | Comillas decorativas (::before) a la izquierda de la cita y la firma |

## Tokens que consume

- `--text-h1 (section-title) / -h4 / -h5 / -display`
- `--color-text-primary`
- `--weight-regular / -medium / -semibold`
- `--spacing-3 / -4 / -5 / -7 / -10`
- `Eyebrow, Button, Divider, Icon (átomos)`

## Accesibilidad

Cita en `<figure>` + `<blockquote>`; firma en `<figcaption>` con `alt`. Comillas generadas sin texto alternativo. Foto con `alt`; checks `aria-hidden`.

## Decisiones y excepciones

- «More about us» lleva al equipo (`#team-profiles`): el diseño no dice adónde va.
- Ícono nuevo `circle-check-outline` (el `circle-check` del theme es relleno, el de Pricing; esta lista lo muestra en contorno).
- «From Vision to Success» va en `<strong>` con peso normal: el diseño solo lo distingue por color.
- Excepción declarada a anti-patrones #13: los párrafos de «Who we are» llegan a ~85 caracteres por línea en la columna de 680px, como el diseño.
