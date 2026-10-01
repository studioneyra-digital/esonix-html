# Anti-patrones de IA

Checklist para evitar que componentes, sections y templates se vean
"genéricos, hechos con IA". Se aplica **al tomar cada decisión** (paleta,
tipografía, layout, motion) y de nuevo como revisión ítem por ítem antes de
cerrar cada nivel (ver flujo de trabajo en `CLAUDE.md §11`).

Adaptado de un checklist interno de la agencia; acá recortado y reescrito
para apuntar a los docs propios de este repo.

- **Bloqueante:** se corrige sin excepción.
- **Advertencia:** admite excepción, pero se declara por escrito (en el
  `.stories.md` del componente o en `docs/personality.md`) — nunca se ignora
  en silencio.

## Ítems que aplican al kit (revisar en cada componente/section/template)

### A. Tells de IA (casi siempre bloqueantes)

1. **Gradiente morado→azul por defecto** — cualquier gradiente debe salir de
   la paleta de [design-tokens.md](design-tokens.md) /
   [personality.md](personality.md), nunca esa combinación genérica.
2. **Fuente por defecto sin justificar** (Inter, Arial, system-ui, Roboto/Open
   Sans/Montserrat) — la tipografía del theme ya está resuelta en
   [personality.md](personality.md#tipografía); cualquier fuente nueva
   necesita la misma justificación que ahí.
3. **Icono en tile redondeado repetido por heading/feature como único
   diferenciador de la sección.** Un *token* de ícono consistente en el
   design system sí es válido (ver [atomic-design.md](atomic-design.md)); el
   problema es apoyarse solo en eso en vez de variar layout/densidad entre
   secciones.
4. **Cards anidadas** (tarjeta dentro de tarjeta).
5. **"3 features con ícono + título + párrafo" como única estructura** de
   toda una page/template, sin variación de layout entre secciones.
6. **Copy de relleno genérico** en placeholders/labels de showcase
   ("empoderamos tu negocio con soluciones innovadoras") — contradice
   directamente `CLAUDE.md §3` ("Copy de ejemplo... específico y sin
   relleno").
7. **Emoji como ícono funcional** en vez de iconografía real.

### B. Color

8. **Negro/gris puro sin matizar** (`#000`, `#fff`, `#888` sin hue) — las
   escalas de [personality.md](personality.md#color) ya están matizadas por
   diseño; no introducir un neutro nuevo sin hue.
9. **Texto gris sobre fondo de color** con contraste bajo AA — ver
   [accessibility.md](accessibility.md).
10. **Paleta "arcoíris" sin jerarquía** — este theme ya define una jerarquía
    de dos acentos (`--color-brand-*` primario, `--color-brand-accent-*`
    puntual); no sumar un tercer acento sin la misma disciplina.

### C. Tipografía

11. **Jerarquía de encabezados saltada** (h1 → h3 sin h2, o cualquier salto).
12. **Más de 2 familias tipográficas activas** (+1 mono si aplica) sin
    justificación — el theme usa 2 con rol definido (Mona Sans para todo el
    sitio, JetBrains Mono acotado a `/kit`); no sumar una tercera.
13. **Longitud de línea fuera de 45-75 caracteres** en párrafos de lectura.

### D. Layout

14. **Simetría/centrado como default en cada sección**, sin variación entre
    bloques.
15. **Espaciado que no sigue la escala de** [design-tokens.md](design-tokens.md).
16. **Touch targets pequeños** en mobile (mínimo 24×24px CSS, referencia
    práctica ~44px).

## Ítems que NO se auditan a nivel kit (aplican al sitio final de un cliente)

Estos ítems del checklist original están pensados para un sitio ya poblado
con contenido y marca real, no para el theme reusable en sí. Se retoman
cuando este theme se use para lanzar un sitio de cliente concreto, no antes:

- **Prueba del logo tapado** (¿la página podría ser de cualquier otro negocio
  del rubro?) — solo tiene sentido con marca y copy reales.
- **Foto de stock genérica/reconocible** y **overlay/duotono sin necesidad
  funcional** — el kit usa placeholders de Unsplash (`CLAUDE.md §3`) que se
  reemplazan por fotografía curada del cliente en el sitio final.

Accesibilidad y motion (contraste AA, `prefers-reduced-motion`, motion sin
propósito) **no se duplican acá** — ya están cubiertos como no negociables en
[accessibility.md](accessibility.md) e [interaction-motion.md](interaction-motion.md).

## Excepciones

Nunca se aplican "porque se ve bien" — se atan a una decisión de marca ya
tomada en `personality.md` (ej. un easing con rebote solo si la personalidad
fuera explícitamente lúdica, que no es el caso de este theme) y se declaran
por escrito, con la razón, en el `.stories.md` del componente o en
`personality.md`.
