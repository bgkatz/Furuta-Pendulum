# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *

class controller():
    def __init__(self, COM):
        self.id = 0
        self.iq = 0
        try:
            self.ser = serial.Serial(COM, timeout = .1)
            self.ser.baudrate = 921600
            print('conencted to controller')
        except:
            print('failed to connect to controller')
            pass
    def getCurrent(self):
        try:
            
            val = self.ser.readline()
            self.id = val[0]
            self.iq = val[2]
            if(self.id>128):
                self.id = self.id-256
            if(self.iq>128):
                self.iq = self.iq-256
            #print(self.id, self.iq)
            self.ser.flushInput()
        except:
            pass