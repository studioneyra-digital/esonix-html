# CLAUDE.md — New Web Project

## 1. Objetivo

Construir un sitio web impecable con páginas cuidadosamente diseñadas, interacciones fluidas y contenido fácil de editar directo en el HTML. Componentes y Plantillas listas para producción, tanto actuales como futuras. Animaciones, SEO optimizado, accesible (WCAG 2.1 AA mínimo), consistente (todo desde design tokens, sin magic numbers).

Sitio **HTML/CSS/JS estático, sin build ni gestor de paquetes** — mono-idioma por defecto.

## 2. Stack
leer `docs/stack.md`.

## 3. Referencias visuales
- Los diseños/imágenes están en `docs/design/`.
- Si falta un estado, texto o comportamiento, preguntar; no inventar.
- Los valores exactos (colores, tamaños, espaciados) salen de los tokens, no de estimar la imagen. Si hay contradicción, avisar.
- Biblioteca de imagenes a emplear en la paginas estan en `dist/assets/img`.

## 4. Design tokens

leer para `docs/design-tokens.md`.

## 5. Design System

leer `docs/design-system.md`.

## 6. Showcase (`/kit`) y formato de documentación
Cada componente, como sección anclada dentro de `dist/kit/index.html` (sidebar de navegación fija, mismo patrón que `ui-kit.html` en los otros temas HTML del workspace), muestra: variantes/estados renderizados, snippet HTML copiable (botón que copia al portapapeles), tabla de clases/atributos modificadores, notas de accesibilidad.

## 7. Accesibilidad y SEO (no negociable)

Leer `docs/accessibility.md` y `docs/seo.md` para directivas de SEO incluidas en cada página.

## 8. Estructura de carpetas

```
CLAUDE.md
docs/                          ← documentación del theme (este set de archivos)
└── kit/                       ← un `.stories.md` por componente (§7)
dist/                          ← sitio real, sin build — se sirve tal cual
├── index.html
├── [resto de páginas del sitio].html
├── kit/
│   └── index.html             ← showcase, secciones ancladas por nivel (§7, §11)
└── assets/
    ├── css/
    │   ├── tokens/             ← color.css, spacing.css, radius.css, shadow.css,
    │   │                          borders.css, transitions.css, typography.css,
    │   │                          z-index.css (ver docs/design-tokens.md)
    │   └── main.css            ← foundations, átomos, moléculas, organismos, sections
    ├── js/
    │   ├── main.js
    │   └── [librerías vendorizadas: jquery, gsap, ScrollTrigger, lenis, swiper-bundle, wow]
    └── img/                    
```

## 9. Flujo de trabajo (Claude Code)
1. Setup base
2. Construir base de `kit/index.html` (con navegación sidebar funcional)
3. Tokens (color, tipografía, espaciado, radios, sombras).
4. Construir Átomos, Moléculas, Organismos y Sections según se requiera.
9. Documentar y actualizar `dist/kit/index.html` tras construir un componente.
- Antes de construir un componente nuevo, revisar `dist/kit/index.html` (todas las secciones ancladas, por nivel) para confirmar que no exista ya uno equivalente — no duplicar funcionalidad.
- **Usar Skill frontend-design** para construir lo solicitado y construir por etapas o grupo de entregables para revisar y dar feedback.
- Antes de avanzar a la siguiente tarea, auditar lo construido contra `docs/anti-patrones.md`.

### Modelo y esfuerzo por etapa (recomendado)

| Etapa | Modelo | Esfuerzo | Motivo |
|---|---|---|---|
| 0 · Cimientos | Opus | alto | Define tokens y kit: todo lo demás depende de esto. |
| 1 · Átomos | Opus o Sonnet | medio | Piezas chicas acotadas por tokens. |
| 2 · Moléculas | Opus o Sonnet | medio | Combinan átomos ya existentes. |
| 3 · Organismos | Opus | alto | ScrollTrigger + Lenis, Swiper, off-canvas con `inert`, modal con foco: acá aparecen los bugs sutiles. |
| 4 · Sections + `index.html` | Opus | alto | Comparación visual contra los PNG en cada breakpoint e iteración. |

- Con Sonnet en etapas 1–2, auditar con más rigor contra `docs/anti-patrones.md` (tokens semánticos, sin `!important`, contraste AA).
- Cambiar de modelo con `/model` entre etapas, no a mitad de una.

## 10. Distribución (git subtree)
- Sin gestor de paquetes ni build: el theme se distribuye completo (HTML/CSS/JS) como repo propio, no como paquete npm.
- Para usarlo en un proyecto de cliente, importarlo con `git subtree` (conserva el historial); no copiar archivos sueltos.
- Los fixes genéricos (no específicos del cliente) se devuelven al repo del theme, no se quedan solo en el fork.

## 11. Qué NO hacer
- No instalar librerías de terceros (shadcn, Radix, MUI).
- No usar `!important`. Única excepción documentada: el `<select>` del componente Select (bloque `/* Select */` en `assets/css/main.css`), porque Chromium/Windows fuerza el color del placeholder cuando la opción seleccionada es `disabled` y ninguna otra técnica lo pisa. Ante un caso similar: probar alternativas primero y, si no hay ninguna, preguntar antes de usarlo; nunca en silencio.
- No crear variantes sin caso de uso citado.
- No usar tokens primitivos (`--color-brand-*`, `--color-neutral-*`) en componentes; pasar siempre por un token semántico (ver `docs/design-tokens.md`).
- No mezclar px con rem/em sin justificación.
- No subir de versión major sin documentar el breaking change en el changelog.