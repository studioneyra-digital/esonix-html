# Plan.md

Paso 2 — Plan por etapas
Cada etapa se entrega para tu revisión y se audita contra anti-patrones.md antes de pasar a la siguiente.

## Etapa 0 — Cimientos
- color.css reescrito para Esonix:
    - brand-primary amarillo (ancla #fbcb79).
    - brand-secondary petróleo (ancla #344c4e). Hoy figura como "reservada"; la emito porque ya tiene un uso real y actualizo design-tokens.md.
    - Neutrales cálidos con 50 = #fefbf5.
- Mapeo semántico:
    - background-default = crema.
b   - ackground-inverse ≈ #1f2a2b.
    - action-primary = petróleo (botón oscuro).
    - action-secondary = amarillo, solo como relleno con texto oscuro, nunca como texto sobre crema.
Cada par de color verificado a AA.
typography.css con Mona Sans autoalojada, y un token nuevo --text-hero para "FutureGrowth" y el marquee del footer (~170px en 1920, que baja a ~40px en mobile).
main.css y main.js base, con Lenis + ScrollTrigger sincronizados.
kit/index.html con la sidebar funcional y la sección Foundations (colores, tipografía, espaciado, radios, sombras).

## Etapa 1 — Átomos
Componente	Variantes que pide el diseño
Button	pill + círculo con ↗: light (sobre oscuro), dark (sobre claro), block neutro y block acento (pricing)
Icon Button	círculo con borde: flechas de carrusel, "+" de team, play de video
Link con flecha	"Read More ↗", también en versión inversa amarilla ("Contact Us")
Eyebrow	▪ a la izquierda / ▪ centrado a ambos lados / inverso amarillo
Badge	translúcido (fechas del blog, roles del equipo)
Avatar / Avatar stack	con "+" amarillo
Progress bar	label + %
Switch	Monthly / Annually
Divider, Pagination dots, Social icon, Scroll Top	—

## Etapa 2 — Moléculas
Card Service: normal y destacada.
Card Feature numerada: normal y destacada con foto de fondo.
Card Pricing: normal y destacada.
Card Testimonial: texto y video.
Card Team: normal y elevada.
Card Post.
Card Project: // 01 + título, usada en el bloque Finance.
Card CTA con imagen: "Still have questions".
Card Hero: translúcida, estática.
Stat: número + label.
Ítem de acordeón.
Campo de newsletter.
Etapa 3 — Organismos
Header: con dropdowns de Home, Services, Pages y Blog. Pages lleva el contenido real del diseño; el resto, placeholder.
Menú off-canvas mobile: acordeones, Location, Contact y redes. Usa inert y cierra con Escape.
Carrusel (Swiper): una sola base reutilizada en Services (flechas) y Testimonials (dots).
Acordeón: con <button aria-expanded>.
Lista de palabras con scroll (GSAP ScrollTrigger): la palabra activa queda nítida y su card cambia. En mobile se reemplaza por "Works" + cards apiladas, sin efecto de scroll.
Marquee del footer.
Footer.
Modal de video: un <dialog> nativo que carga el iframe de youtube-nocookie recién al hacer click, para no cargar YouTube al abrir la página.
Etapa 4 — Sections + index.html
Las 11 secciones más Stats y Logos, ambas solo en mobile.
Un solo <h1> en la página: "Expert Guidance for FutureGrowth".
Los títulos de sección son <h2> con tamaño --text-h1 (~48px, lo que mide el diseño).
Precios anuales: se derivan del 30% (27.9 / 34.9 / 41.9), así que no son inventados.
El resto del copy faltante va como placeholder, incluidos el teléfono y el copyright.
Cambio de layout desktop → mobile en lg (1024px). El diseño no muestra los tamaños intermedios, así que tablet sale inferido de los dos extremos.
Sin animaciones de entrada (reveals), porque el diseño no las muestra. Si las querés, las sumo en una etapa aparte.