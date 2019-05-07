
import csv

class logFile():
    def __init__(self, filename):
        self.filename = filename
    def open(self):
        self.file = open(self.filename, "wb")
        self.writer = csv.writer(self.file)
    def close(self):
        close(self.filename)
    def writeVec(self, vec):
        self.writer.writerow(vec)
        
        

def saveData(filename, columns):
    pass

def newFile(filename):
    pass