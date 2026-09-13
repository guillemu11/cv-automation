# Auditoría del portfolio y CV de Paula

13 septiembre 2026. Objetivo: aumentar la probabilidad de que recruiters y hiring managers entiendan el encaje de Paula, confíen en su experiencia y quieran entrevistarla. Las valoraciones de impacto son juicio editorial, no datos de conversión.

## Diagnóstico

La experiencia permite una propuesta convincente: una Brand & Marketing Manager que entiende el negocio de los marketplaces, las cuentas y la ejecución comercial. El portfolio transmite cuidado estético, pero dedica demasiado espacio a presentarse y demasiado poco a demostrar cómo trabaja. El CV acumula responsabilidades y herramientas que compiten con sus mejores logros.

El mayor salto vendrá de hacer tres cosas: adelantar pruebas, construir casos que expliquen sus decisiones y asegurar que todas las afirmaciones son consistentes y defendibles.

Conservaría la paleta cálida, la tipografía editorial, la foto del portfolio, los accesos al CV y la separación explícita entre trabajo real y conceptos. No hace falta rehacer toda la identidad visual.

## Evidencias y alcance

- Web publicada: https://paula-de-francisco.vercel.app/; inspección del HTML y navegador Chrome en 1440×1000 y 390×844, con scroll y captura. También comprobación sin JavaScript.
- CV descargado de la web: dos páginas, idéntico por SHA-256 al PDF raíz y al de `output/portfolio_paula/assets/`. Hash: `ae50cc61432348f647f351c3b43bc3ce1c6944fd56a737c1c1e7125abf3e834a`.
- Contraste con `profile.yaml`, `scripts/build_master_cv.py`, código del portfolio y `output/CV_general/Paula De Francisco - CV.pdf`.
- Comprobación HTTP de todos los enlaces externos del portfolio. Lectura adicional en navegador de DoFreeze, Befit Crew, Colgate y Byredo. No se han auditado exhaustivamente los seis conceptos ni probado compras, formularios o transacciones.
- No se ha accedido a analítica, datos internos de campañas, referencias profesionales o sistemas ATS. Las cifras profesionales proceden de los documentos de Paula; no constituyen una verificación independiente.
- Se guardan capturas, HTML, PDF, medidas de navegador y resultados HTTP en esta carpeta. Se ha creado esta auditoría; no se han modificado el portfolio, el CV ni el perfil base.

## Cambios por prioridad

| Prioridad | Hallazgo | Consecuencia | Cambio concreto |
|---|---|---|---|
| P0 | El resumen público de experiencia y las cifras tienen ambigüedades | Un buen entrevistador puede cuestionar el alcance | Aclarar 50+ mercados, período del +30%, cálculo del ~40% y contribución personal |
| P0 | CV publicado desactualizado, sin portfolio y con un bullet cortado entre páginas | Pierde pruebas y cuidado editorial al descargar | Revisar contenido, enlaces y paginación; sincronizar PDF publicado |
| P1 | Los resultados aparecen muy abajo | La primera impresión no explica por qué contratarla | Llevar dos pruebas al hero y la franja de resultados inmediatamente después |
| P1 | Los trabajos reales son tarjetas de texto con enlaces | Ver una tienda no explica la aportación de Paula | Crear casos propios con imágenes, decisiones, alcance y resultados |
| P1 | Faltan señales visibles de gestión | Se aprecia ejecución, pero menos capacidad para dirigir | Mostrar equipo de dos, presupuestos si se pueden compartir, prioridades y coordinación |
| P1 | Todo el contenido depende visualmente de JS | Si el script falla, la página parece vacía | Contenido visible por defecto y animaciones como mejora progresiva |
| P2 | Seis conceptos antes del historial profesional | Mucha exploración para entender el encaje | Destacar dos relevantes y agrupar los demás como trabajo adicional |
| P2 | No hay medición explícita de conversión en el código revisado | No permite atribuir mejoras a entrevistas | Instrumentar clics en CV, contacto y casos; registrar contactos cualificados |
| P3 | Metadatos sociales y descubrimiento incompletos | Presentación al compartir menos robusta | URLs absolutas de imágenes, canonical, og:url y sitemap |

## Portfolio: primera impresión y recorrido

El titular actual, “Brand marketing, run like an operation”, transmite disciplina, pero deja al lector la tarea de descubrir su especialidad y su aportación comercial. La línea posterior enumera cuatro funciones y cuatro sectores. Eso comunica amplitud; no establece una prioridad.

Mi posicionamiento recomendado es Brand & Marketing Manager con fortaleza en e-commerce y crecimiento comercial, especialmente FMCG y beauty. Para candidaturas concretas se puede cambiar el énfasis; la home debe mantener una identidad fácil de recordar.

Propuesta de hero en inglés, basada en las afirmaciones actuales del perfil y pendiente de validar sus métricas:

> **Brand & Marketing Manager · Dubai**
>
> **I build brands with a commercial mindset.**
>
> From beauty marketplaces to FMCG launches, I connect brand strategy with the decisions that drive sales. Currently leading Brand & Marketing at DoFreeze; previously Miravia (Alibaba Group), Glovo and Mondelēz.
>
> **+30% quarterly GMV growth at Miravia · 42 key accounts managed**
>
> Explore my work · Download CV · Get in touch

El dato del +30% deberá incorporar el período y la población medidos en el caso asociado. En el contacto, expresar ubicación y disponibilidad real; no prometer incorporación inmediata sin confirmar el preaviso.

### Lo que muestra la medición

| Elemento | Desktop | Móvil |
|---|---:|---:|
| Altura total de la página | 8.510 px | 12.137 px |
| Inicio de la franja de resultados | ~1.842 px | ~2.047 px |
| Inicio de trabajos | ~2.243 px | ~2.809 px |
| Inicio de experiencia | ~4.593 px | ~6.755 px |
| Botón de CV dentro del hero | ~796 px | ~890 px |

Medidas de una sesión, sujetas a fuentes y viewport; no equivalen a abandonos observados. En móvil sí existe un botón fijo de CV visible desde el principio. El problema es la jerarquía: la foto ocupa 280×280 px antes de que aparezcan el rol y la propuesta.

Reduciría y movería la foto en móvil para poner primero rol, beneficio, prueba y acción. Eliminaría o condensaría la cita personal y el About que preceden a los resultados. La rejilla del About sigue reservando en desktop columnas de una composición cuya segunda foto ya fue eliminada.

Orden propuesto: hero → resultados y empresas → tres casos reales → experiencia breve → dos conceptos → capacidades vinculadas a pruebas → contacto. Educación y herramientas pueden ocupar un bloque compacto.

## El contenido que puede hacerla memorable

### 1. Miravia: crecimiento de cuentas de beauty y fragrances

Es el caso comercial más fuerte disponible y hoy no tiene un caso propio entre los trabajos. Mostrar 42 cuentas, +30% de GMV y expansión de fragrances, explicando el problema, las decisiones de surtido/precio/promociones y el período analizado. Añadir un gráfico anonimizado y un ejemplo de activación.

Confirmar si el +30% corresponde a toda la cartera, a un trimestre concreto o a otro agregado; si las 30+ incorporaciones son tiendas o marcas; y qué parte del crecimiento puede atribuirse a sus decisiones. No presentar un resultado de marketplace en España como resultado de quick-commerce en UAE.

### 2. DoFreeze: construir y operar el canal digital

Usar capturas comentadas de catálogo, bundles, merchandising y recorrido de compra. Explicar el punto de partida, qué decidió Paula, qué ejecutó y con quién colaboró. La etiqueta “built in Lovable” puede ir en los detalles; el titular debería explicar el problema comercial resuelto.

La web habla de Lovable y el CV de Shopify. Pueden convivir: hay que explicar frontend, backend o cambio de plataforma, sin dejar una aparente contradicción. Cuantificar conversión, AOV, ventas o tiempos únicamente si existen datos comparables.

El enlace actual a la tienda abre una experiencia de compra con modal de cookies. Un caso alojado en el portfolio permite entender el trabajo sin atravesar ese recorrido. Mantener “Visit live site” como acción secundaria.

### 3. Befit Crew: diseño del programa de afiliados

Tiene una mecánica visible que permite demostrar criterio: comisiones de 8–10%, descuento del 5%, captación, aprobación, códigos y seguimiento. Mostrar el funnel, un briefing real, un ejemplo de creator y resultados de activación/ventas si están disponibles.

No confundir “25–50 creators por campaña” con afiliados activos o ventas. Son métricas distintas. En la página enlazada hay además una inconsistencia de copy: se menciona revisión de solicitudes en siete días laborables y, al final, obtención inmediata del código. Aclararla reforzaría la calidad del trabajo mostrado.

Email & CRM necesita al menos una pieza y su contexto. Ahora es una tarjeta estática sin muestras. Integrarlo en el caso de DoFreeze hasta tener material suficiente para sostenerlo por separado.

### Qué debe contener cada caso

Problema → rol personal y equipo → restricciones → decisiones → entregables → resultado con período y fuente → aprendizaje. Un caso breve con tres imágenes comentadas y un resultado defendible vale más que una landing extensa sin evidencia.

### Conceptos

Mantener las etiquetas de trabajo autoiniciado. Elegir como destacados los dos que mejor se alineen con la vacante; para un posicionamiento FMCG/beauty, Colgate y Byredo son candidatos razonables, sujetos a corregir su contenido.

En Colgate aparece una cifra de siete de cada diez compras decididas en la primera pantalla, sin fuente visible en el contenido revisado. Citar una fuente que realmente respalde esa afirmación o eliminarla. En Byredo, precisar la referencia a años trabajando con casas de oud del Golfo: distinguir relación con distribuidores desde Miravia de experiencia laboral en el Golfo. El +30% pertenece a Miravia y debe permanecer claramente separado de objetivos del concepto.

Los conceptos ganarían fuerza con una decisión difícil, un presupuesto hipotético claramente etiquetado, una prueba de 30 días y criterios para continuar o parar. El acabado visual ya comunica gusto; falta mostrar más criterio de negocio.

## CV base

### Qué funciona

Tiene cronología comprensible, compañías reconocibles y cifras relevantes. El texto del PDF es extraíble y su orden general se conserva en la extracción realizada. Esto no garantiza compatibilidad con todos los ATS, pero descarta que sea únicamente una imagen.

### Qué cambiar

1. **Acortar el summary:** el publicado tiene aproximadamente 136 palabras. Objetivo editorial: 50–70 palabras que expliquen rol, sectores y dos pruebas. Quitar “Results-driven”, “proven track record” y la tesis del resumen.
2. **Simplificar titular:** `Brand & Marketing Manager | E-Commerce & Commercial Growth`. Para KAM o e-commerce, preparar versiones con otro orden de evidencias y headline, manteniendo cargos reales.
3. **Actualizar gestión:** `profile.yaml` menciona un diseñador y un social media executive; el PDF público y la experiencia de la web omiten ese dato. Para puestos manager, merece un bullet visible.
4. **Reordenar DoFreeze:** responsabilidad de marca/equipo, lanzamientos, canales digitales, creators y, después, automatización. La IA debe demostrar una mejora de ejecución, con autoría y medición precisas.
5. **Concentrar bullets:** aproximadamente 4–5 en DoFreeze, 3 en Miravia, 2 en Glovo y 1 en Mondelēz. Cada uno debe aportar una decisión, un alcance o un resultado diferente.
6. **Limpiar habilidades:** reducir repeticiones entre las cinco categorías y mantener solo herramientas relevantes que Paula pueda explicar con ejemplos. Eliminar datos corporativos genéricos de facturación/empleados que no explican su aportación.
7. **Enlaces reales:** incluir portfolio y LinkedIn como hipervínculos embebidos. Los PDFs inspeccionados no contienen anotaciones de enlace; algunos visores podrían detectar URLs automáticamente, pero no conviene depender de ello.
8. **Maquetación:** corregir el bullet de Miravia que empieza en la página 1 y termina al comienzo de la 2. Mantener texto cómodo de leer; no comprimir indiscriminadamente para llegar a una página.

Propuesta de summary, sujeta a confirmar las afirmaciones del perfil:

> Dubai-based Brand & Marketing Manager with experience across FMCG, beauty and e-commerce. Currently leading brand marketing and a two-person creative/social team at DoFreeze. Previously managed 42 beauty, fragrance and fashion accounts at Miravia (Alibaba Group), achieving 30% quarter-on-quarter GMV growth through pricing, assortment and promotions. Combines brand development, marketplace operations and commercial account management.

La versión general de una página tampoco está lista para sustituir al PDF público: la foto queda recortada casi por completo en la parte superior, el encabezado ocupa demasiadas líneas y el resumen mezcla quick-commerce, 50+ mercados y +30% sin atribución suficiente. La corregiría antes de usarla.

## Coherencia y datos que Paula debe confirmar

| Punto | Duda concreta | Criterio de publicación |
|---|---|---|
| 50+ países | ¿Presencia de DoFreeze o mercados gestionados directamente por Paula? | Separar alcance de la empresa de responsabilidad personal |
| +30% GMV | ¿Qué trimestre, cuentas, comparación y fuente? | Dato atribuido a Miravia con período y alcance |
| ~40% menos trabajo manual | ¿Qué tareas, horas antes/después y papel de Paula? | Estimación etiquetada y método, o descripción cualitativa |
| Seis lanzamientos | ¿Productos, fechas, mercados y rol en cada uno? | Evidencia de productos y alcance personal |
| Shopify/Lovable | ¿Arquitectura actual, migración o proyectos diferentes? | Explicación consistente entre CV y caso |
| Miravia/AliExpress | El PDF agrupa ambos; perfil y web dicen Miravia | Nombre de empresa y experiencia real, sin fusionar por pertenecer al mismo grupo |
| Creators | ¿Captados, aprobados, activos o participantes por campaña? | Mismo denominador en todos los documentos |
| LinkedIn | Producción usa slug corto; perfil y local usan slug largo | Confirmar cuál identifica el perfil actual; un HTTP 200 no demuestra identidad |
| Experiencia | “4+” sigue en documentos con carrera desde 2021 | Decidir si cuenta prácticas; expresar el criterio de forma consistente |

## Técnica, accesibilidad y distribución

Los enlaces a los ocho trabajos devolvieron HTTP 200. La página principal se recorrió sin errores JavaScript capturados, sin secciones pendientes de revelar y sin desbordamiento horizontal en los dos tamaños probados. Esto no equivale a una auditoría de accesibilidad completa ni a una medición de Core Web Vitals.

Sin JS, el hero y las secciones quedan ocultos por el CSS; la captura muestra esencialmente la navegación sobre un fondo vacío. Además, las métricas parten de cero en HTML. Corregir con contenido y cifras finales visibles de base. Revisar también impresión, navegación por teclado y compensación de anclas para la cabecera fija.

`robots.txt` y `sitemap.xml` devuelven 404. No implica que la web esté bloqueada para indexación. Faltan canonical y og:url, y las imágenes sociales usan rutas relativas: mejoras secundarias frente al contenido y los casos. No se ha probado el preview real de LinkedIn ni medido posicionamiento en buscadores.

Para atraer visitas cualificadas: usar el caso adecuado en el CV, LinkedIn Featured y candidaturas; no depender de que alguien encuentre el dominio por búsqueda. Añadir UTMs por canal sin datos personales y eventos como `cv_download`, `contact_click` y `case_open`. Medir contactos e entrevistas junto con visitas; un clic de email no es un mensaje enviado ni una candidatura convertida. No se han enviado mensajes ni publicado cambios.

## Secuencia recomendada

Primero: confirmar datos, corregir CV y sincronizar enlaces. Después: hero móvil, pruebas arriba y contenido visible sin JS. A continuación: construir los casos de Miravia, DoFreeze y Befit con materiales reales. Por último: recortar conceptos, completar metadatos y medir el recorrido hasta contactos e entrevistas. No prometer una mejora porcentual sin datos iniciales y observación posterior.
