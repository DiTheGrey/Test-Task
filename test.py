from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://localhost:8080/")
driver.implicitly_wait(4)
driver.find_element(By.CSS_SELECTOR, ".style__component___3dz3r:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR,
                         ".style__component___39nuQ:nth-child(1) > .style__input___3L2xw").click()
driver.find_element(By.CSS_SELECTOR,
                         ".style__component___39nuQ:nth-child(1) > .style__input___3L2xw").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, ".style__component___QIBbi").click()
driver.find_element(By.CSS_SELECTOR, ".style__select___3-I2q").click()
driver.find_element(By.XPATH, "//option[. = 'finance']").click()
driver.find_element(By.CSS_SELECTOR, ".style__select___3-I2q").click()
driver.find_element(By.CSS_SELECTOR, ".style__textarea___3za4S").click()
driver.find_element(By.CSS_SELECTOR, ".style__textarea___3za4S").send_keys("Test test test")
driver.find_element(By.CSS_SELECTOR, "#react-node > div > div:nth-child(2)").click()
print('Customer created.')
print('-----------')
driver.find_element(By.CSS_SELECTOR,
                         ".style__component___Q4USl:nth-child(6) > .style__text___2g6Kj").click()
assert driver.find_element(By.CSS_SELECTOR,
                                ".style__component___1zdC3:nth-child(19) > .style__name___1iuXf").text == "Test"
driver.find_element(By.CSS_SELECTOR,
                         ".style__component___1zdC3:nth-child(19) > .style__name___1iuXf").click()
print('Assertion passed!')
print('------------')
print('Test Passed!')

driver.close()
