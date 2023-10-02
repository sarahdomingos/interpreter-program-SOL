from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def acessar_whatsapp_web(seconds):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://web.whatsapp.com/")

    if seconds > 0:
        time.sleep(seconds)
        driver.quit()
