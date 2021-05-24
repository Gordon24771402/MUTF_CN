from capture import captureTopic
from store import storeTopic
from datetime import datetime
from requests import get
from time import sleep


def updateByTopic():
    print("DataBase is Ready to Run!\n")
    while True:
        date, time = datetime.now().strftime("%Y-%m-%d"), datetime.now().strftime("%H:%M")
        calendar = get("http://fund.eastmoney.com/fundguzhi.html").text
        if date in calendar:
            if time in ["09:35", "10:35", "11:35", "13:35", "14:35", "15:35"]:
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
