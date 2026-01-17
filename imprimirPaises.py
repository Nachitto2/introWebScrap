from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.firefox.launch(headless=False, slow_mo=200)
    page = browser.new_page()

    page.goto("https://www.scrapethissite.com/pages/simple/")
    

    loc_paises = page.locator(".country-name")

    for i in range(100):
        print(loc_paises.nth(i).inner_text())