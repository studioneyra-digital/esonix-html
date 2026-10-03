# Service Nav

**Nivel:** Molécula · 14  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Service Nav */`) · showcase en `dist/kit/index.html#service-nav`

## Descripción

Card con la lista de servicios en píldoras; la actual con `aria-current="page"` (petróleo, cuadrado ámbar).

## Snippets

**Con el servicio actual marcado**

```html
<nav class="service-nav" aria-labelledby="service-nav-demo-title">
  <h3 class="service-nav__title" id="service-nav-demo-title">Exclusive Services</h3>
  <ul class="service-nav__list" role="list">
    <li><a class="service-nav__link" href="#">Strategic Planning<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
    <li><a class="service-nav__link" href="#" aria-current="page">Business Optimization<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
    <li><a class="service-nav__link" href="#">IT Consulting<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
    <li><a class="service-nav__link" href="#">Change Management<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
    <li><a class="service-nav__link" href="#">Leadership<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
  </ul>
</nav>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `nav.service-nav + aria-labelledby` | Landmark de navegación nombrado por su título |
| `.service-nav__title` | Título de 24px; h2 en la página (aside), h3 en el kit |
| `ul.service-nav__list + role="list"` | La lista de servicios |
| `a.service-nav__link` | Píldora gris con el texto y el cuadrado de flecha |
| `aria-current="page"` | Servicio de la página actual: petróleo y cuadrado ámbar |
| `.service-nav__icon` | Cuadrado blanco con icon--arrow-right; ámbar en hover y en el actual |

## Tokens que consume

- `--color-border-default / -subtle`
- `--color-background-subtle`
- `--color-action-primary / -on-primary`
- `--color-action-secondary / -on-secondary`
- `--color-surface-default`
- `--radius-md / -sm / -xs`
- `--text-h4`
- `--weight-medium / -semibold`
- `--spacing-2 / -4 / -5 / -6 / -8`
- `--ease-fast`

## Accesibilidad

`<nav>` nombrado por su título; actual con `aria-current="page"`; flechas `aria-hidden`; foco del theme por fuera de la píldora.

## Decisiones y excepciones

- El diseño no muestra el hover: el cuadrado toma el ámbar del activo, sin cambiar el fondo de la píldora.
- En la página, los servicios que todavía no tienen página enlazan a `#`; Business Optimization enlaza a `service-details.html`.
