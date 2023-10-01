#antes de rodar, vá no terminal e digite: pip install webdriver-manager 

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com/")

driver.quit()
