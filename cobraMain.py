import json

class DataFile:
    fileName = "data.json"
    def __init__(self):
        self.data = []
    
    def load(self):
        f = open(self.fileName, "r")
        tempData = json.loads(f.read())
        f.close()
        if self.data != tempData:
            choice = input("This will delete all data currently stored. Okay? \n(Y or N) > ")
            if choice == "N":
                return
        self.data = tempData
    
    def save(self):
        f = open(self.fileName, "w")
        f.write(json.dumps(self.data))
    
    def get(self, x, y):
        for i in self.data:
            if i['x'] == x and i['y'] == y:
                return i
        raise Exception("Cell not found.")

    def put(self, x, y, key, value):
        for i in range(len(self.data)-1):
            if self.data[i]['x'] == x and self.data[i]['y'] == y:
                self.data[i][key] == value
                return
        self.data.append({"x": x, "y": y, key: value})

dataFile = DataFile()
while True:
    userInput = input("(L, S, G, P) > ").split(" ")
    command = userInput[0]
    if command == "L":
        dataFile.load()
    elif command == "S":
        dataFile.save()
    elif command == "G":
        x = int(userInput[1])
        y = int(userInput[2])
        print(dataFile.get(x, y))
    elif command == "P":
        x = int(userInput[1])
        y = int(userInput[2])
        key = userInput[3]
        value = userInput[4]
        dataFile.put(x, y, key, value)
        print(dataFile.get(x, y))
    else:
        print("Huh?")

    

