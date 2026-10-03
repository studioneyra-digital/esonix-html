# Team Profiles

**Nivel:** Section · 15  
**Dónde:** markup en `dist/about-us.html` (entre `<!-- section:team-profiles -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#team-profiles`

## Descripción

Section Head centrado + tres Card Team `--profile`, 3 columnas desde lg; la central `--reverse`.

## Snippet

```html
<section class="section team-profiles" id="team-profiles" aria-labelledby="team-profiles-title">
  <div class="container">
    <div class="section-head section-head--center">
      <div class="section-head__main" data-reveal>
        <p class="eyebrow eyebrow--center">Consulting Experts</p>
        <h2 class="section-title section-head__title" id="team-profiles-title">Meet Our Expert Team</h2>
      </div>
    </div>
    <div class="team-profiles__grid">
      <article class="card-team card-team--profile" data-reveal>
        <img class="card-team__photo" src="assets/img/h1-team-member-img-1.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Olivia Bennet</h3>
          <p class="card-team__role">Financial Advisor</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Olivia Bennet on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
      <article class="card-team card-team--profile card-team--reverse" data-reveal>
        <img class="card-team__photo" src="assets/img/h1-team-member-img-2.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Emma Wilson</h3>
          <p class="card-team__role">Business Analyst</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#" class="card-team__social" aria-label="Emma Wilson on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Emma Wilson on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Emma Wilson on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Emma Wilson on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
      <article class="card-team card-team--profile" data-reveal>
        <img class="card-team__photo" src="assets/img/h1-team-member-img-3.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Michael Turner</h3>
          <p class="card-team__role">Corporate Trainer</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#" class="card-team__social" aria-label="Michael Turner on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Michael Turner on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Michael Turner on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#" class="card-team__social" aria-label="Michael Turner on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.section-head--center` | Eyebrow y h2 centrados |
| `.team-profiles__grid` | Una columna en mobile; 3 columnas (424px a 1920) desde lg |
| `.card-team--profile.card-team--reverse` | La card central: texto arriba y foto abajo desde lg |

## Tokens que consume

- `--spacing-6`
- `Eyebrow (átomo)`
- `Card Team --profile (molécula)`

## Accesibilidad

`<article>` + `<h3>`; redes nombradas con la persona; fotos decorativas; `--reverse` no cambia el orden del DOM.

## Decisiones y excepciones

- Las redes llevan a `#`: no hay perfiles todavía.
- El id `team-profiles` es el destino de «More about us».
