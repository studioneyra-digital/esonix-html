# Select

**Nivel:** Átomo · 12  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Select */`) · showcase en `dist/kit/index.html#select`

## Descripción

`.input` sobre `<select>` nativo sin flecha del sistema; el chevron y el label flotante los pone Field `--select`.

## Snippets

**Vacío y con una opción elegida (--filled)**

```html
<div class="field field--filled field--select">
  <label class="field__label" for="select-demo-empty">Service<span aria-hidden="true">*</span></label>
  <select class="input input--filled field__control" id="select-demo-empty" name="service" required>
    <option value="" hidden selected></option>
    <option>Strategic Planning</option>
    <option>Business Optimization</option>
    <option>IT Consulting</option>
  </select>
</div>
<div class="field field--filled field--select">
  <label class="field__label" for="select-demo-chosen">Service<span aria-hidden="true">*</span></label>
  <select class="input input--filled field__control" id="select-demo-chosen" name="service" required>
    <option value="" hidden></option>
    <option>Strategic Planning</option>
    <option selected>Business Optimization</option>
    <option>IT Consulting</option>
  </select>
</div>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `select.input` | Sin apariencia nativa; deja lugar al chevron a la derecha |
| `option[value=""][hidden][selected]` | Opción vacía inicial: deja el label en reposo y hace fallar required hasta elegir |
| `.field--select` | Dibuja el chevron y maneja el label (ver Field) |
| `required` | Obligatorio: main.js muestra «Choose an option.» si queda vacío |

## Tokens que consume

- `Input (átomo)`
- `Field (átomo)`
- `--color-text-primary (chevron)`
- `--spacing-5 / -7`

## Accesibilidad

`<select>` nativo (teclado, lector, selector del sistema); nombre del `<label>`; chevron decorativo; opción vacía `hidden`.

## Decisiones y excepciones

- Nativo antes que un select a medida: el diseño no pide nada que el nativo no haga, y uno a medida necesita JS y ARIA de listbox.
- La opción vacía no lleva `disabled`: con `disabled`, Chromium/Windows fuerza el color del texto y obligaría a usar `!important`, que el theme no admite (CLAUDE.md §11).
- El chevron repite el data URI de `icon--chevron-down` (un pseudo-elemento no puede usar `.icon`): si cambia uno, cambiar el otro.
- Safari no oculta opciones con `hidden`: ahí la lista muestra una fila vacía al principio. Elegirla deja el campo vacío y la validación lo marca.
