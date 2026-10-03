# Check List

**Nivel:** Átomo · 14  
**Dónde:** `dist/assets/css/main.css` (bloque `/* Check List */`) · showcase en `dist/kit/index.html#check-list`

## Descripción

Lista con `icon--circle-check` relleno: ícono en texto fuerte, texto en secundario (Service Details).

## Snippets

**Cuatro ítems**

```html
<ul class="check-list" role="list">
  <li><span class="icon icon--circle-check" aria-hidden="true"></span>Market research and competitive analysis</li>
  <li><span class="icon icon--circle-check" aria-hidden="true"></span>Operational efficiency and process optimization</li>
  <li><span class="icon icon--circle-check" aria-hidden="true"></span>Risk assessment and decision-making support</li>
  <li><span class="icon icon--circle-check" aria-hidden="true"></span>Strategic business planning and roadmap</li>
</ul>
```

## Clases y atributos

| Clase o atributo | Efecto |
|---|---|
| `ul.check-list + role="list"` | La lista; role="list" porque list-style: none la oculta como lista en Safari |
| `span.icon.icon--circle-check + aria-hidden="true"` | Check decorativo, centrado en la primera línea |

## Tokens que consume

- `--color-text-primary (ícono)`
- `--color-text-secondary (texto)`
- `--spacing-3 / -4`

## Accesibilidad

Lista real con `role="list"` (VoiceOver); check `aria-hidden`.

## Decisiones y excepciones

- La lista de About Us (`about-intro__list`, check en contorno) queda como está: es otro ícono y vive en su Section.
- El ícono se centra en la primera línea con `1lh`: los ítems que en mobile ocupan dos líneas no lo desalinean.
