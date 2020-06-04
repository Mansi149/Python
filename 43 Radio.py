"""
PROBLEM 43
Write a program to print the output of the following poblem statement :-

Characteristics    |   Functionality
---------------------------------------
color              |
brand              |
ACPower            |
headphone          |
                   |
power_led          | power_switch  ( ON / OFF)
mode_led           | mode_switch   ( AM / FM )
frequency          | band_tuner    ( 88 - 108 )
volume             | volume_tuner  ( 1 - 10 )
---------------------------------------

Go to the market and buy a new Radio
Switch ON the radio
Set the mode to FM
Set the frequency to 102.2
Set the volume to 8
Listen to your song
Switch OFF the radio
Destroy the Radio ?
"""
 
class radio:
    color = "Black"
    brand = "Boat"
    ACPower = False
    headphone = True
    
    def __init__(self):
        self.power_led = None
        self.mode_led = None
        self.frequency = 0.0
        self.volume = 0
        print("Play Your Radio")
    def power_switch(self,power_status):
        self.power_led=power_status
        print("Radio is : "+power_status) 
    def mode_switch(self,mode_status):
        self.mode_led=mode_status
        print("Radio Mode is set : "+mode_status)
    def band_tuner(self,freq):
        self.frequency=freq
        print("Radio frequency is set at : ",freq)
    def volume_tuner(self,vol):
        self.volume=vol
        print("Volume set at : ",vol)
        
national_radio=radio()
national_radio.power_switch("ON")
national_radio.mode_switch("FM")
national_radio.band_tuner(93.8)
national_radio.volume_tuner(100)        