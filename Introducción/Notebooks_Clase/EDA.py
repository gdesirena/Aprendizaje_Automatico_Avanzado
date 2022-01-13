import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt

class EDA:
    
    def dqr(data):
        # lista de variables de la base de datos
        columns = pd.DataFrame(list(data.columns.values), columns = ['Nombres Columnas'],
                               index = list(data.columns.values))
        #Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns=['Tipo de Dato'])

        #Lista de valores nullos
        missing_values = pd.DataFrame(data.isnull().sum(), columns=['Valores nullos'])

        #Lista de valores unicos
        unique_values = pd.DataFrame(columns=['Valores unicos'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]

        #promedio de los valores numéricos
        mean_values = pd.DataFrame(columns=['promedio'])
        for col in list(data.columns.values):
            try:
                mean_values.loc[col] = [data[col].mean()]
            except:
                pass
        #minimo de los valores numériocos
        min_values = pd.DataFrame(columns=['min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
        #maximo de los valores numéricos
        max_values = pd.DataFrame(columns=['max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
        #columna que se llame categórica (booleano) cuando sea una variable categóirica (True)
        categorical = pd.DataFrame(columns=['categorical'])
        for col in list(data.columns.values):
            if data[col].dtype=='object':
                categorical.loc[col]=True
            else:
                categorical.loc[col]=False
        #si la variable es categórica entonces agregar los valores únicos de esa variable
        #(los valores unicos no mayores a 10)
        categorical_unique = pd.DataFrame(columns=['categorical unique'])
        for col in list(data.columns.values):
            if data[col].dtype=='object':
                if data[col].nunique() <= 10:
                    categorical_unique.loc[col] = [data[col].unique()]
                else:
                    categorical_unique.loc[col] = ['more than 10']
            else:
                categorical_unique.loc[col] = None


        return columns.join(data_types).join(missing_values).join(unique_values).join(mean_values).join(min_values).join(max_values).join(categorical).join(categorical_unique)
