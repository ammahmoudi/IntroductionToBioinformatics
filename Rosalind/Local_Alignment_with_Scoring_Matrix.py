import blosum as bl


def LocalAlignmentScoringMatrix(s, t, scoring_matrix, gap):
    m, n = len(s), len(t)
    # #make the dp matrix with zereos
    DPMATRIX = [[[0]*2 for _i in range(n+1)]for _j in range(m+1)]

    # initializing
    DPMATRIX[0][0][1] = 3
    for i in range(1, m+1):
        DPMATRIX[i][0][1] = 0

    for j in range(1, n+1):
        DPMATRIX[0][j][1] = 0
    biggestElement = [0, 0, 0]  # i,j,value

    # printDpMatrix(DPMATRIX)

    # filling matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            left = DPMATRIX[i][j-1][0]
            left_up = DPMATRIX[i-1][j-1][0]
            up = DPMATRIX[i-1][j][0]

            scores = [left+gap, up+gap, left_up +
                      scoring_matrix.get(s[i-1]+t[j-1]), 0]
            DPMATRIX[i][j][0] = max(scores)
            DPMATRIX[i][j][1] = scores.index(max(scores))
            if (DPMATRIX[i][j][0] >= biggestElement[2]):
                biggestElement[0] = i
                biggestElement[1] = j
                biggestElement[2] = DPMATRIX[i][j][0]


# making s_p and t_p
    s_p, t_p = "", ""

    i, j = biggestElement[0], biggestElement[1]

    while (i > 0 and j > 0 and DPMATRIX[i][j][1] != 3):
        pointer = DPMATRIX[i][j]
        if (pointer[0] == 0):
            break
        if (pointer[1] == 2):
           # print("diag : "+s[i-1]+" : "+t[j-1])
            t_p += t[j-1]
            s_p += s[i-1]
            i -= 1
            j -= 1
        elif (pointer[1] == 0):
          #  print("left : "-" : "+t[j-1])
            t_p += t[j-1]

            j -= 1

        elif (pointer[1] == 1):
            #print("up : "+s[i-1]+" : "+"-")
            s_p += s[i-1]
            i -= 1
        elif (pointer[1] == 3):
            break
    t_p = t_p[::-1]
    s_p = s_p[::-1]

    return DPMATRIX, s_p, t_p, biggestElement[2]

# fasta input reader


def fasta_inputs(filename):
    f = open(filename, "r")
    inputs = []
    string = ""
    for line in f:
        text = line.strip()
        if text.startswith(">"):
            if string != "":
                inputs.append(string)
            string = ""
        else:
            string += text
    if string != "":
        inputs.append(string)
    return inputs
# function to print matrices


def printDpMatrix(matrix):
    print("dp matrix:")
    for q in matrix:
        for p in q:
            print(str(int(p[0])), end=" ")
        print()
    print("back matrix:")
    for q in matrix:
        for p in q:
            print(str(p[1]), end=" ")
        print()


matrix = bl.loadMatrix("pam250.file")
inputs = fasta_inputs("4.txt")
gap = -5
dp_matrix, s_p, t_p, max_score = LocalAlignmentScoringMatrix(
    inputs[0], inputs[1], matrix, gap)

# printDpMatrix(dp_matrix)
print(int(max_score))
print(s_p)
print(t_p)
