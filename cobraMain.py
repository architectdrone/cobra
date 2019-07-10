import json
from terminaltables import AsciiTable

PROJECT_PATH = "..//cobraTest"

class DataFile:
    DATA_FILE_NAME = "data.json"
    dataPath = PROJECT_PATH+"//"+DATA_FILE_NAME

    def __init__(self):
        self.data = []
    
    def load(self):
        f = open(self.dataPath, "r")
        tempData = json.loads(f.read())
        f.close()
        if self.data != tempData:
            choice = input("This will delete all data currently stored. Okay? \n(Y or N) > ")
            if choice == "N":
                return
        self.data = tempData
    
    def save(self):
        f = open(self.dataPath, "w")
        f.write(json.dumps(self.data))
    
    def get(self, x, y):
        for i in self.data:
            if i['x'] == x and i['y'] == y:
                return i
        raise Exception("Cell not found.")

    def put(self, x, y, key, value):
        for i in range(len(self.data)-1):
            if self.data[i]['x'] == x and self.data[i]['y'] == y:
                self.data[i][key] = value
                return
        self.data.append({"x": x, "y": y, key: value})

class Spreadsheet():
    def __init__(self):
        self.dataFile = DataFile()
    
    def display(self, low_x = 0, low_y = 0, high_x = 10, high_y = 10):
        toDisplay = []
        topRow = ['X']+[str(i+1) for i in range(high_x - low_x)]
        toDisplay.append(topRow)
        for i_y in range(high_y - low_y):
            y = i_y+1
            newRow = [y]
            for i_x in range(high_x - low_x):
                x = i_x+1
                try:
                    dataPoint = self.dataFile.get(x, y)
                    dataPoint = dataPoint['here']
                except:
                    dataPoint = "-"
                newRow.append(dataPoint)
            toDisplay.append(newRow)
        table = AsciiTable(toDisplay)
        print(table.table)


spreadsheet = Spreadsheet()
while True:
    userInput = input("(L, S, D, P) > ").split(" ")
    command = userInput[0]
    if command == "L":
        spreadsheet.dataFile.load()
    elif command == "S":
        spreadsheet.dataFile.save()
    elif command == "D":
        spreadsheet.display()
    elif command == "P":
        x = int(userInput[1])
        y = int(userInput[2])
        key = userInput[3]
        value = userInput[4]
        spreadsheet.dataFile.put(x, y, key, value)
        spreadsheet.display()
    else:
        print("Huh?")

    

