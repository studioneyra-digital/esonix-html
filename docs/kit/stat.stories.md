# Stat

**Nivel:** Molécula · 10  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Stat */`) · showcase en `dist/kit/index.html#stat`

## Descripción

Cifra grande con etiqueta; el sufijo va atenuado. `--center` para la versión centrada.

## Snippets

**A la izquierda**

```html
<div class="stat">
  <p class="stat__value">3M<span class="stat__suffix">+</span></p>
  <p>People Using Our Platform</p>
</div>
```

**Centrada (`--center`)**

```html
<div class="stat stat--center">
  <p class="stat__value">98%</p>
  <p>Excellence in Customer Satisfaction</p>
</div>
<div class="stat stat--center">
  <p class="stat__value">12K<span class="stat__suffix">+</span></p>
  <p>Projects Successfully Finished</p>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.stat` | Cifra arriba y etiqueta abajo |
| `.stat__value` | La cifra en Mona Sans semibold del tamaño de h1 |
| `.stat__suffix` | Sufijo atenuado (tertiary); sigue siendo texto: el lector lo lee |
| `.stat--center` | Centra el texto |

## Tokens que consume

- `--text-h1`
- `--weight-semibold`
- `--color-text-primary / -tertiary / -secondary`
- `--spacing-2`

## Accesibilidad

Texto real; sufijo atenuado cumple AA.

## Decisiones y excepciones

- Las etiquetas «Excellence in Customer Satisfaction» y «Projects Successfully Finished» están cortadas en el diseño de mobile; se completaron como placeholder.
