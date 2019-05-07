#C:\Users\Ben\AppData\Local\Programs\Python\Python37-32\Scripts\pyuic5.exe -x gui.ui -o gui.py
from gui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
import pyqtgraph as pg
from pendulum import*
from datalogging import*
import sys
import time
import pandas
from controller import*
#from daq import*

tStart = time.time();
tVec = [0]
ts = .005;

#Daq = daq(0)
app = QtGui.QApplication(sys.argv)
Plotter = QtGui.QMainWindow()
ui = Ui_Plotter()
ui.setupUi(Plotter)

motor = pendulum('COM19', ts)

#time.sleep(.5);

class DataCollectionThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self, parent=None):
        QThread.__init__(self)
        self.sampleTimer = QtCore.QTimer()
        self.sampleTimer.timeout.connect(lambda:self.sample())
        self.sampleTimer.start(1000*ts)
    def sample(self):
        motor.getData()
        #self.signal.emit(motor.data)


dataThread  = DataCollectionThread()

def logSelected():
    if ui.logButton.isChecked():
        filename = ui.filenameEdit.text()
        filename = "Logs/" + filename+".csv"
        try:
            global writer, logFile
            logFile = open(filename, "a")
            writer = csv.writer(logFile, delimiter=',')
            print("file opened")
        except:
            print("that's not a file")
    else:
        try:
            logFile.close()
            print("file closed")
        except:
            pass
        
def exportPlot():
    filename = ui.filenameEdit.text()
    filename = "Logs/" + filename+".csv"
    #global writer, logFile
    logFile = open(filename, "a")
    writer = csv.writer(logFile, delimiter=',')
    print("file opened")
    for row in motor.dataVec[-4000:-1]:
        writer.writerow([row])
    logFile.close()
    print("file closed")



def updatePlots(plots, xdata, ydata):
    for i in range(len(plots)):
        plots[i].plot(ydata[i], clear=True)

def sampleAll():
    #Daq.sampleAll()
    motor.getData()
    #currentTime = time.time()-tStart
    #tVec.append(currentTime)

dataPlot = pg.PlotWidget(title = 'current')
ui.PlotLayout.addWidget(dataPlot)  # plot goes on right side, spanning 3 rows

ui.logButton.toggled.connect(lambda:logSelected())
ui.saveButton.clicked.connect(lambda:exportPlot())

def refresh():
    #dynoDaq.sampleAll()
    dataVec = motor.dataVec[-2000:-1]    
    dataPlot.plot(dataVec, clear=True)

#sampleTimer = QtCore.QTimer()
#sampleTimer.timeout.connect(lambda:sampleAll())
#sampleTimer.start(1000*ts)

plotTimer = QtCore.QTimer()
plotTimer.timeout.connect(lambda:refresh())
plotTimer.start(100)


Plotter.show()
sys.exit(app.exec_())
