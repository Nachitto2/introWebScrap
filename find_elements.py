from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# 1. Configuración 
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.scrapethissite.com/pages/simple/")

# 2. Encontrar TODOS los elementos con la clase "country-name"
paises = driver.find_elements(By.CLASS_NAME, "country-name")

# 3. Imprimir la cantidad total
print(f"He encontrado {len(paises)} países.")

# 4. Imprimir el texto de los primeros 5

print("Los primeros 3 son:")
for pais in paises[:3]: 
    print(pais.text) 

driver.quit()