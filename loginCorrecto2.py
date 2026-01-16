#Tengo que poner el nombre y la contraseña correctamente utilizando playwright

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False,slow_mo=300)
    url = "https://the-internet.herokuapp.com/login"
    page = browser.new_page()

    print("navegando a la url...")
    page.goto(url)

    print("Poniendo nombre y contraseña...")
    page.fill("#username","tomsmith")
    page.fill("#password","SuperSecretPassword!")

    print("Clickeamos el login...")
    page.click(".radius")


    page.wait_for_timeout(2000) #Lo uso para ver como queda



