#antes de rodar, vá no terminal e digite: pip install webdriver-manager 
#lembre de verificar se você tem o selenium instalado e verrsão compatível do python!!

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time


def acessar_youtube(search, seconds):
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get(f'https://www.youtube.com/results?search_query={search}')

  if seconds > 0:
    time.sleep(seconds)
    driver.quit()
