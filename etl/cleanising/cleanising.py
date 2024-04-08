#%%
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
# %%

def homogen_cols(diccionario, df):
    return df.rename(columns = diccionario, inplace = True)
# %%
def limpieza_duplicados(df):
    df = df.drop_duplicates(keep="first").reset_index()
    return df.drop("index", axis=1, inplace=True)
# %%
def asignar_id(valor, contador):
    
    if pd.isnull(valor):
        contador[0] += 1  # Incrementar el contador si el valor es NaN
        id_nulo = f'nan{contador[0]}'  # Devolver el ID con el contador actualizado
        return id_nulo
    
    else:
        return valor.replace(',0' , '')  # Devolver el valor quitándole los decimales

# Reiniciar el contador cada vez que se aplique la función
def aplicar_asignar_id(columna):
    contador = [0]
    return columna.apply(lambda x: asignar_id(x, contador))
# %%
def asignacion_mismo_id(lista, columna): #columna = df[columna] formato
    indice_sublista = 0
    for indice in lista[1::2]:
    
    dato = lista[indice_sublista]
    
    columna[indice] = columna[dato]
    
    indice_sublista += 2
# %%
def revision_nulos(df):
    print(f"El porcentaje nulos del {df} son: \n")
    (df.isnull().sum()/df.shape[0]) * 100  
# %%
def reemplazo_desconocido(df, columnas):
    for columna in columnas:
    
    # reemplazamos los nulos por el valor Unknown para cada una de las columnas de la lista
    df[columna] = df[columna].fillna("Unknown")
    
# comprobamos si quedan nulos en las columnas categóricas. 
    print("Después del reemplazo usando 'fillna' quedan los siguientes nulos:")
    df[columnas].isnull().sum()
    return df[columna]
# %%
def iterative(df, columnas):
    df_copy = df.copy()
    # hemos dicho que para las tres columnas restantes aplicaremos los dos métodos para luego compararlos, empezaremos por el IterativeImputer
    # instanciamos las clases
    imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)

    # ajustamos y tranformamos los datos
    imputer_iterative_imputado = imputer_iterative.fit_transform(df_copy[columnas])

    # comprobamos que es lo que nos devuelve, que en este caso es un array también
    return imputer_iterative_imputado
#%%
def estetica_df(df):
    df.columns= df.columns.str.replace(" ", "_")
    df.columns = df.columns.str.lower()

# %%
mapa_diccionario = {}

def binary_unification(columna, mapa_diccionario):

  # replace en funcion del diccionario
  columna = columna.replace(mapa_diccionario)

  # gestion de posibles errores 
  columna = pd.to_numeric(columna, errors='coerce')

  return columna
