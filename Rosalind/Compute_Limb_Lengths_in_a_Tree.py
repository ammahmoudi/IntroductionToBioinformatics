import numpy as np
def read(file_name):
    file=open(file_name,'r')
    lines=[]
    #read all lines
    for line in file:
        lines.append(line.strip())
    #set n
    n=int(lines.pop(0))
    #set j
    j=int(lines.pop(0))
    #make distance matrix
    distance_matrix=np.zeros((n,n))
    for i in range(n):
        #make variables
        temp_row=lines[i].split()
        for k in range(n):
            distance_matrix[i][k]=int(temp_row[k])
    return n,j,distance_matrix

def limb_length(distance_matrix, n, j):
    min_distance = float("inf")

    i = 1 if j == 0 else j - 1

    for k in range(n):
        if k != i and k != j:
             distance = (distance_matrix[i][j] + distance_matrix[j][k] - distance_matrix[i][k])/2
             min_distance=min(distance,min_distance)
            
    return int(min_distance)

if __name__ == "__main__":
   n,j,distance_matrix=read('18_input.txt')
   limb_length=limb_length(distance_matrix,n,j)
   print(limb_length)
