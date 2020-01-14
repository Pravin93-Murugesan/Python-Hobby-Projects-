from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example 1 (Asynchronous webpage loading)
url = 'https://www.google.com/earth/'
driver = webdriver.Chrome("path\\to\\chromedriver.exe")
driver.get(url)

wait = WebDriverWait(driver, 5)
lauchEarth = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/div/a/span/span')))
lauchEarth.click()
