✈️ Predicción del Precio de Vuelos
Resumen del Proyecto
Este proyecto de Análisis de Datos y Machine Learning se enfoca en el desarrollo de un modelo predictivo para estimar el precio de los vuelos a partir de un conjunto de datos del mundo real. El objetivo es identificar los factores clave que influyen en el costo de los boletos y construir una herramienta robusta y precisa que pueda ser utilizada para ofrecer estimaciones confiables a los clientes.

El análisis se estructura en varias etapas, desde el preprocesamiento y exploración de datos hasta el modelado predictivo y la evaluación final, siguiendo las mejores prácticas de la industria para asegurar la calidad y la reproducibilidad de los resultados.

Metodología
Exploración y Preprocesamiento de Datos:

Carga y fusión de los conjuntos de datos de vuelos de clase económica y de negocios.

Limpieza de datos: manejo de valores nulos, duplicados y atípicos.

Transformación de variables de tiempo (duración del vuelo, hora de salida y llegada) a un formato numérico.

Codificación de variables categóricas (aerolínea, ciudad de origen y destino, paradas).

Modelado Predictivo:

Entrenamiento de múltiples modelos de regresión, incluyendo Regresión Lineal, Árbol de Decisión y Random Forest, para establecer una línea base de rendimiento.

Análisis de los resultados para seleccionar el modelo más prometedor.

Evaluación y Selección del Modelo:

Evaluación de los modelos utilizando métricas clave como el Error Absoluto Medio (MAE), el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R²).

Conclusión final que resume los hallazgos clave, como la elección del modelo final, y propone próximos pasos para llevar el proyecto a una fase de producción.

Requerimientos
El proyecto requiere las siguientes librerías de Python:

pandas

numpy

scikit-learn

matplotlib

seaborn

joblib

Resultados
El modelo final seleccionado para la predicción de precios fue el Random Forest simple, que demostró un rendimiento superior en comparación con el modelo optimizado, evidenciando que en algunos casos, los parámetros por defecto de un modelo pueden ser más robustos y generalizar mejor a los datos no vistos. Las métricas finales del modelo son:

R²: 0.9908

MAE: 862.41

MSE: 4,718,941

Cómo Usar
Clona este repositorio:

Bash

git clone https://github.com/Jogoanalyst/Precios_vuelos.git
Instala las dependencias:

Bash

pip install -r requirements.txt
Abre el Jupyter Notebook Precio_vuelos.ipynb para ver el análisis completo.

Ejecuta todas las celdas en orden para reproducir el análisis.