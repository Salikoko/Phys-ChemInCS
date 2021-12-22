import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
from scipy.interpolate import interpolate
from direction import move_rand
rows,cols = 20,20
p=0.8
s = (rows,cols)

def time_step(nb_iter,temp):
    for k in range(nb_iter):
        lattemp = temp
        for i in range(rows):
            for j in range(cols):
                move_rand(lattemp,i,j,rows,cols,p)
    return lattemp

def EntrCalc(box,rows,cols):
    box = time_step(5,lattice)
    Pi = np.zeros(s)
    Sum = 0
    K  = 1.38 * 10**(-23)
    for i in range(rows):
        for j in range(cols):
            Pi[i][j] = box[i][j]/400
            if Pi[i][j]!=0: 
                Sum+=Pi[i][j]* np.log(Pi[i][j])
    return Sum * (-K)

def BoltCalc(nb_comp,nb_iter,lattice):

    Result = [0] * nb_comp
    for k in range(nb_comp):
        temp = lattice
        temp = time_step(nb_iter,temp)
        #print('\n{}\n'.format(temp))
        Result[k] = EntrCalc(temp,rows,cols)
    ResMean = statistics.mean(Result)
    print(' t_s = {} r = {} '.format(nb_iter,ResMean))
    return ResMean
    #return Result



lattice = np.zeros(s)
for i in range(9,11):
    for j in range(9,11):
        lattice[i][j] = 100

t_s = int(input('Give number of time steps: '))
n_c = 1
#entropy = [0] * n_c
entropy = BoltCalc(n_c,t_s,lattice)
# arrt = [0] * n_c
# for i in range(4):
#     entropy[i] = BoltCalc(n_c,t_s,lattice)
#     arrt[i] = t_s
#     t_s+=5
#EnMean = statistics.mean(entropy)
t_s+=-10


#print('For {} time steps and {} computations,Entropy is {}\n'.format(t_s,n_c,entropy[n_c-1]))
sum = 0
for i in range(20):
    for j in range(20):
        sum+=lattice[i][j]

print('Sum of all dry particles \n{}\n'.format(sum))

plot1 = plt.figure(1)
plt.imshow(lattice, interpolation='nearest',aspect='equal',extent=[-rows,rows,-cols,cols])
plt.xlabel('Entropy = {}\nTime step = {} Number of computations = {}'.format(entropy[3],t_s,n_c))

plot2 = plt.figure(2)
#plt.plot(entropy,arrt)
plt.xlabel('Entropy')
plt.ylabel('Time steps')

# f = interpolate.interp1d(entropy, arrt)
# plot3 = plt.figure(3)
# timeNew = np.arange(0,10,1)
# EntrNew = f(timeNew)
# plt.plot(entropy,t_s,'o',EntrNew,timeNew,'-') 
plt.show()
        lattice[i][j] = 100 
 
t_s = int(input('Give number of time steps: ')) 
n_c = 1 
#entropy = [0] * n_c 
entropy = EntropyCalc(n_c,t_s,lattice) 
# arrt = [0] * n_c 
# for i in range(4): 
#     entropy[i] = BoltCalc(n_c,t_s,lattice) 
#     arrt[i] = t_s 
#     t_s+=5 
#EnMean = statistics.mean(entropy) 
t_s+=-10 
 
 
#print('For {} time steps and {} computations,Entropy is {}\n'.format(t_s,n_c,entropy[n_c-1])) 
sum = 0 
for i in range(20): 
    for j in range(20): 
        sum+=lattice[i][j] 
 
print('Sum of all dry particles \n{}\n'.format(sum)) 
 
plot1 = plt.figure(1) 
plt.imshow(lattice, interpolation='nearest',aspect='equal',extent=[-rows,rows,-cols,cols]) 
plt.xlabel('Entropy = {}\nTime step = {} Number of computations = {}'.format(entropy[3],t_s,n_c)) 
 
plot2 = plt.figure(2) 
#plt.plot(entropy,arrt) 
plt.xlabel('Entropy') 
plt.ylabel('Time steps') 
 
# f = interpolate.interp1d(entropy, arrt) 
# plot3 = plt.figure(3) 
# timeNew = np.arange(0,10,1) 
# EntrNew = f(timeNew) 
# plt.plot(entropy,t_s,'o',EntrNew,timeNew,'-')  
plt.show()
