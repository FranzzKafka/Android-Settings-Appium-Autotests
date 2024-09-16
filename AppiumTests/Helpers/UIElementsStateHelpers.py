from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UIElementsStateHelpers:

    def is_element_exists(driver, x_path):
        zero_elements = 0
        elements = driver.find_elements(AppiumBy.XPATH, x_path)
        return len(elements) > zero_elements

    def get_element_text(driver, x_path):
        element = driver.find_element(AppiumBy.XPATH, x_path)
        return element.text

    def wait_element_appearing(driver, x_path):
        web_driver_wait_timeout_sec = 10
        WebDriverWait(driver, web_driver_wait_timeout_sec).until(EC.presence_of_element_located((By.XPATH, x_path)))
