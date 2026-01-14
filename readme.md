# web Scraping

La idea del proyecto es poner en practica conceptos introductorios del web scraping usando python explicados en el libro automate the boring stuff with python.

## showmap

Este programa se ejecuta en la terminal de forma genérica de la siguiente manera:
(parado en la carpeta donde esta el programa)> python showmap.py ubicación

ejemplo:
PS C:\Users\ignav\introWebScrap> python showmap.py Buenos Aires

Primero verifica que haya algo escrito en la terminal y lo guarda en una variable, exceptuando la primera palabra (showmap.py)

luego con la funcion webbroser.open abre la direccion deseada.

webbrowser.open(link): Abre en google el link que le mandes-> import webbrowser
sys.adv: Es una lista de lo que esta escrito en la terminal-> import sys
pyperclip.paste(): Pega lo que esta en el portapapeles (En el ctrl + C)-> import pyperclip


## downloadStuff

Funciona para descargar texto de internet.

Se ejecuta copiando y pegando un link. Recomiendo:
https://automatetheboringstuff.com/files/rj.txt

## findLatLong

Funciona para encontrar la latitud y longitud de una ciudad. En este caso Bs As. Como la app mientras realizaba el programa estaba caída, el programa no funciona, ademas que no use una api key real.

El json load transforma el txt a json.}

## findElements

Para practicar esto le fui pidiendo a chatgpt ejercicios como para saber que selectores usar, usando como machete una foto del libro automate Boring Stuff With Python.

Luego hice el ejercicio para evidenciar la practica. 
Lo que hace el programa es:
-Descargar el html de la pagina (dada por el libro)
-Buscar elementos y printearlos

