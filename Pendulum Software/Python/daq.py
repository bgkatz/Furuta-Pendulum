# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 03:27:10 2017

@author: Ben
"""


import UniversalLibrary as UL
import numpy
import time


class daq():
    def __init__(self, BoardNum):
        self.BoardNum = BoardNum
        self.TorqueVec = [0]
        self.CountVec = [0]
        self.VoltageVec = [0]
        self.CurrentVec = [0]
        self.Torque = 0
        self.Count = 0
        self.Voltage = 0
        self.Current = 0
        self.TorqueOffset = 0
        self.VoltageOffset = 0
        self.CurrentOffset = 0
        
    def sampleTorque(self):
        Gain = UL.BIP5VOLTS
        Chan = 0
        try:
            DataValue = UL.cbAIn(self.BoardNum, Chan, Gain)
            engUnits = UL.cbToEngUnits(self.BoardNum, Gain, DataValue)
            self.Torque = 2.26*engUnits# - self.TorqueOffset;
        except:
            pass
        
    def sampleVoltage(self):
        Gain = UL.BIP5VOLTS
        Chan = 1
        try:
            DataValue = UL.cbAIn(self.BoardNum, Chan, Gain)
            engUnits = UL.cbToEngUnits(self.BoardNum, Gain, DataValue)
            self.Voltage = -1*((engUnits-2.5)*20.2030 - self.VoltageOffset);
        except:
            pass
        
    def sampleCurrent(self):
        Gain = UL.BIP5VOLTS
        Chan = 2
        try:
            DataValue = UL.cbAIn(self.BoardNum, Chan, Gain)
            engUnits = UL.cbToEngUnits(self.BoardNum, Gain, DataValue)
            self.Current = (engUnits)/.02 - self.CurrentOffset;
        except:
            pass
        
    def sampleCount(self):
        Chan = 0;
        DataValue = 0
        try:
            self.Count =  UL.cbCIn(self.BoardNum, Chan, DataValue)
        except:
            pass
        
    def zero(self):
        current_error = 0
        voltage_error = 0
        torque_error = 0
        
        for i in range(1000):
            self.sampleTorque()
            self.sampleVoltage()
            self.sampleCurrent()
        #self.sampleAllFast()
            torque_error = torque_error + self.Torque
            current_error = current_error + self.Current
            voltage_error = voltage_error + self.Voltage
        time.sleep(.01)
        self.TorqueOffset = torque_error/1000
        self.CurrentOffset = current_error/1000
        self.VoltageOffset = voltage_error/1000
        
        
        """
        self.sampleAllFast()
        self.TorqueOffset = self.Torque
        self.CurrentOffset = self.Current
        self.voltageOffset = self.Voltage
        """
        print("Torque Offset",  self.TorqueOffset)
        print("Current Offset", self.CurrentOffset)
        print("Voltage Offset",  self.VoltageOffset)
            
        
    def sampleAll(self):
        self.sampleTorque()

        
        filteredTorque = self.Torque#.1*self.Torque + .9*self.TorqueVec[-1]
        filteredVoltage = self.Voltage#.1*self.Voltage + .9*self.VoltageVec[-1]
        #self.TorqueVec.append(self.Torque)
        self.TorqueVec.append(filteredTorque)
        
    def sampleAllFast(self):
        Count = 300
        Rate = 5000
        Gain = UL.BIP5VOLTS
        Options = UL.CONVERTDATA + UL.BACKGROUND + UL.SINGLEIO
        ADData = numpy.zeros((Count,), dtype=numpy.int16)

        UL.cbAInScan(self.BoardNum, 0, 2, Count, Rate, Gain, ADData, Options)
        time.sleep(Count/Rate)
        
        torqueVolts = UL.cbToEngUnits(self.BoardNum, Gain, int(numpy.mean(ADData[0::3])))
        voltageVolts = UL.cbToEngUnits(self.BoardNum, Gain, int(numpy.mean(ADData[1::3])))
        currentVolts = UL.cbToEngUnits(self.BoardNum, Gain, int(numpy.mean(ADData[2::3])))
        print(torqueVolts, voltageVolts, currentVolts)
        
        self.Torque = 2.26*torqueVolts - self.TorqueOffset;
        self.Voltage = -1*((voltageVolts-2.5)*20.2030 - self.VoltageOffset);
        self.Current = (currentVolts)/.02 - self.CurrentOffset;
        
    def getTorqueVec(self):
        return self.TorqueVec
        
    def getCountVec(self):
        return self.CountVec

    def getVoltageVec(self):
        return self.VoltageVec
        
    def getCurrentVec(self):
        return self.CurrentVec