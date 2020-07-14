from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'CB5A295UL8',
    'platformVersion': '7.1.1',
    'appPackage': 'cn.com.bjx.bjxtalents',
    'appActivity': 'cn.com.bjx.bjxtalents.activity.MainActivity',
    'automationName': 'UiAutomator1'

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
