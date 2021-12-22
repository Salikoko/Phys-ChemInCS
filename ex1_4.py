import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
import math 

#function to provide the final position of a particle by generating random number between 0 and 1, with given starting point, chance of succes and number of steps
def FinalPosition(distance,p,nb_steps):
    temp = distance
    for i in range(nb_steps):
        step_res = random.uniform(0,1)
        if step_res<p:
            temp+=1
        else:
            temp+=-1
    return temp
#function to generate list of end points, given start point, number steps , iterations , probability
def EndPoint(start_p,nb_steps,iter,p):
    roadVal = [None] * iter
    for i in range(iter):
        roadVal[i] = FinalPosition(start_p,p,nb_steps)
        
    return roadVal

steps = [20,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
iter = 100
prob = 0.75
start_point = 0
actual_results = [statistics.stdev(EndPoint(start_point,steps[i],iter,prob)) for i in range(len(steps))]
print (actual_results)
assumption_results = [math.sqrt(steps[i]) for i in range(len(steps))]
print (assumption_results)

#plot graphs
plt.plot(steps, actual_results, 'o', label='results')
plt.plot(steps, assumption_results, '-', label='sqrt')
plt.legend()
plt.xlabel('N - Number of steps')
plt.ylabel('Std(N)')
plt.title('Graph for the relationship between std and N')
plt.show()