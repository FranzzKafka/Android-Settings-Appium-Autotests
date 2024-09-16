import pytest

from Helpers import UIInteractionsHelpers
from utils.AppiumUtils import initialize_appium_driver

@pytest.fixture(scope="function")
def appium_driver(request):
    driver = initialize_appium_driver()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver