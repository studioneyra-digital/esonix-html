# Service Details — Plan de implementación

> **Para quien ejecute:** seguir las tareas en orden; cada paso es una casilla (`- [ ]`). Spec: `docs/plan-etapa-5.md` (sección «Service Details»). Contexto: `CLAUDE.md`, `docs/traspaso-etapa-5.md`, `docs/tools/README.md`.

**Objetivo:** construir `dist/service-details.html` (plantilla de servicio con el contenido de **Business Optimization**) desde `docs/design/Service-Details-Desktop.png` (1920×3091) y `Service-Details-Mobile.png` (480×4552).

**Arquitectura:** la página reutiliza el Page Hero, el header `--inner`, el footer, el Quote Form y el Video Modal. Suma una Section nueva (`service-details`: artículo + aside), tres átomos o variantes (Check List, Input/Field `--filled`, Select), una molécula (Service Nav), dos variantes (Quote Form `--outline`, Accordion `--framed`) y un ícono (`badge-check`). Los bloques generados de `main.css` y el kit salen de `docs/tools/*.py`; el bloque `sections:` se escribe a mano.

**Stack:** HTML5, CSS con tokens, JS vanilla (`main.js`), Python 3 (solo librería estándar) para los generadores y `playwright-cli` para la verificación.

## Restricciones globales

- Sin build, sin gestor de paquetes, sin librerías nuevas.
- **Sin `!important`.** El Select se resuelve con una opción vacía sin `disabled` (ver Tarea 1): la excepción de `CLAUDE.md` §11 no hace falta.
- Solo tokens semánticos en componentes (nada de `--color-brand-*` / `--color-neutral-*`). Sin magic numbers: si una medida no cae en la escala, se redondea al token más cercano y se reporta el desvío.
- Los bloques `atoms:` / `molecules:` / `organisms:` de `main.css` **solo se cambian desde su generador**. El bloque `sections:` es manual y la Section nueva va en la subsección «Sections de las páginas interiores», al final.
- El header, el footer y el off-canvas **se editan solo en `index.html`** y se propagan con `python docs/tools/sync_shared.py`.
- Clases y código en inglés; comentarios y documentación en español; copy del sitio en inglés.
- WCAG 2.2 AA: `<label>` asociado, foco visible, ≥ 4.5:1 en texto y ≥ 3:1 en bordes de controles, `prefers-reduced-motion`.
- Breakpoints: `sm` 30rem, `md` 48rem, `lg` 64rem, `xl` 80rem. El diseño pasa de mobile a desktop en `lg`.
- Decisiones del usuario (esta página):
  - Fotos sustitutas: hero `h1-process-img-2.webp`, apretón de manos `h1-process-img-3.webp`, video `download.webp`.
  - `h1` «Business Optimization»; breadcrumb Home › Services › Business Optimization.
  - FAQ adaptado de la Home.
  - Select con los 5 servicios, obligatorio.
  - Campos rellenos con **filete inferior fuerte**.
- Decisiones vigentes de la etapa: dominio `https://esonix.example`, footer de la Home, `h1` interior con `--text-h1`, FormSubmit a `studioneyra@gmail.com`, sin autoplay.
- Archivos en CRLF (`index.html`, `main.css`, …): editarlos con Edit, o con Python leyendo y escribiendo bytes para conservar el fin de línea. Código Python con barras invertidas o comillas tipográficas: siempre con Write/Edit y `PYTHONUTF8=1`, nunca en un heredoc.
- Commits con rutas explícitas, **nunca `git add -A`**. Mensaje terminado en `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. La página se commitea una sola vez, tras la aprobación del usuario.

## Medidas tomadas del PNG (desktop 1920 / mobile 480)

Tipografía medida con el ancho del texto en Mona Sans (receta de `traspaso-etapa-5.md` §6):

| Texto | Desktop | Mobile | Token elegido | Desvío |
|---|---|---|---|---|
| h2 «Explore our Service Lists» | 32 | 24 | `--text-h2` (36/28) | +4 px: con `--text-h3` quedaría igual que los h3 de 28 y se perdería la jerarquía |
| h3 «Document Required», «Key Features» | 28 | 20 | `--text-h3` (28/22) | mobile +2 |
| h3 «Mistakes to avoid…» | 24 | 18 | `--text-h6` → `--text-h4` desde `lg` | — |
| h4 de cada documento | 18 | 18 | `--text-body-lg`, `--weight-medium` | — |
| h2 «Exclusive Services» / «Get a Quote» | 24.5 | 22.5 | `--text-h4` (24/23) | — |
| Preguntas del FAQ | 24.8 | 20.5 | las del Accordion Item (18 → 24 desde `lg`) | mobile −2.5 (se mantiene el componente) |
| Cuerpo, checklist, píldoras, placeholders | 16 | 16 | `--text-body` | — |

Colores muestreados:
- Fondo de los campos, de las píldoras y del ítem abierto del FAQ (246,243,238) → `--color-background-subtle` (247,245,239).
- Píldora activa (52,76,78) → `--color-action-primary`. Cuadrado activo → `--color-action-secondary`; inactivo, blanco → `--color-surface-default`.
- Bordes de las cards del aside, de la caja del FAQ y filetes entre preguntas (207,208,203) → `--color-border-default`.
- Borde de los campos, de las píldoras y del ítem abierto (228,226,222) → `--color-border-subtle`.

Geometría:
- Artículo 870 + gap 30 + aside 420 (contenedor de 1320) → `minmax(0, 29fr) minmax(0, 14fr)`, gap `--spacing-7`.
- Cards del aside: padding de 40 arriba y 36 a los lados en desktop (→ `--spacing-8`) y 21 en mobile (→ `--spacing-5`). Radio ≈ 16 (`--radius-md`) y 31 px entre cards (`--spacing-7`).
- Píldoras de 58 px de alto con cuadrado de 44 y 7 de margen: `--spacing-8` + `--spacing-2` → 56 px; 16 px entre píldoras (`--spacing-4`).
- Campos de 56 px de alto (padding `--spacing-4` / `--spacing-5`) con 16 px entre cajas.
- Bloques del artículo separados entre 31 y 44 px → gap `--spacing-7`.
- Foto del apretón de manos 420×262; foto del video 870×400 (`aspect-ratio: 87 / 40`); radio ≈ 16 (`--radius-md`).
- Caja del FAQ: padding 25 (desktop) / 16 (mobile); el texto de los ítems a 26 / 21 del borde del ítem.
- Mobile: 48–54 px entre el FAQ, el Divider y la primera card del aside (gap `--spacing-9`).

## Cambios respecto de la spec (detectados al planificar)

1. **Input `--filled` y Field `--filled`** (ya sumados a la spec): los campos del diseño son cajas grises, no el filete de About. Filete inferior en `--color-border-strong` por contraste (decisión del usuario).
2. **El `<dialog data-video-modal>` no existe en ninguna página**: el play de la Home no hace nada. Se agrega al bloque `shared:footer` de `index.html` (Tarea 3) y llega a todas las páginas con `sync_shared.py`.
3. **Page Hero mobile:** el diseño de Service Details lo muestra de ≈ 320 px de alto, contra 420 en About. Se mantiene el componente (420) y se reporta como desvío, sin modificador nuevo.
4. **Copy:** a las descripciones del PNG que cortan en coma o sin punto («…for a specific purpose,» y «…documentation purposes») se les pone punto final. La respuesta 2 del FAQ usa las dos primeras oraciones del PNG; la tercera («We serve a wide range of industries…») habla de industrias, ya cubiertas en la respuesta 1. Los párrafos que el diseño corta («strengthening..», «automation tools,») van literales: son relleno de la plantilla.

## Mapa de archivos

| Archivo | Responsabilidad | Tareas |
|---|---|---|
| `docs/tools/atoms_css.py` / `atoms_kit.py` | `badge-check`, Check List, Input/Field `--filled`, Select | 1 |
| `docs/tools/molecules_css.py` / `molecules_kit.py` | Service Nav, Quote Form `--outline` | 2 |
| `dist/assets/js/main.js` | Mensaje de error del Select | 2 |
| `docs/tools/organisms_css.py` / `organisms_kit.py` | Accordion `--framed` | 3 |
| `dist/index.html` | `<dialog>` del Video Modal en `shared:footer`; enlace «Service Details» | 3, 4 |
| `dist/service-details.html` (nuevo) | La página | 4 |
| `dist/assets/css/main.css` | Bloques generados (por script) + Section `service-details` (a mano) | 1–4 |
| `dist/sitemap.xml` | Sumar la página | 4 |
| `docs/tools/sections_kit.py` | Ficha de la Section | 5 |
| `dist/kit/index.html`, `docs/kit/*.stories.md` | Regenerados | 1–3, 5 |
| `docs/plan-etapa-5.md`, `docs/traspaso-etapa-5.md`, `docs/plan.md` | Estado | 5 |

## Preparación (antes de la Tarea 1)

- [x] Levantar los servidores de QA (si no corren): `serve.py` del scratchpad, receta en la memoria `playwright-cli-qa-recipes`. Puerto 8765 sobre la raíz del proyecto y 8766 sobre `docs/design`, con `run_in_background` y `timeout` de 7 200 000 ms.
- [x] Verificar que los generadores están al día:

Run: `cd experiments/design-to-web && for s in atoms_css molecules_css organisms_css atoms_kit molecules_kit organisms_kit sections_kit; do python docs/tools/$s.py; done && python docs/tools/sync_shared.py --check && git diff --stat -- dist docs/kit`
Esperado: `sync_shared.py --check` sale con 0 y `git diff` no muestra cambios en `dist/` ni en `docs/kit/`.

---

### Tarea 1: Átomos — `badge-check`, Check List, Input/Field `--filled` y Select

**Modelo:** Sonnet, esfuerzo medio (avisar al usuario antes de cambiar con `/model`).

**Archivos:**
- Modificar: `docs/tools/atoms_css.py` (dict `ICONS`; bloques Input y Field; bloque nuevo Check List), `docs/tools/atoms_kit.py` (fichas Input y Field; fichas nuevas `check-list` y `select`)
- Regenerados: `dist/assets/css/main.css` (bloque `atoms:`), `dist/kit/index.html`, `docs/kit/{icons,input,field,check-list,select}.stories.md`

**Interfaces:**
- Produce (clases):
  - `.icon--badge-check`.
  - `ul.check-list[role=list] > li > span.icon.icon--circle-check[aria-hidden] + texto`.
  - `.input.input--filled`.
  - `.field.field--filled`.
  - `.field.field--select > label.field__label + select.input.field__control[required] > option[value=""][hidden][selected]` + opciones + `p.field__error`.
  - Las dos variantes de Field se combinan: `.field.field--filled.field--select`.

- [x] **Paso 1: ícono en `ICONS`** (después de `'circle-check-outline'`):

```python
    'badge-check': "<path d='M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z'/><path d='m9 12 2 2 4-4'/>",  # Service Details (Document Required)
```

- [x] **Paso 2: CSS de Input `--filled`.** En `atoms_css.py`, después de la regla `:where([data-surface='inverse'], [data-surface='brand']) .input { … }`:

```css
/* Input --filled — caja gris (Quote Form de Service Details). El borde del diseño (≈ 1.2:1) no alcanza el
   3:1 de los controles (WCAG 1.4.11): tres lados en --color-border-subtle, como el diseño, y el filete
   inferior en --input-border (border-strong), que conserva el hover y el color de error del Input. */
.input--filled {
  padding: var(--spacing-4) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-block-end-color: var(--input-border);
  border-radius: var(--radius-sm);
  background-color: var(--color-background-subtle);
}
```

- [x] **Paso 3: Field con variables de posición, `--filled` y `--select`.** Reemplazar el bloque Field completo (desde el comentario `/* Field — …` hasta `.field__error:empty { … }`) por:

```css
/* Field — campo con label flotante (Quote Form). En reposo el <label> ocupa el lugar del placeholder, como el
   diseño; con foco o con texto sube y se achica sobre el campo, así el nombre del campo nunca desaparece
   (accessibility.md: label asociado, no solo placeholder). El campo lleva placeholder=" " para que
   :placeholder-shown distinga vacío de lleno. Debajo, el mensaje de error: vacío (y sin caja) si no hay.
   --field-rise es el lugar que se reserva arriba para el label subido (22px de alto + el anillo de foco);
   --field-pad-block / --field-pad-inline, el padding del campo (dónde descansa el label). */
.field {
  --field-rise: var(--spacing-7);
  --field-pad-block: var(--spacing-3);
  --field-pad-inline: 0rem;
  position: relative;
  display: grid;
  gap: var(--spacing-1);
  padding-block-start: var(--field-rise);
}
.field__label {
  position: absolute;
  inset-block-start: calc(var(--field-rise) + var(--field-pad-block));
  inset-inline-start: var(--field-pad-inline);
  color: var(--color-text-secondary);
  line-height: var(--leading-normal);
  pointer-events: none;
  transform-origin: left top;
  transition: transform var(--ease-fast);
}
.field:focus-within .field__label,
.field:has(.field__control:not(:placeholder-shown)) .field__label {
  transform: translate(calc(-1 * var(--field-pad-inline)), calc(-1 * (var(--field-rise) + var(--field-pad-block)))) scale(0.875);
}
.field__control::placeholder {
  color: transparent;
}
.field__error {
  color: var(--color-feedback-error-text);
  font-size: var(--text-sm);
}
.field__error:empty {
  display: none;
}
/* --filled — con Input --filled: el label descansa dentro de la caja y, al subir, se alinea con su borde.
   Reserva menos arriba (24px) para que los campos queden cerca de los 72px del diseño. */
.field--filled {
  --field-rise: var(--spacing-6);
  --field-pad-block: var(--spacing-4);
  --field-pad-inline: var(--spacing-5);
}

/* Select — el mismo .input sobre <select>, sin la flecha nativa: el chevron es una máscara en ::after,
   en la misma celda que el campo. Label flotante sin JS: el select arranca en una opción vacía
   (value="", hidden, sin disabled) y, mientras esa opción está elegida y no hay foco, el label queda en
   reposo. Sin disabled no aparece el bug de Chromium que fuerza el color del placeholder: no hace falta
   !important. :placeholder-shown no aplica a <select>, por eso la regla propia. */
select.input {
  appearance: none;
  padding-inline-end: calc(var(--field-pad-inline, 0rem) + var(--spacing-7));
  cursor: pointer;
}
.field--select > .field__control {
  grid-area: 1 / 1;
}
.field--select::after {
  content: '';
  grid-area: 1 / 1;
  align-self: center;
  justify-self: end;
  inline-size: var(--spacing-5);
  block-size: var(--spacing-5);
  margin-inline-end: var(--field-pad-inline);
  background-color: var(--color-text-primary);
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 9 6 6 6-6'/%3E%3C/svg%3E") center / contain no-repeat;
  pointer-events: none;
}
.field--select:not(:focus-within):has(option[value='']:checked) .field__label {
  transform: none;
}
```

Nota para quien ejecute: el chevron repite el data URI de `icon--chevron-down` porque un pseudo-elemento no puede usar la clase `.icon`. Si `ICONS['chevron-down']` cambia, actualizar ambos (dejarlo dicho en `decisions` de la ficha Select).

- [x] **Paso 4: CSS de Check List.** Bloque nuevo, después del bloque Divider:

```css
/* Check List — lista con el check relleno (Service Details: «Mistakes to avoid…» y Key Features). El ícono
   va en el color del texto fuerte y el texto en secundario; se centra en la primera línea con 1lh, así
   los ítems de dos líneas (mobile) no lo desalinean. */
.check-list {
  display: grid;
  gap: var(--spacing-4);
  margin: 0;
  padding: 0;
  color: var(--color-text-secondary);
  list-style: none;
}
.check-list li {
  display: flex;
  align-items: flex-start;
  gap: var(--spacing-3);
}
.check-list .icon {
  margin-block-start: calc((1lh - 1em) / 2);
  color: var(--color-text-primary);
}
```

- [x] **Paso 5: fichas en `atoms_kit.py`.**

En la ficha `input`, sumar este bloque y la fila `('.input--filled', 'Caja gris con filete inferior fuerte (Quote Form de Service Details)')`:

```python
    dict(label='--filled (caja gris)', mods='narrow', html=d('''
      <label for="input-demo-filled" class="visually-hidden">Your name</label>
      <input class="input input--filled" type="text" id="input-demo-filled" name="name" placeholder="Name">''')),
```

Y reemplazar su decisión «Solo existe el estilo de filete…» por: `'Dos estilos: filete (newsletter y Quote Form de About Us) y --filled (Quote Form de Service Details).'`.

En la ficha `field`:
- Sumar el bloque:

```python
    dict(label='--filled y --select: vacío, con valor y con error', mods='narrow stack', html=d('''
      <div class="field field--filled">
        <label class="field__label" for="field-demo-filled-name">Name<span aria-hidden="true">*</span></label>
        <input class="input input--filled field__control" type="text" id="field-demo-filled-name" name="name" placeholder=" " autocomplete="name" required aria-describedby="field-demo-filled-name-error">
        <p class="field__error" id="field-demo-filled-name-error"></p>
      </div>
      <div class="field field--filled field--select">
        <label class="field__label" for="field-demo-filled-service">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="field-demo-filled-service" name="service" required aria-describedby="field-demo-filled-service-error">
          <option value="" hidden selected></option>
          <option>Strategic Planning</option>
          <option>Business Optimization</option>
          <option>IT Consulting</option>
          <option>Change Management</option>
          <option>Leadership</option>
        </select>
        <p class="field__error" id="field-demo-filled-service-error"></p>
      </div>
      <div class="field field--filled field--select">
        <label class="field__label" for="field-demo-filled-service-2">Service<span aria-hidden="true">*</span></label>
        <select class="input input--filled field__control" id="field-demo-filled-service-2" name="service" required aria-invalid="true" aria-describedby="field-demo-filled-service-2-error">
          <option value="" hidden selected></option>
          <option>Strategic Planning</option>
          <option>Business Optimization</option>
        </select>
        <p class="field__error" id="field-demo-filled-service-2-error">Choose an option.</p>
      </div>''')),
```

- Sumar las filas:
  - `('.field--filled', 'Con Input --filled: el label descansa dentro de la caja y sube alineado con su borde')`
  - `('.field--select + option[value=""][hidden][selected]', 'Select con chevron; la opción vacía deja el label en reposo')`
- Cambiar la decisión «Solo sobre fondo claro…» por: `'Solo sobre fondo claro: son los casos del diseño (Quote Form de About Us y de Service Details).'`.
- Sumar a `tokens`: `'--spacing-4 / -6 (--filled)'`.

Ficha nueva `select`, insertada después de `field` (mismo truco de `_i` / `A.insert` que usa `field`):

```python
A.append(dict(id='select', title='Select',
  desc='El <a href="#input">Input</a> sobre un <code>&lt;select&gt;</code> nativo, sin la flecha del sistema: el chevron lo dibuja <a href="#field">Field</a> <code>--select</code>. Va siempre dentro de un Field, que le da el label flotante y el mensaje de error.',
  desc_md='`.input` sobre `<select>` nativo sin flecha del sistema; el chevron y el label flotante los pone Field `--select`.',
  blocks=[
    dict(label='Vacío y con una opción elegida (--filled)', mods='narrow stack', html=d('''
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
      </div>''')),
  ],
  rows=[('select.input', 'Sin apariencia nativa; deja lugar al chevron a la derecha'),
        ('option[value=""][hidden][selected]', 'Opción vacía inicial: deja el label en reposo y hace fallar required hasta elegir'),
        ('.field--select', 'Dibuja el chevron y maneja el label (ver Field)'),
        ('required', 'Obligatorio: main.js muestra «Choose an option.» si queda vacío')],
  tokens=['Input (átomo)', 'Field (átomo)', '--color-text-primary (chevron)', '--spacing-5 / -7'],
  a11y='Es un <code>&lt;select&gt;</code> nativo: teclado, lectores y el selector del sistema (móvil) funcionan sin JS. El nombre lo da el <code>&lt;label&gt;</code> del Field; el chevron es decorativo (pseudo-elemento sin texto). La opción vacía está oculta en la lista (<code>hidden</code>), así nadie la vuelve a elegir por error.',
  a11y_md='`<select>` nativo (teclado, lector, selector del sistema); nombre del `<label>`; chevron decorativo; opción vacía `hidden`.',
  decisions=['Nativo antes que un select a medida: el diseño no pide nada que el nativo no haga, y uno a medida necesita JS y ARIA de listbox.',
             'La opción vacía no lleva `disabled`: con `disabled`, Chromium/Windows fuerza el color del texto y obligaría a usar `!important` (excepción de CLAUDE.md §11, que acá no hace falta).',
             'El chevron repite el data URI de `icon--chevron-down` (un pseudo-elemento no puede usar `.icon`): si cambia uno, cambiar el otro.',
             'Safari no oculta opciones con `hidden`: ahí la lista muestra una fila vacía al principio. Elegirla deja el campo vacío y la validación lo marca.']))
_i = [a['id'] for a in A].index('field')
A.insert(_i + 1, A.pop())
```

Ficha nueva `check-list`, insertada después de `divider`:

```python
A.append(dict(id='check-list', title='Check List',
  desc='Lista con el check relleno (<code>icon--circle-check</code>): el ícono en el color del texto fuerte y el texto en secundario. La usan «Mistakes to avoid…» y Key Features en Service Details.',
  desc_md='Lista con `icon--circle-check` relleno: ícono en texto fuerte, texto en secundario (Service Details).',
  blocks=[
    dict(label='Cuatro ítems', mods='medium', html=d('''
      <ul class="check-list" role="list">
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Market research and competitive analysis</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Operational efficiency and process optimization</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Risk assessment and decision-making support</li>
        <li><span class="icon icon--circle-check" aria-hidden="true"></span>Strategic business planning and roadmap</li>
      </ul>''')),
  ],
  rows=[('ul.check-list + role="list"', 'La lista; role="list" porque list-style: none la oculta como lista en Safari'),
        ('span.icon.icon--circle-check + aria-hidden="true"', 'Check decorativo, centrado en la primera línea')],
  tokens=['--color-text-primary (ícono)', '--color-text-secondary (texto)', '--spacing-3 / -4'],
  a11y='Es una lista real (<code>role="list"</code> la devuelve a VoiceOver, que la pierde con <code>list-style: none</code>). El check es <code>aria-hidden</code>: no aporta información que no esté en el texto.',
  a11y_md='Lista real con `role="list"` (VoiceOver); check `aria-hidden`.',
  decisions=['La lista de About Us (`about-intro__list`, check en contorno) queda como está: es otro ícono y vive en su Section.',
             'El ícono se centra en la primera línea con `1lh`: los ítems que en mobile ocupan dos líneas no lo desalinean.']))
_i = [a['id'] for a in A].index('divider')
A.insert(_i + 1, A.pop())
```

- [x] **Paso 6: regenerar y revisar el diff**

Run: `python docs/tools/atoms_css.py && python docs/tools/atoms_kit.py && git diff --stat -- dist docs/kit`
Esperado: cambian `main.css` (solo entre `atoms:start` y `atoms:end`), `kit/index.html`, `icons`, `input` y `field.stories.md`; aparecen `check-list` y `select.stories.md`.

- [x] **Paso 7: verificar en el navegador** (`playwright-cli -s=sd`, script en el scratchpad y `run-code --filename`). Sobre `http://127.0.0.1:8765/dist/kit/index.html?v=<Date.now()>`:
  - `#field`, bloque `--filled`: el label del campo vacío queda dentro de la caja (`label.top > input.top` y `label.left > input.left`). Con `focus()`, después de 400 ms, el label queda por encima del campo (`label.bottom <= input.top + 2`) y alineado con su borde (`|label.left - input.left| <= 1`).
  - Select vacío: label en reposo. Con `selectOption('Business Optimization')` y `blur()`, label arriba. El chevron (`getComputedStyle(field, '::after').maskImage`) no es `none`.
  - Alto de la caja `--filled`: 56–58 px.
  - Las regiones de Field sin `--filled` siguen igual que antes: label de «Your name» en `top` = input.top + 12 (`--spacing-3`).
  - `#check-list`: el centro vertical del ícono queda a ±1 px del centro de la primera línea.
  - axe sin violaciones dentro de `#icons`, `#input`, `#field`, `#select` y `#check-list`.
  - Captura de las tres fichas para mirar a ojo.

---

### Tarea 2: Moléculas — Service Nav y Quote Form `--outline` (con el campo Service)

**Modelo:** Sonnet, esfuerzo medio.

**Archivos:**
- Modificar: `docs/tools/molecules_css.py` (bloque nuevo Service Nav; `--outline` al final del bloque Quote Form), `docs/tools/molecules_kit.py` (helper `quote_form`, ficha `quote-form`, ficha nueva `service-nav`), `dist/assets/js/main.js` (mensaje del Select)
- Regenerados: `main.css` (bloque `molecules:`), `kit/index.html`, `docs/kit/{quote-form,service-nav}.stories.md`

**Interfaces:**
- Consume: `.input--filled`, `.field--filled`, `.field--select` (Tarea 1).
- Produce:
  - `nav.service-nav[aria-labelledby] > h2.service-nav__title + ul.service-nav__list[role=list] > li > a.service-nav__link[aria-current="page"?] > texto + span.service-nav__icon > span.icon.icon--arrow-right`.
  - `form.quote-form.quote-form--outline` con los Field `--filled`.
  - `FORM_MESSAGES.selectMissing = 'Choose an option.'`.

- [x] **Paso 1: CSS de Service Nav** (en `molecules_css.py`, antes del comentario `/* Quote Form — …`):

```css
/* Service Nav — «Exclusive Services» de Service Details: card con borde y la lista de servicios en píldoras
   grises con un cuadrado de flecha. La página actual va con aria-current="page": petróleo, texto blanco y el
   cuadrado ámbar. El diseño no muestra el hover: el cuadrado toma el ámbar del activo. */
.service-nav {
  display: grid;
  gap: var(--spacing-6);
  padding: var(--spacing-6) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-default);
  border-radius: var(--radius-md);
}
.service-nav__title {
  font-size: var(--text-h4);
  font-weight: var(--weight-semibold);
  line-height: var(--leading-snug);
}
.service-nav__list {
  display: grid;
  gap: var(--spacing-4);
  margin: 0;
  padding: 0;
  list-style: none;
}
.service-nav__link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--spacing-4);
  padding: var(--spacing-2) var(--spacing-2) var(--spacing-2) var(--spacing-5);
  border: var(--border-width-sm) solid var(--color-border-subtle);
  border-radius: var(--radius-sm);
  background-color: var(--color-background-subtle);
  color: var(--color-text-primary);
  font-weight: var(--weight-medium);
  text-decoration: none;
  transition: background-color var(--ease-fast), color var(--ease-fast);
}
.service-nav__icon {
  display: grid;
  place-items: center;
  flex: none;
  inline-size: var(--spacing-8);
  block-size: var(--spacing-8);
  border-radius: var(--radius-xs);
  background-color: var(--color-surface-default);
  color: var(--color-text-primary);
  font-size: var(--text-body-lg);
  transition: background-color var(--ease-fast), color var(--ease-fast);
}
.service-nav__link:hover {
  color: var(--color-text-primary);
}
.service-nav__link:hover .service-nav__icon,
.service-nav__link[aria-current='page'] .service-nav__icon {
  background-color: var(--color-action-secondary);
  color: var(--color-action-on-secondary);
}
.service-nav__link[aria-current='page'] {
  border-color: var(--color-action-primary);
  background-color: var(--color-action-primary);
  color: var(--color-action-on-primary);
}
@media (min-width: 48rem) {
  .service-nav {
    padding: var(--spacing-8);
  }
}
```

(La regla `.service-nav__link:hover { color }` evita que el hover global de enlaces pinte el texto; si foundations no cambia el color de los enlaces en hover, quitarla al verificar.)

- [x] **Paso 2: Quote Form `--outline`** (en `molecules_css.py`, después de la `@media (min-width: 48rem) { .quote-form { … } }`):

```css
/* --outline — card con borde, sin fondo ni sombra (aside de Service Details, «Get a Quote»), con el título
   a 24px y los campos --filled. Misma lógica y estados que el Quote Form base. */
.quote-form--outline {
  border: var(--border-width-sm) solid var(--color-border-default);
  border-radius: var(--radius-md);
  background-color: transparent;
  box-shadow: none;
}
.quote-form--outline .quote-form__title {
  font-size: var(--text-h4);
}
```

- [x] **Paso 3: mensaje del Select en `main.js`.** En `FORM_MESSAGES`, después de `valueMissing`, agregar:

```js
    selectMissing: 'Choose an option.',
```

En `fieldError`, reemplazar la primera línea por:

```js
    if (control.validity.valueMissing) { return control.tagName === 'SELECT' ? FORM_MESSAGES.selectMissing : FORM_MESSAGES.valueMissing; }
```

Y sumar el evento `change` (los `<select>` disparan `input` en los navegadores actuales; `change` cubre los demás). Reemplazar el `forEach` que escucha `input` por:

```js
      // El error se revisa mientras se corrige, no antes del primer envío
      controls.forEach(function (control) {
        ['input', 'change'].forEach(function (type) {
          control.addEventListener(type, function () {
            if (control.getAttribute('aria-invalid') === 'true') { validate(control); }
          });
        });
      });
```

- [x] **Paso 4: helper `quote_form` en `molecules_kit.py`.**
  - Sumar el parámetro `outline=False`: `def quote_form(fid, action, live=False, state='', outline=False):`.
  - Con `outline=True`:
    - el `<form>` lleva la clase `quote-form quote-form--outline`;
    - el título dice «Get a Quote»;
    - los Field llevan `field field--filled` y los controles `input input--filled field__control`;
    - los labels son «Name», «Email», «Phone» y «Message»;
    - entre el teléfono y el mensaje va el campo Service;
    - el botón dice «Submit Now».
  - Con `outline=False`, la salida no cambia: verificarlo con el diff del Paso 6.

Implementación concreta. Dentro de `field()`:

```python
        wrap = 'field field--filled' if outline else 'field'
        cls = 'input input--filled field__control' if outline else 'input field__control'
```

Usar `cls` en lugar de `'input field__control'` en los dos `control = …` y `wrap` en el `<div class="field">`. Después de `field()`, agregar:

```python
    def service():
        return '\n'.join(['  <div class="field field--filled field--select">',
                          '    <label class="field__label" for="%s-service">Service<span aria-hidden="true">*</span></label>' % fid,
                          '    <select class="input input--filled field__control" id="%s-service" name="service" required aria-describedby="%s-service-error">' % (fid, fid),
                          '      <option value="" hidden%s></option>' % ('' if filled else ' selected'),
                          '\n'.join('      <option%s>%s</option>' % (' selected' if filled and s == 'Business Optimization' else '', s) for s in SERVICES),
                          '    </select>',
                          '    <p class="field__error" id="%s-service-error">%s</p>' % (fid, 'Choose an option.' if err else ''),
                          '  </div>'])
```

con `SERVICES = ['Strategic Planning', 'Business Optimization', 'IT Consulting', 'Change Management', 'Leadership']` definido a nivel de módulo, arriba del helper. Ojo: `err` y `filled` se definen hoy después de `field()`; mover sus dos líneas (`err = …`, `filled = …`) antes de `def field`. En el `return`:
- Clase del form: `'quote-form quote-form--outline' if outline else 'quote-form'`.
- Título: `'Get a Quote' if outline else 'Get a free Quote'`.
- Labels:
  - `('Name' if outline else 'Your name')`
  - `('Email' if outline else 'Your email')`
  - `('Phone' if outline else 'Phone number')`
- Después de `field('phone', …)`, insertar `service()` solo si `outline`. Para eso, armar la lista de líneas y usar `+ ([service()] if outline else []) +`.
- Texto del botón cuando no envía: `'Submit Now' if outline else 'Get Started'`.
- `aria-label` de los demos de estado: `'Get a Quote' if outline else 'Get a free Quote'`.

- [x] **Paso 5: fichas.** En la ficha `quote-form`:
  - Sumar al final de `blocks`:

```python
    dict(label='--outline con campos --filled y Select (Service Details)', mods='narrow', html=quote_form('quote-outline', '#', state='error', outline=True)),
```

  - Filas nuevas:
    - `('.quote-form--outline', 'Card con borde, sin fondo ni sombra; título de 24px (aside de Service Details)')`
    - `('.field--filled / .field--select', 'Campos en caja gris y el Select «Service» (ver Field y Select)')`
  - Decisión nueva: `'--outline usa campos --filled: el diseño de Service Details los muestra en caja gris, con el filete inferior fuerte por contraste (decisión del usuario).'`.

Ficha nueva `service-nav`, después de `quote-form`:

```python
M.append(dict(id='service-nav', title='Service Nav',
  desc='«Exclusive Services» de Service Details: card con borde, título y la lista de servicios en píldoras con un cuadrado de flecha. La página actual va marcada con <code>aria-current="page"</code> (petróleo con el cuadrado ámbar).',
  desc_md='Card con la lista de servicios en píldoras; la actual con `aria-current="page"` (petróleo, cuadrado ámbar).',
  blocks=[
    dict(label='Con el servicio actual marcado', mods='narrow', html=d('''
      <nav class="service-nav" aria-labelledby="service-nav-demo-title">
        <h3 class="service-nav__title" id="service-nav-demo-title">Exclusive Services</h3>
        <ul class="service-nav__list" role="list">
          <li><a class="service-nav__link" href="#">Strategic Planning<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#" aria-current="page">Business Optimization<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">IT Consulting<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Change Management<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
          <li><a class="service-nav__link" href="#">Leadership<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
        </ul>
      </nav>''')),
  ],
  rows=[('nav.service-nav + aria-labelledby', 'Landmark de navegación nombrado por su título'),
        ('.service-nav__title', 'Título de 24px; h2 en la página (aside), h3 en el kit'),
        ('ul.service-nav__list + role="list"', 'La lista de servicios'),
        ('a.service-nav__link', 'Píldora gris con el texto y el cuadrado de flecha'),
        ('aria-current="page"', 'Servicio de la página actual: petróleo y cuadrado ámbar'),
        ('.service-nav__icon', 'Cuadrado blanco con icon--arrow-right; ámbar en hover y en el actual')],
  tokens=['--color-border-default / -subtle', '--color-background-subtle', '--color-action-primary / -on-primary', '--color-action-secondary / -on-secondary', '--color-surface-default', '--radius-md / -sm / -xs', '--text-h4', '--weight-medium / -semibold', '--spacing-2 / -4 / -5 / -6 / -8', '--ease-fast'],
  a11y='Es un <code>&lt;nav&gt;</code> nombrado por su título, distinto del menú principal. El servicio actual se anuncia con <code>aria-current="page"</code>, no solo por color. Las flechas son decorativas. El texto blanco sobre petróleo pasa AA; el foco usa el anillo del theme por fuera de la píldora (visible también sobre la activa).',
  a11y_md='`<nav>` nombrado por su título; actual con `aria-current="page"`; flechas `aria-hidden`; foco del theme por fuera de la píldora.',
  decisions=['El diseño no muestra el hover: el cuadrado toma el ámbar del activo, sin cambiar el fondo de la píldora.',
             'En la página, los servicios que todavía no tienen página enlazan a `#`; Business Optimization enlaza a `service-details.html`.']))
```

- [x] **Paso 6: regenerar y revisar**

Run: `python docs/tools/molecules_css.py && python docs/tools/molecules_kit.py && git diff --stat -- dist docs/kit`
Esperado:
- cambian `main.css` (solo `molecules:`), `kit/index.html`, `quote-form.stories.md` y el nuevo `service-nav.stories.md`;
- en `git diff dist/kit/index.html`, los cinco demos existentes del Quote Form no cambian.

- [x] **Paso 7: verificar en el navegador** (kit):
  - `#service-nav`:
    - píldora de 56–58 px de alto y cuadrado de 40 px;
    - la activa tiene `background-color` = `--color-action-primary`;
    - hover sobre «IT Consulting» → el cuadrado pasa a ámbar;
    - foco visible con Tab sobre la activa;
    - axe sin violaciones.
  - `#quote-form`, demo `--outline`:
    - sin sombra y con borde;
    - el Select muestra «Choose an option.»;
    - los cinco demos anteriores se ven igual que antes (captura).
  - Demo en vivo (`quote-demo`): enviar vacío → los 4 errores de siempre, el foco en el primero (el demo en vivo no tiene Select).
  - Consola limpia.

---

### Tarea 3: Organismos — Accordion `--framed` y el `<dialog>` del Video Modal en todas las páginas

**Modelo:** Opus, esfuerzo alto.

**Archivos:**
- Modificar: `docs/tools/organisms_css.py` (después del bloque `--boxed`), `docs/tools/organisms_kit.py` (ficha `accordion`; decisión en `video-modal`), `dist/index.html` (`<dialog>` en `shared:footer`)
- Regenerados: `main.css` (bloque `organisms:`), `kit/index.html`, `docs/kit/{accordion,video-modal}.stories.md`, `dist/about-us.html` (por `sync_shared.py`)

**Interfaces:**
- Produce:
  - `.accordion.accordion--framed > details.accordion-item[name] > summary.accordion-item__summary > span.accordion-item__question + span.accordion-item__toggle[aria-hidden] > span.icon.icon--arrow-right`, sin `accordion-item__mark`.
  - `<dialog class="video-modal" id="video-dialog" data-video-modal …>` en todas las páginas.

- [x] **Paso 1: CSS `--framed`** (en `organisms_css.py`, después de `.accordion--boxed .accordion-item__mark { … }`):

```css
/* --framed — FAQ de Service Details: el grupo en una caja con borde; el ítem abierto en una caja gris; los
   cerrados separados por un filete que respeta el padding del ítem (lo lleva el <summary> del segundo de
   cada par de cerrados, así nunca hay filete junto a la caja abierta). Sin el «?»: la numeración va en el
   texto. El toggle es una sola flecha que gira de → a ↗ al abrir. */
.accordion--framed {
  padding: var(--spacing-4);
  border: var(--border-width-sm) solid var(--color-border-default);
  border-radius: var(--radius-sm);
}
.accordion--framed .accordion-item {
  padding-inline: var(--spacing-5);
  border: var(--border-width-sm) solid transparent;
  border-radius: var(--radius-sm);
  transition: background-color var(--ease-base), border-color var(--ease-base);
}
.accordion--framed .accordion-item[open] {
  border-color: var(--color-border-subtle);
  background-color: var(--color-background-subtle);
}
.accordion--framed .accordion-item:not([open]) + .accordion-item:not([open]) > .accordion-item__summary {
  border-block-start: var(--border-width-sm) solid var(--color-border-default);
}
.accordion--framed .accordion-item__panel {
  padding-inline-start: 0;
}
.accordion--framed .accordion-item__toggle .icon {
  transition: rotate var(--ease-base);
}
.accordion--framed .accordion-item[open] .accordion-item__toggle .icon {
  rotate: -45deg;
}
@media (min-width: 64rem) {
  .accordion--framed {
    padding: var(--spacing-6);
  }
  .accordion--framed .accordion-item {
    padding-inline: var(--spacing-6);
  }
}
```

Nota: el ítem base tiene `border-block-end` (filete del FAQ de la Home); `--framed` lo reemplaza con el `border` transparente de 1 px en los cuatro lados, así el ítem no cambia de tamaño al abrirse.

- [x] **Paso 2: ficha `accordion`.** Agregar un helper al lado de `accordion()`:

```python
FAQ_FRAMED = [
    (True, '1. What industries do you specialize in?', 'Our consulting expertise spans multiple industries including finance, technology, healthcare, retail, and professional services. We have successfully partnered with organizations of all sizes from startups.'),
    (False, '2. How long does a consulting project typically last?', 'Project duration varies depending on the scope and objectives. Some projects may take a few weeks, while others—such as long-term strategic transformation—can extend over several months.'),
    (False, '3. What does a business consultant do?', 'A business consultant reviews how your company works, finds what holds it back and builds a plan with you: strategy, process optimization, sales improvement and financial advisory.'),
    (False, '4. Will consulting disrupt my daily operations?', 'No. We plan each phase around your schedule and work alongside your team, so changes roll out step by step while the business keeps running.'),
]

def accordion_framed(name='faq-framed'):
    items = []
    for open_, q, a in FAQ_FRAMED:
        items.append('\n'.join([
            '<details class="accordion-item" name="%s"%s>' % (name, ' open' if open_ else ''),
            '  <summary class="accordion-item__summary">',
            '    <span class="accordion-item__question">%s</span>' % q,
            '    <span class="accordion-item__toggle" aria-hidden="true">%s</span>' % ic('arrow-right'),
            '  </summary>',
            '  <div class="accordion-item__panel">',
            '    <p>%s</p>' % a,
            '  </div>',
            '</details>']))
    return '<div class="accordion accordion--framed">\n%s\n</div>' % textwrap.indent('\n'.join(items), '  ')
```

En `blocks` de la ficha, sumar `dict(label='--framed (FAQ de Service Details)', mods='narrow-wide', html=accordion_framed())`. Sumar las filas:
- `('.accordion--framed', 'Caja con borde; el abierto en caja gris; filetes entre cerrados; flecha que gira → ↗ (Service Details)')`
- `('.accordion-item__toggle &gt; .icon--arrow-right', 'En --framed, una sola flecha en lugar del par +/−')`

Sumar la decisión: `'--framed: sin el «?» del Accordion Item (el diseño numera las preguntas en el texto); la flecha gira con --ease-base, así con «reducir movimiento» cambia sin animar.'`. En `tokens`, sumar `'--color-border-default / -subtle', '--color-background-subtle', '--radius-sm', '--spacing-4 / -5 / -6'`.

- [x] **Paso 3: `<dialog>` en `index.html`.** Dentro de `<!-- shared:footer -->`, inmediatamente antes de `<!-- /shared:footer -->` y después del último elemento del bloque (verificar dónde están el off-canvas y el Scroll Top para no partir otro elemento), agregar el mismo markup que el demo del kit (`video_modal()` de `organisms_kit.py`):

```html
  <dialog class="video-modal" id="video-dialog" data-video-modal data-surface="inverse" aria-labelledby="video-dialog-title">
    <div class="video-modal__head">
      <h2 class="video-modal__title" id="video-dialog-title">Video</h2>
      <button type="button" class="icon-btn icon-btn--glass icon-btn--sm" data-video-close aria-label="Close video"><span class="icon icon--x" aria-hidden="true"></span></button>
    </div>
    <div class="video-modal__frame"></div>
  </dialog>
```

En la ficha `video-modal`, sumar la decisión: `'En las páginas, el <dialog> vive en el bloque shared:footer de index.html: sync_shared.py lo copia a todas, y cualquier botón con data-video-id lo abre.'`

- [x] **Paso 4: regenerar y sincronizar**

Run: `python docs/tools/organisms_css.py && python docs/tools/organisms_kit.py && python docs/tools/sync_shared.py && python docs/tools/sync_shared.py --check && python docs/tools/test_sync_shared.py`
Esperado:
- `--check` sale con 0 y las pruebas pasan;
- `git diff --stat` muestra `main.css` (solo `organisms:`), el kit, los dos `.stories.md`, `index.html` y `about-us.html` (solo el `<dialog>`).

- [x] **Paso 5: verificar en el navegador**
  - Kit `#accordion`, demo `--framed`:
    - el abierto tiene fondo gris y flecha rotada −45° (`getComputedStyle(icon).rotate === '-45deg'`);
    - abrir el ítem 3 → se cierra el 1 (mismo `name`);
    - hay filete entre 2 y 4 (`borderTopWidth` del summary del ítem 4 = 1 px) y no entre 2 y 3, porque el 3 está abierto;
    - teclado (Tab + Enter);
    - con `emulateMedia({ reducedMotion: 'reduce' })`, la flecha no anima (`transitionDuration` 0 s);
    - axe sin violaciones;
    - los demos de la Home y `--boxed` no cambian (captura).
  - Home (`/dist/index.html`):
    - click en el play de Michael Brooks → el `<dialog>` está abierto, con el iframe de `youtube-nocookie.com` (interceptar la ruta con un predicado sobre `url.hostname` para no cargar YouTube);
    - Escape → cerrado y el foco vuelve al botón.

---

### Tarea 4: `service-details.html` — página, Section `service-details`, `<head>`, sitemap y menú

**Modelo:** Opus, esfuerzo alto.

**Archivos:**
- Crear: `dist/service-details.html`
- Modificar: `dist/assets/css/main.css` (bloque `sections:`, subsección «Sections de las páginas interiores», al final), `dist/index.html` (enlace del submenú Services y del off-canvas), `dist/sitemap.xml`
- Regenerados: `dist/about-us.html` (menú, por `sync_shared.py`)

**Interfaces:**
- Consume: todo lo anterior.
- Produce: `<!-- section:service-details -->` … `<!-- /section:service-details -->` en `service-details.html` (lo lee la Tarea 5).

- [x] **Paso 1: esqueleto y `<head>`.** Crear `dist/service-details.html` copiando de `about-us.html` el `<!doctype>`, el `<html lang="en">` y el `<head>` hasta `<!-- shared:assets -->` inclusive, con estos cambios:
  - `title`: `Business Optimization — Consulting Services | Esonix`.
  - `description` (meta, OG, Twitter): `Business optimization consulting from Esonix: market research, process optimization, risk assessment and strategic planning that drive measurable, sustainable growth.`
  - canonical y `og:url`: `https://esonix.example/service-details.html`.
  - Precarga del hero: `<link rel="preload" href="assets/img/h1-process-img-2.webp" as="image" fetchpriority="high">`.
  - JSON-LD:

```json
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebPage",
        "@id": "https://esonix.example/service-details.html#webpage",
        "url": "https://esonix.example/service-details.html",
        "name": "Business Optimization — Consulting Services | Esonix",
        "isPartOf": { "@id": "https://esonix.example/#website" },
        "about": { "@id": "https://esonix.example/service-details.html#service" },
        "breadcrumb": { "@id": "https://esonix.example/service-details.html#breadcrumb" }
      },
      {
        "@type": "Service",
        "@id": "https://esonix.example/service-details.html#service",
        "name": "Business Optimization",
        "serviceType": "Business Optimization",
        "description": "Business optimization consulting: market research, process optimization, risk assessment and strategic planning that drive measurable, sustainable growth.",
        "provider": { "@id": "https://esonix.example/#organization" },
        "url": "https://esonix.example/service-details.html"
      },
      {
        "@type": "BreadcrumbList",
        "@id": "https://esonix.example/service-details.html#breadcrumb",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://esonix.example/" },
          { "@type": "ListItem", "position": 2, "name": "Business Optimization", "item": "https://esonix.example/service-details.html" }
        ]
      }
    ]
  }
```

  Después, `<!-- /shared:assets -->`, `</head>`, `<body>`, `<!-- shared:header site-header--inner -->` + `<!-- /shared:header -->`, `<main id="main">` … `</main>`, `<!-- shared:footer -->` + `<!-- /shared:footer -->`, `</body></html>`. Los bloques `shared:` van vacíos: los llena `sync_shared.py`.

- [x] **Paso 2: Page Hero** (primer hijo de `<main>`, sin marcadores de Section: es la de About reutilizada):

```html
    <section class="page-hero" aria-labelledby="page-title" data-surface="inverse">
      <div class="page-hero__media">
        <img src="assets/img/h1-process-img-2.webp" alt="" width="1000" height="580" fetchpriority="high">
      </div>
      <div class="container page-hero__content">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <ol class="breadcrumb__list">
            <li><a href="./">Home</a></li>
            <li><span>Services</span></li>
            <li><span aria-current="page">Business Optimization</span></li>
          </ol>
        </nav>
        <h1 class="page-hero__title" id="page-title">Business Optimization</h1>
      </div>
    </section>
```

- [x] **Paso 3: Section `service-details`** (después del Page Hero):

```html
    <!-- section:service-details -->
    <section class="section service-details" aria-labelledby="service-details-title">
      <div class="container service-details__grid">
        <article class="service-details__article">
          <div class="service-details__intro">
            <h2 class="service-details__title" id="service-details-title">Explore our Service Lists</h2>
            <p>We provide comprehensive business consulting services designed to help organizations overcome challenges, unlock growth opportunities, and achieve long-term success. Our expert consultants analyze your current operations, identify gaps, and develop tailored strategies that align with your vision and market demands. From planning to execution, we ensure measurable results that drive sustainable growth. Our consulting services focus on improving operational efficiency, strengthening..</p>
          </div>

          <div class="service-details__media">
            <img class="service-details__photo" src="assets/img/h1-process-img-3.webp" alt="Consultants shaking hands with a client across a meeting table" width="1000" height="580" loading="lazy">
            <div class="service-details__block">
              <h3 class="service-details__subtitle service-details__subtitle--sm">Mistakes to avoid to the dummy</h3>
              <ul class="check-list" role="list">
                <li><span class="icon icon--circle-check" aria-hidden="true"></span>Market research and competitive analysis</li>
                <li><span class="icon icon--circle-check" aria-hidden="true"></span>Operational efficiency and process optimization</li>
                <li><span class="icon icon--circle-check" aria-hidden="true"></span>Risk assessment and decision-making support</li>
                <li><span class="icon icon--circle-check" aria-hidden="true"></span>Strategic business planning and roadmap</li>
              </ul>
            </div>
          </div>

          <div class="service-details__block">
            <h3 class="service-details__subtitle">Document Required</h3>
            <ul class="service-details__docs" role="list">
              <li class="service-details__doc">
                <span class="icon icon--badge-check" aria-hidden="true"></span>
                <h4 class="service-details__doc-title">Learner's License</h4>
                <p>It is a temporary driving permit issued to individuals who are learning to drive a motor vehicle.</p>
              </li>
              <li class="service-details__doc">
                <span class="icon icon--badge-check" aria-hidden="true"></span>
                <h4 class="service-details__doc-title">Application Form</h4>
                <p>An Application Form is an official document used to collect necessary information from an individual for a specific purpose.</p>
              </li>
              <li class="service-details__doc">
                <span class="icon icon--badge-check" aria-hidden="true"></span>
                <h4 class="service-details__doc-title">Proof of Address</h4>
                <p>Proof of Address is an official document used to verify an individual's current residential address.</p>
              </li>
              <li class="service-details__doc">
                <span class="icon icon--badge-check" aria-hidden="true"></span>
                <h4 class="service-details__doc-title">Passport Size Photo</h4>
                <p>A Passport Size Photo is a small, standardized photograph used for official identification &amp; documentation purposes.</p>
              </li>
            </ul>
          </div>

          <div class="service-details__block">
            <h3 class="service-details__subtitle">Key Features</h3>
            <ul class="check-list" role="list">
              <li><span class="icon icon--circle-check" aria-hidden="true"></span>Our business consulting services are built to help organizations adapt, grow</li>
              <li><span class="icon icon--circle-check" aria-hidden="true"></span>We combine strategic insight with deep industry expertise to deliver solutions</li>
              <li><span class="icon icon--circle-check" aria-hidden="true"></span>From identifying growth opportunities to optimizing operations and guiding execution</li>
              <li><span class="icon icon--circle-check" aria-hidden="true"></span>Our approach emphasizes clarity, collaboration, &amp; measurable impact—ensuring strategies</li>
            </ul>
          </div>

          <div class="service-details__video">
            <img src="assets/img/download.webp" alt="" width="735" height="720" loading="lazy">
            <button type="button" class="icon-btn icon-btn--glass icon-btn--lg service-details__play" aria-label="Play video: Business Optimization overview" aria-haspopup="dialog" data-video-id="RqueNBILfVU" data-video-title="Business Optimization overview"><span class="icon icon--play" aria-hidden="true"></span></button>
          </div>

          <p>Our financial and operational consulting services empower businesses to optimize resources, manage risks, and improve cash flow. We provide detailed market analysis, budgeting frameworks, and performance tracking systems that support informed decision-making &amp; long-term stability. We guide companies through digital transformation by integrating modern technologies, automation tools,</p>

          <div class="accordion accordion--framed">
            <!-- 4 <details name="service-faq">, mismo markup que accordion_framed() de organisms_kit.py
                 (FAQ_FRAMED, el primero con open), con name="service-faq" -->
          </div>
        </article>

        <hr class="divider service-details__divider">

        <aside class="service-details__aside" aria-label="Service sidebar">
          <nav class="service-nav" aria-labelledby="service-nav-title">
            <h2 class="service-nav__title" id="service-nav-title">Exclusive Services</h2>
            <ul class="service-nav__list" role="list">
              <li><a class="service-nav__link" href="#">Strategic Planning<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
              <li><a class="service-nav__link" href="service-details.html" aria-current="page">Business Optimization<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
              <li><a class="service-nav__link" href="#">IT Consulting<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
              <li><a class="service-nav__link" href="#">Change Management<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
              <li><a class="service-nav__link" href="#">Leadership<span class="service-nav__icon"><span class="icon icon--arrow-right" aria-hidden="true"></span></span></a></li>
            </ul>
          </nav>
          <!-- Quote Form --outline: el markup de quote_form('quote', 'https://formsubmit.co/studioneyra@gmail.com', live=True, outline=True)
               de molecules_kit.py, con estos cambios: id="quote-form", título <h2> (no h3) y _subject
               «New quote request (Business Optimization) from esonix.example» -->
        </aside>
      </div>
    </section>
    <!-- /section:service-details -->
```

  Escribir el acordeón y el formulario completos en el HTML final (los comentarios de arriba solo indican de dónde copiar; no quedan en la página). El acordeón es el de `FAQ_FRAMED` con `name="service-faq"`. El formulario es el de About (honeypot, `_subject`, `novalidate`, `data-quote-form`, las regiones de estado), con:
  - `class="quote-form quote-form--outline"`;
  - Fields `--filled`: Name, Email, Phone, el Select Service (los 5 servicios, opción vacía `hidden selected`) y Message;
  - el botón «Submit Now».

- [x] **Paso 4: CSS de la Section** (bloque `sections:`, al final de «Sections de las páginas interiores», antes de `/* sections:end */`):

```css
/* Service Details — plantilla de servicio. Artículo y aside medidos en el diseño (870 | 420 con 30px de
   separación = 29fr 14fr) desde lg; antes, apilados con un Divider entre los dos (solo mobile). Los
   bloques del artículo van a 32px (el diseño varía entre 31 y 44). */
.service-details__grid {
  display: grid;
  gap: var(--spacing-9);
}
.service-details__article,
.service-details__aside {
  display: grid;
  align-content: start;
  gap: var(--spacing-7);
  min-inline-size: 0;
}
.service-details__intro,
.service-details__block {
  display: grid;
  gap: var(--spacing-5);
}
.service-details__intro p,
.service-details__article > p {
  margin: 0;
  color: var(--color-text-secondary);
}
.service-details__title {
  font-size: var(--text-h2);
}
.service-details__subtitle {
  font-size: var(--text-h3);
}
.service-details__subtitle--sm {
  font-size: var(--text-h6);
}
/* Foto del apretón de manos (420×262) junto a «Mistakes…», mitad y mitad desde md */
.service-details__media {
  display: grid;
  gap: var(--spacing-5);
  align-items: center;
}
.service-details__photo,
.service-details__video img {
  inline-size: 100%;
  border-radius: var(--radius-md);
  object-fit: cover;
}
.service-details__photo {
  aspect-ratio: 420 / 262;
}
/* Document Required: ícono ámbar a la izquierda; título y descripción en la segunda columna */
.service-details__docs {
  display: grid;
  gap: var(--spacing-5) var(--spacing-7);
  margin: 0;
  padding: 0;
  list-style: none;
}
.service-details__doc {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  gap: var(--spacing-1) var(--spacing-5);
}
.service-details__doc .icon {
  grid-row: span 2;
  font-size: var(--spacing-6);
  color: var(--color-text-highlight);
}
.service-details__doc-title {
  font-size: var(--text-body-lg);
  font-weight: var(--weight-medium);
}
.service-details__doc p {
  margin: 0;
  color: var(--color-text-secondary);
}
/* Video: foto 870×400 con el play centrado (abre el Video Modal) */
.service-details__video {
  position: relative;
}
.service-details__video img {
  aspect-ratio: 87 / 40;
}
.service-details__play {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  translate: -50% -50%;
}
@media (min-width: 48rem) {
  .service-details__media,
  .service-details__docs {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    column-gap: var(--spacing-7);
  }
}
@media (min-width: 64rem) {
  .service-details__grid {
    grid-template-columns: minmax(0, 29fr) minmax(0, 14fr);
    gap: var(--spacing-7);
    align-items: start;
  }
  .service-details__divider {
    display: none;
  }
  .service-details__subtitle--sm {
    font-size: var(--text-h4);
  }
}
```

Comprobar al verificar:
- que `.section` da el padding vertical del diseño (≈ 120 px arriba en desktop);
- que el ícono ámbar (`--color-text-highlight`) es el que usa el resto del theme para acentos sobre claro. Si no pasa 3:1 como gráfico sobre crema, usar `--color-action-secondary` y reportar: los íconos decorativos con `aria-hidden` no están obligados, pero se registra.

- [x] **Paso 5: sincronizar, menú y sitemap.**
  - En `index.html`, cambiar `href="#"` por `href="service-details.html"` en los dos enlaces «Service Details»: el submenú del header (`site-nav__sublink`, línea ≈ 103) y el off-canvas (`offcanvas__sublink`, línea ≈ 984). Usar Edit: el archivo está en CRLF.
  - En `dist/sitemap.xml`, sumar:

```xml
  <url>
    <loc>https://esonix.example/service-details.html</loc>
    <lastmod>2026-10-02</lastmod>
  </url>
```

(usar la fecha del día de la ejecución)

Run: `python docs/tools/sync_shared.py && python docs/tools/sync_shared.py --check`
Esperado: `service-details.html` con el header `--inner`, el footer y el `<dialog>`, y `aria-current="page"` en «Service Details» del submenú y del off-canvas; `about-us.html` solo cambia en los dos enlaces.

- [x] **Paso 6: verificar la página** (servidor 8765, `/dist/service-details.html?v=<Date.now()>`):
  - Capturas a 1920 y 480 px por tramos, comparadas con los recortes del PNG:
    - posiciones de h2, h3, foto, aside y FAQ (±8 px salvo los desvíos declarados);
    - aside de 420 px a 1920 y gap de 30–32 px;
    - campos de ≈ 56 px;
    - píldoras de 56–58 px.
  - 1440, 1280, 1024, 768 y 390 px: sin desborde horizontal (`document.documentElement.scrollWidth === innerWidth`).
  - Teclado:
    - orden lógico: artículo → FAQ → nav → formulario;
    - foco visible en las píldoras (también en la activa), en el Select y en el play;
    - play → modal → Escape → foco de vuelta.
  - Formulario:
    - enviar vacío → 5 errores («Choose an option.» en el Select) y foco en Name;
    - completar todo con la ruta `url.hostname === 'formsubmit.co'` interceptada y respondiendo `{"success":"true"}` → estado enviado y formulario limpio (el Select vuelve a vacío y su label a reposo);
    - con la ruta respondiendo error → `role="alert"`;
    - nunca enviar de verdad.
  - axe a 1440 y 390 sin violaciones nuevas. Consola limpia. `prefers-reduced-motion`.
  - Home y About: el menú «Service Details» lleva a la página; sin cambios visuales (captura del FAQ de About y del Quote Form de About).

---

### Tarea 5: kit de Sections, documentación, auditoría y entrega

**Modelo:** Opus, esfuerzo alto.

**Archivos:**
- Modificar: `docs/tools/sections_kit.py` (dict `service-details`), `docs/plan-etapa-5.md` (estado y desvíos de Service Details), `docs/traspaso-etapa-5.md` (siguiente página), `docs/plan.md` (si lleva estado por página)
- Regenerados: `dist/kit/index.html`, `docs/kit/service-details.stories.md`

- [x] **Paso 1: ficha de la Section** (después del último `S.append` de About Us):

```python
S.append(dict(id='service-details', title='Service Details', page='service-details.html',
  desc='Plantilla de servicio: a la izquierda el artículo (intro, foto con <a href="#check-list">Check List</a>, Document Required, Key Features, video, párrafo y FAQ <code>accordion--framed</code>); a la derecha el aside con <a href="#service-nav">Service Nav</a> y el <a href="#quote-form">Quote Form</a> <code>--outline</code>. Desde lg, 29fr | 14fr (870 y 420 px a 1920); en mobile, apilado con un Divider entre artículo y aside.',
  desc_md='Plantilla de servicio: artículo (intro, foto + Check List, Document Required, Key Features, video, FAQ --framed) y aside (Service Nav + Quote Form --outline). 29fr | 14fr desde lg; mobile apilado con Divider.',
  mods='section',
  rows=[('.service-details__grid', 'Una columna en mobile; desde lg 29fr | 14fr con 32px de separación'),
        ('.service-details__article / __aside', 'Columnas con bloques a 32px'),
        ('.service-details__media', 'Foto (420×262) y «Mistakes…» mitad y mitad desde md'),
        ('.service-details__docs / __doc', 'Document Required: grilla 2×2 desde md, ícono badge-check ámbar'),
        ('.service-details__video + .service-details__play', 'Foto 87:40 con el play que abre el Video Modal'),
        ('.service-details__subtitle(--sm)', 'h3 de 28px; --sm de 18 a 24px («Mistakes…»)'),
        ('hr.service-details__divider', 'Separador entre artículo y aside, solo por debajo de lg'),
        ('aside[aria-label="Service sidebar"]', 'Service Nav y Quote Form --outline')],
  tokens=['--text-h2 / -h3 / -h4 / -h6 / -body-lg', '--color-text-secondary / -highlight', '--radius-md', '--spacing-1 / -5 / -7 / -9', 'Check List, Divider, Icon Button, Field, Select (átomos)', 'Service Nav, Quote Form (moléculas)', 'Accordion, Video Modal (organismos)'],
  a11y='Jerarquía h1 (Page Hero) → h2 del artículo → h3 por bloque → h4 por documento; el aside tiene sus propios h2 (navegación y formulario). El aside es un landmark nombrado y el Service Nav marca el servicio actual con <code>aria-current</code>. El play tiene nombre propio y <code>aria-haspopup="dialog"</code>. La foto del video es decorativa (el botón la nombra); la del apretón de manos lleva <code>alt</code>.',
  a11y_md='h1 → h2 → h3 → h4; aside nombrado con sus h2; Service Nav con `aria-current`; play con nombre y `aria-haspopup`; foto del video decorativa.',
  decisions=['Copy del diseño, literal (relleno de la plantilla incluido); se corrigió «residen- tial» y se cerraron con punto dos descripciones.',
             'Fotos sustitutas de la biblioteca (decisión del usuario): el diseño usa fotos que no están en `dist/assets/img`.',
             'h1 «Business Optimization» y breadcrumb Home › Services › Business Optimization (decisión del usuario); «Services» es texto hasta que exista su página, y el JSON-LD omite ese nivel.',
             'El h2 del artículo usa --text-h2 (36px) contra 32 del diseño: con --text-h3 quedaba igual que los h3 de 28.',
             'El aside no es sticky: el diseño no lo muestra y es más alto que el viewport.']))
```

Run: `python docs/tools/sections_kit.py && git diff --stat -- dist/kit docs/kit`
Esperado: ficha nueva en el kit y en `service-details.stories.md`; las demás fichas, sin cambios.

- [x] **Paso 2: verificar el kit:**
  - `#service-details`: la Section se ve completa, el formulario neutralizado (sin `data-quote-form`, `action="#"`) y los ids con sufijo `-section`;
  - IDs duplicados en todo el kit: ninguno;
  - axe del kit sin violaciones nuevas (falsos positivos conocidos: slides con opacidad 0 del fade).

- [x] **Paso 3: auditoría contra `docs/anti-patrones.md`.** Repasar uno por uno sobre lo construido:
  - tokens semánticos en todo el CSS nuevo (`grep -n "brand-\|neutral-"` en los bloques nuevos: sin resultados);
  - sin `!important` nuevo (`grep -c "!important" dist/assets/css/main.css` igual que antes);
  - sin px sueltos (solo `0rem` y los tokens);
  - contraste AA (texto secundario sobre `--color-background-subtle`, label en reposo dentro de la caja, texto blanco sobre `--color-action-primary`);
  - longitud de línea de los párrafos: la columna de 870 px da ~110 caracteres. Excepción declarada como en About, porque así lo muestra el diseño.

- [x] **Paso 4: documentación**
  - `docs/plan-etapa-5.md`: «Estado» de Service Details con lo construido, cambios respecto de la spec, desvíos medidos y lo verificado. Seguir el formato de About Us: estado, cambios, desvíos, verificado y pendientes.
  - `docs/traspaso-etapa-5.md`:
    - §1: Service Details ✅ y siguiente página (Contact, si no hay PNG de Services);
    - §4: sumar Check List, Select, Input/Field `--filled`, Service Nav, Quote Form `--outline`, Accordion `--framed` y el `<dialog>` compartido;
    - §8: el nivel «Services» del breadcrumb y del JSON-LD cuando exista la página.
  - `docs/plan.md`: estado de la Etapa 5 (si lleva una línea por página).

- [x] **Paso 5: checkpoint con el usuario.** Reporte con:
  - capturas a 1920 y 390;
  - desvíos (h2 +4 px, preguntas del FAQ mobile −2.5 px, hero mobile 420 contra 320, campos a ≈ 80 px entre sí contra 72, foto del hero blanda);
  - el bug del Video Modal corregido;
  - pendientes (nivel Services, fotos originales).

Esperar la aprobación.

- [x] **Paso 6: commit de la página** (tras la aprobación):

```bash
git add docs/tools/atoms_css.py docs/tools/atoms_kit.py docs/tools/molecules_css.py docs/tools/molecules_kit.py \
  docs/tools/organisms_css.py docs/tools/organisms_kit.py docs/tools/sections_kit.py \
  dist/assets/css/main.css dist/assets/js/main.js dist/index.html dist/about-us.html dist/service-details.html \
  dist/sitemap.xml dist/kit/index.html \
  docs/kit/icons.stories.md docs/kit/input.stories.md docs/kit/field.stories.md docs/kit/select.stories.md \
  docs/kit/check-list.stories.md docs/kit/quote-form.stories.md docs/kit/service-nav.stories.md \
  docs/kit/accordion.stories.md docs/kit/video-modal.stories.md docs/kit/service-details.stories.md \
  docs/plan-etapa-5.md docs/traspaso-etapa-5.md docs/plan.md
git commit -m "feat(design-to-web): página Service Details (etapa 5)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

(Las rutas son relativas a `experiments/design-to-web`. Antes de `git add`, revisar `git status` y quitar de la lista lo que no haya cambiado.)
