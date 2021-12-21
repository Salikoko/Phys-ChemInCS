import matplotlib.pyplot as plt
import numpy as np
import random
import statistics

rows,cols = 20,20
p=0.8
s = (rows,cols)

def move_rand(lattice,x,y):
    if(lattice[x][y]!=0):
        step_res = random.uniform(0,1)
        if  (x>0 and y>0) :
            k=4
        elif (x==0 and y==0) or (x==rows-1 and y==cols-1) or (x==0 and y==cols-1) or (x==rows-1 and y==0):
            k=2
        else:
            k=3
        #print('\n\n\n{}'.format(k))
        if(step_res<p): 
            lattice[x][y]+=-1
            if (step_res<p/k) and (y<cols-1):
                lattice[x][y+1]+=1
                     
            elif (step_res<p/k*2) and (x<rows-1):
                lattice[x+1][y]+=1
                
            elif (step_res<p/k*3) and (y>0):
                lattice[x][y-1]+=1
                
            elif (step_res<p) and (x>0):
                lattice[x-1][y]+=1
                
        
        

def time_step(nb_iter):
    for k in range(nb_iter):
        #plt.imshow(lattice, interpolation='none')
        #plt.pause(0.15)
        for i in range(rows):
            for j in range(cols):
                move_rand(lattice,i,j)

def BoltCalc(nb_comp,nb_iter):
    time_step(nb_iter)
    Pi = np.zeros(s)
    Result = 0
    K  = 1.38 * 10**(-23)
    for k in range(nb_comp):
        for i in range(rows):
            for j in range(cols):
                Pi[i][j] = lattice[i][j]/400
                if Pi[i][j]!=0: Result+=Pi[i][j]* np.log(Pi[i][j])
        Result = Result/nb_comp * (-K) 
        return Result



lattice = np.zeros(s)

for i in range(9,11):
    for j in range(9,11):
        lattice[i][j] = 100

#H = np.array(lattice)
print('Bolt result is {}\n'.format(BoltCalc(25,50)))
sum = 0
for i in range(20):
    for j in range(20):
        sum+=lattice[i][j]
#print('{} {} {} {}'.format(f,s,t,fo))
print('Sum is \n{}\n'.format(sum))
plt.imshow(lattice, interpolation='none')
plt.show()

