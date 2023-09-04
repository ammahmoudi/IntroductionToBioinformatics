
import random

def hamming_distance(s,t):
    return len([a for (a,b) in zip(s,t) if a!=b])

def SmallParsimony(T, alphabet='ATGC'):

    # SingleCharacterSmallParsimony Solve small parsimony for one character

    def SingleCharacterSmallParsimony(Character):

        def get_ripe():
            for node in T.get_nodes():
                # if node is not tagged one check the children
                if not processed[node] and node in T.edges:
                    for node_2, weight in T.edges[v]:
                        if node_2 > node:
                            continue
                        if not processed[node_2]:
                            break

                    return node

            return None

        def single_score(char, symbol):
            return 0 if char == symbol else 1

        def calculate_score_if(symbol, node):
            def get_min(e):
                return min(scores[e][alphabet.index(char)]+single_score(symbol, char) for char in alphabet)
            scores_for_alphabet = [get_min(e) for e, _ in T.edges[node]]
            return sum(scores_for_alphabet)

        def update_tree(v, scores):
            if not v in result_tree.labels:
                result_tree.labels[v] = ''
            index = 0
            min_s = float('inf')
            for i in range(len(scores)):
                if scores[i] < min_s:
                    min_s = scores[i]
                    index = i
            result_tree.set_label(v, result_tree.labels[v]+alphabet[index])
            return alphabet[index]

        def backtrack(v, current_symbol):
            for v_next, _ in T.edges[v]:
                if T.is_leaf(v_next):
                    continue
                if not v_next in result_tree.labels:
                    result_tree.labels[v_next] = ''
                min_score = min([scores[v_next][i]
                                for i in range(len(alphabet))])
                indices = [i for i in range(
                    len(alphabet)) if scores[v_next][i] == min_score]
                matched = False
                for i in indices:
                    if alphabet[i] == current_symbol:

                        matched = True
                        result_tree.set_label(
                            v_next, result_tree.labels[v_next]+current_symbol)
                        backtrack(v_next, current_symbol)
                if not matched:
                    next_symbol = alphabet[indices[random.randrange(
                        0, (len(indices)))]]
                    result_tree.set_label(
                        v_next, result_tree.labels[v_next]+next_symbol)
                    backtrack(v_next, next_symbol)

        processed = {}
        scores = {}
        # scores of leaves
        for v in T.get_nodes():
            if T.is_leaf(v):
                processed[v] = True
                scores[v] = [0 if char == Character[v]
                             else float('inf') for char in alphabet]
            else:
                processed[v] = False

        v = get_ripe()
        while not v == None:
            processed[v] = True
            scores[v] = [calculate_score_if(char, v) for char in alphabet]
            # keep track of last ripe
            v_last = v
            # update the ripe to contonue the loop
            v = get_ripe()

        backtrack(v_last, update_tree(v_last, scores[v_last]))
        return min([scores[v_last][c] for c in range(len(alphabet))])

    result_tree = Tree(T.N)
    result_tree.deep_copy(T)

    return sum([SingleCharacterSmallParsimony([v[i] for l, v in T.labels.items()]) for i in range(len(T.labels[0]))]), result_tree

def print_tree_with_hummingdistances(result_tree,mode):
    result_tree.nodes.sort()
    for node in result_tree.nodes:
        if node in result_tree.edges:
            for edge in result_tree.edges[node]:
                end, weight = edge
                if node in result_tree.labels and end in result_tree.labels:
                    print('{0}->{1}:{2}'.format(result_tree.labels[node],
                                                result_tree.labels[end],
                                                hamming_distance(result_tree.labels[node], result_tree.labels[end])),file=mode)
                    print('{0}->{1}:{2}'.format(result_tree.labels[end],
                                                result_tree.labels[node],
                                                hamming_distance(result_tree.labels[node], result_tree.labels[end])),file=mode)


def read(file_name):
    file = open(file_name, 'r')
    lines = []
    # read all lines
    for line in file:
        lines.append(line.strip())
    # set n
    n = int(lines.pop(0))
    # make variables
    tree = Tree()
    for line in lines:
        temp_split = line.split('->')
        first = int(temp_split[0])
        second = temp_split[1]
        if second.isnumeric():
            j = int(second)
        else:
            j = tree.get_leaf_of_label(second)
            if j == None:
                j = tree.append_leaf(second)
        tree.link(first, j)

    return n, tree


class Tree(object):

    def __init__(self, N=-1):
        self.nodes = list(range(N))
        self.edges = {}

        self.N = N
        self.labels = {}
        self.leaves = []

    def link(self, a, b, weight=1):
        if not a in self.nodes:
            self.nodes.append(a)
        if a in self.edges:
            self.edges[a] = [(b0, w0) for (b0, w0)
                             in self.edges[a] if b0 != b] + [(b, weight)]
        else:
            self.edges[a] = [(b, weight)]

    def unlink(self, a, b):
        links = [(e, w) for (e, w) in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
 
        

    def are_linked(self, a, b):
        return len([e for (e, w) in self.edges[a] if e == b]) > 0

    def print_adjacency(self, includeNodes=False, show_labels=False):
        self.nodes.sort()
        if includeNodes:
            print(self.nodes)
        for node in self.nodes:
            if node in self.edges:
                for edge in self.edges[node]:
                    end, weight = edge
                    if (show_labels):
                        print('{0}({1})->{2}({3}):{4}'.format(
                            node, self.labels[node] if node in self.labels else "None", end, self.labels[end] if end in self.labels else "None", weight))
                    else:
                        print('{0}->{1}:{2}'.format(node, end, weight))

    def next_node(self):
        return len(self.nodes)


    def get_nodes(self):
        for node in self.nodes:
            yield (node)

    def deep_copy(self, T):
        for node in T.nodes:
            if not node in self.nodes:
                self.nodes.append(node)
                if node in T.edges:
                    for a, w in T.edges[node]:
                        self.link(node, a, w)
        for node, label in T.labels.items():
            self.set_label(node, label)

    def get_links(self):
        return [(a, b, w) for a in self.nodes for (b, w) in self.edges[a] if a in self.edges]


    def is_leaf(self, v):
        return v in self.leaves

    def set_label(self, node, label):
        if not node in self.nodes:
            self.nodes.append(node)
        self.labels[node] = label

    def get_leaf_of_label(self, string):
        for index, label in self.labels.items():
            if string == label:
                return index
        return None

    def next_label(self):
        return len(self.labels)

    def append_leaf(self, label):
        index = self.next_label()
        if not index in self.leaves:
            self.leaves.append(index)
        self.set_label(index, label)
        return index


if __name__ == '__main__':

    n, tree = read('22_input.txt')
   # tree.print_adjacency(False, True)
    # print(tree.labels)
    # print(tree.nodes)
    # print(tree.leaves)
    # print(tree.edges)

 
    score,result_tree=SmallParsimony(tree)
   
   
        # Print output
    with open('22_out.txt', 'w') as outFile:
         print (score,file=outFile)
         print_tree_with_hummingdistances(result_tree,outFile)

