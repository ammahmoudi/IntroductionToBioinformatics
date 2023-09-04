from collections import defaultdict
def read(file_name):
    file = open(file_name, 'r')
    lines = list()
    # read all lines
    for line in file:
        lines.append(line.strip())
    return lines[0]
def inverse_BWT(string):
    sorted_alphabet=set()
    for char in string:
      sorted_alphabet.add(char)
    sorted_alphabet=sorted(sorted_alphabet)
    print("sorted alphabet: ",sorted_alphabet)
    shifts=defaultdict(list)
    for i in range(len(string)):
        shifts[string[i]].append(i)
    
    
    traverse=list()
    for alphabet in sorted_alphabet:
        traverse+=shifts[alphabet]
    
    result=""
    x=traverse[0]
    print(x)
    for i in range(len(string)):
        x=traverse[x]
        result+=string[x]
    return result
        

    
if __name__ == "__main__":
    data = read("23_input.txt")
# # Print output
#     with open('23_output.txt', 'w') as outFile:

    print(inverse_BWT(data))

