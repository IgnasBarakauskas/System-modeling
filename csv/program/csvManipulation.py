import csv


def main():
    data = readCSV("csv/program/calculate.csv")
    calculatedData = []
    for row in data:
        calculatedData.append([row[0], row[1], calculateFib(int(row[2]))])
    writeCSV("csv/program/answerCalculate.csv", calculatedData)


def writeCSV(path, data):
    f = open(path, "w")
    for row in data:
        line = row[0] + "," + row[1] + "," + str(row[2]) + "\n"
        f.write(line)
    f.close()


def calculateFib(number):
    if number <= 1:
        return number
    else:
        return (calculateFib(number-1) + calculateFib(number-2))


def readCSV(path):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        rows = []
        for row in spamreader:
            rows.append(row)
        return rows


if(__name__ == "__main__"):
    main()
