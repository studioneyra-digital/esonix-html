# docs/tools — generadores del kit

Scripts de Python 3 (solo librería estándar) que generaron el CSS de los átomos y moléculas y las fichas de `dist/kit/index.html` y `docs/kit/*.stories.md` desde **una sola fuente de datos**, para que el kit y los `.stories.md` no se desfasen. No forman parte del sitio: `dist/` no los referencia y no hay build (`docs/stack.md`).

| Script | Escribe |
|---|---|
| `atoms_css.py` | Bloque `/* atoms:start … atoms:end */` de `main.css` (iconos Lucide como máscara, 13 átomos) |
| `molecules_css.py` | Bloque `/* molecules:start … molecules:end */` de `main.css` (12 moléculas) |
| `atoms_kit.py` | Nivel «Átomos» del kit (fichas + navegación) y `docs/kit/<átomo>.stories.md` |
| `molecules_kit.py` | Nivel «Moléculas» del kit y `docs/kit/<molécula>.stories.md` |
| `organisms_css.py` | Bloque `/* organisms:start … organisms:end */` de `main.css` |
| `organisms_kit.py` | Nivel «Organismos» del kit y `docs/kit/<organismo>.stories.md` |
| `sections_kit.py` | Nivel «Sections» del kit y `docs/kit/<sección>.stories.md`, **extrayendo el markup de `dist/index.html`** |
| `sync_shared.py` | Las piezas comunes (hojas de estilo, header, footer + off-canvas + Scroll Top + scripts) de cada página de `dist/`, copiadas de `dist/index.html` |

## Uso

```
python docs/tools/atoms_css.py
python docs/tools/molecules_css.py
python docs/tools/atoms_kit.py
python docs/tools/molecules_kit.py
```

Desde cualquier carpeta (la raíz del proyecto sale de la ubicación del script). Son **idempotentes**: ejecutarlos sin cambios no modifica nada versionado. Revisar siempre `git diff` después.

## Antes de tocar nada

- **Los scripts son la fuente de los bloques que generan.** Cada ejecución reemplaza por completo lo que haya entre los marcadores `atoms:` / `molecules:` de `main.css`. Una edición a mano dentro de esos bloques se pierde en la siguiente ejecución: cambia el componente en el script, o descarta el script de ese nivel.
- **Todo lo que está fuera de los marcadores es manual:** foundations, reglas de `data-surface`, `main.js` y los tokens.
- **`kit.css`:** el bloque de estilos de demos (`atoms-kit:` / `molecules-kit:`) solo se agrega la primera vez. Si luego cambia, se edita a mano.
- **El kit y los `.stories.md` se sobrescriben** en cada ejecución. Las notas y excepciones deben vivir en el campo `decisions` / `a11y` del script, no en el archivo generado.
- Los scripts de `*_kit.py` reemplazan por expresión regular el `<section>` de su nivel hasta el siguiente nivel: no cambiar los `id` de `atoms`, `molecules`, `organisms` ni `sections` en el kit.

## Cómo agregar un componente

1. CSS: agregar el bloque comentado al string `CSS` de `*_css.py` (solo tokens semánticos; sin `!important` ni valores sueltos).
2. Ficha: agregar un `dict` a la lista `A` (átomos) o `M` (moléculas) con `id`, `title`, `desc`, `blocks` (demos con `label`, `html`, `mods`, `surface`), `rows` (clases y atributos), `tokens`, `a11y` y `decisions`. Los demos van en inglés (copy del diseño) y llevan `lang="en"` automáticamente.
3. Ejecutar los dos scripts del nivel y revisar `git diff`.

## Organismos

`organisms_*.py` siguen el mismo patrón, con dos diferencias:

- **El JS va en `main.js`, a mano** (un bloque comentado por organismo). Los scripts no lo tocan.
- **Bloques especiales en la lista `O`:** `snippet=False` arma un bloque de prueba sin código (p. ej. el botón que abre el off-canvas), y el mod `source` oculta un demo cuyo organismo vive fuera de flujo: el snippet se lee igual de ese demo y `main.js` mueve el organismo a `<body>`. La vista estática del off-canvas la clona el JS inline del kit (`data-kit-clone`), que no se regenera.

## Sections

- **La fuente es la página que declara cada sección (`page` en su `dict`, por defecto `index.html`), no el script.** Cada sección va entre `<!-- section:<id> -->` y `<!-- /section:<id> -->`; `sections_kit.py` la extrae, cambia las rutas a `../assets/`, agrega el sufijo `-section` a sus ids (para no chocar con los demos del kit) y arma la ficha. El script solo guarda los metadatos (descripción, clases, tokens, accesibilidad, decisiones) en la lista `S`.
- **El CSS se escribe a mano** en el bloque `/* sections:start … sections:end */` de `main.css`, que ningún script toca.
- Para agregar una sección: marcarla en `index.html`, sumar su `dict` a `S` y ejecutar `python docs/tools/sections_kit.py`.
- Una sección reutilizada en otra página con un modificador no lleva marcadores allí: la ficha existente documenta el modificador en sus filas.

## Piezas compartidas entre páginas

- `dist/index.html` es la fuente del header, el footer (con off-canvas, Scroll Top y scripts) y las hojas de estilo, entre `<!-- shared:x -->` y `<!-- /shared:x -->`. Cada página nueva trae los tres pares de marcadores (pueden ir vacíos).
- `python docs/tools/sync_shared.py` los copia a las demás páginas y marca con `aria-current="page"` el enlace del menú que apunta a cada una. `--check` solo verifica (sale con 1 si hay páginas desfasadas). Pruebas: `python docs/tools/test_sync_shared.py`.
- **Variantes por página:** el marcador de apertura puede llevar modificadores BEM, p. ej. `<!-- shared:header site-header--inner -->` (las páginas interiores). El script agrega cada modificador a la clase de su componente (`site-header`) dentro del bloque copiado; el marcador conserva el modificador y la fuente no lleva ninguno.
- Nunca editar esas piezas en otra página que no sea `index.html`: se pierden en la siguiente sincronización.
