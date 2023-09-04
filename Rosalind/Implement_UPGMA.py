import numpy as np
import math
from collections import defaultdict
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
    return n,distance_matrix.tolist()

class Cluster(object):

    def __init__(self, id, age, nodes):
        self.id = id
        self.age = age
        self.nodes = nodes


    def distance_with_cluster(self, cluster, distance_matrix):
            distance=0
            # print(self.nodes)
            for i in  self.nodes:
                for j in cluster.nodes:
                   # print(i,j,len(distance_matrix))
                    distance+=distance_matrix[i][j]
            return distance / float(len(self.nodes) * len(cluster.nodes))
    
def merge_clusters(cluster_1, cluster_2, id, age):
    return Cluster(id, age, cluster_1.nodes + cluster_2.nodes)

    
def find_closest_clusters(clusterList, cluster_ids,  distance_matrix):
    min_distance=math.inf
    c1,c2=None,None
    for _cluster_1 in cluster_ids:
        for _cluster_2 in cluster_ids:
            if(_cluster_1!=_cluster_2):
                cluster_1=clusterList[_cluster_1]
                cluster_2=clusterList[_cluster_2]
                distance=cluster_1.distance_with_cluster(cluster_2,distance_matrix)
                if distance<=min_distance:
                    min_distance=distance
                    c1,c2=cluster_1,cluster_2

    return c1,c2



def connect_nodes(graph, parent, child):
    distance = parent.age - child.age
    graph[parent.id].append((child.id, distance)) 
    graph[child.id].append((parent.id, distance))

def update_distance_matrix(cluster_new, clusterList, distance_matrix):
    distances = [cluster_new.distance_with_cluster(cluster, distance_matrix) for cluster in clusterList]
    #print(len(distance_matrix),len(distances))
    for i in range(len(distance_matrix)):
        distance_matrix[i].append(distances[i])

    distance_matrix.append(distances + [0])
    return distance_matrix


def upgma_tree(distance_matrix, n):

    clusterList = [Cluster(id, age=0, nodes=[id]) for id in range(n)]
    clusters_ids = set([id for id in range(n)])
    graph = defaultdict(list)
    # id of the new node.
    next_id = n

    while len(clusters_ids) > 1:  
        c1, c2 = find_closest_clusters(clusterList,clusters_ids, distance_matrix)
        print(c1.id,c2.id)


        age = c1.distance_with_cluster(c2, distance_matrix) / 2

        
        cluster_new = merge_clusters(c1, c2, next_id, age=age)
        #update next_id variable
        next_id += 1

        connect_nodes(graph, cluster_new, c1)
        connect_nodes(graph, cluster_new, c2)

        
        clusters_ids.remove(c1.id)
        clusters_ids.remove(c2.id)
        clusters_ids.add(cluster_new.id)
        clusterList.append(cluster_new)
        update_distance_matrix(cluster_new, clusterList, distance_matrix)



    return graph

def printAdj(adj):
    for node_1,edges in sorted(adj.items()):
        for node_2,weight in sorted(edges):
            print(str(node_1)+"->"+str(node_2)+":"+str(int(weight)))

if __name__ == '__main__':
    
    n,distance_matrix=read("20_input.txt")

    tree = upgma_tree(distance_matrix, n)
    printAdj(tree)

 





