# Switch

**Nivel:** Átomo · 09  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Switch */`) · showcase en `dist/kit/index.html#switch`

## Descripción

Interruptor sobre `<input type="checkbox" role="switch">`. La posición de la perilla es el estado.

## Snippets

**Apagado, encendido y deshabilitado**

```html
<input class="switch" type="checkbox" role="switch" id="switch-demo-off">
<label for="switch-demo-off">Monthly billing</label>
<input class="switch" type="checkbox" role="switch" id="switch-demo-on" checked>
<label for="switch-demo-on">Annual billing</label>
<input class="switch" type="checkbox" role="switch" id="switch-demo-disabled" disabled>
<label for="switch-demo-disabled">Unavailable</label>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `.switch` | Pista petróleo de 80×40px con perilla blanca ovalada |
| `role="switch"` | Obligatorio: sin él un lector de pantalla lo anuncia como casilla |
| `checked / disabled` | Estados nativos; la perilla se desplaza con :checked |
| `<label for>` | Obligatorio: el nombre accesible no puede ser solo un placeholder |

## Tokens que consume

- `--color-action-primary(-hover/-disabled)`
- `--color-surface-default`
- `--spacing-1 / -7 / -8 / -11`
- `--radius-full`
- `--ease-fast / --ease-base`

## Accesibilidad

Control nativo (Tab/Espacio); el estado lo da la posición de la perilla; sin animación con reducir movimiento.

## Decisiones y excepciones

- El diseño solo muestra el estado apagado: el encendido se deriva (perilla a la derecha, misma pista) en vez de inventar un color nuevo.
