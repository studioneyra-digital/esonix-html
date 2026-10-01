# Card Project

**Nivel:** Molécula · 07  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Project */`) · showcase en `dist/kit/index.html#card-project`

## Descripción

Proyecto del bloque Finance: foto con marco blanco, número decorativo y título.

## Snippets

**Dos proyectos**

```html
<article class="card-project">
  <img class="card-project__img" src="../assets/img/h1-portfolio-img-3.webp" alt="" width="1920" height="1084" loading="lazy">
  <div class="card-project__caption">
    <span class="card-project__index" aria-hidden="true">// 01</span>
    <h3 class="card-project__title">Corporate Finance Management</h3>
  </div>
</article>
<article class="card-project">
  <img class="card-project__img" src="../assets/img/h1-portfolio-img-1.webp" alt="" width="1920" height="1076" loading="lazy">
  <div class="card-project__caption">
    <span class="card-project__index" aria-hidden="true">// 02</span>
    <h3 class="card-project__title">Advisory Services</h3>
  </div>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-project` | Card blanca con marco de 12px alrededor de la foto |
| `.card-project__img` | Foto 10:7 con esquinas redondeadas |
| `.card-project__index` | Número decorativo («// 01»), aria-hidden |
| `.card-project__title` | Título del proyecto (h3) |

## Tokens que consume

- `--color-surface-default`
- `--shadow-sm`
- `--radius-lg / -md`
- `--spacing-3 / -4 / -5`
- `--text-sm / -h4`
- `--color-text-tertiary`

## Accesibilidad

Número `aria-hidden`; título `h3`; foto decorativa.

## Decisiones y excepciones

- En mobile el diseño muestra el título de una card en amarillo sobre claro (1.4:1): no se replica, no pasa contraste.
- Solo hay una foto de proyecto fiel al diseño (la de las notas adhesivas); las demás son placeholders del set de portfolio.
