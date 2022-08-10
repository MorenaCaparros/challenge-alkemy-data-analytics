from urllib import response
import requests as req
import pandas as pd
import os
import csv

museum = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
cinema = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
popularLibraries = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

def response(url):
    return req.get(url)
    

def cc(archive_name, url):
    with open(archive_name, 'w', encoding= 'utf-8') as file:
        writer = csv.writer(file)
        for line in response(url).iter_lines():
            writer.writerow(line.decode('utf-8').split(','))

cc('museum.csv', museum)
cc('cinema.csv', cinema)
cc('popular_libraries.csv', popularLibraries)

