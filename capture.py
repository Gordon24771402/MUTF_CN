from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from datetime import datetime


# function to capture net rate by topic
def captureTopic():
    # 01 - WebDriver Configuration
    chromeOptions = Options()
    # headless mode
    chromeOptions.add_argument('--headless')
    # disable console message
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome(options=chromeOptions)

    # 02 - Capture Net Rate by Topic
    driver.get('http://fund.eastmoney.com/ztjj/')
    # capture (date & time)
    nowDate, nowTime = datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M")
    # capture topic
    key = [w.text for w in driver.find_elements_by_class_name('spanwz')]
    # capture net rate
    value = [float(z.text.strip('%'))/100 for z in driver.find_elements_by_class_name('spanzzl')]
    # store in dictionary
    dic = {"date": nowDate, "time": nowTime, "content": {key[i]: value[i] for i in range(len(key))}}

    # 03 - Exit WebDriver & Return dic
    driver.quit()
    return dic
