import random

def dir_sel(lattice,x,y,k,p,rows,cols):
    lattice[x][y]+=-1
    if(k==4):
        if (p<1/k) and (y<cols-1):
            lattice[x][y+1]+=1                 
        elif (p<1*2/k) and (x<rows-1):
            lattice[x+1][y]+=1
                
        elif (p<1*3/k) and (y>0):
            lattice[x][y-1]+=1
                
        elif (p<1) and (x>0):
            lattice[x-1][y]+=1 
    if(k==3):
        if(y==cols-1) or (y==0):
            if (p<1/3):
                lattice[x+1][y]+=1
            elif (p<2/3):
                lattice[x-1][y]+=1    
            elif (y==0): 
                lattice[x][y+1]+=1
            else: 
                lattice[x][y-1]+=1
        if(x==rows-1) or (x==0):
            if (p<1/2):
                lattice[y+1][y]+=1
            elif (p<2/3):
                lattice[y-1][y]+=1
            elif (x==0): 
                lattice[x+1][y]+=1
            else: 
                lattice[x-1][y]+=1
    if (k==2):
        if((x==0 and y==cols-1) or (x==rows-1 and y==cols-1)):
            if (p<1/2):
                lattice[x][y-1]+=1
            elif (x==0):
                lattice[x+1][y]+=1
            else:
                lattice[x-1][y]+=1
        if((x==0 and y==0) or (x==rows-1 and y==0)):
            if (p<1/2):
                lattice[x][y+1]+=1
            elif (x==0):
                lattice[x+1][y]+=1
            else:
                lattice[x-1][y]+=1


def move_rand(lattice,x,y,rows,cols,p):
    
    if(lattice[x][y]!=0):
        if  (x==0 and y==0) or (x==rows-1 and y==cols-1) or (x==0 and y==cols-1) or (x==rows-1 and y==0):
            k=2
        elif x==0 or y==0 or x==rows-1 or y== cols-1 :
            k=3
        else:
            k=4

        for i in range(int(lattice[x][y])):
            step_res = random.uniform(0,1)
            if(step_res<p): 
                step_res = random.uniform(0,1)
                dir_sel(lattice,x,y,k,step_res,rows,cols)