from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://egov.uscis.gov/casestatus/landing.do')

# Add your receipt in the send_keys parameter
driver.find_element(By.ID, 'receipt_number').send_keys('')
driver.find_element(By.NAME, 'initCaseSearch').click()
