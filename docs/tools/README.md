# docs/tools — generadores del kit

Scripts de Python 3 (solo librería estándar) que generaron el CSS de los átomos y moléculas y las fichas de `dist/kit/index.html` y `docs/kit/*.stories.md` desde **una sola fuente de datos**, para que el kit y los `.stories.md` no se desfasen. No forman parte del sitio: `dist/` no los referencia y no hay build (`docs/stack.md`).

| Script | Escribe |
|---|---|
| `atoms_css.py` | Bloque `/* atoms:start … atoms:end */` de `main.css` (iconos Lucide como máscara, 13 átomos) |
| `molecules_css.py` | Bloque `/* molecules:start … molecules:end */` de `main.css` (12 moléculas) |
| `atoms_kit.py` | Nivel «Átomos» del kit (fichas + navegación) y `docs/kit/<átomo>.stories.md` |
| `molecules_kit.py` | Nivel «Moléculas» del kit y `docs/kit/<molécula>.stories.md` |

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

## Para los organismos y las sections

No existen `organisms_*.py` ni `sections_*.py`. Si se quieren generar igual, copiar `molecules_css.py` y `molecules_kit.py`, cambiar los marcadores (`organisms:`), el `id` de la sección y el rótulo «Molécula» por «Organismo». Los organismos llevan JS: ese código va en `main.js`, a mano.
