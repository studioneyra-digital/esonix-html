# Atomic Design

| Nivel | Qué va aquí | Regla de oro |
|---|---|---|
| **Foundations** | Brand (logos o wordmark, variante claro y oscuro), Colors, Typography (Escala tipografica, pesos disponibles, interlineados), Spacing, Sombras, Radius & Sombras, Borders, Radius, Breakpoints| --- | 
| **Átomos** | Iconos (Lucide Icons — única librería de iconos permitida; excepción: logos de marca/redes sociales, que Lucide no incluye — ver `SocialIcon`), Socials Icons (svg personalizados), Botones (primario, secundario, ghost, icon button, tamaños), Link, Inputs de texto (text field, Select,textarea, search), Checkbox, Radio, Switch, Labels / Etiquetas, Badge, Avatar, Spinner, Divider, Tooltip base, Scroll Top, etc | No pueden depender de otro componente del kit. Tokens + HTML/CSS; `<script>` propio solo cuando el comportamiento es indispensable y no existe alternativa CSS-only (ej. Tooltip: toggle por click, cierre con click-outside/Escape) — la mayoría de los átomos no lo necesita. |
| **Moléculas** | Form field (label + input + mensaje de error/ayuda), Search bar (input + botón + icono), Cards (Services, Portfolio, Team, Post Card, etc), Breadcrumbs, Pagination, etc. | Componen 2-4 átomos. No conocen contexto de página (no hacen fetch, no asumen layout). |
| **Organismos** | Header / Navbar, Footer , Hero section, Sub-Hero, Formulario completo, Gallery, Carousel, Stepper, Marquee, etc. | Pueden orquestar estado y varias moléculas/átomos. Reciben datos editando directo el markup copiado (texto, atributos `data-*`), pero no hacen fetch propio salvo que sea explícitamente un organismo "conectado" documentado como tal. |
| **Sections** | Secciones o bloques de contenido de página completa: About Us, Value Proposition, Mission Statement, How it Works, Services, Proyectos/Portfolio, Case Studies, etc. | Reutilizables entre proyectos |

- Clasificar siempre un componente nuevo en este cuadro; si no encaja, dividirlo.

**Cada componente trae:**
- Alternativas y variantes respectiva sobre fondo oscuro.
- Spec strip (tabla de tokens usados)
- Un botón "Copy" que copia el snippet real al portapapeles.
- Si es necesario, cada **Sections** debe registrarse como componente con variantes de layout (ej. Hero-imagen-derecha, Hero-video-fondo, Hero-solo-texto) para que sea intercambiable entre proyectos sin rehacer código — catálogo de referencia orientado a marketing/contenido.


