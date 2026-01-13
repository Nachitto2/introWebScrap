import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

with open("RomeoAndJuliet.txt", "wb") as play_file:
    for chunks in response.iter_content(100000):
        play_file.write(chunks)