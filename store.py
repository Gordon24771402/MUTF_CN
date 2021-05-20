import os


def storeTopic(data):
    for key in data["content"].keys():
        with open("./Data/ByTopic/{}.csv".format(key), "a") as df:
            if os.path.getsize("./Data/ByTopic/{}.csv".format(key)) != 0:
                df.write("\n")
            df.write("{},{},{}".format(data["date"], data["time"], data["content"][key]))
