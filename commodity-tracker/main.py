from selenium import webdriver
#Extracting the price from PayTm
driver = webdriver.Chrome()
driver.get('https://paytm.com/digitalgold')
value = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div/div[1]/div/div/div[1]/div[3]')
driver.quit()
print(value)