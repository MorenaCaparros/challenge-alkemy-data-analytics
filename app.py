from tkinter.messagebox import NO
import requests as req
import pandas as pd
import os
import csv
import datetime
import locale

    


x = datetime.datetime.now()
categories = {'museos': 'https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA/export?format=csv', 'salas_de_cine': "https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM/export?format=csv",
              'bibliotecas_populares': "https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk/export?format=csv"}

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
        dfMuseum = convertCSVToDataFrame(archiveName)
    elif category == 'salas_de_cine':
        dfCinema = convertCSVToDataFrame(archiveName) 
    elif category == 'bibliotecas_populares':
        dfLibrary = convertCSVToDataFrame(archiveName)
   
for key in categories:
    setFoldersAndFiles(key)

# Uniendo Cod_area con el telefono y llenando los null
dfMuseum['cod_area'] = dfMuseum['cod_area'].fillna(0)
dfMuseum['telefono'] = dfMuseum['telefono'].fillna('s/d')

# Convirtiendo columnas del dfMuseum para poder concatenarlas despues
dfMuseum['cod_area'] = dfMuseum['cod_area'].astype(int).astype(str)
dfMuseum['telefono'] = dfMuseum['telefono'].astype(str)

#Concatenacion de las columnas cod_area + telefono en una nueva columna: telefono_completo
dfLibrary['telefono_completo'] = dfLibrary.Cod_tel.str.cat(dfLibrary.Teléfono)
dfMuseum['telefono_completo'] =  dfMuseum['cod_area'].str.cat(dfMuseum.telefono).str.replace(' ',  '')
dfCinema['telefono_completo']  = dfCinema.cod_area.str.cat(dfCinema.Teléfono)

#depuracion de datos
dfLibraryMapped = dfLibrary[['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Domicilio','CP','telefono_completo','Mail','Web']]
dfMuseumMapped = dfMuseum[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','direccion','CP','telefono_completo','Mail','Web']]
dfCinemaMapped = dfCinema[['Cod_Loc','IdProvincia','IdDepartamento','Categoría','Provincia','Localidad','Nombre','Dirección','CP','telefono_completo','Mail','Web']]

column_names = (['cod_localidad','id_provincia','id_departamento','categoría','provincia','localidad', 'nombre', 'domicilio','código_postal', 'número_de_teléfono','mail','web'])

def renameDf (df, columnNames):
    df.columns = columnNames
    return df

renameDf(dfLibraryMapped, column_names)
renameDf(dfMuseumMapped, column_names)
renameDf(dfCinemaMapped, column_names)

dfEntertainment =pd.concat([dfLibraryMapped,dfMuseumMapped,dfCinemaMapped])


print(dfEntertainment)

##
# [Cod_Loc,IdProvincia,IdDepartamento,Observacion,Categoría,Subcategoria,Provincia,Departamento,Localidad,Nombre,Domicilio,Piso,CP,Cod_tel,Teléfono,Mail,Web,Información adicional,Latitud,Longitud,TipoLatitudLongitud,Fuente,Tipo_gestion,año_inicio,Año_actualizacion]
# [Cod_Loc,IdProvincia,IdDepartamento,Observaciones,categoria,subcategoria,provincia,localidad,nombre,direccion,piso,CP,cod_area,telefono,Mail,Web,Latitud,Longitud,TipoLatitudLongitud,Info_adicional,fuente,jurisdiccion,año_inauguracion,actualizacion]
# [Cod_Loc,IdProvincia,IdDepartamento,Observaciones,Categoría,Provincia,Departamento,Localidad,Nombre,Dirección,Piso,CP,cod_area,Teléfono,Mail,Web,Información adicional,Latitud,Longitud,TipoLatitudLongitud,Fuente,tipo_gestion,Pantallas,Butacas,espacio_INCAA,año_actualizacion]
##
#dfFilteredMuseum = dfMuseum[['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP', 'Mail', 'Web']]
#dfFilteredMuseum.insert(9,'numero de telefono',(dfMuseum['cod_area'].astype(str) + '-' + dfMuseum['telefono'].astype(str)), allow_duplicates=False)
#dfFilteredMuseum['numero de telefono'] = dfMuseum['cod_area'] + '' + dfMuseum['telefono']
# x = str(dfMuseum['telefono'])
# print(str(dfMuseum['cod_area'])2.cat(x))
# dfFilteredLibrary = dfLibrary[columnsNamesL]
# dfFilteredCinema = dfCinema[columnsNamesC]
#print (dfMuseum['cod_area'].astype(str(int)))
#pd.set_option('display.max_rows', None, 'display.max_columns', None)



###############

# titulos que necesito:
#cod_localidad; id_provincia; id_departamento; categoría; provincia;
# localidad; nombre; domicilio; código postal; número de teléfono; mail; web
##
# titulos que tengo


