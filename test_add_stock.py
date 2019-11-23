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
caps["noReset"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(8)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/item_add_stock")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.click()
el3.send_keys("alibaba")
driver.implicitly_wait(6)
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[2]")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/follow_btn")
el5.click()
caps["resetKeyboard"] = "true"

driver.quit()