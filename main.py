from capture import captureTopic
from store import storeTopic
from datetime import datetime
import time

print("DataBase is Ready to Run!\n")

while True:
    now = datetime.now().strftime("%H:%M")
    if now in ["09:35", "10:35", "11:35", "13:35", "14:35", "15:35"]:
        dataTopic = captureTopic()
        print("{} dataTopic is Captured".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        storeTopic(dataTopic)
        print("{} dataTopic is Stored\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        time.sleep(60)
    else:
        time.sleep(60)

# pyinstaller -F --add-binary "C:\Users\97262\OneDrive\Pycharm\MUTF_CN\chromedriver.exe";"." --clean main.py
