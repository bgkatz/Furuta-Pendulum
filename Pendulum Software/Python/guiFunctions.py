
def enableTMControls():
    ui.testVMinBox.setEnabled(True)
    ui.testVMaxBox.setEnabled(True)
    ui.testVSetBox.setEnabled(True)
    ui.periodMinBox.setEnabled(True)
    ui.periodMaxBox.setEnabled(True)
    ui.periodBox.setEnabled(True)

def disableTMControls():
    ui.testVMinBox.setEnabled(False)
    ui.testVMaxBox.setEnabled(False)
    ui.testVSetBox.setEnabled(False)
    ui.periodMinBox.setEnabled(False)
    ui.periodMaxBox.setEnabled(False)
    ui.periodBox.setEnabled(False)

def enableRLControls():
    ui.jBox.setEnabled(True)
    ui.c1Box.setEnabled(True)
    ui.c2Box.setEnabled(True)
    
def disableRLControls():
    ui.jBox.setEnabled(False)
    ui.c1Box.setEnabled(False)
    ui.c2Box.setEnabled(False)

def enableMSControls():
    ui.speedSlider.setEnabled(True)
    ui.sBox.setEnabled(True)

def disableMSControls():
    ui.speedSlider.setEnabled(False)
    ui.sBox.setEnabled(False)

def enableProfileControls():
    ui.browseButton.setEnabled(True)
    ui.csvEdit.setEnabled(True)
    ui.startButton.setEnabled(True)
    ui.stopButton.setEnabled(True)

def disableProfileControls():
    ui.browseButton.setEnabled(False)
    ui.csvEdit.setEnabled(False)
    ui.startButton.setEnabled(False)
    ui.stopButton.setEnabled(False)

def enableBuckControls():
    ui.buckBox.setEnabled(True)
    ui.iMaxBox.setEnabled(True)
    
def disableBuckControls():
    ui.buckBox.setEnabled(False)
    ui.iMaxBox.setEnabled(False)


def disableSelected():
    disableRLControls()
    disableMSControls()
    disableProfileControls()
    ui.speedSlider.setValue(0)
    ui.sBox.setValue(0)


def rlSelected():
    enableRLControls()
    enableBuckControls()
    enableTMControls()
    disableMSControls()
    disableProfileControls()
    ui.sBox.setValue(0)
    ui.speedSlider.setValue(0)
    #dynoAbsorber.speedcmd = 0
    
def msSelected():
    enableMSControls()
    enableBuckControls()
    enableTMControls()
    disableRLControls()
    disableProfileControls()
    
def profileSelected():
    enableProfileControls()
    disableRLControls()
    disableMSControls()
    disableTMControls()
    disableBuckControls()
    ui.sBox.setValue(0)
    ui.speedSlider.setValue(0)
    


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
