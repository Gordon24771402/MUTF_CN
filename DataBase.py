from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from datetime import datetime
from requests import get
from time import sleep
from os.path import getsize


# Function to Capture Net Rate by Topic
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
    nowDate, nowTime = datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M")  # 2021-05-20, 14:35
    # capture topic
    key = [w.text for w in driver.find_elements_by_class_name('spanwz')]
    # capture net rate
    value = [round(float(z.text.strip('%'))/100, 3) for z in driver.find_elements_by_class_name('spanzzl')]
    # store in dictionary
    dic = {"date": nowDate, "time": nowTime, "content": {key[i]: value[i] for i in range(len(key))}}

    # 03 - Exit WebDriver
    driver.quit()
    return dic


# Function to Store Net Rate by Topic
def storeTopic(data):
    # iterate through each topic
    for key in data["content"].keys():
        # open csv file in appending mode, if non-existent, create a new one
        with open("./Data/ByTopic/{}.csv".format(key), "a") as df:
            # if csv isn't empty, start in a new line
            if getsize("./Data/ByTopic/{}.csv".format(key)) != 0:
                df.write("\n")
            # append data to csv file
            df.write("{},{},{}".format(data["date"], data["time"], data["content"][key]))  # 2021-05-20,14:35,-0.0012
            # close csv file
            df.close()


def updateByTopic():
    print("DataBase is Ready to Run!\n")
    while True:
        date, time = datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M")
        calendar = get("http://fund.eastmoney.com/fundguzhi.html").text
        if date in calendar:
            if time in ["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00"]:
                dataTopic = captureTopic()
                print("{} dataTopic is Captured".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                storeTopic(dataTopic)
                print("{} dataTopic is Stored\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                sleep(60)
            else:
                sleep(60)
        else:
            sleep(1800)


if __name__ == "__main__":
    updateByTopic()

# pyinstaller -F --onefile --add-binary "chromedriver.exe";"." --clean DataBase.py
