# Propuestas de tablas

## Employee
- EmployeeID (PK)
- Age
- AgeGroup // Propuesta de nueva columna para agrupar las distintas edades, por ejemplo: <30 / 30-40 / 41-50 / >50
- Gender
- MaritalStatus
- NumberChildren
- DateBirth
- Over18

## EmployeeDetails
- EmployeeID (FK)
- Education
- EducationField
- NumCompaniesWorked
- TotalWorkingYears

## Surveys
- EmployeeID (FK)
- EnvironmentSatisfaction
- JobSatisfaction
- RelationshipSatisfaction
- OverallSatisfaction // Propuesta de nueva columna combinando las tres anteriores
- WorkLifeBalance

## SurveysSupervisor
- JobInvolvement
- PerformanceRating


## EmploymentGeneral
- EmployeeID (FK)
- Attrition
- OverTime
- DistanceFromHome
- RemoteWork
- BusinessTravel
- TrainingTimesLastYear

## EmploymentTeams
- EmployeeID (FK)
- Department
- JobRole
- JobLevel

## EmploymentExperience
- EmployeeID (FK)
- YearsAtCompany
- YearsSinceLastPromotion
- YearsInCurrentRole
- YearsWithCurrentManager

## SalaryDetails
- EmployeeID (FK)
- HourlyRate
- DailyRate
- MonthlyRate
- MonthlyIncome
- VSAverageSalary // Propuesta de nueva columna para revisar si los ingresos están por encima (o por debajo) de la media
- PercentSalaryHike
- StockOptionLevel

## CompanyStandards
- Salary 
- AverageSalary // Propuesta de nueva columna para hacer la media de ingresos de los empleados
- StandardHours


# Propuestas de estilo
- Usar el inglés como idioma vehicular en las tablas y sus datos
- Cambiar el género por Male - Female
- Poner los nombres de las columnas con la primera letra de cada palabra en mayúscula
- Poner todos aquellos datos que sean string con la primera letra de cada palabra en mayúscula
- Siempre que una columna de datos pueda ser representada por un número, dar prioridad al valor numérico
- Convertir a integer los datos numéricos siempre y cuando no tengan decimales representativos
- No emplear símbolos (como "$" o "%") en los datos
- Cambiar nan, NaN, NAN por None
- Eliminar los espacios en blanco al principio y final de cada celda
- Mantener los resultados de satisfacción del 1 al 4 en beneficio del análisis de datos y estadística
- Cambiar todos aquellos datos que sean True-False o Yes-No por 1 (true/yes) 0 (false/no) en beneficio del análisis de datos y estadística
