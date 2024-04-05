creacion_esquema = "CREATE SCHEMA IF NOT EXISTS `ABC_Corporation`;"

crear_tabla_employee = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`Employee` (
                EmployeeID VARCHAR(50) PRIMARY KEY,
                DateBirth INT,
                Gender VARCHAR(50),
                MaritalStatus VARCHAR(255),
                NumberChildren INT
            )
            """

insertar_employee = "INSERT INTO Employee (EmployeeID, DateBirth, Gender, MaritalStatus, NumberChildren) VALUES (%s, %s, %s, %s, %s)"
            
crear_tabla_employee_details = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`EmployeeDetails` (
                EmployeeID VARCHAR(50) PRIMARY KEY,
                Education INT,
                EducationField VARCHAR(255),
                NumCompaniesWorked INT,
                TotalWorkingYears INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            )
            """

insertar_employee_details = "INSERT INTO EmployeeDetails (EmployeeID, Education, EducationField, NumCompaniesWorked, TotalWorkingYears) VALUES (%s, %s, %s, %s, %s)"
              
crear_tabla_surveys = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`Surveys` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                EnvironmentSatisfaction INT,
                JobSatisfaction INT,
                RelationshipSatisfaction INT,
                OverallSatisfaction INT,
                WorkLifeBalance INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """
            
insertar_surveys = "INSERT INTO Surveys (EmployeeID, EnvironmentSatisfaction, JobSatisfaction, RelationshipSatisfaction, OverallSatisfaction, WorkLifeBalance) VALUES (%s, %s, %s, %s, %s, %s)"
            
crear_tabla_supervisor_surveys = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`SupervisorSurveys` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                JobInvolvement INT,
                PerformanceRating INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """
            
insertar_supervisor_surveys = "INSERT INTO SupervisorSurveys (EmployeeID, JobInvolvement, PerformanceRating) VALUES (%s, %s, %s)"
           
crear_tabla_employment_gen = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`EmploymentGeneral` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                Attrition VARCHAR(50),
                OverTime VARCHAR(50),
                DistanceFromHome INT,
                RemoteWork VARCHAR(50),
                BusinessTravel VARCHAR(255),
                TrainingTimesLastYear INT,
                StandardHours FLOAT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """

insertar_employment_gen = "INSERT INTO EmploymentGeneral (EmployeeID, Attrition, OverTime, DistanceFromHome, RemoteWork, BusinessTravel, TrainingTimesLastYear, StandardHours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

crear_tabla_employment_teams = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`EmploymentTeams` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                Department VARCHAR(255),
                JobRole VARCHAR(255),
                JobLevel INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """
            
insertar_employment_teams = "INSERT INTO EmploymentTeams (EmployeeID, Department, JobRole, JobLevel) VALUES (%s, %s, %s, %s)"
            
crear_tabla_employment_exp = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`EmploymentExperience` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                YearsAtCompany INT,
                YearsSinceLastPromotion INT,
                YearsInCurrentRole INT,
                YearsWithCurrManager INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """

insertar_employment_exp = "INSERT INTO EmploymentExperience (EmployeeID, YearsAtCompany, YearsSinceLastPromotion, YearsInCurrentRole, YearsWithCurrManager) VALUES (%s, %s, %s, %s, %s)"
            
crear_tabla_salary = """
            CREATE TABLE IF NOT EXISTS `ABC_Corporation`.`SalaryDetails` (
                RecordID INT AUTO_INCREMENT PRIMARY KEY,
                RecordDate DATE,
                EmployeeID VARCHAR(50),
                HourlyRate FLOAT,
                DailyRate FLOAT,
                MonthlyRate FLOAT,
                MonthlyIncome FLOAT,
                PercentSalaryHike FLOAT,
                StockOptionLevel INT,
                FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
            ) AUTO_INCREMENT=0
            """
            
insertar_salary = "INSERT INTO EmploymentGeneral (EmployeeID, HourlyRate, DailyRate, MonthlyRate, MonthlyIncome, PercentSalaryHike, StockOptionLevel) VALUES (%s, %s, %s, %s, %s, %s, %s)"