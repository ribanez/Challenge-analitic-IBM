
# README 

En este archivo se exponen los antecedentes del proyecto, la metodología utilizada para abordar los desafíos, así como métricas y principales resultados que se obtienen durante el concurso.

## Antecendentes Generales 

En esta sección se muestran los antecedentes generales del concurso, como son el contexto del concurso, los objetivos y desafios planteados.

### Contexto del concurso 

El sistema de "Tarjeta de Crédito Unicard" forma parte de SMU y es un medio de financiamiento para los clientes de Unimarc, permitiéndoles acceder a beneficios, descuentos y oportunidades exclusivas. La estrategia de negocio de UNIRED se enfoca en el uso de datos para la toma de decisiones por lo que se requiere de equipos altamente especializados en el manejo de gran volumen de datos y en técnicas avanzadas para distintos análisis de segmentación de clientes, identificación de patrones, modelos predictivos, etc. Uno de los desafíos comerciales que se pueden abordar desde un enfoque analítico es aprovechar los datos transaccionales que se generan en los distintos negocios del retail y	construir distintos modelos analíticos.

### Objetivo del concurso

Plantear un desafío analítico a la comunidad académica para analizar, usando software de IBM, problemas de negocio que nos permitan identificar talentos en las áreas de interés de la compañía. Unicard entregará los tres casos de uso que se deben resolver y también proporcionará distintos conjuntos de datos necesarios para que los alumnos trabajen y presenten una solución analítica a cada desafío. El software para desarrollar los casos de uso será proporcionado por IBM.

### Desafios del concurso

1. Encontrar correlaciones entre la información de comportamiento de compras de los clientes en los locales de Unimarc y el uso del medio de pago Unicard, con el fin de identificar prospectos o perfiles de mejores clientes.

2. Identificar posibles indicadores en base al comportamiento de pago de cuentas en Unired de clientes sin información bancaria disponible. Estos, deben ser capaces de evaluar a los clientes sin tarjeta para determinar la factibilidad de apertura con el fin de aumentar la cartera actual minimizando el riesgo. 

3. Para clientes de tarjeta Unicard, usando comportamientos de compras en el retail y en el portal de pago de servicios, determinar principales palancas que determinan el uso de la tarjeta para el pago de sus compras en Unimarc.


## Antecedentes específicos 

En esta sección se muestran los antecedentes específicos, correspondientes a las metodologías de trabajo y objetivos planteados por el equipo.

### Metodología de trabajo

Para la resolución de los desafios propuestos hemos decidido seguir una metodología [Agile Process](https://www.itemis.com/en/agile/scrum/compact/fundamentals-of-project-management/agile-process-models) la cual fue modificada para su aplicación en Machine Learning para incorporar como se procesan, modelan y prueban los datos y los algoritmos.

La metodología [Agile Process](https://www.itemis.com/en/agile/scrum/compact/fundamentals-of-project-management/agile-process-models) nos permite aprovechar la fragmentación de las tareas de manera rápida, incorporando caminos paralelos para fallar e iterar rápidamente, permitiendo mejorar la productividad del equipo.

Los componentes de este proceso incluyen preprocesamiento de datos (incluyendo imputación de valor perdido si es necesario), análisis de datos exploratorios (por ejemplo, distribución univariada, distribución bivariada, análisis de correlación), extracción de características (por ejemplo, adición de características, eliminación de características, PCA), selección de algoritmos ajuste de hiperpares, ajuste de modelos, evaluación de modelos, reingeniería de modelos, pruebas de validación cruzada, predicción y, finalmente, presentación. 

A diferencia del oleoducto secuencial tradicional de Machine Learning donde los modelos se seleccionan y ajustan de uno en uno y el ajuste del modelo no puede comenzar antes de que se decida el método de imputación, Agile Process aprovecha al máximo el hecho de que varias personas trabajan en el proyecto al faltar la imputación de datos, la extracción de características y el ajuste del modelo se ejecutan en paralelo.

En resumen la metodología consiste en:
* Preprocesamiento de los datos
* Análisis exploratorio de los datos
* Extracción de características
* Selección de Algoritmos y ajuste de hiperparámetros
* Evaluación de modelos
* Predicción
* Presentación de resultados

<p style="text-align: center;"> Figura representativa de la metodología Agile process </p>
<img src="https://nycdatascience.com/blog/wp-content/uploads/2016/09/Screen-Shot-2016-09-21-at-2.38.04-AM.png" width="800" height="400" />

### Objetivos planteados por el equipo

El equipo se ha planteado abordar el desafío 
