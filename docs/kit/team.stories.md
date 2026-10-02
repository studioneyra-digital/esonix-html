# Team

**Nivel:** Section · 09  
**Dónde:** markup en `dist/index.html` (entre `<!-- section:team -->`), CSS en `dist/assets/css/main.css` (bloque `sections:`) · showcase en `dist/kit/index.html#team`

## Descripción

Section Head `--split` sin acciones (texto contra el borde derecho) y tres Card Team; desde lg en 3 columnas con la central elevada 20px.

## Snippet

```html
<section class="section team" id="team" aria-labelledby="team-title">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="section-head__main">
        <p class="eyebrow">Consulting Experts</p>
        <h2 class="section-title section-head__title" id="team-title">Meet Our Expert Team</h2>
      </div>
      <p class="section-head__text">We are passionate about supporting businesses with expert advice, smart strategies.</p>
    </div>
    <div class="team__grid">
      <article class="card-photo card-team" data-surface="inverse">
        <img class="card-photo__img" src="assets/img/h1-team-member-img-1.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__body">
          <div class="card-team__top">
            <span class="badge">Financial Advisor</span>
            <a href="#" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Olivia Bennet"><span class="icon icon--plus" aria-hidden="true"></span></a>
          </div>
          <h3 class="card-team__name">Olivia Bennet</h3>
        </div>
      </article>
      <article class="card-photo card-team card-team--elevated" data-surface="inverse">
        <img class="card-photo__img" src="assets/img/h1-team-member-img-2.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__body">
          <div class="card-team__top">
            <span class="badge">Business Analyst</span>
            <a href="#" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Emma Wilson"><span class="icon icon--plus" aria-hidden="true"></span></a>
          </div>
          <h3 class="card-team__name">Emma Wilson</h3>
        </div>
      </article>
      <article class="card-photo card-team" data-surface="inverse">
        <img class="card-photo__img" src="assets/img/h1-team-member-img-3.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__body">
          <div class="card-team__top">
            <span class="badge">Corporate Trainer</span>
            <a href="#" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Michael Turner"><span class="icon icon--plus" aria-hidden="true"></span></a>
          </div>
          <h3 class="card-team__name">Michael Turner</h3>
        </div>
      </article>
    </div>
  </div>
</section>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.section-head--split` | Título | texto; sin __actions no hay tercera columna |
| `.team__grid` | Una columna en mobile; 3 desde lg, con padding que reserva la elevación |
| `.card-team--elevated` | La central, 20px más alta arriba y abajo (desde lg) |

## Tokens que consume

- `--spacing-5 / -6`
- `Badge, Icon Button (átomos)`
- `Card Team (molécula)`

## Accesibilidad

`<article>` con `<h3>`; «+» nombrado «View profile of …». Fotos decorativas.

## Decisiones y excepciones

- La grilla reserva con su padding (20px) el espacio de la card elevada: así no invade el encabezado. Medido a 1920: 84px del título a las cards laterales y 64px a la elevada.
- Los «+» llevan a `#`: no hay páginas de perfil todavía.
