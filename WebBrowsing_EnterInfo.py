from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\RAM\\Desktop\\Python\\chromedriver.exe") # need file path to work
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

#Example 1
messagefield = driver.find_element_by_xpath('//*[@id="user-message"]')
messagefield.send_keys('Hi Pravin')
showmessage = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showmessage.click()

#Example 2
messagefield1 = driver.find_element_by_xpath('//*[@id="sum1"]')
messagefield1.send_keys('10')
messagefield2 = driver.find_element_by_xpath('//*[@id="sum2"]')
messagefield2.send_keys('15')
showtotal = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
showtotal.click()

