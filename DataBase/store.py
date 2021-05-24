from os.path import getsize


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
