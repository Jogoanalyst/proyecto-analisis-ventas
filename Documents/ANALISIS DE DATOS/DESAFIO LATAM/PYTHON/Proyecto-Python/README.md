# Análisis de Ventas y Clientes - Base de Datos classicmodels

### Descripción del Proyecto
Este proyecto es un análisis de datos completo realizado en un Jupyter Notebook. Su objetivo es extraer, transformar y analizar datos de una base de datos de PostgreSQL llamada `classicmodels` para responder a preguntas de negocio clave. El análisis se enfoca en métricas de ventas, rentabilidad y desempeño de clientes y productos.

### Preguntas de Negocio Resueltas
El análisis en el notebook aborda las siguientes preguntas estratégicas:

* **Ventas por línea de productos**: ¿Cuál fue el total de ventas por cada línea de productos?
* **Clientes**: ¿Cuántos clientes únicos hicieron compras y cuántos no han realizado ninguna?
* **Top 10 Clientes (2005)**: ¿Cuáles fueron los 10 clientes con mayores ventas brutas en dinero durante el año 2005?
* **Top 10 Productos (2005)**: ¿Cuáles fueron los 10 artículos más vendidos durante el año 2005, considerando la cantidad neta?

### Estructura del Proyecto
El proyecto está organizado en los siguientes archivos:

* `proyecto_final.ipynb`: El notebook principal que contiene el análisis paso a paso.
* `funciones.py`: Un módulo de Python con funciones reutilizables para filtrar datos y escribir en la base de datos, lo que mantiene el notebook limpio y modular.
* `README.md`: Este archivo, que proporciona una descripción general del proyecto.

### Tecnologías y Librerías Utilizadas
El análisis fue realizado con las siguientes herramientas:

* **Lenguaje**: Python 3.x
* **Análisis de datos**: Pandas
* **Base de datos**: PostgreSQL
* **Conexión a DB**: `sqlalchemy` y `psycopg2`
* **Entorno**: Jupyter Notebook

### Instrucciones de Uso
Para replicar este análisis, asegúrate de tener una base de datos de PostgreSQL con la información de `classicmodels`. Luego, sigue estos pasos:

1.  Instala las dependencias necesarias:
    ```bash
    pip install pandas sqlalchemy psycopg2-binary jupyter
    ```
2.  Abre el notebook `proyecto_final.ipynb` en tu entorno de Jupyter.
3.  Asegúrate de que la conexión a la base de datos en el notebook esté configurada correctamente.
4.  Ejecuta las celdas en orden para realizar el análisis completo.



