from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# import selenium


driver = webdriver.Edge()
driver.get("https://m.facebook.com/login/?locale=en_GB")
# actual_title=driver.title
# exp_title="Log in to Facebook | Facebook"
# if actual_title==exp_title:
#     print(actual_title)
# else:
#     print("We are on wrong page")
# time.sleep(2)
# driver.maximize_window()
# driver.find_element(By.ID,"m_login_email").send_keys("Mahammedrafiq@gmail.com")
# driver.find_element(By.NAME,"pass").send_keys("Something")
# driver.find_element(By.NAME,"login").click()

# tag and id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("9901222501")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("9901222501")

# tag and class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("9901222501")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("9901222501")

# tag  and attribute
# driver.find_element(By.CSS_SELECTOR,"input[placeholder=Email address or phone number]").send_keys("9901222501")
# driver.find_element(By.CSS_SELECTOR,"[placeholder=Email address or phone number]").send_keys("9901222501")

# tag class and attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[placeholder=Email address or phone number]").send_keys("9901222501")


time.sleep(10)
driver.close()
