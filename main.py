from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

print("wait")
time.sleep(5)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

print("driver")
driver = webdriver.Remote(
command_executor='http://selenium:4444/wd/hub',
options=options
)

driver.maximize_window()
time.sleep(2)
print("web")
driver.get("http://siteweb:8000/")
elements = driver.find_elements(By.CLASS_NAME, 'form_container_input')
username_input = elements[0]
password_input = elements[1]

time.sleep(2)
driver.close()
driver.quit()
print("Test Execution Successfully Completed!")

