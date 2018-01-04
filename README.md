
# README

# Estamos dentro de los 3 primeros !


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

A diferencia de los métodos secuencial tradicional de Machine Learning donde los modelos se seleccionan y ajustan de uno en uno y el ajuste del modelo no puede comenzar antes de que se decida el método de imputación, Agile Process aprovecha al máximo el hecho de que varias personas trabajan en el proyecto al faltar la imputación de datos, la extracción de características y el ajuste del modelo se ejecutan en paralelo.

En resumen la metodología consiste en:
* Preprocesamiento de los datos
* Análisis exploratorio de los datos
* Extracción de características
* Selección de Algoritmos y ajuste de hiperparámetros
* Evaluación de modelos
* Predicción
* Presentación de resultados

<p style="text-align: center;"> Figura representativa de la metodología Agile process </p>
<img src="https://nycdatascience.com/blog/wp-content/uploads/2016/09/Screen-Shot-2016-09-21-at-2.38.04-AM.png" width="600" height="300" />

### Objetivos planteados por el equipo

El equipo se ha planteado abordar el desafío (1) con lo cual el objetivo del equipo es encontrar correlaciones entre el comportamiento de compra y el uso de la tarjeta UNICARD como medio de pago.

Siendo objetivos secundarios del problema:

* Caracterizar a los buenos clientes, es decir, determinar las principales características de estos.
* Determinar palancas de uso de la tarjeta UNICARD. 
* Cruzar la información existente de los clientes para encontrar correlaciones en su comportamiento, ya sea en UNICARD o en UNIRED.

### Revisión de la base de datos

En base a una lectura y análisis preliminar de la base de datos BLUADMIN y las distintas tablas que esta posee, se construyó un diagrama que nos permita relacionar la distinta información que se encuentra en ellas. De esta manera, se pueden extraer características de los clientes, comportamientos de pagos, comportamientos de compras, centros comerciales, etc.

<p style="text-align: center;"> Diagrama de flujo de la base de datos </p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/diagrama_db.png" width="600" height="300" />

### Análisis exploratorio.

Utilizando Python y PySpark se revisaron las distintas tablas de la base de datos en busca de caracterísicas de los clientes. Por medio de las herramientas de visualización y exploración de IBM PIXIESDUST y otras como SEABORN se graficaron algunas características de los clientes.

En primer lugar, los clientes que componen la base de datos en su mayoría son mujeres, representando el 55% de la muestra. 
<p style="text-align: center;">Gráfico del genero de los clientes con tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/gender.png" width="500" height="250" />


La mayoría de los clientes se encuentran en el rango etáreo 20-40 años. 
<p style="text-align: center;"> Histograma de las edades de los clientes con tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/edad.png" width="500" height="250" />

<p style="text-align: center;"> Histogramas relacionales de edad y género</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/gender-edad.png" width="500" height="250" />


Por otra parte, gran parte de los usuarios de unicard son personas que se encuentran en en los grupos socioeconómicos D-E-C3 con el 25%, 33% y 34% respectivamente.
<p style="text-align: center;">Gráfico del grupo socio económico (GSE) de los clientes con tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/gse.png" width="500" height="250" />


Dentro de los usuarios de UNICARD, los cupos de las tarjetas en su mayoría están en el rago 100000 - 200000 CLP.

<p style="text-align: center;"> Histograma del cupo nacional de la tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/cupo_nacional.png" width="600" height="300" />

Mientras que los cupos disponibles de las tarjetas UNICARD son menores a los 200000 CLP en su mayoría.

<p style="text-align: center;">Histograma del saldo disponible de la tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/saldo_disponible.png" width="600" height="300" />




<p style="text-align: center;"> Gráfico de personas con bloqueo en su tarjeta UNICARD</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img/bloqueo.png" width="600" height="300" />

# EXPERIMENTOS

### i) Experimentos Realizados
Para realizar el estudio, se plantean 2 experimentos principales:

1. El primero consiste en identificar las features que más significativamente impactan a la hora de caracterizar a un cliente que es usuario de la tarjeta y se encuentra bloqueado, lo que a su vez permite encontrar indicadores para caracterizar su comportamiento en Unired

2. El segundo experimento busca retratar las features que mayor influencia tienen a la hora de determinar el uso de tarjeta Unimarc como medio de pago, lo que permite caracterizar las cualidades del cliente y también determinar las palancas que determinan su uso.

En base a estos experimentos, se determina el patrón característico de comportamiento y la relevancia de cada uno de sus elementos, con respecto a la incidencia que estos tienen en la determinación del uso de la tarjeta Unimarc y del estado de morosidad del mismo.

### ii) Balance de Clases

Para el primer experimento descrito, se observa que la cantidad de datos por clase se encuentran desbalanceados con respecto de la cantidad de usuarios 'bloqueados' y usuarios 'no bloqueados', constitiyendo estos últimos el orden del 75% de la muestra. Por tanto, se realizó un sub-muestreo de la categoría predominante, de modo que ambas clases contengan igual cantidad de información y se construyeron dos nuevas tablas que fueron guardadas en archivos csv.

1. **bloqueo2balanceado.csv** esta tabla está formada por la información conjunta de las tablas persona-unired-retail y contiene la misma cantidad de usuarios bloqueados y no bloqueados.
2. **unicard2balanceado.csv** esta tabla está formada por la información conjunta de las tablas persona-unired-retail y contiene la misma cantidad de usuarios que usan o no la tarjeta unimarc.

### iii) Data Augmentation

En muchas aplicaciones de machine learning, los métodos conocidos como "data augmentation" han permitido construir mejores modelos. Teniendo esto en cuenta, para la construcción del SET DE DATOS analizados se considera que **cada experiencia de compra es única para cada cliente**, de esta forma si el mismo individuo realiza compras en diferentes ocasiones y/o con medios de pago distintos, se consideran como eventos no relacionados.

Así se puede estudiar de mejor manera el comportamiento de los clientes y los estímulos que le gatillan a utilizar o no la tarjeta Unimarc como medio de pago.

Esta muestra constituye el SET DE DATOS utilizados para realizar los análisis y resultados que se presentarán en este documento. 

## Representatividad de la Muestra
#### Estimación del tamaño mínimo de la muestra

A continuación, se realiza la estimación del tamaño mínimo de la muestra que permite garantizar que esta sea representativa, para cierto nivel de confianza exigido.

$$TM = \frac{\frac{z^2 ~ \times ~ p~ \cdot ~ ( ~1 ~ - ~ p ~)}{e^2}}{1+\frac{z^2 ~ \times ~ p ~ \cdot ~ ( ~ 1 ~ - ~ p ~ )}{e^2 ~ \cdot ~ N}}$$

TM = Tamaño de la muestra
N = Tamaño de la población 
e = Margen de error 
z = Puntuación dependiendo del nivel de confianza deseado.

Asumiendo una población de 14 millones de habitantes ($N$), cantidad que corresponde a la fracción de la población Chilena mayor a 18 años. Exigiendo un nivel de confianza del $95\%$ ($z=1,96$) y un margen de error de $2\%$, se requiere de un tamaño de muestra de al menos $2400$ individuos.

Para el experimento 1 se trabajó muestras balanceadas con información del comportamiento del orden de 500 mil individuos, y para el experimento 2 con información del orden 200 mil individuos.

## Comportamiento de compras

Para representar el comportamiento de compras de los clientes en los locales Unimarc, se lleva a cabo la extracción características significativas y la creación de nuevas features a partir de los datos de cada individuo.


### Listado de caracterésticas extraídas

Se presenta un listado de las características extraídas directamente a partir de la base de datos.

* **SPEND_AMT**: Monto de la compra realizada por el cliente en CLP.
* **DISCOUNT_AMT**: Monto del descuento al momento de la compra del cliente en CLP.
* **GENDER**: Genero del cliente 0 si es femenino y 1 si es másculino.
* **EDAD**: Edad del cliente.
* **MOBILE_CONTACTABILITY**: Conocimiento del teléfono del cliente, 1 si se conoce 0 si no.
* **EMAIL_CONTACTABILITY**: Conocimiento del email del cliente, 1 si se conoce 0 si no.
* **GSE**: Grupo socio-económico en el cual se ubica el cliente.
* **CIVIL_STATUS**: Estado civil del cliente.


### Listado de features creadas

Se presenta un listado de las features creadas para caracterizar el comportamiento de compra de los clientes de Unimarc, a partir de la base de datos.

* **std_pago_unired**: Desviación estandar del pago del cliente en unired.
* **max_pago_unired**: Máximo gasto realizado por el cliente en unired.
* **avg_pago_unired**: Promedio de los servicios pagados por el cliente en unired.
* **pago_unired_mensual**: Pago total del cliente en unired.
* **avg_dia_pago_unired**: Día promedio del mes en que el cliente paga servicios en unired.
* **max_dia_pago_unired**: Máximo día del mes en que el cliente paga servicios en unired.
* **min_dia_pago_unired**: Mínimo día del mes en que el cliente paga servicios en unired.
* **avg_uso_tarjeta**: Cantidad de veces que el cliente utilizó la tarjeta unicard como medio de pago.

* **avg_pago_retail_mensual**: promedio del gasto del cliente en cada compra con el mismo medio de pago.
* **max_pago_retail_mensual**: valor del producto más costoso cancelado por el cliente en el retail.
* **std_pago_retail_mensual**: Desviación estandar de los productos comprados por el cliente en el retail en una compra.

Adicionalmente, se construye la feature **'avg_uso_tarjeta'**, la cual será utilizada exclusivamente en el experimento 1 para determinar la condición de bloqueo.

* **'avg_uso_tarjeta':** Corresponde al uso promedio de un cliente de la tarjeta unicard al momento de comprar.


### Listado de Etiquetas estudiadas

Para caracterizar el comportamiento de los clientes de Unimarc, como se mencionó en la descripción de **Experimentos Realizados**, se definen casos de estudio respecto a las siguientes etiquetas.

* **PAYMENT_MEAN_ID**: Medio de pago utilizado por el cliente, 1 si utiliza tarjeta unimarc 0 si no.
* **bloqueo**: Condición del cliente, 1 si el cliente se encuentra bloqueado 0 si no.

## Resultados Experimentos
### XGBOOST

#### Para realizar los experimentos descritos se utilizó el algoritmo XGBoost.

Para identificar las features:
* Que más significativamente impactan a la hora de caracterizar a un cliente que es usuario de la tarjeta y se encuentra bloqueado
* Que mayor influencia tienen a la hora de determinar el uso de tarjeta Unimarc como medio de pago

Se implementó una técnica de machine learning basada en ensembles, conocida como Gradient Boosting, en particular se implementó el algoritmo XGBoost.

> [Gradient boosting](https://es.wikipedia.org/wiki/Gradient_boosting), es una técnica de aprendizaje automático utilizado para el análisis de regresiones y para problemas de clasificación estadística, el cual produce un modelo predictivo en forma de un conjunto de modelos de predicción débiles, típicamente árboles de decisión. Construye el modelo de forma escalonada como lo hacen otros métodos de boosting, y los generaliza permitiendo la optimización arbitraria de una función de pérdida diferenciable.

### Criterios de Evaluación de Modelos

Para la evaluación de los modelos desarrollados se utilizan las siguientes métricas y objetivos

* Maximización del **AUC** utilizando una curva [ROC](https://es.wikipedia.org/wiki/Curva_ROC), lo que se busca es la maximización del área bajo la curva pudiendo de esta manera obtener mejores modelos.
* [ Precision-Recall ](https://en.wikipedia.org/wiki/Precision_and_recall) corresponde a las metricas de comparación entre los diferentes modelos obtenidos con el fin de seleccionar 1.


# DESAFIO 1

1. Encontrar **correlaciones** entre la información de **comportamiento de compras** de los clientes en los locales de Unimarc y el **uso del medio de pago Unicard**, con el fin de identificar prospectos o perfiles de mejores clientes.

Para afrontar este desafío, se extrae una muestra representativa de datos a partir de la intersección de las bases de datos entregadas, bajo la premisa de que la muestra contenga información del cliente (la cual se encuentra en la tabla 'PERSONAS') tales como género, edad, grupo socio-económico, etc. Y la información de las compras del cliente contenidas en las tablas 'RETAIL' y 'UNIRED'.

### Primer experimento: bloqueo como etiqueta

Al implementar XGBoost para el primer experimento se obtuvo los siguiente resultados:


#### Resultados
> * Area under the precision-recall curve test set: 0,999560.
> * Precision score de 0,990370 
> * Recall score de 0,999373.


#### Gráfica de Importancia de Features

A continuación se muestra la gráfica que representa la **importancia de las diferentes features** de acuerdo a su impacto en caracterizar a un cliente que es usuario de la tarjeta y que se encuentra **bloqueado**

<p style="text-align: center;"> Caracteristicas principales para medio de pago </p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/xgb_features_pago.png" width="600" height="300" /> 

Se puede observar que las caraácteristicas más relevantes al momento de realizar la clasificación de los individuos se logra con la información historica del gasto de los clientes.


#### Curva ROC

A continuación se presenta la gráfica de la curva ROC, obtenida para el modelo seleccionado.


<p style="text-align: center;"> Curva ROC para bloqueo</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/xgb_roc_bloqueo.png" width="500" height="300" /> 

Se puede observar con respecto a la curva que obtenemos un modelo que se encuentra muy cercano al punto (0,1), es decir, con una clasificación casi perfecta al momento de aplicar el modelo al conjunto de datos de validación y logra diferenciar cuales son buenos y malos clientes según la etiqueta de bloqueo.

### Segundo experimento, medio de pago como etiqueta

Al implementar XGBoost para el segundo experimento se obtuvo los siguiente resultados:

> * Area under the precision-recall curve test set: 0,967155
> * Precision score: 0,943355
> * Recall score: 0,988584.
 
#### Gráfica de Importancia de Features

A continuación se muestra la gráfica que representa la **importancia de las diferentes features** que mayor influencia tienen a la hora de determinar el **uso de tarjeta Unimarc como medio de pago**.


<p style="text-align: center;"> Caracteristicas principales para el bloqueo</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/xgb_features_bloqueo.png" width="600" height="300" /> 


#### Curva ROC

A continuación se presenta la gráfica de la curva ROC, obtenida para el modelo seleccionado.

<p style="text-align: center;"> Curva ROC para medio de pago</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/xgb_roc_pagos.png" width="500" height="300" /> 


Se puede observar respecto a la curva que el medio de pago es una caracteristica un poco más dificil a predecir, pero que de igual manera se logra una exactitud bastante alta.


## Desafio 2

2. Identificar posibles **indicadores** en base al **comportamiento de pago de cuentas en Unired** de clientes sin información bancaria disponible. Estos, deben ser capaces de **evaluar a los clientes sin tarjeta** para determinar la factibilidad de apertura con el fin de aumentar la cartera actual minimizando el riesgo.

En la busqueda de indicadores que permitan vincular el comportamiento de pago de cuentras en Unired de clientes sin información bancaria disponible, se utilizó un modelo de XGBoost como el descrito previamente pero con solo la información perteneciente a las personas y al comportamiento de pago.

### Listado de caracterésticas extraídas

Se presenta un listado de las características extraídas directamente a partir de la base de datos y que resultan de mayor importancia en la toma de decisiones sobre .

* **GENDER**: Genero del cliente 0 si es femenino y 1 si es másculino.
* **EDAD**: Edad del cliente.
* **MOBILE_CONTACTABILITY**: Conocimiento del teléfono del cliente, 1 si se conoce 0 si no.
* **EMAIL_CONTACTABILITY**: Conocimiento del email del cliente, 1 si se conoce 0 si no.
* **GSE**: Grupo socio-económico en el cual se ubica el cliente.
* **CIVIL_STATUS**: Estado civil del cliente.


### Listado de features creadas

Se presenta un listado de las features creadas para caracterizar el comportamiento de compra de los clientes de Unimarc, a partir de la base de datos.

* **std_pago_unired**: Desviación estandar del pago del cliente en unired.
* **max_pago_unired**: Máximo gasto realizado por el cliente en unired.
* **avg_pago_unired**: Promedio de los servicios pagados por el cliente en unired.
* **pago_unired_mensual**: Pago total del cliente en unired.
* **avg_dia_pago_unired**: Día promedio del mes en que el cliente paga servicios en unired.
* **max_dia_pago_unired**: Máximo día del mes en que el cliente paga servicios en unired.
* **min_dia_pago_unired**: Mínimo día del mes en que el cliente paga servicios en unired.

### Listado de Etiquetas estudiadas

Para caracterizar el comportamiento de los clientes de Unimarc, como se mencionó en la descripción de **Experimentos Realizados**, se definen casos de estudio respecto a las siguientes etiquetas.

* **bloqueo**: Condición del cliente, 1 si el cliente se encuentra bloqueado 0 si no.


### Experimento: bloqueo como etiqueta

Al implementar XGBoost se obtuvo los siguiente resultados:


#### Resultados
> * Area under the precision-recall curve test set: 0,763946
> * Precision score: 0,730994
> * Recall score: 0,856164.


#### Gráfica de Importancia de Features

A continuación se muestra la gráfica que representa la **importancia de las diferentes features** de acuerdo al impacto que estas tienen a la hora de evaluar a un **potencial cliente** para determinar si éste **será bloqueado** en el caso de que se le diera tarjeta.


<p style="text-align: center;"> Caracteristicas principales para el bloqueo</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/features_unired.png" width="600" height="300" /> 

Se puede observar que las caraácteristicas más relevantes al momento de realizar la clasificación de los individuos se logra con la información historica de retail de los clientes y, naturalmente, el orden de importancia de las features se mantiene con relación a los resultados presentados para el experimento 1 del Desafío 1.


#### Curva ROC

A continuación se presenta la gráfica de la curva ROC, obtenida para el modelo seleccionado.


<p style="text-align: center;"> Curva ROC para medio de pago</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/roc_unired.png" width="500" height="300" /> 

Se obtiene un modelo menos robusto en comparación a los obtenidos en los otros desafios, con lo que podemos concluir que la información de unired no es suficiente para caracterizar cabalmente el comportamiento crediticio de los individuos.

## Desafío 3

3. Para clientes de tarjeta Unicard, usando **comportamientos de compras en el retail y en el portal de pago de servicios**, determinar principales **palancas** que determinan el **uso de la tarjeta para el pago de sus compras en Unimarc**.

En la busqueda de indicadores que permitan vincular el comportamiento de compras en Retail, se utilizó un modelo de XGBoost como el descrito previamente pero con solo la información perteneciente a las personas y al comportamiento de compras.


### Listado de caracterésticas extraídas

Se presenta un listado de las características extraídas directamente a partir de la base de datos.

* **GENDER**: Genero del cliente 0 si es femenino y 1 si es másculino.
* **EDAD**: Edad del cliente.
* **MOBILE_CONTACTABILITY**: Conocimiento del teléfono del cliente, 1 si se conoce 0 si no.
* **EMAIL_CONTACTABILITY**: Conocimiento del email del cliente, 1 si se conoce 0 si no.
* **GSE**: Grupo socio-económico en el cual se ubica el cliente.
* **CIVIL_STATUS**: Estado civil del cliente.


### Listado de features creadas

Se presenta un listado de las features creadas para caracterizar el comportamiento de compra de los clientes de Unimarc, a partir de la base de datos.

* **std_pago_unired**: Desviación estandar del pago del cliente en unired.
* **max_pago_unired**: Máximo gasto realizado por el cliente en unired.
* **avg_pago_unired**: Promedio de los servicios pagados por el cliente en unired.
* **pago_unired_mensual**: Pago total del cliente en unired.
* **avg_dia_pago_unired**: Día promedio del mes en que el cliente paga servicios en unired.
* **max_dia_pago_unired**: Máximo día del mes en que el cliente paga servicios en unired.
* **min_dia_pago_unired**: Mínimo día del mes en que el cliente paga servicios en unired.

### Listado de Etiquetas estudiadas

Para caracterizar el comportamiento de los clientes de Unimarc, como se mencionó en la descripción de **Experimentos Realizados**, se definen casos de estudio respecto a las siguientes etiquetas.

* **PAYMENT_MEAN_ID**: Medio de pago utilizado por el cliente, 1 si utiliza tarjeta unimarc 0 si no.

### Experimento, medio de pago como etiqueta

Al implementar XGBoost para el segundo experimento se obtuvo los siguiente resultados:

#### Resultados
> * Area under the precision-recall curve test set: 0,997705.
> * Precision score de 0,983601
> * Recall score de 0,996552. 


#### Gráfica de Importancia de Features

A continuación se muestra la gráfica que representa la **importancia de las diferentes features** que mayor influencia tienen a la hora de determinar el **uso de tarjeta Unimarc como medio de pago** para identificar palancas.


<p style="text-align: center;"> Caracteristicas principales para medio de pago </p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/features_retail.png" width="600" height="300" />

#### Curva ROC

A continuación se presenta la gráfica de la curva ROC, obtenida para el modelo seleccionado.

<p style="text-align: center;"> Curva ROC para bloqueo</p>
<img src="https://raw.githubusercontent.com/robibanez/Challenge-analitic-IBM/master/img2/roc_retail.png" width="500" height="300" />

Se puede observar respecto a la curva que el medio de pago es una caracteristica fácil de predecir, por lo que se logra una exactitud bastante alta.
