from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service_obg = Service()
driver = webdriver.Firefox(service=service_obg)

driver.get("https://rahulshettyacademy.com/angularpractice/")


# -- Different locators: ID, Xpath, CSSSelector, Classname, name, linkText

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")

driver.find_element(By.ID, "exampleCheck1").click()


# to CREATE Xpath use it: //tagname[@attribute='value']
# to CREATE CSSSelector use it: tagname[attribute='value']


driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
