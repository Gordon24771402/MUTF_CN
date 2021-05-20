from capture import captureTopic
from store import storeTopic
from datetime import datetime

print("DataBase is Ready to Run!\n")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    if now in ["09:35:00", "10:35:00", "11:35:00", "13:35:00", "14:35:00", "15:35:00"]:
        dataTopic = captureTopic()
        print("{} dataTopic is Captured".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        storeTopic(dataTopic)
        print("{} dataTopic is Stored\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# pyinstaller -F --add-binary "C:\Users\97262\OneDrive\Pycharm\MUTF_CN\chromedriver.exe";"." --clean main.py
