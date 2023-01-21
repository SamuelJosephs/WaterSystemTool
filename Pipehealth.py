import numpy as np

def pipehealth(loc1):
    #generates some random numbers
    #to be given more physical interpretation later
    mu, sigma = 1,0.95
    FR = np.random.uniform(mu,sigma)
    NumBlock = np.random.uniform(mu,sigma)
    DetRate = np.random.uniform(mu,sigma)
    TimeCheck = np.random.uniform(mu,sigma)
    return (FR,NumBlock,DetRate,TimeCheck)

#testcase = pipehealth([0,0])
#print(testcase)


loc = [[0,0],[1,1],[1,0],[2,3]]

pipey = []

for i in range(len(loc)-1):
   
    pipey = [pipehealth(loc[i]), 
            pipehealth(loc[i+1])]
    pipey.append(pipey)


print(pipey)
