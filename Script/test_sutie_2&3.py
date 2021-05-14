import unittest
import selenium
import time
import os
import base64
from appium import webdriver

class Test_Suite_2_3(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['appPackage'] = 'com.sendbird.android.sample'
        desired_caps['appActivity'] = 'com.sendbird.android.sample.main.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        self.channel_name = 'test1009'
        self.text_message = 'Hello'
        self.image_name = 'image.jpg'

    def test_sutie_2(self):
        # Login as User A
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_id').send_keys('123456')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_nickname').send_keys(
            'User A')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_login_connect').click()
        time.sleep(2)
        self.assertIn('Select channel type', self.driver.page_source, msg="Login Failed")

        # Enter Open Channel
        self.driver.find_element_by_id('com.sendbird.android.sample:id/linear_layout_open_channels').click()
        time.sleep(2)
        self.channel_xpath = "//android.widget.TextView[@text='" + self.channel_name + "']"
        self.driver.find_element_by_xpath(self.channel_xpath).click()
        time.sleep(2)
        self.assertIn('Enter message', self.driver.page_source, msg='Enter Open Channel Failed')

        # Send a text message
        self.driver.find_element_by_id(
            'com.sendbird.android.sample:id/edittext_chat_message').send_keys(self.text_message)
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_open_channel_chat_send').click()
        time.sleep(2)
        # Verify text message sent correctly
        list_of_text = self.driver.find_elements_by_xpath(
            "//android.widget.TextView[@resource-id='com.sendbird.android.sample:id/text_open_chat_message']")
        text_list = []
        for value in list_of_text:
            chat_text = value.get_attribute("text")
            text_list.append(chat_text)
        self.assertEqual(self.text_message, text_list[-1], msg='Send a text message failed')

        # Send a file message (upload an image)
        self.driver.find_element_by_accessibility_id('Upload file').click()
        time.sleep(2)
        # Click on 'Allow' - permission
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)
        # Push image to device
        remote_path = '/sdcard/Pictures/' + self.image_name
        local_path= os.getcwd() + '\\' + self.image_name
        with open(local_path, 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_message = base64_encoded_data.decode('utf-8')
        self.driver.push_file(remote_path, base64_message)
        time.sleep(3)
        # Upload image file
        self.driver.find_element_by_accessibility_id('Upload file').click()
        self.driver.find_element_by_id('com.google.android.documentsui:id/icon_thumb').click()
        self.driver.find_element_by_id('android:id/button1').click()
        time.sleep(4)
        # Verify image file uploaded
        list_of_file = self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='com.sendbird.android.sample:id/text_open_chat_file_name']")
        file_list = []
        for value in list_of_file:
            file_text = value.get_attribute('text')
            file_list.append(file_text)
        self.assertEqual(self.image_name, file_list[-1], msg='Image upload failed')

        # Logout from User A
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id('Navigate up').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_disconnect').click()
        time.sleep(2)
        self.assertIn('Sendbird Sample', self.driver.page_source, msg='Logout Failed')


    def test_sutie_3(self):
        # Login as another User B
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_id').send_keys('234567')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/edittext_login_user_nickname').send_keys(
            'User B')
        self.driver.find_element_by_id('com.sendbird.android.sample:id/button_login_connect').click()
        time.sleep(2)
        self.assertIn('Select channel type', self.driver.page_source, msg='Login Failed')

        # Enter Open Channel
        self.driver.find_element_by_id('com.sendbird.android.sample:id/linear_layout_open_channels').click()
        time.sleep(2)
        self.channel_xpath = "//android.widget.TextView[@text='" + self.channel_name + "']"
        self.driver.find_element_by_xpath(self.channel_xpath).click()
        time.sleep(4)
        self.assertIn('Enter message', self.driver.page_source, msg='Enter Open Channel Failed')

        # Display text message
        # Verify User A message displayed
        list_of_text = self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='com.sendbird.android.sample:id/text_open_chat_message']")
        chat_list=[]
        for value in list_of_text:
            chat_text = value.get_attribute('text')
            chat_list.append(chat_text)
        self.assertIn(self.text_message, chat_list, msg='Text message not found in channel')
        # Display file message
        # Verify User A file displayed
        list_of_file = self.driver.find_elements_by_xpath("//android.widget.TextView[@resource-id='com.sendbird.android.sample:id/text_open_chat_file_name']")
        file_list=[]
        for value in list_of_file:
            file_text = value.get_attribute('text')
            file_list.append(file_text)
        self.assertIn(self.image_name, file_list, msg='File not found in channel')


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)