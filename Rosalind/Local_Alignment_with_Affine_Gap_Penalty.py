import blosum as bl

    
def LocalAlignmmentAffineGapPenalty(s, t,scoring_matrix,a,b):
    m, n = len(s), len(t)
    #make the dp matrix with zereos
    #the 3rd dimension has four data: M,I_x,I_y,4th dimension has two sides
    DPMATRIX = [[[[0]*3 for _k in range(2)]for _i in range(n+1)]for _j in range(m+1)]
    
    #filling matrix
    biggests=[[0,0,0]for _ in range(3)] #middle,Ix,Iy [i,j,value]
    for i in range(1, m+1):
        for j in range(1, n+1):
            left = DPMATRIX[i-1][j][0]
            down = DPMATRIX[i][j-1][0]
            left_up = DPMATRIX[i-1][j-1][0]
            #i_x
            I_x_scores=[left[0]-a,left[1]-b]
            DPMATRIX[i][j][0][1]=max(I_x_scores)
            # DPMATRIX[i][j][1][1]=I_x_scores.index(max(I_x_scores))
            # if(DPMATRIX[i][j][0][1]>biggests[1][2]):
            #     biggests[1][2]=DPMATRIX[i][j][0][1]
            #     biggests[1][0]=i
            #     biggests[1][1]=j

            #i_y
            I_y_scores=[down[0]-a,down[2]-b]
            DPMATRIX[i][j][0][2]=max(I_y_scores)
            # DPMATRIX[i][j][1][2]=I_y_scores.index(max(I_y_scores))
            # if(DPMATRIX[i][j][1][2]==1): DPMATRIX[i][j][1][2]+=1
            # if(DPMATRIX[i][j][0][2]>biggests[2][2]):
            #     biggests[2][2]=DPMATRIX[i][j][0][2]
            #     biggests[2][0]=i
            #     biggests[2][1]=j

            M_scores=[DPMATRIX[i][j][0][1],left_up[0]+scoring_matrix.get(s[i-1]+t[j-1]),DPMATRIX[i][j][0][2],0]

            #middle
            DPMATRIX[i][j][0][0]=max(M_scores)
            DPMATRIX[i][j][1][0]=M_scores.index(max(M_scores))
            if(DPMATRIX[i][j][0][0]>biggests[0][2]):
                biggests[0][2]=DPMATRIX[i][j][0][0]
                biggests[0][0]=i
                biggests[0][1]=j

    # printDpMatrix(dp_matrix)

#making s_p and t_p
    s_p, t_p = "", ""
    i, j = biggests[0][0], biggests[0][1]

    while (i>0 and j>0):
        if(DPMATRIX[i][j][0][0]==0):
                break
        #if its match
        if(DPMATRIX[i][j][1][0]==0):
            i-=1
            s_p+=s[i]
        elif(DPMATRIX[i][j][1][0]==1):
            i-=1
            j-=1
            s_p+=s[i]
            t_p+=t[j]
        elif(DPMATRIX[i][j][1][0]==2):
            j-=1
            t_p+=t[j]

    s_p=s_p[::-1]
    t_p=t_p[::-1]

    return DPMATRIX,s_p,t_p,biggests[0][2]



def fasta_inputs(filename):
    f = open(filename, "r")
    inputs=[]
    string=""
    for line in f:
        text=line.strip()
        if text.startswith(">"):
            if string!="":inputs.append(string)
            string=""
        else:
            string+=text
    if string!="":inputs.append(string)
    return inputs

def printDpMatrix(matrix):
    print("dp matrix:")
    for q in matrix:
        for p in q:
            print(p[0],end=" ")
        print()
    print("backtrack matrix:")
    for q in matrix:
        for p in q:
            print(p[1],end=" ")
        print()




#matrix=bl.BLOSUM("ms.file")

#import the blosum62 
matrix = bl.BLOSUM(62)
import FASTA
  

   # Parse the two input protein strings.
inputs = [fasta[1] for fasta in FASTA.ReadFASTA('5.txt')]
# inputs=fasta_inputs("5.txt")
a=11
b=1
dp_matrix,s_p,t_p,score=LocalAlignmmentAffineGapPenalty(inputs[0],inputs[1],matrix,a,b)
# score=score_calc(s_p,t_p,a,b,matrix)
print(int(score))

print(s_p)
print(t_p)
#printDpMatrix(dp_matrix)
