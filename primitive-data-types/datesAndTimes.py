from datetime import datetime
import time
def main():
    now = datetime.now()
    today = str(datetime.today())
    yyyy = today[0:4]
    mm = today[5:7]
    dd = today[8: 10]
    H = now.strftime("%H")
    M = now.strftime("%M")
    S = now.strftime("%S")
    dateFormating(yyyy,mm,dd,H,M,S)
    epochTimeStamp()
    addTimeToCurrent(1, 1,2)
    #Main function calling
def dateFormating(yyyy,mm,dd,H,M,S):
    print("_"*150)
    print("Date formating: \n")
    print("Lithuanian date format: " +yyyy + "/" + mm + "/" + dd + " " + H + ":" + M + ":" + S)
    print("French date format: " + dd + "/" + mm + "/" + yyyy + " " + H + ":" + M + ":" + S)
    print("US date format: " + mm + "-" + dd + "-" + yyyy + " " + H + ":" + M + ":" + S)
    print("_"*150)
def epochTimeStamp():
    print("Epoch time stamp conversion: \n")
    timeStamp = time.time()
    readableTime = datetime.fromtimestamp(timeStamp)
    print("Epoch time stamp: " +str(int(timeStamp)))
    print("Readable time: " + str(readableTime))
    print("_"*150)
def addTimeToCurrent(yyyy,mm,dd):
    currentTime = datetime.today()
    print("time changement: \n")
    print("Current time: " + str(currentTime))
    print("Time added: " + str(yyyy) + " year "+ str(mm) + " month "+ str(dd) + " day")
    print(currentTime.replace(year = currentTime.year + yyyy).replace(month = currentTime.month + mm).replace( day = currentTime.day + dd))
    print("_"*150)

if(__name__ == "__main__"):
    main()
