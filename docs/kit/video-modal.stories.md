# Video Modal

**Nivel:** Organismo · 05  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Video Modal */`) y `dist/assets/js/main.js` · showcase en `dist/kit/index.html#video-modal`

## Descripción

`<dialog>` nativo para YouTube. Lo abre cualquier botón con `data-video-id`; el iframe (youtube-nocookie) se crea en el click y se quita al cerrar. No está en el diseño: sale de tokens.

## Snippets

**Markup**

```html
<dialog class="video-modal" id="video-modal" data-video-modal data-surface="inverse" aria-labelledby="video-modal-title">
  <div class="video-modal__head">
    <h2 class="video-modal__title" id="video-modal-title">Video</h2>
    <button type="button" class="icon-btn icon-btn--glass icon-btn--sm" data-video-close aria-label="Close video"><span class="icon icon--x" aria-hidden="true"></span></button>
  </div>
  <div class="video-modal__frame"></div>
</dialog>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `dialog.video-modal + data-video-modal + data-surface="inverse"` | El modal; main.js lo mueve al final de <body> |
| `.video-modal__head / __title` | Barra con el título del video (nombre del diálogo) y «Close» |
| `data-video-close` | Botón que cierra |
| `.video-modal__frame` | Marco 16:9 donde main.js inserta el iframe |
| `data-video-id` | En el botón que abre: ID del video de YouTube |
| `data-video-title` | En el botón que abre: título del video (diálogo e iframe) |

## Tokens que consume

- `--color-background-inverse`
- `--color-overlay (fondo)`
- `--radius-lg`
- `--shadow-lg`
- `--spacing-3 / -4 / -5 / -6 / -8 / -13`
- `--text-body-lg`
- `--weight-medium`
- `--ease-base`

## Accesibilidad

`showModal()`: resto inert, foco en «Close»; Escape/«Close»/fondo cierran y el foco vuelve al botón. Nombre = título visible; iframe con `title`; openers con `aria-haspopup="dialog"`. Fundido con `--ease-base`.

## Decisiones y excepciones

- El diseño no muestra el modal: fondo inverso, velo `--color-overlay` y entrada con fundido y desplazamiento corto.
- El iframe no se carga hasta el click (`youtube-nocookie.com`, autoplay): la página no descarga YouTube al abrirse. Lleva `referrerpolicy="strict-origin-when-cross-origin"`, porque YouTube rechaza el embed sin referrer.
- Ancho máximo 64rem y nunca más alto que la ventana: el ancho se limita a `(100dvh - 8rem) × 16/9`.
