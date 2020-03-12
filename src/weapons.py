import sys
import time

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver


from report import Report

url = sys.argv[2]

driver = webdriver.Chrome(sys.argv[1])
driver.get(url)

# for request in driver.requests:
#     if request.response:
#        print (request.path,
#               request.response.status_code,
#               request.response.headers)

html_report = Report(url)
html_report.add_request(driver.requests)

kSECOND_WAIT = 10
try:
    time.sleep(kSECOND_WAIT)
    element = WebDriverWait(driver, kSECOND_WAIT).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )



finally:
    pass
html_report.generate()
driver.close()
