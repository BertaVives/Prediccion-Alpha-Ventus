# Predicción de la potencia generada en Alpha Ventus
## ¿Qué problema o necesidad vamos a resolver? ¿Podemos solucionarlo con ML?
El parque eólico marino Alpha Ventus es el primer parque eólico marino de Alemania. Está situado en el Mar del Norte y consta de doce turbinas, todas con una capacidad de cinco megavatios. En 2011, el parque eólico registro el factor de capacidad más alto de todos los parques eólicos marinos europeos. Sin embargo, dos años más tarde, este bajo un 10%. 
El objetivo de este proyecto es poder estimar la variación del factor de capacidad en los próximos años prediciendo la generación de energía a partir de ciertos parámetros.
## ¿Qué solución aporta tu modelo de ML?
El factor de capacidad determina la rentabilidad de un parque eólico; mientras este sea rentable no hay ningún inconveniente, pero en el momento que deja de serlo, hay ciertas consecuencias y acciones que deben realizarse. Además, el conocimiento del factor de capacidad de este también determina la cantidad de energía consumida en Alemania que proviene de esta fuente renovable.  
## ¿Qué modelos has probado?
La variable que predecir es de tipo continúa, luego los modelos utilizados son de regresión.
Para poder determinar con que modelo se obtiene una predicción más exacta, se han implementado diferentes tipos de algoritmos. Inicialmente, se han implementado dos algoritmos de regresión: regresión lineal y regresión polinomial de grado 4. Al ver que los resultados obtenidos no han sido los esperados, no se ha implementado la regresión de Lasso o de Ridge. A continuación, se ha implementado un algoritmo basado en instancia (k-Nearest Neighbor), un árbol de decisión, un algoritmo de ensembled (Random Forest), LightGBM y uno de boosting (XGBoost). En todo ellos se ha requerido determinar los parámetros para evitar overfitting.
## ¿Qué resultados y conclusiones has obtenido?

## ¿Cuáles han sido las variables de mayor impacto?
La variable que más influencia tiene sobre la generación de energía es la velocidad del viento, hecho bastante predecible ya que las aspas de cada generador giraran más o menos rápido según esta variable. A mayor velocidad, mayor será la generación de energía.
## ¿Qué decisiones o acciones te permiten llevar a cabo tu modelo? ¿Qué consecuencias tiene en negocio?
Hoy en día se está intentando cambiar el planeta a uno más sostenible. Sobre todo, desde hace ya unos años, se han estado buscando e implementando nuevas formas para obtener energía de forma renovable siendo una de ellas los parques eólicos tanto marinos como terrestres. Por ello, es importante llevar un control de la energía que se puede llegar a obtener para poder mejorar la obtención de energía mediante fuentes renovables y disminuir el consumo de aquella que proviene de fuentes no renovables.
