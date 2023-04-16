import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url='https://vk.com'

s = Service('C:\\Users\\...\\chromedriver.exe')
driver = webdriver.Chrome(service=s)

try:
    driver.get(url=url)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()