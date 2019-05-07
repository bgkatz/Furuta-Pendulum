# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *
import math

class absorber():
    def __init__(self, COM):
        self.data = 0
        self.dataVec = [0]
        self.encoderCount0 = 0
        self.encoderCount1 = 0
        self.q0 = 0
        self.q1 = 0
        self.qd0 = 0
        self.qd1 = 0
        self.counter = 0
        self.tau = 0
        try:
            self.ser = serial.Serial(COM, timeout = .05)
            self.ser.baudrate = 115200
            print('conencted to absorber')
        except:
            print('failed to connect to absorber')
            pass
    def getData(self):

        try:
            #self.readQ0()
            #self.readQ1()
            #self.readQD0()
            #self.readQD1()
            self.read_encoders()
            #self.control()
            self.setTorque()

            self.dataVec.append(self.q1)
            
            

        except:
            self.dataVec.append(self.data)
            pass


    def setTorque(self):
        try:

            torque = self.tau
            tb = (pack("f", torque))
            self.ser.write(tb)
            self.ser.write(b'\x01')
        except:
            pass

    def readEncoder0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x06')
                b = self.ser.read(3)
                self.encoderCount0 = (b[1]<<8) + b[0]
            except:
                pass
    def readEncoder1(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x07')
                b = self.ser.read(3)
                self.encoderCount1 = (b[1]<<8) + b[0]
            except:
                pass
    def readQ0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x08')
                b = self.ser.read(5)
                val = b[0:-1]
                q0 = unpack('f', val)
                self.q0 = q0[0]
            except:
                pass
    def readQ1(self):

            try:
                self.ser.write(b'\x00\x00\x00\x00\x09')
                b = self.ser.read(5)
                val = b[0:-1]
                q1 = unpack('f', val)
                self.q1 = q1[0]
            except:
                pass
    def readQD0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x0A')
                b = self.ser.read(5)
                val = b[0:-1]
                qd0 = unpack('f', val)
                self.qd0 = qd0[0]
                #self.ser.flushInput()
            except:
                pass
    def readQD1(self):
            try:
                
                self.ser.write(b'\x00\x00\x00\x00\x0B')
                b = self.ser.read(5)
                val = b[0:-1]
                qd1 = unpack('f', val)
                self.qd1 = qd1[0]
                #self.ser.flushInput()
            except:
                pass
    def readEncoders(self):
            try:
                
                self.ser.write(b'\x00\x00\x00\x00\x0C')
                b = self.ser.read(5)
                self.encoderCount0 = (b[3]<<8) + b[2]
                self.encoderCount1 = (b[1]<<8) + b[0]
                #self.ser.flushInput()
            except:
                pass


    def control(self):
        if(abs(self.q1)> .6):
            c = math.cos(self.q1)
            self.tau = .0001*(c*c*c*c)*self.qd1*(9.81*(1.0-c) - self.qd1*self.qd1*.0075);
        else:
            self.tau = .00*self.qd0 + 2.5*self.q1 + .15*self.qd1;
        self.tau = min(max(-1, self.tau), 1)
