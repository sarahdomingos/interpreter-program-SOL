#antes de rodar, vá no terminal e digite: pip install webdriver-manager 
#lembre de verificar se você tem o selenium instalado e verrsão compatível do python!!

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com/")

driver.quit()
