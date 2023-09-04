import itertools 
alphabet_string = "A B C D E F G H I J"
alphabet = alphabet_string.split(' ')
alphabet_len = len(alphabet)
n = 2

permutation = itertools.product(alphabet, repeat = n)
output = []
for i, j in enumerate(list(permutation)):
    permutation = ''
    for item in j:
        permutation += str(item)
    output.append(permutation)
for item in output:
    print(item, end="\n")