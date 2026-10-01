# Accesibilidad

Objetivo de conformidad: **WCAG 2.2 AA** (superset de 2.1, mismo esfuerzo).

- Navegable/operable por teclado, sin trampas de foco. Foco visible con contraste suficiente — nunca se remueve sin reemplazo (error de proceso más común al pulir estética).
- HTML semántico antes que ARIA. Componentes personalizados (Select, tabs, modales) exponen nombre, rol y valor vía ARIA.
- Contraste mínimo AA (4.5:1 texto normal, 3:1 texto grande/iconos). El color nunca es único portador de significado (acompañar con texto/ícono/patrón).
- Objetivos táctiles ≥24×24px CSS.
- `alt=""` en decorativas, `alt` descriptivo en informativas.
- Respetar `prefers-reduced-motion`.
- Inputs siempre con `<label>` asociado (no solo placeholder). Mensajes de error/confirmación/progreso anunciados vía `aria-live`/`role="status"` sin robar el foco.
- Jerarquía de encabezados sin saltos de nivel; navegación (header/footer) mantiene el mismo orden entre páginas.
- Flujos críticos (login, checkout) no dependen de pruebas cognitivas sin alternativa accesible, ni piden de nuevo un dato ya ingresado.

## Testeo
Ningún scanner automatizado cubre más del 30–40% de las violaciones — combinar siempre:
1. Automatizado (axe-core, Lighthouse) para lo obvio.
2. Manual solo-teclado en flujos críticos (Form, nav).
3. Al menos un pase con lector de pantalla real (NVDA+Firefox o VoiceOver) antes de dar un organismo/template por terminado.
4. Contraste verificado desde diseño, no después.

## Contenido rotable (carruseles, sliders)

El `alt` de un elemento que rota (imagen de fondo, slide) no se decide por defecto: si cada elemento porta un mensaje/CTA distinto es informativo (`alt` real); si el mensaje es único y el elemento solo rota el fondo, sigue siendo decorativo (`alt=""` o `aria-hidden`) aunque se mueva.
