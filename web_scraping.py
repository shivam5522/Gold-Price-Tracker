from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from config import CHROME_PROFILE_PATH
from datetime import datetime

# Configuring Chrome Options

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
# Extracting gold prices from PayTm website

driver = webdriver.Chrome(options=options)
driver.get('https://paytm.com/digitalgold')
driver.implicitly_wait(10)
gold_price = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div/div[1]/div/div/div[1]/div[3]').text


# Converting the prices to 10 gm

price = gold_price[8:15]
price = float(price)
price = price*10

# Getting current time

now = datetime.now()
current_time = now.strftime("%H:%M")

# Sending the message to person using whatsapp web

driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(20)
driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys('Pappa')
driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys("The price of gold at " + current_time + ' is ' + str(price))
driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)


