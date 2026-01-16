from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    browser = p.firefox.launch(headless=False,slow_mo=200)
    page = browser.new_page()

    print("Navegando a Swag Labs...")
    page.goto('https://www.saucedemo.com/')


    print("Escribiendo nombre y contraseña...")
    page.fill("#user-name","standard_user")
    page.fill("#password","secret_sauce")

    print("Clickeamos login...")
    page.click("#login-button")


    page.wait_for_timeout(2000) #Lo uso para ver como queda
