# Interacción y motion

Reglas de movimiento del theme. Las citan `assets/css/tokens/transitions.css`, `docs/stack.md` y
`docs/anti-patrones.md`. El movimiento comunica (llegada de contenido, estado, cambio de página); no decora.

## 1. Curvas y duraciones

- **Entra = ease-out · sale = ease-in · cambio de estado = ease-in-out.** Nada de rebotes ni elásticos: la
  personalidad del theme es corporativa (ver `anti-patrones.md` §Excepciones).
- Todo valor sale de un token de `transitions.css`. Cada token es duración + curva y se usa como
  `transition: color var(--ease-fast)` o `animation: nombre var(--ease-reveal)`.

| Token | Valor | Uso |
|---|---|---|
| `--ease-fast` | 150ms ease | hover, focus, tap |
| `--ease-base` | 250ms ease | abrir, cerrar, cambiar de estado |
| `--ease-slow` | 420ms expo-out | reveals de componente (acordeón, barras) |
| `--ease-reveal` | 800ms expo-out | entrada de contenido al hacer scroll |
| `--ease-reveal-mask` | 1100ms quart-out | máscara que descubre una foto |
| `--reveal-distance` | `--spacing-7` | recorrido vertical de la entrada |
| `--reveal-stagger` | 90ms | desfase entre elementos que entran juntos |
| `--duration-count` | 1600ms | contadores (solo duración; la curva la aplica `main.js`) |
| `--ease-page-out` | 200ms ease-in | salida de la página al navegar |
| `--ease-page-in` | 450ms expo-out | llegada de la página nueva |
| `--duration-spin` | 900ms | animaciones infinitas (spinners) |

## 2. Capa 1 — revelado al entrar en el viewport

API declarativa: el contenido se edita en el HTML y el efecto se elige con un atributo.

| Atributo | Efecto | Dónde |
|---|---|---|
| `data-reveal` | Sube `--reveal-distance` mientras aparece | Encabezados de sección, cards, bloques de texto, formularios, carruseles (el contenedor, nunca las slides) |
| `data-reveal="mask"` | Una máscara (`clip-path`) descubre el elemento de abajo hacia arriba | Fotos grandes y sus marcos. Nunca en la foto del LCP |
| `data-count` | Cuenta desde 0 hasta el valor del HTML | `.stat__value` y `.progress` (anima el `<progress>`, `--progress` y el porcentaje) |

- **Desfase automático:** los elementos que entran en el mismo cuadro (una fila de cards, el bloque del hero
  al cargar) se escalonan solos, en orden de lectura, con `--reveal-stagger`. Tope de 6 pasos. No hace falta
  numerarlos en el HTML.
- **Se activa a ~10 % del borde inferior** del viewport y una sola vez; no se repite al volver a subir.
- **Lo que ya pasó** (recarga a mitad de página, salto a un ancla) se muestra sin animar.
- **Foco por teclado:** si el foco entra a un elemento todavía oculto, se revela en el acto.
- **No anidar** `data-reveal` dentro de otro `data-reveal`.
- **Nunca** en: la foto ni el `<h1>` que sean candidato a LCP con `mask` (el texto del hero sí puede subir,
  porque la foto es el LCP y no se anima), slides de Swiper, el footer y el header (compartidos), la lista
  de palabras de la Home (ya tiene su propio ScrollTrigger).

### Mecánica

- Una línea en el `<head>` (bloque `shared:assets`) pone la clase `has-reveal` en `<html>` antes del primer
  pintado, para que no parpadee. Si `main.js` no llegó al evento `load`, la misma línea saca la clase:
  **sin JS, todo se ve**.
- El estado oculto vive en `@media screen and (prefers-reduced-motion: no-preference)`: con «reducir
  movimiento» o al imprimir, el contenido nunca se oculta y los contadores muestran el valor final.
- Las entradas son `animation` con `animation-fill-mode: backwards` sobre `opacity`, `translate` y
  `clip-path`. No usan `transform` ni `transition`, así no pisan los hovers de los componentes. Al terminar,
  el elemento vuelve a sus estilos propios.
- Sin CLS: solo se animan propiedades que no mueven el layout. El número de un contador reserva el ancho
  de su valor final y usa cifras tabulares.
- Accesibilidad de los contadores: el número que cambia va `aria-hidden`; el lector de pantalla lee el
  valor final de un texto oculto.

## 3. Capa 3 — transición entre páginas

- `@view-transition { navigation: auto; }` (CSS, sin JS), solo con `prefers-reduced-motion: no-preference`.
- La página sale con un fundido (`--ease-page-out`) y la nueva llega con otro (`--ease-page-in`). Solo
  opacidad: mover la captura entera deja una franja vacía arriba durante el fundido. El movimiento de llegada
  lo dan los `data-reveal` del Page Hero (breadcrumb y `<h1>`).
- El header `--inner` lleva `view-transition-name: site-header`: entre páginas interiores queda quieto.
  La Home tiene otro header (fijo sobre la foto), así que de la Home a una interior el header se funde con
  la página.
- Navegadores sin soporte navegan como siempre. Solo aplica entre páginas del mismo origen.

## 4. Propuesta por capas (2026-10-03)

El motion del sitio se planteó en cuatro capas, de la más barata y segura a la más ambiciosa. El usuario eligió
**Capa 1 + Capa 3 con intensidad media**. Las otras dos quedan documentadas para retomarlas si el sitio lo pide.
Para casi todas hay precedentes probados en `experiments/lenis-sandbox/experiments/` (`reveal-stagger`,
`reveal-mascara`, `parallax-fondo`, `escalado-imagenes`, `navbar-direccion-scroll`, `split-text-lineas`) y en
`experiments/dental-website` (`data-reveal`, contadores).

| Capa | Qué incluye | Motor | Estado |
|---|---|---|---|
| **1 · Entradas al hacer scroll** | Subida de títulos, cards, formularios y carruseles con desfase automático; máscara en las fotos grandes; contadores en Stats; barras de progreso que se llenan | CSS + `IntersectionObserver` (sin GSAP) | ✅ Hecha (§2) |
| **2 · Movimiento ligado al scroll** | Parallax suave en la foto del Hero y del Page Hero; zoom leve (1.1 → 1) en fotos grandes mientras cruzan el viewport. Desactivado o reducido en mobile | GSAP + ScrollTrigger (ya cargado a demanda con `requireLib`) | No elegida |
| **3 · Transición entre páginas** | Fundido entre páginas; el header `--inner` queda quieto | `@view-transition` (CSS puro) | ✅ Hecha (§3) |
| **4 · Microinteracciones y extras** | Header que se esconde al bajar y vuelve al subir; zoom de imagen en hover en las cards que no lo tienen; titulares revelados línea por línea (split text) | CSS + JS propio | No elegida |

### Niveles de intensidad que se ofrecieron

- **Sutil** (corporativo): solo entrada suave con desfase corto.
- **Media** (elegida): sutil + máscaras en las fotos + contadores. El parallax de la propuesta original es de la
  Capa 2, que no se eligió.
- **Expresiva**: media + titulares por línea.

### Si se retoma la Capa 2

- Cada efecto con su propio `ScrollTrigger` y `scrub`, sin `pin` (los bugs de pin + Lenis ya se evitaron en la
  Word List, ver `docs/stack.md`).
- La foto del LCP solo se puede mover con `transform` (nunca `opacity` ni `clip-path` al cargar).
- Con «reducir movimiento», ni siquiera se pide GSAP (mismo patrón que `initWordList`).
- Revisar la trampa conocida: `transform` + `overflow: hidden` en el mismo elemento rompe el recorte; el zoom va
  en la `<img>` y el recorte en su contenedor.

### Si se retoma la Capa 4

- **Header que se esconde:** se descartó porque el header `--inner` ya es una píldora compacta y esconderlo aporta
  poco. Si se agrega, no debe esconderse mientras tiene el foco o un submenú abierto.
- **Split text:** el split en `<span>` infla el alto de línea real y rompe la lectura de los lectores de pantalla.
  Exige `aria-label` con el texto completo en el titular y `aria-hidden` en los fragmentos. Solo para el `<h1>` de
  los heros.

### Descartado

- WOW.js: vendorizado pero sin uso; el revelado lo resuelve `IntersectionObserver`. Además necesita
  `animate.css`.

## 5. Reducir movimiento

Los tokens de duración caen a `0ms` (no `0.01ms`); `--reveal-distance` y `--reveal-stagger`, a `0`. Además:
sin Lenis, sin la lista de palabras animada, sin estado oculto, sin contadores y sin transición entre páginas.
