# Progress

**Nivel:** Átomo · 08  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Progress */`) · showcase en `dist/kit/index.html#progress`

## Descripción

Barra con etiqueta y porcentaje. Usa `<progress>` nativo.

## Snippets

**Tres valores**

```html
<div class="progress">
  <div class="progress__head">
    <label for="progress-operational">Operational assessment</label>
    <span aria-hidden="true">90%</span>
  </div>
  <progress class="progress__bar" id="progress-operational" value="90" max="100">90%</progress>
</div>
<div class="progress">
  <div class="progress__head">
    <label for="progress-consultation">Consultation & analysis</label>
    <span aria-hidden="true">76%</span>
  </div>
  <progress class="progress__bar" id="progress-consultation" value="76" max="100">76%</progress>
</div>
<div class="progress">
  <div class="progress__head">
    <label for="progress-strategic">Strategic interpretation</label>
    <span aria-hidden="true">85%</span>
  </div>
  <progress class="progress__bar" id="progress-strategic" value="85" max="100">85%</progress>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.progress` | Contenedor: cabecera + barra |
| `.progress__head` | Fila con la etiqueta (<label for>) y el porcentaje (aria-hidden) |
| `.progress__bar` | El <progress> nativo: 3px de alto, relleno petróleo sobre pista clara |
| `value / max` | El avance real (0–100); el relleno lo dibuja el navegador |

## Tokens que consume

- `--color-action-primary`
- `--color-background-muted`
- `--color-text-primary`
- `--border-width-sm / -md`
- `--radius-full`
- `--ease-slow`

## Accesibilidad

`<label for>` + valor nativo; el % visible es `aria-hidden`.

## Decisiones y excepciones

- El diseño no muestra animación de llenado: el relleno aparece en su valor final. Una animación al entrar al viewport se decide en la Section.
