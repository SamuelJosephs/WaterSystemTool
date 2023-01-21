import numpy as np
from time import time, ctime

class node(object):
    def __init__(self, flowRate: float, lastChecked: float, numRepairs: int, longitude: float, latitude: float):
        self.flowRate = flowRate
        self.lastChecked = lastChecked
        self.numRepairs = numRepairs

        self.averageFlowRate = flowRate
        self.avarray = np.zeros((2,))
        


        self.longitude = longitude
        self.latitude = latitude

    percentageChangeFlowRate = 0.




    def update(self,flowRate: float, lastChecked: float, numRepairs: int ) -> None:
        # flowrate: self explanatory, lastChecked: When the pipe was last checked, None if has not been checked since last time,
        self.percentageChangeFlowRate = (self.flowRate - flowRate)/flowRate * 100
        self.flowRate = flowRate
        if lastChecked != None:
            self.lastChecked = lastChecked
        if numRepairs != None:
            self.numRepairs = numRepairs
        #TODO: finish
    









        


    