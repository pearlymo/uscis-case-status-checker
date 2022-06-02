from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/mothighimire/Repos/programming/programs/tps-checker/chromedriver")

driver.get('https://egov.uscis.gov/casestatus/landing.do')
driver.find_element(By.ID, 'receipt_number').send_keys('') # Add your receipt in the send_keys parameters
driver.find_element(By.NAME, 'initCaseSearch').click()
