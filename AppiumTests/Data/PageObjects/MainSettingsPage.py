from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainSettingsPage:

    high_battery_usage_notification_close_icon = "//android.widget.FrameLayout[@content-desc=\"Close Button\"]/android.widget.ImageView"

    connects_button = "//android.view.ViewGroup[@resource-id=\"com.android.settings:id/recycler_view\"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout"

    find_setting_icon = "//android.widget.Button[@content-desc=\"Search settings\"]"

    search_setting_input_field = "//android.widget.EditText[@resource-id=\"com.android.settings.intelligence:id/search_src_text\"]"

    setting_name = "//android.widget.TextView[@resource-id=\"android:id/title\"]"

    high_battery_usage_popup = "//android.widget.FrameLayout[@resource-id=\"com.android.settings:id/suggestion_card\"]/android.widget.FrameLayout/android.widget.LinearLayout"
