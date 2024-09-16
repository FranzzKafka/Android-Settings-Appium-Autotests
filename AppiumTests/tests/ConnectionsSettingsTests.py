from Data.PageObjects.MainSettingsPage import MainSettingsPage
from Data.PageObjects.ConnectiosSettingsPage import ConnectionsSettingsPage
from Helpers.UIElementsStateHelpers import UIElementsStateHelpers
from Helpers.UIInteractionsHelpers import UIInteractionsHelpers
from tests.conftest import appium_driver
settings_main_page = MainSettingsPage
connections_settings_page = ConnectionsSettingsPage

def test_turn_nfc_payment(appium_driver):
    expected_turned_off_nfc_text = "Make mobile payments, share data, and read or write NFC tags."
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.connects_button)
    UIInteractionsHelpers.click_on_element(appium_driver, connections_settings_page.nfc_payment_toggle)
    nfc_payment_status_text = UIElementsStateHelpers.get_element_text(appium_driver, connections_settings_page.nfc_payment_status_text)
    assert nfc_payment_status_text == expected_turned_off_nfc_text

def test_turn_off_wifi(appium_driver):
    expected_turned_off_wifi_text = "Connect to Wi-Fi networks."
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.connects_button)
    UIInteractionsHelpers.click_on_element(appium_driver, connections_settings_page.wifi_toggle)
    actual_turned_off_wifi_text = UIElementsStateHelpers.get_element_text(appium_driver, connections_settings_page.turned_off_wifi_text)
    assert expected_turned_off_wifi_text == actual_turned_off_wifi_text

def test_turn_on_airplane_mode(appium_driver):
    expected_turned_on_airplane_mode_text = "On"
    UIInteractionsHelpers.click_on_element(appium_driver, settings_main_page.connects_button)
    UIInteractionsHelpers.click_on_element(appium_driver, connections_settings_page.airplane_mode_toggle)
    actual_turned_on_airplane_mode_text = UIElementsStateHelpers.get_element_text(appium_driver, connections_settings_page.airplane_mode_turned_on_status)
    assert actual_turned_on_airplane_mode_text == expected_turned_on_airplane_mode_text