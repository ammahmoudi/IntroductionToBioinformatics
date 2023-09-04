def read(file_name):
    file = open(file_name, 'r')
    lines = set()
    # read all lines
    for line in file:
        lines.add(line.strip())

    return lines


def reverse_complement(string):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'}
    result = ""
    for char in reversed(string):
        result += complements[char]
    return result

#get kmers of the string
def get_k_mers(string, k):
    return [string[i:i+k] for i in range(len(string)-k + 1)]

#a debruijn graph with k
def deBruijnGraph(strings, k):
    data=set()
    for i in strings:
       data=data|set(get_k_mers(i,k))

    reverse_complements = set()
    for line in data:
        reverse_complements.add(reverse_complement(line))
    data = data | reverse_complements
    edges = dict()
    for line in data:
        edges[line[:len(line)-1]]= line[1:]
        
    return edges


def print_edges(edges:dict, outfile):
    for item in edges:
        print('(' + item[0] + ", " + item[1] + ')', file=outfile)
#get edges and output a superstring and a edges dictinary contained of remaining edges and also the cycle patth tupples
def get_cycle(adj):
    import copy
    edges=copy.deepcopy(adj)
    superstring=''
    cycle_path=[]
    #first pair of the edges
    pair=next(iter(edges.items()))
    edges.pop(pair[0])
    cycle_path.append(pair)
    superstring=pair[0][-1]

    while  pair[1]  in edges.keys():
        superstring+=pair[1][-1]
        remove_key=pair[1]
        #update pair iterator
        pair=list(edges.items())[list(edges.keys()).index(pair[1])]
        #add to path
        cycle_path.append(pair)
        edges.pop(remove_key)

    return superstring,edges,cycle_path

#shortestSuperString
def shortestSuperString(data):
    #find the k with exact 2 cycles
    for k in range (len(list(data)[0])-1,1,-1):
        adj=deBruijnGraph(data,k)
        superstring_1,edges_1,cycle_path_1=get_cycle(adj)
        superstring_2,edges_2,cycle_path_2=get_cycle(edges_1)
        if len(edges_2)==0:return superstring_2
    return None



if __name__ == "__main__":
    data = read("20_input.txt")
    # Print output
    with open('20_output.txt', 'w') as outFile:

        print(shortestSuperString(data))
#AGATT
#TTACA
#TAATC
#TCTGT

# AATCT
# TGTAA
# GATTA
# ACAGA