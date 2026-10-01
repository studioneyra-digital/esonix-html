# Avatar

**Nivel:** Átomo · 07  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Avatar */`) · showcase en `dist/kit/index.html#avatar`

## Descripción

Retrato circular de 40px; `--portrait` retrato cuadrado de autor (80px). Avatar Stack solapa avatares y cierra con «+».

## Snippets

**Avatar y retrato de autor**

```html
<img class="avatar" src="../assets/img/h1-testimonial-thumb-img-1.webp" alt="" width="40" height="40">
<img class="avatar avatar--portrait" src="../assets/img/h1-testimonial-thumb-img-2.webp" alt="" width="80" height="80">
```

**Avatar Stack**

```html
<div class="avatar-stack">
  <img class="avatar" src="../assets/img/h1-testimonial-thumb-img-1.webp" alt="" width="40" height="40">
  <img class="avatar" src="../assets/img/h1-testimonial-thumb-img-2.webp" alt="" width="40" height="40">
  <img class="avatar" src="../assets/img/h1-testimonial-thumb-img-3.webp" alt="" width="40" height="40">
  <span class="avatar-stack__more"><span class="icon icon--plus" aria-hidden="true"></span></span>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.avatar` | Imagen circular de 40px con object-fit: cover |
| `.avatar--portrait` | Retrato de autor: 80px con esquinas de 8px |
| `.avatar-stack` | Contenedor que solapa a sus hijos; el anillo es --avatar-ring (por defecto, el fondo de página) |
| `.avatar-stack__more` | Cierre amarillo con «+» |
| `--avatar-ring` | Propiedad: poner el color del fondo donde se use el stack (ej. surface-default en una card) |

## Tokens que consume

- `--spacing-8 / -11`
- `--radius-full / -sm`
- `--color-background-muted / -default`
- `--color-action-secondary`
- `--color-action-on-secondary`
- `--border-width-md`

## Accesibilidad

Caras con `alt=""` (el texto vecino da el sentido); `width`/`height` explícitos.

## Decisiones y excepciones

- El diseño usa una imagen horneada con 3 caras (`h1-about-users.png`); aquí se arma con avatares reales para que el stack sea reutilizable. Las caras de los demos son las de los testimonios, no las del PNG.
