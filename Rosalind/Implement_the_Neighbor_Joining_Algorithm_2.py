import numpy as np
def read(file_name):
    file = open(file_name, 'r')
    lines = []
    # read all lines
    for line in file:
        lines.append(line.strip())
    # set n
    n = int(lines.pop(0))
    # make distance matrix
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        # make variables
        temp_row = lines[i].split()
        for k in range(n):
            distance_matrix[i][k] = int(temp_row[k])
    return n, distance_matrix



def neighbour_joining_algorithm(distance_matrix,n,node_list=None):
      
    if node_list==None:
        node_list=list(range(n))
        
    if n==2:
        from collections import defaultdict

        adj_matrix=defaultdict(lambda:dict())
        adj_matrix[node_list[0]][node_list[1]]=distance_matrix[0][1]
        adj_matrix[node_list[1]][node_list[0]]=distance_matrix[0][1]

        return adj_matrix
    else:
        
        DPrime=create_DPrime(distance_matrix,n)
        i,j=get_min_ij(DPrime,n)
        Delta=createDelta(distance_matrix,n)   
        limbLength_i=(distance_matrix[i][j]+Delta[i][j])/2
        limbLength_j=(distance_matrix[i][j]-Delta[i][j])/2

        distance_matrix=add_new_row(distance_matrix,n,i,j)

        m=node_list[-1]+1
        #print(i,j,m)
        node_list.append(m)
        distance_matrix = np.delete(distance_matrix, max(i, j), 0)
        distance_matrix = np.delete(distance_matrix, max(i, j), 1)
        distance_matrix = np.delete(distance_matrix, min(i, j), 0)
        distance_matrix = np.delete(distance_matrix, min(i, j), 1)
        distance_matrix=distance_matrix.tolist()
        #print(distance_matrix)
        node_i=node_list[i]
        node_j=node_list[j]
        #print(node_i,node_j)
        node_list.remove(node_i)
        node_list.remove(node_j)
        adj_matrix=neighbour_joining_algorithm(distance_matrix,n-1,node_list)
        adj_matrix[node_i][m]=limbLength_i
        adj_matrix[m][node_i]=limbLength_i
        adj_matrix[node_j][m]=limbLength_j
        adj_matrix[m][node_j]=limbLength_j

        return adj_matrix
def printAdj(adj):
    for node_1,edges in sorted(adj.items()):
        for node_2,weight in edges.items():
            print(str(node_1)+"->"+str(node_2)+":"+str((weight)))
def create_DPrime(distance_matrix,n):
    total_distance=np.sum(distance_matrix,0).tolist()
    DPrime=[[0]*n for dummy in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            DPrime[i][j]=(n-2)*distance_matrix[i][j]-total_distance[i]-total_distance[j]
            DPrime[j][i]= DPrime[i][j]
    return DPrime
def get_min_ij(DPrime,n):
    i=-1
    j=-1
    minD=float('inf')
    for ii in range(n):
        for jj in range(ii,n):
            if  DPrime[ii][jj]<minD:
                i=ii
                j=jj
                minD= DPrime[i][j]
    return i,j
def createDelta(distance_matrix,n):
    total_distance=np.sum(distance_matrix,0).tolist()
    Delta=[[0]*n for dummy in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            Delta[i][j]=(total_distance[i]-total_distance[j])/(n-2)
            Delta[j][i]=Delta[i][j]
    return Delta    
def add_new_row(distance_matrix, n,i,j):

    row_new = [(distance_matrix[k][i]+distance_matrix[k][j] -
                distance_matrix[i][j])*0.5 for k in range(n)]
    # print(row_new)
    # print(distance_matrix)
    distance_matrix=np.vstack([distance_matrix,row_new])
    
    row_new=row_new+[0]
  #  print(row_new)
    distance_matrix=distance_matrix.tolist()

    for l in range(len(row_new)):
        distance_matrix[l].append(row_new[l])
    
  # print(distance_matrix)
    
    return distance_matrix
if __name__=='__main__':
    n,distance_matrix=read('21_input.txt')
    adj_matrix=neighbour_joining_algorithm(distance_matrix.tolist(),n)
    printAdj(adj_matrix)