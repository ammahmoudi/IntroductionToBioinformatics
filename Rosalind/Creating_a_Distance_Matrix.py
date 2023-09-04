f = open("input.txt", "r")
inputs=[]
string=""
for line in f:
    text=line.strip()
    if text.startswith(">"):
        if string!="":inputs.append(string)
        string=""
    else:
        string+=text
if string!="":inputs.append(string)
    
import numpy as np   

distance_matrix=np.zeros((len(inputs),len(inputs)))
import itertools
for i,j in itertools.product(range(len(inputs)),range(len(inputs))):
    d_n=0
    for l in range(len(inputs[i])):
        if(inputs[i][l]!=inputs[j][l]):d_n+=1
    distance_matrix[i][j]=distance_matrix[j][i]=d_n/len(inputs[0])
    
    
def printMatrixE(a):
   rows = a.shape[0]
   cols = a.shape[1]
   for i in range(0,rows):
      for j in range(0,cols):
         print("%6.5f" %a[i,j],end=" ")
      print()
   
printMatrixE(distance_matrix)
