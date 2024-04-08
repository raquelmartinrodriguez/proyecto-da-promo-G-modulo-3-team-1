class limpieza_employment(df, columna_unif,numero_pos):
    def __init__(self):
    self.columna_unif= columna_unif
    self.numero_pos = numeros

    def binary_unification(columna_unif):

    # diccionario de mapeo
    mapping = {'Yes': 1, 'No': 0, 'False': 0, 'True': 1}

    # replace en funcion del diccionario
    columna_unif = columna_unif.replace(mapping)

    # gestion de posibles errores 
    columna_unif = pd.to_numeric(columna_unif, errors='coerce')

    return columna_unif

    #conv a positivo
    #conv astype 

    return df

class limpieza_salary(df, columnas, mapa):
    def __init__(self):
        df.self = self

        def salary_details(df, columnas):
            return salary_details == data.loc[: , columnas]
        
        def unification(df, columnas):
            
            for columna in columnas: 
                # Reemplaza las strings de 'nan' por valores NaN en DAILYRATE
            return df[columna] = df[columna].replace({'nan$': float('NaN')})

            # Reemplaza las ',' por '.' en MONTHLYINCOME
            return df[columna] = df[columna].str.replace(',' , '.')

            # Reemplaza las strings de 'Not Available' por valores NaN
        def mapeo(df, map, columna):    
           
           return  df[columna] = df[columna].replace(map)
    return df

class surveys(df,columnas, numero):
    def __init__(self):
        df.self = self
    
    def surveys(df, columnas):
            return surveys == data.loc[: , columnas]
    
    def nueva_satisfaccion(df, columnas):
        for columna in columnas: 
            if columna.values().unique() > 4:
                try:

                    nueva_valor = ((valor - 1) * 4) // 49 + 1
                    nueva_satisfaccion.append(nueva_valor)

                    return (nueva_satisfaccion)
        
                except:
                    pass
    def categorizar_environment(numero):
    
        if numero == 1:
            return 1
        
        elif numero == 2:
            return 2
        
        elif numero == 3:
            return 3
        
        elif numero == 4:
            return 4
        
        elif numero >= 5 and numero <= 14:
            return 1
        
        elif numero >= 15 and numero <= 25:
            return 2

        elif numero >= 26 and numero <= 35:
            return 3
        
        else:
            return 4
        
     def unification(df, columnas):
            
            for columna in columnas: 
                # Reemplaza las strings de 'nan' por valores NaN en DAILYRATE
            return df[columna] = df[columna].replace({'nan$': float('NaN')})

            # Reemplaza las ',' por '.' en MONTHLYINCOME
            return df[columna] = df[columna].str.replace(',' , '.')
    
    return df

class employees(df, columnas, mapa):
        __def__


        def employees(df, columnas):
            
            return employees == data.loc[: , columnas]
        
        def mapeo(df, map, columna):    
           
           return  df[columna] == df[columna].replace(map)
        
        ## int 

        return df
        
