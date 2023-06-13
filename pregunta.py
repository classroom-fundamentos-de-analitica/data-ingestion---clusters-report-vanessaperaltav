"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    import re

    i = 0
    dict_linea = {}
    df = pd.DataFrame()
    with open('./clusters_report.txt') as f:
        for line in f:

            line = re.sub(r"\s+", " ", line)
            if len(line)>1 and i > 3:
                if line.split()[0].isnumeric() == True:
                    try: 
                        dict_linea['principales_palabras_clave'] = ' '.join(dict_linea['principales_palabras_clave'])
                        df = df.append(dict_linea, ignore_index=True)
                    except: pass
                    dict_linea = {'cluster': int(line.split()[0]),
                                'cantidad_de_palabras_clave': int(line.split()[1]),
                                'porcentaje_de_palabras_clave': float(line.split()[2].replace(',','.')),
                                'principales_palabras_clave': line.split()[4:]}
                else: 
                    dict_linea['principales_palabras_clave'].append(' '.join(line.split()))
            i += 1
    dict_linea['principales_palabras_clave'] = ' '.join(dict_linea['principales_palabras_clave'])
    df = df.append(dict_linea, ignore_index=True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('\.')
    
    return df
