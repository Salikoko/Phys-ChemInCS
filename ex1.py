import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
#function to generate random number between 0 and 1, with given starting point, chance of succes and number of steps
def roll_dice(distance,p,nb_steps):
    temp = distance
    for i in range(nb_steps):
        step_res = round(random.uniform(0,1),2)
        if step_res<p:
            temp+=1
        else:
            temp+=-1
    return temp
#function to generate list of end points, given start point, number steps , iterations , probability
def EndPoint(start_p,nb_steps,iter,p):
    roadVal = [None] * iter
    for i in range(iter):
        roadVal[i] = roll_dice(start_p,p,nb_steps)
        
    return roadVal



steps = int(input('Enter number of steps for a drunk walker: '))
iter = int(input('Enter number of iterations: '))
prob = float(input('Enter probability value: '))
start_point = 0
results = EndPoint(start_point,steps,iter,prob)

SD = round(statistics.stdev(results),2)     #Standard devaiation
MN = round(statistics.mean(results),2)      #Mean

first_part = 0
second_part = 0
third_part = 0

for i in range(iter):
    if (results[i] >= MN - SD) and (results[i] <= MN + SD):
        first_part += 1
        second_part += 1
        third_part += 1
    elif (results[i] >= MN - 2*SD) and (results[i] <= MN + 2*SD):
        second_part += 1
        third_part += 1
    elif (results[i] >= MN - 3*SD) and (results[i] <= MN + 3*SD):
        third_part += 1

print('Standard deviaton {}\nMean {}'.format(SD,MN))
# the number of records is 100, so division by it turns to 1 after multiplying by 100%
# so the counted values are equal to the percentage
print('Percentage of values in first partition: {}'.format(first_part))
print('Percentage of values in second partition: {}'.format(second_part))
print('Percentage of values in third partition: {}'.format(third_part))
#plot histograph
n, bins, patches = plt.hist(x=results, bins='auto', color='g',alpha=0.6, rwidth=0.8)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Final position\nSigma={}, mean={}'.format(SD,MN))
plt.ylabel('Repetition')
plt.title('Histogram for {} steps, {} iterations'.format(steps,iter))
plt.show()