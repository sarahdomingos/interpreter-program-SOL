# import required modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def acessar_videoconferencia(meeting_link, seconds):
	
	# assign email id and password
	mail_address = 'grupo9086@gmail.com'
	password = 'GRUPO6@CC'

	# create chrome instance
	opt = Options()
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument('--start-maximized')
	opt.add_experimental_option("prefs", {
		"profile.default_content_setting_values.media_stream_mic": 1,
		"profile.default_content_setting_values.media_stream_camera": 1,
		"profile.default_content_setting_values.geolocation": 0,
		"profile.default_content_setting_values.notifications": 1
	})
	#driver = webdriver.Chrome(options=opt)
	driver = webdriver.Chrome(ChromeDriverManager().install())

	# login to Google account
	Glogin(mail_address, password, driver)

	# go to google meet
	driver.get(meeting_link)
	#turnOffMicCam(driver)
	AskToJoin(driver)
	joinNow(driver)


def Glogin(mail_address, password, driver):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element(By.ID, "identifierId").send_keys(mail_address)
	driver.find_element(By.ID, "identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element(By.XPATH,
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element(By.ID, "passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def turnOffMicCam(driver):
	# turn off Microphone
	time.sleep(2)
	driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
	driver.implicitly_wait(3000)

	# turn off camera
	time.sleep(1)
	driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
	driver.implicitly_wait(3000)


def joinNow(driver):
	# Join meet
	print(1)
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element(By.CSS_SELECTOR,
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	print(1)


def AskToJoin(driver):
	# Ask to Join meet
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element(By.CSS_SELECTOR,
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	# Ask to join and join now buttons have same xpaths
