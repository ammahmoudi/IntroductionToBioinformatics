def read(file_name):
    file = open(file_name, 'r')
    lines = set()
    # read all lines
    for line in file:
        lines.add(line.strip())

    return lines




#get kmers of the string
def get_k_mers(string, k):
    return [string[i:i+k] for i in range(len(string)-k + 1)]

#a debruijn graph without reverse complement
def deBruijnGraph(data):

    edges = dict()
    for line in data:
        edges[line[:len(line)-1]]= line[1:]
        
    return edges


def print_edges(edges, outfile):
    for item in edges.items():
        print('(' + item[0] + ", " + item[1] + ')', file=outfile)
#get edges and output a superstring and a edges dictinary contained of remaining edges and also the cycle patth tupples
def get_cycle(adj):
    import copy
    edges=copy.deepcopy(adj)
    superstring=''
    cycle_path=[]
    #first pair of the edges
    pair=next(iter(edges.items()))
   # edges.pop(pair[0])
    # cycle_path.append(pair)
   

    while  pair[0]   in edges :
        superstring+=pair[1][-1]
        remove_key=pair[0]
        #update pair iterator
        # print(pair)
        # print(edges)
        if len(edges)>1:
          pair=list(edges.items())[list(edges.keys()).index(pair[1])]
        #add to path
        
        edges.pop(remove_key)

    return superstring

#shortestSuperString
def shortestSuperString_prefect_coverage(data):
        adj=deBruijnGraph(data)
       # print_edges(adj,None)
        superstring=get_cycle(adj)
      
        return superstring



if __name__ == "__main__":
    data = read("21_input.txt")
    # Print output
    with open('21_output.txt', 'w') as outFile:

      print(shortestSuperString_prefect_coverage(data))
