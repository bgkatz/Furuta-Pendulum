import UniversalLibrary as UL
BoardNum = 0

def getTorque():
    Gain = UL.BIP5VOLTS
    Chan = 0
    DataValue = UL.cbAIn(BoardNum, Chan, Gain)
    #return (UL.cbToEngUnits(BoardNum, Gain, DataValue))
    engUnits = UL.cbToEngUnits(BoardNum, Gain, DataValue)
    return (2.26*engUnits)

def getCount():
    Chan = 0;
    DataValue = 0
    #return UL.cbCIn32(BoardNum, Chan, DataValue)
    return UL.cbCIn(BoardNum, Chan, DataValue)

def sampleAll():
    torque = getTorque()
    count = getCount()
    #return (torque, count)
