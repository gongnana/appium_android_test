# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


from appium import webdriver


caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "Redmi"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"
caps["unicodeKeyboard"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(6)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.view.ViewGroup/android.widget.FrameLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout/"
                                   "android.widget.FrameLayout/android.widget.RelativeLayout/"
                                   "android.widget.LinearLayout/android.widget.FrameLayout[1]/"
                                   "android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
driver.implicitly_wait(5)
el2.click()

driver.quit()
