# Librerías necesarias ------------------------------------------------

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------

def limpieza_datos (df):
    
    lista_columnas_explorar = ['Age', 'Gender','MaritalStatus', 'NUMBERCHILDREN','DateBirth', 'Over18', 'Education','EducationField', 'NUMCOMPANIESWORKED', 'TOTALWORKINGYEARS']

    df_exploracion = df.loc[:,lista_columnas_explorar]
    diccionario_edades = {
        'forty-seven':47,
        'fifty-eight': 58,
        'thirty-six': 36,
        'fifty-five': 55, 
        'fifty-two': 52,
        'thirty-one': 31,
        'thirty': 30,
        'twenty-six': 26, 
        'thirty-seven' : 37, 
        'thirty-two': 32,
        'twenty-four' : 24
        }                   
    df_exploracion["Age"] = df_exploracion["Age"].replace(diccionario_edades)
    df_exploracion["Age"] = df_exploracion["Age"].astype('Int64', errors="ignore")
    df_exploracion["Gender"].replace(to_replace=[0,1],value= ["Male","Female"],inplace=True)
    df_exploracion['MaritalStatus'].replace(to_replace=['Marreid','divorced'],value= ['Married','Divorced'],inplace=True)
    df_exploracion["DateBirth"] = df_exploracion["DateBirth"].astype('Int64', errors="ignore")
    df_exploracion['TOTALWORKINGYEARS'] = df_exploracion['TOTALWORKINGYEARS'].apply (lambda x: float(x.replace(',','.') if isinstance(x,str) else np.nan))
    df_exploracion['TOTALWORKINGYEARS'] = df_exploracion['TOTALWORKINGYEARS'].astype('Int64', errors = 'ignore')
    
    
    columnas_patri = ["Attrition", "OverTime", "DistanceFromHome", "RemoteWork", "BusinessTravel", "TrainingTimesLastYear", "Department", "JobRole", "JobLevel"]
    df_patri = df.loc[:,columnas_patri]
    df_patri['RemoteWork'] = df_patri['RemoteWork'].apply(lambda x : 1 if x == "Yes" or x == "True" else x)
    df_patri['RemoteWork'] = df_patri['RemoteWork'].apply(lambda x : 0 if x == "No" or x == "False" else x)
    df_patri["JobRole"] = df_patri["JobRole"].str.lower()
    df_patri["DistanceFromHome"] = df_patri["DistanceFromHome"].apply(lambda x : np.abs(x) if x < 0 else x)
    df_patri['OverTime'] = df_patri['OverTime'].apply(lambda x: 1 if x == 'Yes' else (0 if x == 'No' else np.nan))
    df_patri ['OverTime'] = df_patri['OverTime'].astype('Int64', errors = 'ignore')
    
    salary_details = df.loc[: , ['DailyRate', 'HourlyRate' , 'MonthlyRate' , 'MonthlyIncome' , 'PercentSalaryHike' , 'StockOptionLevel']]
    salary_details['DailyRate'] = salary_details['DailyRate'].replace({'nan$': float('NaN')})
    dict_remplazo = {'\$' : '' , ',' : '.'}
    salary_details['DailyRate'] = salary_details['DailyRate'].replace(dict_remplazo , regex=True)
    salary_details['MonthlyIncome'] = salary_details['MonthlyIncome'].str.replace(',' , '.')
    salary_details['HourlyRate'] = salary_details['HourlyRate'].replace({'Not Available': float('NaN')})
    for columna in salary_details.columns:
        salary_details[columna] = pd.to_numeric(salary_details[columna], errors='coerce', downcast='float')
    integers = ['StockOptionLevel' , 'PercentSalaryHike']
    for columna in integers:
        salary_details[columna] = salary_details[columna].astype('int64', errors='ignore')


    surveys = df.loc [:, ['EnvironmentSatisfaction', 'JobSatisfaction', 'RelationshipSatisfaction', 'WORKLIFEBALANCE', 'JobInvolvement', 'PerformanceRating' ]]
    categorizar_environment_lambda = lambda numero: 1 if numero == 1 else (2 if numero == 2 else (3 if numero == 3 else (4 if numero == 4 else (1 if numero >= 5 and numero <= 14 else (2 if numero >= 15 and numero <= 25 else (3 if numero >= 26 and numero <= 35 else 4))))))
    surveys['EnvironmentSatisfaction'] = surveys['EnvironmentSatisfaction'].apply(categorizar_environment_lambda)
    surveys['WORKLIFEBALANCE'] = surveys['WORKLIFEBALANCE'].str.replace(',', '.').astype(float).fillna(np.nan)
    surveys['WORKLIFEBALANCE'] = surveys['WORKLIFEBALANCE'].astype('Int64')
    surveys['PerformanceRating'] = surveys['PerformanceRating'].str.replace(',', '.').astype(float).fillna(np.nan)
    surveys['PerformanceRating'] = surveys['PerformanceRating'].astype('Int64')
    
    
    employee_experience= df.loc[: , ['YearsAtCompany','YearsInCurrentRole', 'YearsSinceLastPromotion','YEARSWITHCURRMANAGER']]
    employee_experience['YearsInCurrentRole'] = employee_experience['YearsInCurrentRole'].str.replace(',' , '.')
    employee_experience['YearsInCurrentRole'] = pd.to_numeric(employee_experience['YearsInCurrentRole'], errors='coerce', downcast='float')
    employee_experience['YearsInCurrentRole'] = employee_experience['YearsInCurrentRole'].astype('Int64', errors='ignore')
    integers= ['YearsInCurrentRole']
    for columna in integers:
        #convierte los valores de la columna a enteros
        #mantiene los valores NaN con NaN 
        employee_experience[columna] = employee_experience[columna].astype('Int64', errors= 'ignore')
        
        
    salary= df.loc[: , ["Salary", "StandardHours"]]
    salary["Salary"] = salary["Salary"].str.replace('\$$', '', regex=True)
    salary['StandardHours'] = salary['StandardHours'].str.replace(',' , '.')
    salary['StandardHours'] = pd.to_numeric(salary['StandardHours'], errors='coerce', downcast='float')
    salary['StandardHours'] = salary['StandardHours'].astype('Int64', errors='ignore')
    integers_STH= ['StandardHours']
    for columna in integers_STH:
        #convierte los valores de la columna a enteros
        #mantiene los valores NaN con NaN 
        salary[columna] = salary[columna].astype('Int64', errors= 'ignore')

    df_limpio = pd.concat([df['employeenumber'], df_exploracion, employee_experience, surveys, df_patri, salary_details, salary], axis = 1, ignore_index = False)
    
    return df_limpio

def transformacion_datos(df):
    
    df_limpio = df
    
    nuevas_columnas = {'employeenumber' : 'EmployeeID' , 'NUMBERCHILDREN' : 'NumberChildren' , 'NUMCOMPANIESWORKED' : 'NumCompaniesWorked', 'TOTALWORKINGYEARS' : 'TotalWorkingYears' , 'YEARSWITHCURRMANAGER' : 'YearsWithCurrManager' , 'WORKLIFEBALANCE' : 'WorkLifeBalance'}
    
    df_limpio.rename(columns = nuevas_columnas, inplace = True)
    
    df_limpio = df_limpio.drop_duplicates(keep="first")
    
    df_limpio = df_limpio.reset_index()
    df_limpio.drop("index", axis=1, inplace=True)
    
    # Filtra las filas con valores nulos en 'EmployeeID'
    filas_nulas = df_limpio['EmployeeID'].isnull()
    df_filas_nulas = df_limpio[filas_nulas]

    # Excluye la columna 'RemoteWork' para buscar duplicados
    df_sin_remote = df_filas_nulas.drop(columns=['RemoteWork'])

    # Busca duplicados en las filas filtradas
    duplicados_sin_RW = df_sin_remote[df_sin_remote.duplicated(keep=False)]

    # Extrae los indices
    indices_duplicados = duplicados_sin_RW.index

    # Crea una lista de los indices con las coincidencias
    lista_indices_mismo_empleado = df_limpio.loc[indices_duplicados , :].sort_values(['Age' , 'Gender']).index
    
    # Función lambda para asignar un ID a los valores nulos
    asignar_id_lambda = lambda valor, contador: f'nan{contador[0]}' if pd.isnull(valor) else valor.replace(',0', '')

    # Función lambda para aplicar la asignación de ID a una columna
    aplicar_asignar_id_lambda = lambda columna: columna.apply(lambda x: asignar_id_lambda(x, contador))

    # Reiniciar el contador cada vez que se aplique la función
    contador = [0]

    # Aplicar la función lambda a la columna 'EmployeeID' y reasignar los resultados
    df_limpio['EmployeeID'] = aplicar_asignar_id_lambda(df_limpio['EmployeeID'])
    
    indice_sublista = 0

    for indice in lista_indices_mismo_empleado[1::2]:
        
        dato = lista_indices_mismo_empleado[indice_sublista]
        
        df_limpio['EmployeeID'][indice] = df_limpio['EmployeeID'][dato]
        
        indice_sublista += 2
    
    return df_limpio
        
        
def imputacion_nulos (df):
    
    df_limpio = df

    df_limpio.drop (['NumberChildren', 'Over18', 'YearsInCurrentRole', 'Department', 'StandardHours', 'MonthlyIncome'], axis =1, inplace =True)

    columnas_desconocido = ['MaritalStatus' , 'EducationField', 'BusinessTravel']
    
    # iteramos por la lista de columnas a las que le vamos a cambiar los nulos por "Uknown"
    for columna in columnas_desconocido:
        
        # reemplazamos los nulos por el valor Unknown para cada una de las columnas de la lista
        df_limpio[columna] = df_limpio[columna].fillna("Unknown")
        
    
    numericas = ['WorkLifeBalance', 'PerformanceRating', 'DailyRate', 'HourlyRate', 'TotalWorkingYears', 'OverTime']
    
    # hemos dicho que para las tres columnas restantes aplicaremos los dos métodos para luego compararlos, empezaremos por el IterativeImputer
    # instanciamos las clases
    imputer_iterative = IterativeImputer(max_iter = 20, random_state = 42)

    # ajustamos y tranformamos los datos
    imputer_iterative_imputado = imputer_iterative.fit_transform(df_limpio[numericas])

    # comprobamos que es lo que nos devuelve, que en este caso es un array también
    imputer_iterative_imputado
    
    return df_limpio