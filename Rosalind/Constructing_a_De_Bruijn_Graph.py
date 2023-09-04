def read(file_name):
    file=open(file_name,'r')
    lines=set()
    #read all lines
    for line in file:
        lines.add(line.strip())

    return lines
    
def reverse_complement(string):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G' }
    result=""
    for  char in reversed(string):
        result+=complements[char]
    return result
def deBruijnGraph(data):
    reverse_complements=set()
    for line in data :
        reverse_complements.add(reverse_complement(line))
    data=data| reverse_complements
    edges=set()
    for line in data : 
        edges.add((line[:len(line)-1],line[1:]))
    return edges
def print_edges(edges,outfile):
     for item in edges:
        print('(' + item[0] + ", " + item[1] + ')',file=outFile)

    

if __name__ == "__main__":
    data=read("19_input.txt")
            # Print output
    with open('19_output.txt', 'w') as outFile:
         print_edges(deBruijnGraph(data),outFile)

    


        
