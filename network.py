import numpy as np
import pandas as pd
from time import time, ctime
from node import node
import numpy.random as rand


class network:
    def __init__(self,nodes: np.ndarray, edges: np.ndarray, PH = 0.) -> None:
        # nodes are a (n,) dimensional array of nodes, edges are a (n,n) dimensional array of integers keeping track of which nodes are connected to each other
        self.nodes = nodes
        self.edges = edges
        self.PH = PH
        self.numNodes = len(nodes)

    def updateNodes(self,flowRates: np.ndarray):
        if len(flowRates) != self.numNodes:
            AssertionError("cannot update nodes with array of different dimension\n")
        for i in range(0,self.numNodes):
            self.nodes[i].update(flowRates[i],None,None)# Slow but I'm not restructuring the entire program for this
    
    def getNodesDownStream(self, i: int,n: int): 
        # Returns n downstream nodes from node i using depth first search
        counter = 0
        output = []
        stack = []
        discovered = []
        discovered.append(i)
        stack.append(self.edges[i]) # edges for the i'th node
        onNode = i
        while len(stack) > 0:
            if counter >= n:
                break
            counter += 1
            v = stack.pop()
            
            if onNode in discovered:
                continue
            output.append(self.nodes[onNode])
            for k in range(0,len(v)):
                if self.edges[onNode][k] == 0:
                    continue
                stack.append(self.edges[k])
                discovered.append(k)
            onNode = discovered[-1]
        return output





    

def genRandNetwork(n: int) -> network:
    # Generate random netwrok with n nodes
    array = np.ndarray((n,),dtype = object)
    edges = rand.randint(0,high = 2, size = (n,n)) # high is exclusive
    # set the trace = 0 so that there no node is connected to itself
    for i in range(0,n):
        edges[i][i] = 0
    
    flowrate = rand.uniform(size = (n,)) * 100
    lastChecked = [time() for i in range(0,n)]
    numRepairs = rand.randint(0,high = 30,size = (n,))
    longitude = rand.uniform(53.,55.,size = (n,)) # from google maps, should be roughly the area we want feel free to change
    latitude = rand.uniform(-1.57,-1.58,size = (n,))
    for i in range(0,n):
        array[i] = node(flowrate[i],lastChecked[i],numRepairs[i],longitude[i],latitude[i])
    output = network(array,edges)
    print(edges)
    return output


testNet = genRandNetwork(10)
testDownStream = testNet.getNodesDownStream(1,100)
print(testDownStream)



def randUpdateNetwork(net: network,pertubationScale: float) -> None: #In place mutation of net
    # Randomly perturb the flow rate 
    randPertubation = rand.randn(net.numNodes) * pertubationScale
    net.updateNodes(randPertubation)
    
    

    



        
#hello world



        




