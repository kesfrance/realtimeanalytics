import random
from datetime import datetime
import time
import numpy as np 


import pdb

MSG_TXT = "{\"deviceId\": \"myPythonDevice\",\"site\": \"%s\", \"tonnage\": %.2f,\"tph_setpoint\": %d,\"feedingtime\": %.1f, \"TPH\": %d, \"comodity\": \"%s\"}"

PREVIOUS_TPH = 0
PREVIOUS_TONNAGE = 0
TPH_setpoints = {'Wheat': 900,
                 'Barley': 800,
                 'BarleyMlt': 600,
                 'Oats' : 750,
                 'Canola': 750,
                 'Lupin': 600,
                }
class PLC:
    def __init__(self, site, comodity, tph_setpoint):
        self.site = site
        self.tph_setpoint = tph_setpoint
        self.comodity = comodity
    
    def simulate_data(self, duration):
        """simulate plc data"""
        tonnage = 0
        tn = np.random.uniform(0.20, 0.25)
        tonnage = round(tn *duration, 1)
        tph = round((3600/(duration) ) * tonnage)
        return (self.site, int(tonnage), int(self.tph_setpoint), 
                round(duration, 1), int(tph), self.comodity)
    
    def get_data(self, starttime):
        """returns value of simulated data every 5 seconds"""
        sampling_duration = time.time() - starttime
        data = ()
        if sampling_duration:
            data = self.simulate_data(sampling_duration)
        return data

    def run_loop(self):
        """returns current TPH value of equipment"""
        starttime=time.time()
        pdb.set_trace()
        while True:
            dataout = self.get_data(starttime)
            if dataout:
           # print("tick start time is: %d" %sampling_duration)
                message = MSG_TXT % dataout
                # import json
                # message = json.dumps(message)
                print(message)
                time.sleep(10.0 - ((time.time() - starttime) % 10.0))
            


if __name__== "__main__":  
    plc1 = PLC("Kwinana", "Wheat", "900")

    plc1.run_loop()
        
