# Card Team

**Nivel:** Molécula · 05  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Team */`) · showcase en `dist/kit/index.html#card-team`

## Descripción

Foto con rol (badge), acción («+») y nombre. `--elevated` sube la card 20px desde lg.

## Snippets

**Tres cards, la central elevada**

```html
<article class="card-photo card-team" data-surface="inverse">
  <img class="card-photo__img" src="../assets/img/h1-team-member-img-1.webp" alt="" width="848" height="920" loading="lazy">
  <div class="card-team__body">
    <div class="card-team__top">
      <span class="badge">Financial Advisor</span>
      <a href="#card-team" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Olivia Bennet"><span class="icon icon--plus" aria-hidden="true"></span></a>
    </div>
    <h3 class="card-team__name">Olivia Bennet</h3>
  </div>
</article>
<article class="card-photo card-team card-team--elevated" data-surface="inverse">
  <img class="card-photo__img" src="../assets/img/h1-team-member-img-2.webp" alt="" width="848" height="920" loading="lazy">
  <div class="card-team__body">
    <div class="card-team__top">
      <span class="badge">Business Analyst</span>
      <a href="#card-team" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Emma Wilson"><span class="icon icon--plus" aria-hidden="true"></span></a>
    </div>
    <h3 class="card-team__name">Emma Wilson</h3>
  </div>
</article>
<article class="card-photo card-team" data-surface="inverse">
  <img class="card-photo__img" src="../assets/img/h1-team-member-img-3.webp" alt="" width="848" height="920" loading="lazy">
  <div class="card-team__body">
    <div class="card-team__top">
      <span class="badge">Corporate Trainer</span>
      <a href="#card-team" class="icon-btn icon-btn--glass icon-btn--sm" aria-label="View profile of Michael Turner"><span class="icon icon--plus" aria-hidden="true"></span></a>
    </div>
    <h3 class="card-team__name">Michael Turner</h3>
  </div>
</article>
```

**--profile (About Us), la central con --reverse**

```html
      <article class="card-team card-team--profile">
        <img class="card-team__photo" src="../assets/img/h1-team-member-img-1.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Olivia Bennet</h3>
          <p class="card-team__role">Financial Advisor</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#card-team" class="card-team__social" aria-label="Olivia Bennet on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Olivia Bennet on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Olivia Bennet on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Olivia Bennet on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
      <article class="card-team card-team--profile card-team--reverse">
        <img class="card-team__photo" src="../assets/img/h1-team-member-img-2.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Emma Wilson</h3>
          <p class="card-team__role">Business Analyst</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#card-team" class="card-team__social" aria-label="Emma Wilson on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Emma Wilson on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Emma Wilson on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Emma Wilson on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
      <article class="card-team card-team--profile">
        <img class="card-team__photo" src="../assets/img/h1-team-member-img-3.webp" alt="" width="848" height="920" loading="lazy">
        <div class="card-team__info">
          <h3 class="card-team__name">Michael Turner</h3>
          <p class="card-team__role">Corporate Trainer</p>
          <ul class="card-team__socials" role="list">
            <li><a href="#card-team" class="card-team__social" aria-label="Michael Turner on Facebook"><span class="icon icon--facebook" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Michael Turner on X"><span class="icon icon--x-twitter" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Michael Turner on Instagram"><span class="icon icon--instagram" aria-hidden="true"></span></a></li>
            <li><a href="#card-team" class="card-team__social" aria-label="Michael Turner on LinkedIn"><span class="icon icon--linkedin" aria-hidden="true"></span></a></li>
          </ul>
        </div>
      </article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-photo` | Patrón base: foto + velo + contenido en la misma celda (con data-surface="inverse") |
| `.card-team--profile` | Variante clara: card blanca con marco de 12px, foto arriba, nombre, cargo y redes |
| `.card-team--reverse` | Con --profile: texto arriba y foto abajo desde lg |
| `a.card-team__social + aria-label` | Red social con área de 32px; el nombre dice persona y red («Olivia Bennet on LinkedIn») |
| `.card-team__top` | Fila superior: badge de rol y botón «+» |
| `.card-team__name` | Nombre (h3) centrado abajo |
| `.card-team--elevated` | Margen negativo de 20px desde lg y botón «+» amarillo |

## Tokens que consume

- `--radius-lg`
- `--scrim (degradé inferior)`
- `--color-background-inverse`
- `--spacing-3 / -5`
- `--text-h4`
- `--weight-medium`

## Accesibilidad

«+» como enlace con `aria-label` que nombra a la persona; foto decorativa; foco amarillo.

## Decisiones y excepciones

- El diseño no dice qué hace el «+»: se implementa como enlace al perfil (el menú Pages incluye «Team Members»). Pendiente de confirmar.
- La elevación es margen negativo, no `transform`, para que la card crezca y no se solape con las vecinas; la Section reserva el espacio.
