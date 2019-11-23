# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiu(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print('一个类只执行一次')
        cls.init_appium()


    def setup_method(self):
        print('一个方法只执行一次')
        TestXueqiu.driver = self.restart_appium()
        self.driver = TestXueqiu.driver


    def test_login(self):

        el1 = TestXueqiu.driver.find_element_by_id("user_profile_icon")
        el1.click()
        self.driver.implicitly_wait(6)
        el2 = TestXueqiu.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
        el2.click()

    def test_fund(self):
        self.driver.find_element_by_xpath("//*[contains(resource-id, 'indicator')]//*[text='基金']")

    def teardown_method(self):
        self.driver.quit()

    def test_swipe(self):
        self.driver.find_element_by_xpath("//*[contains(resource-id, 'indicator')]//*[text='基金']")
        for i in range(5):
            self.driver.swipe(1000, 1000, 800, 800)
            time.sleep(2)

    def test_action(self):
        # 去掉更新的广告弹窗
        eli = self.driver.find_element_by_id("image_cancel")
        eli.click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'buttons_container')]//*[@text='基金']")
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=1000, y=1000).move_to(x=200, y=200).release().perform()
            time.sleep(3)

    def test_action_p(self):
        # 去掉更新的广告弹窗
        eli = self.driver.find_element_by_id("image_cancel")
        eli.click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'buttons_container')]//*[@text='基金']")
        rect = self.driver.get_window_rect()
        x = rect['width']
        y = rect['height']
        action = TouchAction(self.driver)
        for i in range(5):
            action.press(x=x*0.8, y=y*0.8).move_to(x=x*0.2, y=x*0.2).release().perform()
            time.sleep(3)


    @classmethod
    def init_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Redmi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["unicodeKeyboard"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(6)
        return driver

    @classmethod
    def restart_appium(cls) -> WebDriver:
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Redmi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["unicodeKeyboard"] = "true"
        caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    pytest.main(['-s', 'xueqiu_test.py::TestXueqiu::test_action_p'])
