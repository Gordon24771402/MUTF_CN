from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from datetime import datetime


def captureTopic():
    # WebDriver Configuration
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = Chrome(options=chromeOptions)
    # Get to Topic Page
    driver.get('http://fund.eastmoney.com/ztjj/')
    nowDate, nowTime = datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M")
    key = [w.text for w in driver.find_elements_by_class_name('spanwz')]
    value = [float(z.text.strip('%'))/100 for z in driver.find_elements_by_class_name('spanzzl')]
    dic = {"date": nowDate, "time": nowTime, "content": {key[i]: value[i] for i in range(len(key))}}
    # Exit WebDriver
    driver.quit()
    return dic
