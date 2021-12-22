import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
from scipy.interpolate import interpolate
from direction import move_rand
rows,cols = 20,20
p=0.8
s = (rows,cols)

def time_step(nb_iter,temp):   #proceed movement of all particles in nb_iter time step
    for k in range(nb_iter):
        lattemp = temp
        for i in range(rows):
            for j in range(cols):
                move_rand(lattemp,i,j,rows,cols,p)  #function to calculate movement of each particle
    return lattemp

def EntropyCalc(box,rows,cols):  #determine entropy of lattice 
    Pi = np.zeros(s)
    Sum = 0
    K  = 1.38 * 10**(-23)
    for i in range(rows):
        for j in range(cols):
            Pi[i][j] = box[i][j]/400
            if Pi[i][j]!=0: 
                Sum+=Pi[i][j] * np.log(Pi[i][j])
    return Sum * (-K)

def MinnEntropy(nb_comp,nb_iter,lattice):

    Result = [0] * nb_comp
    for k in range(nb_comp):
        temp = lattice
        temp = time_step(nb_iter,temp)
        #print('\n{}\n'.format(temp))
        Result[k] = EntropyCalc(temp,rows,cols)
    ResultMin = min(Result)
    
    return ResultMin
    



lattice = np.zeros(s)
for i in range(9,11):
    for j in range(9,11):
        lattice[i][j] = 100

t_s = 5
n_c = 25
size = 10
entropy = [0] * size
arrt = [0]*size
for i in range(size):
    entropy[i] = MinnEntropy(n_c,t_s,lattice)
    arrt[i] = t_s
    t_s+=1
EntropyMean = statistics.mean(entropy)


print('For {} time steps and {} computations,Entropy is {}\n'.format(t_s,n_c,entropy[1]))
sum = 0
for i in range(20):
    for j in range(20):
        sum+=lattice[i][j]

print('Sum of all dry particles \n{}\n'.format(sum))

plot1 = plt.figure(1)
plt.imshow(lattice, interpolation='nearest',aspect='equal',extent=[-rows,rows,-cols,cols])
plt.xlabel('Entropy = {}\nTime step = {} Number of computations = {}'.format(entropy[1],t_s,n_c))

plot2 = plt.figure(2)
plt.plot(entropy,arrt)
plt.xlabel('Entropy')
plt.ylabel('Time steps')


plot3 = plt.figure(3)

f = interpolate.interp1d(arrt, entropy,axis =0,fill_value='extralopate')
timeNew = np.linspace(9,10,10)
EntropyNew = f(timeNew)
plt.plot(arrt,entropy,'o',timeNew,EntropyNew,'-') 
plt.show()
