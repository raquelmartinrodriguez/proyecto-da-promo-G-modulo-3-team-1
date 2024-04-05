import pandas as pd

from src import database as db
from src import queries_database as query

#%%
df_sql = pd.read_csv('../files/df_to_SQL.csv')

#%%
df_sql = db.limpieza_especifica_sql(df_sql)

#%%
db.creacion_tablas_esquema(query.creacion_esquema , 'AlumnaAdalab', 'ABC_Corporation')

#%%
db.creacion_tablas_esquema(query.crear_tabla_employee, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_employee_details, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_surveys, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_supervisor_surveys, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_employment_gen, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_employment_teams, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_employment_exp, 'AlumnaAdalab')
#%%
db.creacion_tablas_esquema(query.crear_tabla_salary, 'AlumnaAdalab')

#%%
tuplas_employee = list(set(zip(df_sql['EmployeeID'] , df_sql['DateBirth'] , df_sql['Gender'] , df_sql['MaritalStatus'] , df_sql['NumberChildren'])))
tuplas_employee_details = list(set(zip(df_sql['EmployeeID'] , df_sql['Education'] , df_sql['EducationField'] , df_sql['NumCompaniesWorked'] , df_sql['TotalWorkingYears'])))
tuplas_surveys = list(zip(df_sql['EmployeeID'] , df_sql['EnvironmentSatisfaction'] , df_sql['JobSatisfaction'] , df_sql['RelationshipSatisfaction'] , df_sql['OverallSatisfaction']))
tuplas_supervisor_surveys = list(zip(df_sql['EmployeeID'] , df_sql['JobInvolvement'] , df_sql['PerformanceRating']))
tuplas_employment_gen = list(zip(df_sql['EmployeeID'] , df_sql['Attrition'] , df_sql['OverTime'] , df_sql['DistanceFromHome'] , df_sql['RemoteWork'], df_sql['BusinessTravel'], df_sql['TrainingTimesLastYear']))
tuplas_employment_teams = list(zip(df_sql['EmployeeID'] , df_sql['Department'] , df_sql['JobRole'] , df_sql['JobLevel']))
tuplas_employment_exp = list(zip(df_sql['EmployeeID'] , df_sql['YearsAtCompany'] , df_sql['YearsSinceLastPromotion'] , df_sql['YearsInCurrentRole'] , df_sql['YearsWithCurrManager']))
tuplas_salary = list(zip(df_sql['EmployeeID'] , df_sql['HourlyRate'] , df_sql['DailyRate'] , df_sql['MonthlyRate'] , df_sql['MonthlyIncome'], df_sql['PercentSalaryHike'], df_sql['StockOptionLevel']))

#%%
db.insertar_datos(query.insertar_employee, 'AlumnaAdalab', 'ABC_Corporation', tuplas_employee)
#%%
db.insertar_datos(query.insertar_employee_details, 'AlumnaAdalab', 'ABC_Corporation', tuplas_employee_details)
#%%
db.insertar_datos(query.insertar_surveys, 'AlumnaAdalab', 'ABC_Corporation', tuplas_surveys)
#%%
db.insertar_datos(query.insertar_supervisor_surveys, 'AlumnaAdalab', 'ABC_Corporation', tuplas_supervisor_surveys)
#%%
db.insertar_datos(query.insertar_employment_gen, 'AlumnaAdalab', 'ABC_Corporation', tuplas_employment_gen)
#%%
db.insertar_datos(query.insertar_employment_teams, 'AlumnaAdalab', 'ABC_Corporation', tuplas_employment_teams)
#%%
db.insertar_datos(query.insertar_employment_exp, 'AlumnaAdalab', 'ABC_Corporation', tuplas_employment_exp)
#%%
db.insertar_datos(query.insertar_salary, 'AlumnaAdalab', 'ABC_Corporation', tuplas_salary)