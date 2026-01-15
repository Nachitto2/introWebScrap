from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.saucedemo.com/")

usuario = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
login = driver.find_element(By.NAME,"login-button")

print(usuario.is_displayed())

print(password.is_displayed())

print(login.is_displayed())

driver.quit()