def rc(string):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'}
    result = ""
    for char in reversed(string):
        result += complements[char]
    return result


with open('20_input.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# We don't know which k value gives exactly two directed cycles, so iterate until we find the right value.
for kval in range(1,len(k_mers[0])):
	# Begin by constructing the De Bruijn Graph 
	
	DBG_edge_elmts = set()
	for kmer in k_mers:
		for i in range(kval):
			DBG_edge_elmts.add(kmer[i:len(kmer)+i-kval+1])
			DBG_edge_elmts.add(rc(kmer[i:len(kmer)-kval+i+1]))

	# Create the edges of the Graph.
	k = len(list(DBG_edge_elmts)[0])
	
	edge = lambda elmmt: [elmmt[0:k-1],elmmt[1:k]]
	DBG_edges = [edge(elmmt) for elmmt in DBG_edge_elmts]

	# Construct the cyclic superstrings from the edges. 
	cyclics = []
	for repeat in range(2):
		temp_kmer = DBG_edges.pop(0)
		cyclic = temp_kmer[0][-1]
		
		while temp_kmer[1] in [item[0] for item in DBG_edges]:
			cyclic += temp_kmer[1][-1]
			[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
			temp_kmer = DBG_edges.pop(index)
			#print('index',index)
		cyclics.append(cyclic)
		if k==4:
			print(cyclics)
			print(DBG_edges)
		
	# Break if we've found exactly two directed cycles.
	if len(DBG_edges) == 0:
		break

# Print and save the output.
print (cyclics[0])
with open('20_3_out.txt', 'w') as output_file:
	output_file.write(cyclics[0])