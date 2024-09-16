from appium import webdriver
from appium.options.android import UiAutomator2Options


def initialize_appium_driver():
    capabilities = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Galaxy S9',
        appPackage='com.android.settings',
        appActivity='.Settings',
        language='en',
        locale='US'
    )

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(5)
    return driver

