import requests as req
import pandas as pd
import os
import csv
import datetime
import locale


locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # cambia el idioma
x = datetime.datetime.now()
categories = {'museos': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv', 'salas_de_cine': "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv",
              'bibliotecas_populares': "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"}

# Tener en cuenta que las urls pueden cambiar en un futuro
global df_library
global df_museum
global df_cinema


def getURL(url):
    return req.get(url)


def saveCSVFile(archive_name, url):
    with open(archive_name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in url.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))


def convertCSVToDataFrame(datafram, csv):
    datafram = pd.read_csv(csv)


def createFolder(path):
    os.makedirs(path, exist_ok=True)


def setFoldersAndFiles(category):
    fullDate = x.strftime(category+'-%d-%m-%Y')
    monthName = x.strftime('%Y-%B')
    archiveName = f'.\{category}\{monthName}\{fullDate}.csv'
    fullNameFile = f'.\{category}\{monthName}'
    createFolder(fullNameFile)
    for key in categories:
        if (key == category):
            valueCategory = categories[key]
            saveCSVFile(archiveName, getURL(valueCategory))


###############

# titulos que necesito:
#cod_localidad; id_provincia; id_departamento; categoría; provincia;
# localidad; nombre; domicilio; código postal; número de teléfono; mail; web
##
# titulos que tengo

# Hacer una lista que sea fileName y qeu se vaya pisando con los nuevos nombres de archivos
# def readAndNormalizeFiles(fileKey):
#     monthName = x.strftime('%Y-%B')
#     archiveName = f'./{fileKey}/{monthName}/{fullDate}.csv'
#     fullDate = x.strftime(fileKey+'-%d-%m-%Y')
#     with open(archiveName, 'r', encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         header = next(csv_reader)
#         print(header)


for key in categories:

    setFoldersAndFiles(key)
