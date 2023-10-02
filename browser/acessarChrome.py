#antes de rodar, vá no terminal e digite: pip install webdriver-manager 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time


def acessar_chrome(seconds):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    
    if seconds > 0:
        time.sleep(seconds)
        driver.quit()

def abrir_pdf(path, seconds):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(path)
    
    if seconds > 0:
        time.sleep(seconds)
        driver.quit()
