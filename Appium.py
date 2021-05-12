import unittest
import selenium
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class MyTestCase(unittest.TestCase):

    def setUp(self):
        print('selenium version = ', selenium.__version__)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '5.1.1'
        #desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.sendbird.android.sample'
        #desired_caps["noReset"] = True
        desired_caps['appActivity'] = 'com.sendbird.android.sample.main.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testsutie1(self):
            time.sleep(2)
            self.driver.find_element_by_id("com.sendbird.android.sample:id/edittext_login_user_id").send_keys("UserA")
            time.sleep(2)
            self.driver.find_element_by_id("com.sendbird.android.sample:id/edittext_login_user_nickname").send_keys(
                "123456")
            time.sleep(2)
            self.driver.find_element_by_id('com.sendbird.android.sample:id/button_login_connect').click()
            time.sleep(2)
            result = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.view.ViewGroup/android.widget.TextView").text
            self.assertIn("Select channel type", result, msg="Login Failed")
            self.driver.find_element_by_id('com.sendbird.android.sample:id/linear_layout_open_channels').click()
            time.sleep(10)
            # self.driver.find_element_by_id('com.sendbird.android.sample:id/fab_open_channel_list').click()
            element = self.driver.find_element_by_id("com.sendbird.android.sample:id/fab_open_channel_list")
            actions = TouchAction(self.driver)
            actions.long_press(element)
            actions.perform()
            time.sleep(10)
            self.driver.find_element_by_id("com.sendbird.android.sample:id/edittext_create_open_channel_name").send_keys(
                "M")
            time.sleep(2)
            self.driver.find_element_by_id('com.sendbird.android.sample:id/button_create_open_channel').click()
            time.sleep(2)
            self.driver.find_element_by_id('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]').click()
            time.sleep(2)
            self.driver.find_element_by_id(
                "com.sendbird.android.sample:id/edittext_chat_message").send_keys(
                "P")
            time.sleep(2)
            self.driver.find_element_by_id('com.sendbird.android.sample:id/button_open_channel_chat_send').click()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id('Navigate up').click()
            time.sleep(2)
            self.driver.find_element_by_accessibility_id('Navigate up').click()
            time.sleep(2)
            self.driver.find_element_by_id('com.sendbird.android.sample:id/button_disconnect').click()
            assert "Sendbird Sample" in driver.page_source

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()