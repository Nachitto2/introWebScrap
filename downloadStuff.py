import requests

link = input("Ingrese el link que quiera agregar a su pc")

response = requests.get(link)

with open("archivo.txt", "wb") as play_file:
    for chunks in response.iter_content(100000):
        play_file.write(chunks)