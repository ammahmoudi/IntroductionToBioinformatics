import numpy as np
def read(file_name):
    file=open(file_name,'r')
    lines=[]
    #read all lines
    for line in file:
        lines.append(line.strip())
    #set n
    n=int(lines.pop(0))
    #make distance matrix
    distance_matrix=np.zeros((n,n))
    for i in range(n):
        #make variables
        temp_row=lines[i].split()
        for k in range(n):
            distance_matrix[i][k]=int(temp_row[k])
    return n,distance_matrix

def calc_limb_length(distance_matrix, n, j):
    min_distance = float("inf")

    i = 1 if j == 0 else j - 1

    for k in range(n):
        if k != i and k != j:
             distance = (distance_matrix[i][j] + distance_matrix[j][k] - distance_matrix[i][k])/2
             min_distance=min(distance,min_distance)
            
    return int(min_distance)

def additive_phylogeny(distance_matrix,n,tree,real_N):
    def find_ikn(DD):
        for i in range(n):
            for k in range(n):
                if DD[i][k]==DD[i][n-1]+DD[n-1][k] and i!=k:
                    return(i,k,n-1,DD[i][n-1])

   # print("n ",n)
  #  print("tree",tree)
    # print("dist",distance_matrix)
    if n==2:
        node_1=0
        node_2=1
        weight=distance_matrix[0][1]
        if node_1 not in tree: tree[node_1]=dict()
        if node_2 not in tree: tree[node_2]=dict()
        #add the edge
        tree[node_1][node_2]=weight
        tree[node_2][node_1]=weight
        return tree,real_N
    else:
        limb_length=calc_limb_length(distance_matrix,n,n-1)
      #  print("limb:",limb_length)
       # print(distance_matrix)
        for j in range(n-1):
            distance_matrix[j][n-1] -= limb_length
            distance_matrix[n-1][j] = distance_matrix[j][n-1]
       # print(distance_matrix)
        #find i n k
        # for _i in range(n):
        #     for _k in range(n):
        #         if (_i!=_k and distance_matrix[_i][_k]==distance_matrix[_i][n-1]+distance_matrix[n-1][_k]):
        #             i=_i
        #             k=_k   
        i,k,node,x=find_ikn(distance_matrix)
       # x=distance_matrix[i][n-1]
        #print(distance_matrix[3][2])
       # print("i,k,m=",i,",",k,",",n-1)
       # print("x:",x)
       # print("-")

        distance_matrix_trimmed=np.delete(distance_matrix,n-1,0)
        distance_matrix_trimmed=np.delete(distance_matrix_trimmed,n-1,1)

        tree,real_N=additive_phylogeny(distance_matrix_trimmed,n-1,tree,real_N)

       # print("last ",tree)
        #find a path from i to k
        has_path,path=get_path(tree,i,k)
       # print("has path:",has_path)
        #check if v is found in tree or not
        #c0 last node , c1 is next node
        found,c0,c1,d0,d1=find_v_postition(path,x)
       # print("c0",c0)
       # print("c1",c1)

        if found:
            v=c0
            if v not in tree: tree[v]=dict()
            if n-1 not in tree: tree[n-1]=dict()
            #print("Add",tree)
            tree[n-1][v]=limb_length
            tree[v][n-1]=limb_length
            # print("v:",v)
           # real_N+=1
        else:
            v=real_N
            real_N+=1
            # print("c0",c0)
            # print("c1",c1)
            # weight_i=limb_length(distance_matrix,n,i)
            # weight_k=limb_length(distance_matrix,n,k)
         #   print("v:",v)
            if c0 not in tree: tree[c0]=dict()
            if c1 not in tree: tree[c1]=dict()
          #  print(tree[c0])
            del(tree[c0][c1])
            del(tree[c1][c0])
            if v not in tree: tree[v]=dict()
            tree[v][c0]=x-d0
            tree[c0][v]=x-d0

            tree[v][c1]=d1-x
            tree[c1][v]=d1-x
        if v not in tree: tree[v]=dict()
        if n-1 not in tree: tree[n-1]=dict()
        tree[n-1][v]=limb_length
        tree[v][n-1]=limb_length

        return tree,real_N

def printAdj(adj):
    for node_1,edges in sorted(adj.items()):
        for node_2,weight in edges.items():
            print(str(node_1)+"->"+str(node_2)+":"+str(int(weight)))


    
def get_path(adj,i,j,path=dict()):
   # print("treeee",adj)

    if i not in adj.keys() : return False,dict()
    if len(path)==0:
        path[i]=dict()
        path[i]=0
    # print(i)
    # print(j)
    # print(adj)
    for _j,weight in adj[i].items():
        if _j in path.keys():
            continue
        temp_path={**path,**{_j:weight}}
      #  print("temp",temp_path)
        if _j==j : 
            return True,temp_path
        else:
            has_path,temp_path=get_path(adj,_j,j,temp_path)
            if has_path: return True,temp_path
    return False,dict()

def find_v_postition(path,x):
    distance=0
  #  print("path: ",path)
    for node,weight in path.items():
        distance_prev=distance
        distance+=weight
        if distance==x:
            return True,node,node,distance_prev,distance
        if distance>x: return False,node_prev,node,distance_prev,distance
        node_prev=node
    return False,node_prev,node,distance_prev,distance










    
if __name__ == "__main__":
   n,distance_matrix=read('19_input.txt')
   printAdj(additive_phylogeny(distance_matrix,n,dict(),n)[0])
