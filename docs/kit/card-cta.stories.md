# Card CTA

**Nivel:** Molécula · 08  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card CTA */`) · showcase en `dist/kit/index.html#card-cta`

## Descripción

Card con foto: ícono arriba; título, texto y enlace amarillo abajo (FAQ).

## Snippets

**Sobre foto**

```html
<article class="card-photo card-cta" data-surface="inverse">
  <img class="card-photo__img" src="../assets/img/h1-cta-img.webp" alt="" width="1040" height="700" loading="lazy">
  <div class="card-cta__body">
    <span class="card-cta__icon"><span class="icon icon--hexagon" aria-hidden="true"></span></span>
    <div class="card-cta__text">
      <h3 class="card-cta__title">Still have questions?</h3>
      <p>Our results-focused strategies are designed to deliver measurable business growth</p>
      <a href="#card-cta" class="link-arrow link-arrow--highlight">
        Contact Us
        <span class="icon icon--arrow-up-right" aria-hidden="true"></span>
      </a>
    </div>
  </div>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-photo` | Patrón base con foto, velo y contenido (con data-surface="inverse") |
| `.card-cta__icon` | Círculo translúcido con ícono |
| `.card-cta__text` | Título (h3), texto y enlace amarillo |

## Tokens que consume

- `--radius-lg`
- `--scrim (velo del 45% al 90%)`
- `--color-overlay-light`
- `--color-text-highlight (enlace)`
- `--text-h4`
- `--spacing-3 / -6 / -8 / -9`

## Accesibilidad

Texto sobre velo del 45–90%; enlace amarillo solo sobre oscuro.

## Decisiones y excepciones

- El ícono del diseño (poliedro) es un Lucide `hexagon` equivalente.
