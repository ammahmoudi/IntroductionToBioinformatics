import queue as Queue
import numpy as np
def read(file_name):
    file=open(file_name,'r')
    lines=[]
    #read all lines
    for line in file:
        lines.append(line.strip())
    #set n
    n=int(lines[0])
    #make adjency dictianory
    adj=dict()
    for line in lines[1:]:
        #make variables
        temp_split=line.split(':')
        temp_nodes=temp_split[0].split('->')
        node_1=int(temp_nodes[0])
        node_2=int(temp_nodes[1])
        weight=int(temp_split[1])
        #make a empty value for node_1 for the first time
        if node_1 not in adj: adj[node_1]={}
        #add the edge
        adj[node_1][node_2]=weight
    return n,adj

def bfs(start,adj,distance_matrix):
   # distances=np.zeros(len(adj[start]))
    queue=Queue.Queue()
    queue.put(start)
    while not queue.empty():
        current_node=queue.get()
        for node, weight in adj[current_node]:
          if(distance_matrix[start][node]==0 and start!=node):
              #  distances[node]=distances[current_node]+weight
            distance_matrix[start][node]=distance_matrix[start][current_node]+weight
            queue.put(node)
    return distance_matrix
def calculateDistanceMatrix(n,adj):
    distance_matrix=np.zeros((len(adj),len(adj)))
    #print(len(adj))
    for i in range(n):
        distance_matrix=bfs(i,adj,distance_matrix)
    return distance_matrix
def printSpaceSeperatedMatrix(matrix,n):
        for d in matrix[0:n]:
            print(' '.join([str(int(i)) for i in d[0:n]]))

def get_path(adj,i,j,path=dict()):
    #print(adj)
    # if len(path)==0:
    #     path[i].append((j,adj[i][j]))
    for _j,weight in adj[i].items():
        if _j in path.keys():
            continue
        temp_path={**path,**{_j:weight}}
        #print(temp_path)
        if _j==j : 
            return True,temp_path
        else:
            has_path,temp_path=get_path(adj,_j,j,temp_path)
            if has_path: return True,temp_path
    return False,dict()



if __name__ == "__main__":
   n,adj=read('17_input.txt')
   #print(adj)
   print(get_path(adj,0,1,dict()))
#    matrix=calculateDistanceMatrix(n,adj)
#    printSpaceSeperatedMatrix(matrix,n)
   #print(matrix)
   

        


