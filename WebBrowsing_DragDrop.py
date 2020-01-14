from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # For drag & drop
driver = webdriver.Chrome("C:\\Users\\RAM\\Desktop\\Python\\chromedriver.exe")
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element_by_xpath('//*[@id="box4"]')
destination = driver.find_element_by_xpath('//*[@id="box104"]')

action = ActionChains(driver)
action.drag_and_drop(source, destination).perform()
