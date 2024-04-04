# LIBRERÍAS NECESARIAS

# Tratamiento de datos
import pandas as pd
import numpy as np
import re


def apertura_y_exploracion(ruta):
    
    """
    Esta función carga un archivo CSV ubicado en la ruta especificada y realiza una exploración básica del mismo.

    Parámetros:
    ruta (str): La ruta del archivo CSV a cargar.

    Devoluciones:
    DataFrame: El DataFrame cargado desde el archivo CSV.

    Esta función carga el archivo CSV especificado en 'ruta', elimina la columna 'Unnamed: 0' si existe,
    e imprime información sobre la forma, columnas, tipos de datos, valores nulos, duplicados, valores duplicados 
    de cada columna, valores únicos de cada columna, y realiza un resumen estadístico para las columnas numéricas 
    y categóricas. Finalmente, devuelve el DataFrame cargado.
    """
    
    df = pd.read_csv(ruta)

    # Si al cargar el dataframe se creó una columna de unnamed, la elimina
    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis = 1, inplace=True)
       
    print(f"INFORMACIÓN SOBRE EL DATAFRAME")
    print(f"---La forma:")
    print(f"{df.shape}\n")
    print(f"---Las columnas:")
    print(f"{df.columns}\n")
    print(f"---Los tipos de datos:")
    print(f"{df.dtypes}\n")
    print(f"---Los nulos:")
    print(f"{df.isnull().sum()/df.shape[0] * 100}\n")
    print(f"---Los duplicados:")
    print(f"{df.duplicated().sum()}\n")
    print(f"---Los valores (y su total) de cada columna:")
    for columna in df.columns:
        print(f"-------{columna.upper()}")
        print(f"{df[columna].value_counts()}\n")
    print(f"---Los principales estadísticos para las columnas numéricas:")
    display(df.describe().T)
    print(f"---Los principales estadísticos para las columnas categóricas:")
    display(df.describe(include=['object']).T)
    
    return df