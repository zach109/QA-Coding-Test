import unittest
import selenium
import time
from appium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['appPackage'] = 'com.sendbird.android.sample'
        desired_caps['appActivity'] = 'com.sendbird.android.sample.main.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testsutie1(self):
            #Login as User A
            self.driver.find_element_by_id("com.sendbird.android.sample:id/edittext_login_user_id").send_keys("123456")
            self.driver.find_element_by_id("com.sendbird.android.sample:id/edittext_login_user_nickname").send_keys(
                "User A")
            self.driver.find_element_by_id('com.sendbird.android.sample:id/button_login_connect').click()
            time.sleep(2)
            self.assertIn("Select channel type", self.driver.page_source, msg="Login Failed")

            #Enter Open Channel M
            self.driver.find_element_by_id('com.sendbird.android.sample:id/linear_layout_open_channels').click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='M']").click()
            time.sleep(2)
            self.assertIn("Enter message", self.driver.page_source, msg="Enter Open Channel Failed")

            #Send a text message P
            #self.driver.find_element_by_id(
            #    "com.sendbird.android.sample:id/edittext_chat_message").send_keys(
            #    "P")
            #self.driver.find_element_by_id('com.sendbird.android.sample:id/button_open_channel_chat_send').click()
            time.sleep(2)
            list_of_values = self.driver.find_element_by_xpath("//*[@resource-id='com.sendbird.android.sample:id/text_open_chat_message']").text
            print(list_of_values)
            text_list = []
            for value in list_of_values:
                chat_text = value.get_attribute("text")
                print(chat_text)
                text_list.append(chat_text)
            print(text_list)


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