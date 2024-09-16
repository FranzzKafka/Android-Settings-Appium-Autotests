import time

from appium.webdriver.common.appiumby import AppiumBy


class ConnectionsSettingsPage:

    wi_fi_button = "//android.view.ViewGroup[@resource-id=\"com.android.settings:id/recycler_view\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout"

    nfc_payment_toggle = "//android.widget.Switch[@content-desc=\"NFC and payment\"]"

    wifi_toggle = "//android.widget.Switch[@content-desc=\"Wi-Fi\"]"

    turned_off_wifi_text = "//android.widget.TextView[@resource-id=\"android:id/summary\" and @text=\"Connect to Wi-Fi networks.\"]"

    nfc_payment_status_text = "//android.widget.TextView[@resource-id=\"android:id/summary\" and @text=\"Make mobile payments, share data, and read or write NFC tags.\"]"

    airplane_mode_toggle = "//android.widget.Switch[@content-desc=\"Airplane mode\"]"

    airplane_mode_turned_on_status = "//android.widget.TextView[@resource-id=\"android:id/summary\" and @text=\"On\"]"