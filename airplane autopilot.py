# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:04:00 2023

@author: riley.barrett
"""

class aircraft:
    def __init__(self,name,max_speed,max_altitude):
        self.name = name
        self.max_speed=max_speed
        self.max_altitude=max_altitude
        self.current_speed=0
        self.current_altitue=0
        self.is_flying=False
    def take_off(self):
        if not self.flying:
            print(f"{self.name} takes off.")
            
            self.is_flying=True
            self.current_speed=200
            self.current_altitude=1000
        else:
            print(f"{self.name}is already flying")
            
    def gain_altitude(self,altitude_gain):
        if self.is_flying:
            self.current_altitude+=altitude_gain
            print(f"{self.name} gained {altitude_gain}feet of altitude.currentaltitude:{self.current_altitude}feet.")
        else:
            print(f"{self.name}cannot gain altitude while on the ground")
    def decrease_speed(self,speed_loss):
        if self.is_flying:
            self.current_speed -=speed_loss
            print("{self.name}decreased speed by{speed_loss knots.currentspeed:{self.current_speed}knots:")
        else:
            print(f"{self.name}cannot decrease speed while on the ground")
    def land(self):
        if self.is_flying:
            print(f"{self.name}lands.")
            self.is_flying=False
            self.current_speed=0
            self.current_altitude=0
        else:
            print(f"{self.name}is already on the ground")
            
            my_aircraft=aircraft("my aircraft",500, 35000)
            my_aircraft.take_off()
            my_aircraft.gain_altitude(5000)
            my_aircraft.decrease_speed(100)
            my_aircraft.land()