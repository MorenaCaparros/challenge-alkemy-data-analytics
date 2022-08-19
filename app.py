from tkinter.messagebox import NO
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
def getURL(url):
    return req.get(url)


def saveCSVFile(archive_name, url):
    with open(archive_name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in url.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))


def createFolder(path):
    os.makedirs(path, exist_ok=True)

    
def convertCSVToDataFrame(csv):
    df = pd.read_csv(csv, on_bad_lines='skip')
    return df

def setFoldersAndFiles(category):
    global dfLibrary
    global dfMuseum
    global dfCinema
    
    fullDate = x.strftime(category+'-%d-%m-%Y')
    monthName = x.strftime('%Y-%B')
    archiveName = f'.\{category}\{monthName}\{fullDate}.csv'
    fullNameFile = f'.\{category}\{monthName}'
    createFolder(fullNameFile)
    
    for key in categories:
        if (key == category):
            valueCategory = categories[key]
            saveCSVFile(archiveName, getURL(valueCategory))

    if category == 'museos':
        # temp_lines = archiveName.readline() + '\n' + archiveName.readline()
        # dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')
        # archiveName.seek(0) 
        dfMuseum = convertCSVToDataFrame(archiveName)
    elif category == 'salas_de_cine':
        # temp_lines = archiveName.readline() + '\n' + archiveName.readline()
        # dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')
        # archiveName.seek(0) 
        dfCinema = convertCSVToDataFrame(archiveName) 
    elif category == 'bibliotecas_populares':
        # temp_lines = archiveName.readline() + '\n' + archiveName.readline()
        # dialect = csv.Sniffer().sniff(temp_lines, delimiters=';,')
        # archiveName.seek(0) 
        dfLibrary = convertCSVToDataFrame(archiveName)
   
for key in categories:
    setFoldersAndFiles(key)

# Depuracion de datos
columnsNamesM = list(dfMuseum.columns.values)
columnsNamesL = list(dfLibrary.columns.values)
columnsNamesC = list(dfCinema.columns.values)

##
# ['Cod_Loc' 'IdProvincia' 'IdDepartamento' 'Observaciones' 'categoria'
#  'subcategoria' 'provincia' 'localidad' 'nombre' 'direccion' 'piso' 'CP'
#  'cod_area' 'telefono' 'Mail' 'Web' 'Latitud' 'Longitud'
#  'TipoLatitudLongitud' 'Info_adicional' 'fuente' 'jurisdiccion'
#  'año_inauguracion' 'actualizacion']
# ['Cod_Loc' 'IdProvincia' 'IdDepartamento' 'Observacion' 'Categoría'
#  'Subcategoria' 'Provincia' 'Departamento' 'Localidad' 'Nombre'
#  'Domicilio' 'Piso' 'CP' 'Cod_tel' 'Teléfono' 'Mail' 'Web'
#  'Información adicional' 'Latitud' 'Longitud' 'TipoLatitudLongitud'
#  'Fuente' 'Tipo_gestion' 'año_inicio' 'Año_actualizacion']
# ['Cod_Loc' 'IdProvincia' 'IdDepartamento' 'Observaciones' 'Categoría'
#  'Provincia' 'Departamento' 'Localidad' 'Nombre' 'Dirección' 'Piso' 'CP'
#  'cod_area' 'Teléfono' 'Mail' 'Web' 'Información adicional' 'Latitud'
#  'Longitud' 'TipoLatitudLongitud' 'Fuente' 'tipo_gestion' 'Pantallas'
#  'Butacas' 'espacio_INCAA' 'año_actualizacion']
##
dfFilteredMuseum = dfMuseum[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP', 'Mail', 'Web']]
dfFilteredMuseum.insert(9,'numero de telefono',(dfMuseum['cod_area'].astype(str) + '-' + dfMuseum['telefono'].astype(str)), allow_duplicates=False)
#dfFilteredMuseum['numero de telefono'] = dfMuseum['cod_area'] + '' + dfMuseum['telefono']
# x = str(dfMuseum['telefono'])
# print(str(dfMuseum['cod_area']).cat(x))
# dfFilteredLibrary = dfLibrary[columnsNamesL]
# dfFilteredCinema = dfCinema[columnsNamesC]
print (dfMuseum['cod_area'].astype(str(int)))
pd.set_option('display.max_rows', None, 'display.max_columns', None)
#print(dfFilteredMuseum['numero de telefono'])
# print(columnsNamesL)
#print(dfFilteredMuseum['numero de telefono'])
 


# dfMuseumFiltered = dfMuseum[['']]


###############

# titulos que necesito:
#cod_localidad; id_provincia; id_departamento; categoría; provincia;
# localidad; nombre; domicilio; código postal; número de teléfono; mail; web
##
# titulos que tengo


