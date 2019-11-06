# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *
import math
import time

class pendulum():
    def __init__(self, COM, DT):
        self.data = 0
        self.dataVec = [0]
        self.dt = DT

        self.encoderCount0 = 0
        self.encoderCount1 = 0
        self.q0 = 0
        self.q1 = 0
        self.qd0 = 0
        self.qd1 = 0
        self.counter = 0
        self.tau = 0
        self.kq0 = 0
        self.kqd0 = 0
        self.kq1 = 0
        self.kqd1 = 0
        self.q0des = 0
        self.q1des = 0
        self.qd0des = 0
        self.qd1des = 0
        self.first_read = 1;
        self.q1_control = 0;

        self.e0_rotations = 0
        self.e1_rotations = 0
        self.e0_old = 0
        self. e1_old = 0
        self.q0_old = 0
        self.q1_old = 0

        self.CPR0 = 20000
        self.CPR1 = 16384


        try:
            self.ser = serial.Serial(COM, timeout = .05)
            self.ser.baudrate = 115200
            print('conencted to pendulum')
        except:
            print('failed to connect to pendulum')
            pass
    def getData(self):

        try:

            #self.readQ1()
            #self.readQD0()
            #self.readQD1()
            self.readEncoders()
            self.stateFromEncoder()
            self.control()
            self.setTorque()

            self.dataVec.append(self.q1)

        except:
            self.dataVec.append(self.data)
            pass


    def setTorque(self):
        try:
            b = (pack("f", self.tau))
            self.ser.write(b)
            self.ser.write(b'\x01')
        except:
            pass


    def readEncoder0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x02')
                b = self.ser.read(3)
                self.encoderCount0 = (b[1]<<8) + b[0]

            except:
                pass
    def readEncoder1(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x03')
                b = self.ser.read(3)
                self.encoderCount1 = (b[1]<<8) + b[0]
            except:
                pass
    def readQ0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x04')
                b = self.ser.read(5)
                val = b[0:-1]
                q0 = unpack('f', val)
                self.q0 = q0[0]
            except:
                pass
    def readQ1(self):

            try:
                self.ser.write(b'\x00\x00\x00\x00\x05')
                b = self.ser.read(5)
                val = b[0:-1]
                q1 = unpack('f', val)
                self.q1 = q1[0]
            except:
                pass
    def readQD0(self):
            try:
                self.ser.write(b'\x00\x00\x00\x00\x06')
                b = self.ser.read(5)
                val = b[0:-1]
                qd0 = unpack('f', val)
                self.qd0 = qd0[0]
            except:
                pass
    def readQD1(self):
            try:
                
                self.ser.write(b'\x00\x00\x00\x00\x07')
                b = self.ser.read(5)
                val = b[0:-1]
                qd1 = unpack('f', val)
                self.qd1 = qd1[0]
            except:
                pass
    def readEncoders(self):
            #try:
                
            self.ser.write(b'\x00\x00\x00\x00\x08')
            b = self.ser.read(5)
            self.encoderCount1 = (b[3]<<8) + b[2]
            self.encoderCount0 = (b[1]<<8) + b[0]
            self.ser.flushInput()

    def enable(self):
            #try:
        self.ser.write(b'\x00\x00\x00\x00\x09')
    def disable(self):
            #try:
        self.ser.write(b'\x00\x00\x00\x00\x0A')
    
            #except:
            #    pass

    def control(self):
        self.q1_control = math.fmod(self.q1, 2*math.pi)
        if(self.q1_control <0):
            self.q1_control = self.q1_control + 2*math.pi
        if(abs(self.q1_control-math.pi)> .7):
            c = math.cos(self.q1_control-math.pi)
            self.tau = .000075*(c*c*c*c)*self.qd1*(9.81*(1.0-c) - self.qd1*self.qd1*.0075);
        else:
            self.tau = .25*0.05*self.qd0 + .25*1.5*(self.q1_control-math.pi) + .25*.1*self.qd1;

        #self.tau = 1*(5 - self.q0) + .05*(-self.qd0)
        self.tau = min(max(-.2, self.tau), .2)

    def stateFromEncoder(self):
        
        if(self.first_read != 0):
            if((self.encoderCount0 - self.e0_old) > (self.CPR0/2)):
                self.e0_rotations -= 1
            elif((-self.encoderCount0 + self.e0_old) > (self.CPR0/2)):
                self.e0_rotations += 1
            if((self.encoderCount1 - self.e1_old) > (self.CPR1/2)):
                self.e1_rotations -= 1
            elif((-self.encoderCount1 + self.e1_old) > (self.CPR1/2)):
                self.e1_rotations += 1
            self.first_read = 0
        
        self.q0 = 2*math.pi*self.e0_rotations + 2*math.pi*self.encoderCount0/self.CPR0
        self.q1 = 2*math.pi*self.e1_rotations + 2*math.pi*self.encoderCount1/self.CPR1


        self.qd0 = (self.q0 - self.q0_old)/(self.dt*2)
        self.qd1 = (self.q1 - self.q1_old)/(self.dt*2)
        self.e0_old = self.encoderCount0
        self.e1_old = self.encoderCount1
        self.q0_old = self.q0
        self.q1_old = self.q1
       