#!/usr/bin/python
# -*- coding:utf-8 -*-


import time
import DAC8532
import RPi.GPIO as GPIO


def dac_control():
    try:
        print("Program start\r\n")
        
        DAC = DAC8532.DAC8532()
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 0)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 0)
        

        while(1):
            for i in range(0,50,1):
                DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 5.0 * i / 55)
                DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 5.0 - 5.0 * i / 50)
                time.sleep(0.2)
                
            for i in range(0,50,1):
                DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 5.0 * i / 50)
                DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 5.0 - 5.0 * i / 50)
                time.sleep(0.2)


    except :
        DAC.DAC8532_Out_Voltage(DAC8532.channel_A, 0)
        DAC.DAC8532_Out_Voltage(DAC8532.channel_B, 0)
        GPIO.cleanup()
        print ("\r\nProgram end     ")
        exit()


if __name__ == "__main__":
    dac_control()