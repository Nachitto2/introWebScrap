from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    url= 'https://autbor.com/example3.html'
    page.goto(url)
    print(page.title())
    browser.close()