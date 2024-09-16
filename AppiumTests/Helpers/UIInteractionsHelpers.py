from appium.webdriver.common.appiumby import AppiumBy


class UIInteractionsHelpers:

    def click_on_element(driver, x_path):
        element = driver.find_element(AppiumBy.XPATH, x_path)
        element.click()

    def set_text_to_element(driver, text, x_path):
        element = driver.find_element(AppiumBy.XPATH, x_path)
        element.send_keys(text)

    def scroll_to_text(driver, text):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{}"))'.format(text))

    def get_element(driver, x_path):
        return driver.find_element(AppiumBy.XPATH, x_path)