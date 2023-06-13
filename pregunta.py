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

    # Leer el txt 
    with open('clusters_report.txt', 'r') as f:
        data = f.readlines()

    columns = []
    Lines12 = data[:2]

    line1 = re.split(r'([A-Z])' ,Lines12[0])
    line1 = line1[1:]
 
    for i in range((len(line1)//2)):
        line1[i] = line1[i] + line1[i+1]
        line1.pop(i+1)
        line1[i] = line1[i].lower()
        line1[i] = line1[i].strip()
        line1[i] = line1[i].replace(' ', '_')

    line2 = Lines12[1].split()
    line2 = [line2[i] + '_' + line2[i+1] for i in range(0, len(line2)-1, 2)]
    for i in range(len(line1)):
        if i == 1:
            line1[i] = line1[i] + "_"+ line2[i-1]
        if i == 2:
            line1[i] = line1[i] + "_"+ line2[i-1]

    columnas = line1

    info = data[2:]

    clusters = []
    cantidad_de_palabras_clave = []
    porcentaje_de_palabras_clave = []
    result = []
    for i in info:
        result.append(i.split())
        numbers = re.findall(r'\d+',i)
        if len(numbers) > 0:
            numbers[2] = float(str(numbers[2]) + '.' + str(numbers[3]))
            numbers.pop(3)

            clusters.append(int(numbers[0]))
            cantidad_de_palabras_clave.append(int(numbers[1]))
            porcentaje_de_palabras_clave.append(numbers[2])

        palabras = i.split()

        palabras_separada = []

        for elemento in palabras:
            if elemento != "[]":
                texto = elemento.strip("[]").replace("'", "").split(", ")
                palabras_separada.append(texto)
    listas_divididas = []
    sublista = []

    for lista in result:
        if lista:
            sublista.append(lista)
        else:
            if sublista:
                listas_divididas.append(sublista)
                sublista = []

    if sublista:
        listas_divididas.append(sublista)

    for i in range(len(listas_divididas)):
        if i == 0:
            listas_divididas[0] = listas_divididas[0][1:]
        listas_divididas[i][0] = listas_divididas[i][0][4:]

    lista_unida = []

    for i in range(len(listas_divididas)):

        for sublist in listas_divididas[i]:
            lista_unida += sublist

    totalString = (' '.join(lista_unida)).split(".")
    data = [0,0,0,'']
    cluster = []
    for i in range(len(clusters)):
        data[0] = clusters[i]
        data[1] = cantidad_de_palabras_clave[i]
        data[2] = porcentaje_de_palabras_clave[i]
        data[3] = totalString[i].strip()
        cluster.append(data)
        data = [0,0,0,'']

    df = pd.DataFrame (cluster, columns = columnas)

    return df
