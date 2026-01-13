import webbrowser, sys, pyperclip

#Ver si escribiste argumentos en la terminal
if len(sys.argv) > 1:
    # Si escribiste: python showmap.py 870 Valencia St
    # sys.argv es: ['showmap.py', '870', 'Valencia', 'St']
    # Lo unimos con espacios:
    address = ' '.join(sys.argv[1:])
else:
    #Si no escribiste nada, obtener del portapapeles
    print("No escribiste dirección, buscando en el portapapeles...")
    address = pyperclip.paste()

#Abrir el navegador
print(f"Buscando en Google Maps: {address}")
webbrowser.open('https://www.google.com/maps/place/' + address)