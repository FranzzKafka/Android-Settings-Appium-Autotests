from Data.PageObjects.MainSettingsPage import MainSettingsPage
from Data.PageObjects.ConnectiosSettingsPage import ConnectionsSettingsPage
from Helpers.UIElementsStateHelpers import UIElementsStateHelpers
from Helpers.UIInteractionsHelpers import UIInteractionsHelpers
from tests.conftest import appium_driver
settings_main_page = MainSettingsPage
connections_settings_page = ConnectionsSettingsPage

def test_close_high_battery_usage_info_popup(appium_driver):
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.high_battery_usage_notification_close_icon)
    is_battery_usage_popup_exists= UIElementsStateHelpers.is_element_exists(appium_driver, settings_main_page.high_battery_usage_popup)
    assert is_battery_usage_popup_exists == False

def test_find_required_setting(appium_driver):
    input_setting_name = "Stay awake"
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.find_setting_icon)
    UIInteractionsHelpers.set_text_to_element(appium_driver, input_setting_name, settings_main_page.search_setting_input_field)
    UIElementsStateHelpers.wait_element_appearing(appium_driver, settings_main_page.setting_name)
    displayed_setting_name = UIElementsStateHelpers.get_element_text(appium_driver, settings_main_page.setting_name)
    assert input_setting_name == displayed_setting_name

def test_scroll_in_main_settings_window(appium_driver):
    setting_name_scroll_to = "Developer options"
    UIInteractionsHelpers.scroll_to_text(appium_driver, setting_name_scroll_to)

def test_connections_button_opens_connections_window(appium_driver):
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.connects_button)
    assert UIInteractionsHelpers.get_element(appium_driver, connections_settings_page.wi_fi_button).is_enabled()


