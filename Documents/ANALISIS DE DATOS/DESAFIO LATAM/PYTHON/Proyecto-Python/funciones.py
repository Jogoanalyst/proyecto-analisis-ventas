import pandas as pd
from sqlalchemy import create_engine
# Para este punto debes aplicar el principio DRY, por lo que se deben utilizar funciones para
 #realizar el filtrado por fechas, generar tablas pivote y escribir tabla en Postgre. Las funciones
 #deben estar en un archivo separado llamado funciones.py y ser importadas al Jupyter
 #Notebook. En este archivo se debe incluir:
# Listado de Funciones que usaremos en la prueba final de python 

# Comenzamos importando las librerias necesarias para crear nuestras funciones.



import pandas as pd
from sqlalchemy import create_engine

# Creamos funcion 'filtrar_por_nombre'
def filtrar_por_fecha(df, columna_fecha, fecha_inicio, fecha_fin):
    
    # Convertimos las fechas de formato object a formato datetime
    
    df[columna_fecha] = pd.to_datetime(df[columna_fecha])
    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)
    # Filtrar el DataFrame por fechas
    df_filtrado = df[(df[columna_fecha] >= fecha_inicio) & (df[columna_fecha] <= fecha_fin)]
    return df_filtrado

"""
    Filtra un DataFrame por un rango de fechas.

    Parametro df: El DataFrame que se quiere filtrar.
    Parametro columna_fecha: El nombre de la columna que tiene la fecha
    Parametro fecha_inicio: Fecha de inicio del periodo requerido
    Parametro fecha_fin:  Fecha final del periodo requerido
    Return El DataFrame filtrado por el rango de fechas solicitado.
    """

# Creamos funcion 'generar_reporte'

def generar_reporte(df, filas, valores,columnas=None, medida='sum'):
    
    # Crear tabla pivote
    pivot_table = pd.pivot_table(df,
                                 index=filas,
                                 columns=columnas,
                                 values=valores,
                                 aggfunc=medida,
                                 fill_value=0)
    pivot_table = pivot_table[valores]
    return pivot_table

"""
    Genera un reporte pivotado.

    Parametro df: DataFrame de entrada.
    Parametro filas: Las filas requeridas de las columnas necesarias .
    Parametro columnas: Las columnas que se utilizarán como columnas la tabla pivote.
    Parametro valores: Las columnas que se utilizarán como valores en el tabla pivote.
    Parametro medida: La función de agregación a aplicar sobre los valores.
    Parametro: Un DataFrame con la tabla pivote aplicada.
    """

# Definir funcion 'escribir_en_base_de_datos'

def escribir_en_base_de_datos(df, nombre_tabla, engine, if_exists='replace'):
    """
    Escribe un DataFrame en una tabla de una base de datos.

    :param df: El DataFrame que se quiere escribir en la base de datos.
    :param nombre_tabla: El nombre de la tabla en la que se desea escribir.
    :param engine: El objeto Engine de SQLAlchemy para la conexión a la base de datos.
    :param if_exists: Comportamiento en caso de que la tabla ya exista ('fail', 'replace', 'append').
                      Por defecto, 'fail' (falla si la tabla ya existe).
    """
    try:
        
        # Escribir el DataFrame en la base de datos
        
        df.to_sql(nombre_tabla, con=engine, if_exists=if_exists, index=False)
        print(f"Datos escritos correctamente en la tabla '{nombre_tabla}'.")
    except Exception as e:
        print(f"Error al escribir datos en la tabla '{nombre_tabla}': {str(e)}")
