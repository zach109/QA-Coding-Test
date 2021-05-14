import unittest
import selenium
import time
from appium import webdriver

class Test_Suite_1(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['appPackage'] = 'com.sendbird.android.sample'
        desired_caps['appActivity'] = 'com.sendbird.android.sample.main.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_suite_1(self):
        #Login as User A
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_id').send_keys('123456')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_nickname').send_keys(
            'User A')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_login_connect').click()
        time.sleep(2)
        self.assertIn('Select channel type', self.driver.page_source, msg='Login Failed')

        #Enter Open Channel
        self.driver.find_element_by_id('com.sendbird.android.sample:id/linear_layout_open_channels').click()
        time.sleep(2)
        channel_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'
        self.driver.find_element_by_xpath(channel_xpath).click()
        time.sleep(2)

        self.assertIn("Enter message", self.driver.page_source, msg="Enter Open Channel Failed")

        #Send a text Message
        self.driver.find_element_by_id(
            "com.sendbird.android.sample:id/edittext_chat_message").send_keys('Hello World')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_open_channel_chat_send').click()
        time.sleep(2)
        self.assertEqual('Enter message', self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_chat_message').text, msg='Send a Text Message Failed')

        #Logout from User A
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_disconnect').click()
        self.assertIn('Sendbird Sample', self.driver.page_source, msg='Logout Failed')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

