# Directrices: construir sitios web con Claude Code a partir de diseños PNG/JPG

Objetivo: que Claude Code interprete el diseño compartido con la mayor fidelidad posible.

Principio base: Claude puede inventar detalles plausibles pero incorrectos cuando a la imagen le faltan pistas. Reduce la ambigüedad y dale cómo verificarse.

---

## A. Preparar las imágenes (equipo)

1. formato PNG para interfaces; JPG solo para fotografía. Máx. 5 MB por imagen.
2. Un frame por breakpoint (mínimo desktop y mobile), además exportar cada sección por separado (hero, servicios, footer) para no perder detalle en páginas largas.
3. Nombres descriptivos: `home-desktop-01-hero.png`, `home-mobile-01-hero.png`.
4. Incluir estados relevantes: hover, focus, menú abierto, errores.
5. Sin anotaciones sobre el diseño.
6. Exportar Assets aparte: logos e iconos en SVG, imágenes optimizadas.
7. Definir por escrito lo que la imagen no transmite (ver Parte B, sección "Tokens y reglas"). Claude estima los valores exactos a partir de la imagen; no los conoce.

---

## B. Reglas para Claude (pegar en CLAUDE.md)

### Referencias visuales
- Los diseños/imágenes están en `[ruta/a/las/referencias]`.
- Si falta un estado, texto o comportamiento, preguntar; no inventar.
- Los valores exactos (colores, tamaños, espaciados) salen de los tokens, no de estimar la imagen. Si hay contradicción, avisar.


### Tokens y reglas (completar)
- Colores: `[hex por rol: primario, secundario, fondo, texto, acentos]`
- Tipografía: `[familias, pesos, escala de tamaños, interlineado]` y dónde se cargan las fuentes
- Espaciado, radios y sombras: `[escala]`
- Breakpoints: `[valores]` y comportamiento responsive (qué colapsa, qué se oculta, cómo cambia la grilla)
- Interacciones y animaciones: `[descripción]`
- Componentes del design system que se deben reutilizar: `[lista o ruta]`
- Contenido real: `[ruta a textos y assets]`

### Flujo de trabajo
1. Explorar: Describir lo que se ve (estructura, jerarquía, grilla, componentes, tokens inferidos). No codificar en este paso.
2. Planificar: Proponer la estructura de componentes, reutilizando el design system. Esperar aprobación antes de implementar.
3. Implementar por secciones, no la página completa de una vez.

### Verificación
- Después de implementar, renderizar la página, capturar en cada breakpoint y compararla con la referencia correspondiente. Iterar hasta que coincida.
- Criterios de aceptación: alineaciones, espaciados, jerarquía tipográfica, colores, comportamiento responsive.
- Al terminar, reportar explícitamente lo que no se pudo igualar.

### Contexto
- Cargar solo las referencias de la sección en curso.
- Usar `/clear` entre tareas no relacionadas.

---

## Plantilla de prompt

```
Referencias: @home-desktop-01-hero.png y @home-mobile-01-hero.png
Tokens y reglas: ver CLAUDE.md
Paso 1: describe lo que ves (estructura, jerarquía, grilla, componentes). No escribas código.
Paso 2 (tras mi OK): propón el plan de componentes, reutilizando el design system.
Paso 3: implementa solo esta sección, responsive.
Verifica: renderiza, captura en desktop y mobile, compara con las referencias
y corrige diferencias hasta que coincidan. Reporta lo que no pudiste igualar.
```

---

## Notas
- La verificación visual requiere una herramienta de navegador o capturas ya configurada.
- Pega o arrastra las imágenes al prompt; si la ruta no funciona, pégalas.
- El reparto por pasos y el commit por iteración son criterios de trabajo sugeridos,