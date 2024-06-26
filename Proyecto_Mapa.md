## Mapa del proyecto

Nombre equipo: Hasta numpy

Scrum Master 1: Marina
Scrum Master 2: Maite
Scrum Master Final: Patri

### Fase 1: Exploración
**Exploración inicial**:
- Ruta de archivo: `notebooks/01-exploration/exploracion.ipynb`
- Descripción: Jupyter con el desglose de los datos del CSV base del proyecto (`files/HR RAW DATA.csv`)

**Exploración detallada**:
- Ruta de los archivos: `notebooks/01-exploration`
- Descripción: Archivos Jupyter con análisis exploratorio más detallado, separado según las tablas a generar en BBDD

### Fase 2: Limpieza
- Ruta de los archivos: `notebooks/02-transformation`
- Descripción: Archivos Jupyter con la primera limpieza de los datos, separados según las tablas a generar en BBDD

**Criterios de unificación y limpieza**:
- Todos aquellos datos "True/False" "Yes/No" "1/0" pasarlos a int 1,0
- Cambiar el género por Male - Female
- Todos los elementos string en .lower()
- Siempre que una columna de datos pueda ser representada por un número, dar prioridad al valor numérico
- Convertir a integer los datos numéricos siempre y cuando no tengan decimales representativos
- Si nan es una string, cambiarlo a nulo ('nan': float('NaN'))
- Quitar símbolos (como "$" o "%") en los datos y reemplazar "," por "."
- Eliminar los espacios en blanco al principio y final de cada celda (.strip())
- Usar el inglés como idioma vehicular en las tablas y sus datos
- No reordenar las filas
- No eliminar filas
- Revisar que los strings no estén escritos de forma distinta ('married' - 'merried'), faltas de ortografía, etc (unificar los unique)

**Una vez unifiquemos**:
- A la hora de tomar la decisión de eliminar una columna justificar el motivo por el que se prescinde de ella (y revisar si aún así es salvable para la BBDD)

**Columnas a las que imputamos nulos**
- Marital Status: Tiene un 40% de nulos. Hemos intentado sacar una moda concluyente de los datos, pero no hay una que sea determinante (married 27%, single 20%, divorced 12%). Imputaremos los nulos como "Unknown". **Next Steps:** Recomendar al cliente obtener más información sobre esta columna
- EducationField: Tiene un 46% de nulos. Hemos intentado sacar una moda concluyente de los datos, pero no hay una que sea determinante. Imputaremos los nulos como "Unknown". **Next Steps:** Recomendar al cliente obtener más información sobre esta columna
- TotalWorkingYears: Tiene un 32% de nulos. Probar con Iterative vs KNN Imputer
- WorkLifeBalance: 6,5%
- PerformanceRating: 12,09%
- OverTime: 41,8%
- BusinessTravel: 47,85%
- DailyRate: 7,67%
- HourlyRate: 5,37%

**Columnas que no analizaremos**
- NumberChildren: Por ser una columna que no contiene ni un solo dato.
- Over18: Además de su alto valor de nulos, creemos que al tener una columna de Edad (Age) esta columna podría resultar redundante
- YearsInCurrentRole: Tiene un 97% de nulos
- Department: Tiene un 81% de nulos
- StandardHours: Tiene un 73% de nulos
- MonthlyIncome: Tiene un 52% de nulos y podemos utilizar HourlyRate (que no llega a 6% de nulos) para estimar las ganancias de los empleados de un modo más fiable
