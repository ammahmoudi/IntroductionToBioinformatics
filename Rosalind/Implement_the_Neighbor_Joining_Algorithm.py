import numpy as np
from collections import defaultdict


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


def neighbour_joining_algorithm(distance_matrix, n, nodes=None):

    # first
    if nodes == None:
        nodes = list(range(n))

    if n == 2:

        tree = defaultdict(lambda:dict())
        node_1 = nodes[0]
        node_2 = nodes[1]
        weight = distance_matrix[0][1]
        # add the edge
        tree[node_1][node_2] = weight
        tree[node_2][node_1] = weight
        print(tree.items())
        return tree
    else:

        DPrime = create_DPrime(distance_matrix, n)
        i, j = get_min_ij(DPrime, n)
        delta_matrix = createDelta(distance_matrix, n)

        limb_i = (distance_matrix[i][j]+delta_matrix[i][j])/2
        limb_j = (distance_matrix[i][j]-delta_matrix[i][j])/2

        new_row=[0.5*(distance_matrix[k][i]+distance_matrix[k][j]-distance_matrix[i][j]) for k in range(n)]+[0]

        distance_matrix.append(new_row)
        for l in range(n):
            distance_matrix[l].append(new_row[l])
       # distance_matrix = add_new_row(distance_matrix, n,i,j)
        m = nodes[-1]+1
        print(i,j,m)
        nodes.append(m)
        # distance_matrix = np.delete(distance_matrix, max(i, j), 0)
        # distance_matrix = np.delete(distance_matrix, max(i, j), 1)
        # distance_matrix = np.delete(distance_matrix, min(i, j), 0)
        # distance_matrix = np.delete(distance_matrix, min(i, j), 1)
        distance_matrix=remove(max(i,j),distance_matrix)
        distance_matrix=remove(min(i,j),distance_matrix)
        #distance_matrix=distance_matrix.tolist()
        print(distance_matrix)
        node_i = nodes[i]
        node_j = nodes[j]
        print(node_i,node_j)
        nodes.remove(node_i)
        nodes.remove(node_j)
        tree = neighbour_joining_algorithm(distance_matrix, n-1, nodes)
        tree[i][m] = limb_i
        tree[m][i] = limb_i
        tree[j][m] = limb_j
        tree[m][j] = limb_j
        print("libm ",limb_i,limb_j)
        # print(i,m,limb_i)
        # print(j,m,limb_j)
        print(tree.items())
        return tree


def create_DPrime(distance_matrix, n):
    total_distance = np.sum(distance_matrix, 0)
    DPrime=[[0]*n for dummy in range(n)]
    #DPrime = np.zeros((n, n)).tolist()
    for i in range(n):
        for j in range(i+1, n):
            DPrime[i][j] = (n-2)*distance_matrix[i][j]-total_distance[i]-total_distance[j]
            DPrime[j][i] = DPrime[i][j]
    return DPrime


def get_min_ij(DPrime, n):
    i = -1
    j=-1

    minD = float('inf')
    for _i in range(n):
        for _j in range(_i, n):
            if DPrime[_i][_j] < minD:
                i = _i
                j = _j
                minD = DPrime[i][j]
    return i, j


def createDelta(distance_matrix, n):
    total_distance = np.sum(distance_matrix, 0)
    #delta_matrix = np.zeros((n, n)).tolist()
    delta_matrix=[[0]*n for dummy in range(n)]
    # make a delta in shape of distance_matrix
    for i in range(n):
        for j in range(i+1, n):
            delta_matrix[i][j] = (total_distance[i]-total_distance[j])/(n-2)
            delta_matrix[j][i] = delta_matrix[i][j]
    return delta_matrix


def add_new_row(distance_matrix, n,i,j):
    new_row=[0.5*(distance_matrix[k][i]+distance_matrix[k][j]-distance_matrix[i][j]) for k in range(n)]+[0]

    distance_matrix.append(new_row)
    for l in range(n):
        distance_matrix[l].append(new_row[l])

#     row_new = [(distance_matrix[k][i]+distance_matrix[k][j] -
#                 distance_matrix[i][j])*0.5 for k in range(n)]
#     # print(row_new)
#     # print(distance_matrix)
#     distance_matrix=np.vstack([distance_matrix,row_new])
    
#     row_new=row_new+[0]
#   #  print(row_new)
#     distance_matrix=distance_matrix.tolist()

#     for l in range(len(row_new)):
#         distance_matrix[l].append(row_new[l])
#     distance_matrix=np.array(distance_matrix)
 #   print(distance_matrix)
    
    return distance_matrix

def printAdj(adj):
    for node_1,edges in sorted(adj.items()):
        for node_2,weight in edges.items():
            print(str(node_1)+"->"+str(node_2)+":"+str((weight)))

def remove(i,D):
    D_new=[]
    for j in range(len(D)):
        if j!=i:
            D_new.append([D[j][k] for k in range(len(D[j])) if k!=i])
    return D_new   
if __name__ == "__main__":
   n,distance_matrix=read('21_input.txt')
#
  # print(distance_matrix)
   printAdj(neighbour_joining_algorithm(distance_matrix.tolist(),n))

