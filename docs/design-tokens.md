# Contrato de tokens CSS

Estos son los ÚNICOS nombres de variables que los componentes del kit leen.
Usa exactamente estos nombres al escribir los archivos en
`assets/css/tokens/` (ver `docs/stack.md`); los componentes no reconocerán
variables con otros nombres.

## Arquitectura de tokens

Dos capas, no una escala plana:

- **Primitivos** — escalas crudas sin significado de uso: `--color-brand-primary-50…950`,
  `--color-brand-accent-50…950`, `--color-neutral-50…950` y los `-50/-100/-500` de feedback.
- **Semánticos** — todo lo demás: `--color-text-*`, `--color-background-*`,
  `--color-surface-*`, `--color-border-*`, `--color-action-*`, `--color-feedback-*`
  y `--color-overlay*`. Nombran un *uso*, no un valor.

Los componentes consumen **solo semánticos**. Un primitivo se referencia
únicamente al definir un semántico (ej. `--color-text-primary:
var(--color-neutral-900);`), nunca directo en un componente — así un
rebrand cambia el primitivo en un solo lugar sin tocar componentes.
 
```css
/* color.css */
:root {
/* Color / Brand */
--color-brand-primary-500: #fbcb79
--color-brand-secondary-500: #344c4e
--color-brand-primary-50 … --color-brand-primary-950       /* escala de marca (primario) */
--color-brand-secondary-50 … --color-brand-secondary-950  /* petróleo de Esonix: anclas 500 (#344c4e) y 900 (#1f2a2b, fondo de bloques oscuros) */
--color-brand-accent-50 … --color-brand-accent-950  /* en Esonix apunta a brand-secondary: no hay tercer color de marca */

/* Neutral (grises) */
--color-neutral-50 … --color-neutral-950    /* base para texto, bordes, fondos. Esonix: 50 = #fefbf5 (crema), 950 = #122325 (tinta) */

/* Feedback / Estado semántico */
--color-success-500 (+ -50/-100 para fondos suaves)
--color-warning-500 (+ -50/-100 para fondos suaves)
--color-error-500 (+ -50/-100 para fondos suaves)
--color-info-500 (+ -50/-100 para fondos suaves)

/* Color / Estado semántico */
--color-feedback-success-bg
--color-feedback-success-text
--color-feedback-success-border
--color-feedback-warning-bg
--color-feedback-warning-text
--color-feedback-warning-border
--color-feedback-error-bg
--color-feedback-error-text
--color-feedback-error-border
--color-feedback-info-bg
--color-feedback-info-text
--color-feedback-info-border

/* Texto */
--color-text-primary
--color-text-secondary
--color-text-tertiary
--color-text-disabled
--color-text-inverse /* texto sobre fondo oscuro/brand */
--color-text-inverse-secondary  /* texto secundario sobre fondo oscuro (rgba blanco 78%): ≈9.4:1 sobre background-inverse, ≈4.8:1 sobre el panel claro de una card brand */
--color-text-link
--color-text-highlight /* propio de Esonix: amarillo como texto, solo sobre fondos oscuros */

/* Color Fondo */
--color-background-default /* fondo general de la página */
--color-background-subtle 
--color-background-muted 
--color-background-inverse /* secciones oscuras si hay modo claro base */

/* Color / Surface */
--color-surface-default  /* cards, paneles */
--color-surface-raised
--color-surface-overlay

/* Bordes */
--color-border-default
--color-border-subtle
--color-border-strong
--color-border-focus        /* outline de focus-visible */
--color-border-focus-inverse /* foco dentro de [data-surface="inverse"] (en Esonix, brand-primary-500: 9.77:1) */
--color-border-error

/* Interactivo (estados) */
--color-action-primary
--color-action-primary-hover
--color-action-primary-active
--color-action-primary-disabled
--color-action-secondary
--color-action-secondary-hover
--color-action-on-primary
--color-action-on-secondary /* propio de Esonix: texto oscuro sobre el amarillo de action-secondary */

/* Overlay */
--color-overlay             /* fondo semitransparente para modales/drawers */
--color-overlay-light       /* overlay claro (rgba blanco 0.08-0.12) sobre --color-background-inverse: cards/dividers en secciones oscuras, ver docs/personality.md */
}
 
/* spacing.css */
:root {
  --spacing-1: 0.25rem;   /* 4px */
  --spacing-2: 0.5rem;    /* 8px */
  --spacing-3: 0.75rem;   /* 12px */
  --spacing-4: 1rem;      /* 16px */
  --spacing-5: 1.25rem;   /* 20px */
  --spacing-6: 1.5rem;    /* 24px */
  --spacing-7: 2rem;      /* 32px */
  --spacing-8: 2.5rem;    /* 40px */
  --spacing-9: 3rem;      /* 48px */
  --spacing-10: 4rem;     /* 64px */
  --spacing-11: 5rem;     /* 80px */
  --spacing-12: 6rem;     /* 96px */
  --spacing-13: 8rem;     /* 128px */
}

/* radius.css */
:root {
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 16px;
  --radius-lg: 24px;
  --radius-xl: 40px;
  --radius-full: 100px;
}

/* shadow.css */
:root {
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.06);
  --shadow-md: 0 8px 32px rgba(0, 0, 0, 0.10);
  --shadow-lg: 0 24px 64px rgba(0, 0, 0, 0.14);

  /* Sombra del propio color del elemento (docs/personality.md), derivada con
     color-mix() de --color-brand-primary-500 / --color-brand-accent-500, no negra genérica. */
  --shadow-glow-brand: 0 6px 20px color-mix(in srgb, var(--color-brand-primary-500) 35%, transparent);
  --shadow-glow-accent: 0 6px 20px color-mix(in srgb, var(--color-brand-accent-500) 35%, transparent);

  /* Desenfoque del fondo detrás de un panel (off-canvas): el diseño desenfoca la página sin oscurecerla.
     Solo en capas sin descendientes position: fixed (backdrop-filter los recortaría). */
  --blur-backdrop: 6px;

  /* Desenfoque de texto en segundo plano (palabras inactivas del Word List): se lee la forma de la
     palabra pero no compite con la activa, que queda nítida. */
  --blur-text: 4px;

  /* Desenfoque de una foto de fondo (bloque Finance): se reconoce la escena pero no compite con el
     texto. Va en filter sobre la capa de la imagen, nunca en backdrop-filter. */
  --blur-photo: 12px;
}

/* borders.css */
:root {
  --border-width-sm: 1px;
  --border-width-md: 2px;
}

/* transitions.css */
:root {
  --ease-fast: 150ms ease;
  --ease-base: 250ms ease;
  --ease-slow: 420ms cubic-bezier(0.16, 1, 0.3, 1);
  --duration-spin: 900ms; /* solo duración, para animaciones infinitas/lineales (spinners) */
}

/* z-index.css — 5 niveles nombrados por función, no una escala numérica
   libre. Cada uno ya tiene un dueño real, construido o documentado en
   atomic-design.md (Modal/Dialog, Alerts/Toast, Dropdown). */
:root {
  --z-dropdown: 20;  /* paneles flotantes anclados a un trigger: Tooltip, futuro Dropdown */
  --z-sticky: 30;    /* elementos fixed/sticky persistentes: Scroll Top */
  --z-overlay: 40;   /* backdrop de Modal/Dialog (organismo futuro) */
  --z-modal: 50;     /* el propio Modal/Dialog, encima de su overlay */
  --z-toast: 60;     /* Alerts/Toast (molécula futura) — siempre por encima de todo */
}

/* typography.css */
:root {
  --font-sans: 'Mona Sans', ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-display: 'Mona Sans', var(--font-sans);
  --font-mono: 'JetBrains Mono', ui-monospace, 'SFMono-Regular', Menlo, Consolas, monospace;

  /* clamp() con base en rem en el valor preferido (no solo vw): así el
     tamaño sigue respondiendo al zoom/tamaño de fuente del usuario
     (WCAG 1.4.4) — ver docs/personality.md §Tipografía. Curva calculada
     entre los breakpoints sm (480px) y xl (1280px) de esta misma tabla,
     preservando los mismos mín/máx que antes. */
  --text-hero: clamp(2.5rem, 0.25rem + 8.6vw, 10.75rem); /* 40px → 172px, propio de Esonix: hero y marquee del footer (curva hasta 1920px) */
  --text-display: clamp(4rem, 3.4rem + 2vw, 5rem);       /* 64px → 80px */
  --text-giant: clamp(2.75rem, 2rem + 2.5vw, 4rem);       /* 44px → 64px */
  --text-h1: clamp(2.25rem, 1.8rem + 1.5vw, 3rem);        /* 36px → 48px */
  --text-h2: clamp(1.75rem, 1.45rem + 1vw, 2.25rem);      /* 28px → 36px */
  --text-h3: clamp(1.375rem, 1.15rem + 0.75vw, 1.75rem);  /* 22px → 28px */
  --text-h4: clamp(1.4375rem, 1.4rem + 0.125vw, 1.5rem);  /* 23px → 24px */
  --text-h5: 1.375rem;   /* 22px */
  --text-h6: 1.125rem;   /* 18px */
  --text-body-lg: 1.125rem; /* 18px */
  --text-body: 1rem;     /* 16px */
  --text-sm: 0.875rem;   /* 14px */
  --text-xs: 0.75rem;    /* 12px */

  --weight-light: 200;
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;

  /* Interlineado: 1.6 en cuerpo cumple WCAG 1.4.12 (al menos 1.5) */
  --leading-tight: 1.1; /* display, giant, h1 */
  --leading-snug: 1.25; /* h2–h6 */
  --leading-normal: 1.6; /* cuerpo */
  --leading-relaxed: 1.75; /* texto largo */

  /* Tracking: negativo solo en display/giant/h1; suelto solo en mayúsculas cortas (eyebrows, badges) */
  --tracking-tight: -0.03em;
  --tracking-normal: 0;
  --tracking-wide: 0.06em; /* personality.md fija 0.04–0.08em */
}
```

Breakpoints (referencia — no existen como custom property porque `@media` no puede leer `var()`; se escriben directo en el código, siempre estos valores):

| Nombre | Valor |
|---|---|
| `sm` | 30rem (480px) |
| `md` | 48rem (768px) |
| `lg` | 64rem (1024px) |
| `xl` | 80rem (1280px) |

**Regla del grid:** las columnas usan las clases del grid de Bootstrap con sus propios breakpoints (sm 576, md 768, lg 992, xl 1200, xxl 1400); todo `@media` propio usa los de esta tabla; no se mezclan ambos en un mismo componente. Solo `md` coincide.

**Excepción (Etapa 4):** las Sections arman sus columnas con CSS Grid y los breakpoints de esta tabla, no con las clases `col-*`: las proporciones del diseño (p. ej. 500 / 400 / 290 px en What We Do) no caen en 12 columnas con gutter, y el `lg` de Bootstrap (992px) no es el del theme (1024px). De Bootstrap se usan los contenedores: `.container` se amplía a 1320px de contenido desde su `xxl` y se suma `.container-wide` (1620px), ambos con gutter `--spacing-7` (bloque `sections:` de `main.css`). Única mezcla permitida de breakpoints: las reglas que **replican el ancho del `.container`** (que es de Bootstrap) usan los breakpoints de Bootstrap, porque siguen a ese componente y no deciden layout; hoy, `--why-container` de Why Choose Us (Grupo B), con el que el texto se alinea con el resto de las secciones en todos los anchos.

## Reglas al personalizar

- No borres ninguna variable aunque no la uses todavía: los componentes
  del ui-kit asumen que todas existen.
- Puedes añadir variables nuevas propias del proyecto (ej.
  `--color-brand-2`), pero nunca renombres las de arriba.
- No hay modo oscuro de usuario (docs/personality.md lo descartó). Un bloque oscuro fijo se
  declara con `data-surface="inverse"` (fondo `--color-background-inverse`) y una card destacada
  con `data-surface="brand"` (fondo `--color-action-primary`); ambos se definen en
  `assets/css/main.css` y reasignan el token de foco para todo su árbol.
