# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver


class TestXueqiuLogin(object):
    driver = WebDriver
    @classmethod
    def setup_class(cls):
        print('一个类只执行一次')
        cls.driver = cls.install_app()
        cls.driver.implicitly_wait(10)
        eli = cls.driver.find_element_by_id("image_cancel")
        eli.click()
        el1 = cls.driver.find_element_by_id("user_profile_icon")
        el1.click()

    def setup_method(self):
        print('一个方法只执行一次')
        # 获取启动后appium的driver实例
        pass

    def test_login_mobile(self):
        el2 = self.driver.find_element_by_id("iv_login_phone")
        el2.click()

    def test_login_password(self):
        self.driver.implicitly_wait(20)
        el2 = self.driver.find_element_by_id("iv_login_phone")
        el2.click()
        el3 = self.driver.find_element_by_xpath("//*[@text='邮箱手机号密码登录']")
        el3.click()

    def test_login_wechat(self):
        el3 = self.driver.find_element_by_id("iv_login_wx")
        el3.click()

    def teardown_method(self):
        self.driver.back()

    @classmethod
    def install_app(cls) -> WebDriver:
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
    def restart_app(cls) -> WebDriver:
        caps = {}
        # 如果有必要，进行第一次安装
        caps["app"] = ""
        caps["platformName"] = "android"
        caps["deviceName"] = "Redmi"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 第一次启动赋予权限
        caps["autoGrantPermissions"] = "true"
        # caps["unicodeKeyboard"] = "true"
        # 保留，不清除数据
        caps["noReset"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    pytest.main(['-s', 'test_xueqiu_login.py'])
