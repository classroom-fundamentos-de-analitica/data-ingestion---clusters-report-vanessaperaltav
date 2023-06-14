"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    filename = 'clusters_report.txt'
    with open(filename, mode='r') as clusters_report:
        report = clusters_report.readlines()

    clusters = []
    cluster = [0, 0, 0, '']

    for fila in report[4:]:
        if re.match('^ +[0-9]+ +', fila):
            lista = fila.split()
            cluster = [int(lista[0]), int(lista[1]), float(lista[2].replace(',', '.')), ' '.join(lista[4:])]

        elif re.match('^ +[a-z]', fila):
            palabras = ' '.join(fila.split())
            cluster[3] += ' ' + palabras

        elif re.match('^\n|^\s*$', fila):
            cluster[3] = cluster[3].replace('.', '')
            clusters.append(cluster)
            cluster = [0, 0, 0, '']

    df = pd.DataFrame(clusters, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    return df
