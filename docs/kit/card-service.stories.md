# Card Service

**Nivel:** Molécula · 01  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Card Service */`) · showcase en `dist/kit/index.html#card-service`

## Descripción

Card de servicio: foto, ícono, título y texto. `data-surface="brand"` la destaca (petróleo, ícono amarillo).

## Snippets

**Normal y destacada**

```html
<article class="card-service">
  <img class="card-service__media" src="../assets/img/h1-service-img-2.webp" alt="" width="1500" height="900" loading="lazy">
  <div class="card-service__body">
    <div class="card-service__head">
      <span class="icon icon--target card-service__icon" aria-hidden="true"></span>
      <h3 class="card-service__title">Marketing Guidance</h3>
    </div>
    <p>Through expert insights and strategic planning, marketing guidance enables businesses to understand customer.</p>
  </div>
</article>
<article class="card-service" data-surface="brand">
  <img class="card-service__media" src="../assets/img/h1-service-img-3.webp" alt="" width="1500" height="900" loading="lazy">
  <div class="card-service__body">
    <div class="card-service__head">
      <span class="icon icon--trending-up card-service__icon" aria-hidden="true"></span>
      <h3 class="card-service__title">Process Optimization</h3>
    </div>
    <p>By analyzing existing operations and implementing effective improvements, process optimization helps business.</p>
  </div>
</article>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.card-service` | Card blanca con sombra suave; ocupa el alto de su contenedor |
| `.card-service__media` | Foto 5:3 con esquinas redondeadas (la fuente es 1500×900) |
| `.card-service__head / __icon / __title` | Fila con el ícono de 32px y el título (h3) al lado |
| `data-surface="brand"` | Versión destacada: fondo petróleo, texto claro, ícono amarillo y foco amarillo |

## Tokens que consume

- `--color-surface-default`
- `--shadow-sm`
- `--radius-lg / -md`
- `--spacing-3 / -4 / -5 / -7`
- `--text-h4`
- `--weight-medium`
- `--color-text-secondary / -inverse-secondary / -highlight`

## Accesibilidad

Foto decorativa; título `h3`; ícono `aria-hidden`; la card no es un enlace.

## Decisiones y excepciones

- Los iconos del diseño son glifos propios de cada servicio; aquí se usan Lucide equivalentes (target, trending-up, chart-pie, users, lightbulb) hasta tener los del cliente.
- Las cards del diseño tienen esquinas de ~20px: se usa `--radius-lg` (24px) para cards y `--radius-md` (16px) para sus fotos.
