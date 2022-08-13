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


def getURL(url):
    return req.get(url)


def saveFile(archive_name, url):
    with open(archive_name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in getURL(url).iter_lines():
            writer.writerow(line.decode('utf-8').split(','))


def createFolder(path):
    os.makedirs(path, exist_ok=True)


def setFoldersAndFiles(category):
    fullDate = x.strftime(category+'-%d-%m-%Y')
    monthName = x.strftime('%Y-%B')
    fullNameFile = f'.\{category}\{monthName}'
    createFolder(fullNameFile)
    saveFile(fullDate, category)


print(categories(0))

# Tiene que decir “museos\2021-noviembre\museos-03-11-2021”

# saveFile('museum.csv', museum)
# saveFile('cinema.csv', cinema)
# saveFile('popular_libraries.csv', popularLibraries)
