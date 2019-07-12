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
        for index, element in enumerate(self.data):
            if element['x'] == int(x) and element['y'] == int(y):
                self.data[index][key] = value
                return
        self.data.append({"x": x, "y": y, key: value})

class ScriptRunner():
    SCRIPT_FOLDER_NAME = "scripts"
    def __init__(self, scriptName, here, x, y):
        if scriptName[-3:] == ".py":
            self.script_path = PROJECT_PATH+"//"+self.SCRIPT_FOLDER_NAME+"//"+scriptName
        else:
            self.script_path = PROJECT_PATH+"//"+self.SCRIPT_FOLDER_NAME+"//"+scriptName+".py"
        
        try:
            f = open(self.script_path, "r")
            f.close()
        except:
            raise Exception("Script does not exist. Try creating it first.")
        
        self.here = here
        self.x = x
        self.y = y

    def run(self):
        f = open(self.script_path, "r")
        script = f.read()
        cobraData = CobraData(self.here, self.x, self.y)
        globals = {}
        locals = {'cobraData': cobraData}
        exec(script, globals, locals)
        self.cobraData = locals['cobraData']
        f.close()

class CobraData():
    def __init__(self, here, x, y):
        self._changes = []
        self.here = here
        self.x = x
        self.y = y
    
    def setCell(self, x, y, value):
        for i in self._changes:
            if i['x'] == x and i['y'] == y:
                i['value'] = value
                return
        self._changes.append({'x':x, 'y':y, 'value': value})

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

class Cobra():
    def __init__(self):
        self.spreadsheet = Spreadsheet()
        try:
            self.spreadsheet.dataFile.load()
        except:
            pass
    
    def update(self, x, y, newValue):
        try:
            oldData = self.spreadsheet.dataFile.get(x, y)
        except:
            pass
        else:
            if "script" in oldData:
                scriptRunner = ScriptRunner(oldData['script'], newValue, x, y)
                scriptRunner.run()
                for i in scriptRunner.cobraData._changes:
                    self.update(i['x'], i['y'], i['value'])
        self.spreadsheet.dataFile.put(x, y, 'here', newValue)
    
    def setScript(self, x, y, script):
        self.spreadsheet.dataFile.put(x, y, 'script', script)

cobra = Cobra()
while True:
    userInput = input("(Command) > ").split(" ")
    command = userInput[0]
    if command == "load":
        cobra.spreadsheet.dataFile.load()
    elif command == "save":
        cobra.spreadsheet.dataFile.save()
    elif command == "display":
        cobra.spreadsheet.display()
    elif command == "put":
        x = int(userInput[1])
        y = int(userInput[2])
        key = userInput[3]
        value = userInput[4]
        cobra.spreadsheet.dataFile.put(x, y, key, value)
        cobra.spreadsheet.display()
    elif command == "update":
        x = int(userInput[1])
        y = int(userInput[2])
        value = userInput[3]
        cobra.update(x, y, value)
        cobra.spreadsheet.display()
    elif command == "script":
        x = int(userInput[1])
        y = int(userInput[2])
        value = userInput[3]
        cobra.setScript(x, y, value)
        cobra.spreadsheet.display()
    elif command == "quit":
        break
    else:
        print("Huh?")

    

