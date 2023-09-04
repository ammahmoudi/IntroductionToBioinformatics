import blosum as bl

import math

def score_calc(s_p,t_p,a,b,scoring_matrix):
    score=0
    gap_opening=True
    for i in range(len(s_p)):
        if(s_p[i]!="-" and t_p[i]!="-"):
            gap_opening=True
            score+= scoring_matrix.get(s_p[i]+t_p[i])
           # print(s_p[i]+" "+t_p[i]+" : "+str(scoring_matrix.get(s_p[i]+t_p[i])))
        else:
            if(gap_opening):
                
                score-=(a)
            #    print(s_p[i]+" "+t_p[i]+" open : "+str(a))
                gap_opening=False
            else:
                score-=b
             #   print(s_p[i]+" "+t_p[i]+" expension:  "+str(b))
    return score
        

def GlobalAlignmmentAffineGapPenalty(s, t,scoring_matrix,a,b):
    m, n = len(s), len(t)
    #make the dp matrix with zereos
    #the 3rd dimension has four data: M,I_x,I_y,4th dimension has two sides
    DPMATRIX = [[[[0]*3 for _k in range(2)]for _i in range(n+1)]for _j in range(m+1)]
    
    #initializing
    DPMATRIX[0][0][0][1]=-a
    DPMATRIX[0][0][0][2]=-a
    for i in range(1,m+1):
        DPMATRIX[i][0][0][0] = -math.inf
        DPMATRIX[i][0][0][1] = -a-(i)*b
        DPMATRIX[i][0][0][2] = -math.inf
        DPMATRIX[i][0][1][1] = 1
        DPMATRIX[i][0][1][0] = -math.inf
        DPMATRIX[i][0][1][2] = -math.inf

    for j in range(1,n+1):
        DPMATRIX[0][j][0][0] = -math.inf
        DPMATRIX[0][j][0][1] = -math.inf
        DPMATRIX[0][j][0][2] = -a-(j)*b
        DPMATRIX[0][j][1][2] = 2
        DPMATRIX[0][j][1][0] = -math.inf
        DPMATRIX[0][j][1][1] = -math.inf
    #filling matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            left = DPMATRIX[i-1][j][0]
            down = DPMATRIX[i][j-1][0]
            left_down = DPMATRIX[i-1][j-1][0]
            M_scores=[scoring_matrix.get(s[i-1]+t[j-1])]*3
            #middle
            for k in range(3):M_scores[k]+=left_down[k]
            DPMATRIX[i][j][0][0]=max(M_scores)
            DPMATRIX[i][j][1][0]=M_scores.index(max(M_scores))
            #i_x
            I_x_scores=[left[0]-a-b,left[1]-b]
            DPMATRIX[i][j][0][1]=max(I_x_scores)
            DPMATRIX[i][j][1][1]=I_x_scores.index(max(I_x_scores))
            #i_y
            I_y_scores=[down[0]-a-b,down[2]-b]
            DPMATRIX[i][j][0][2]=max(I_y_scores)
            DPMATRIX[i][j][1][2]=I_y_scores.index(max(I_y_scores))
            if(DPMATRIX[i][j][1][2]==1): DPMATRIX[i][j][1][2]+=1


#making s_p and t_p
    s_p, t_p = s, t
    i, j = len(s), len(t)
    #back
    start=max(DPMATRIX[i][j][0])
    back=DPMATRIX[i][j][0].index(start)
    while (i>0 and j>0):

        #if its match
        if(back==0):
            #update theh back
            if DPMATRIX[i][j][1][0]==1 : back=1
            elif DPMATRIX[i][j][1][0]==2 : back=2
            
            i-=1
            j-=1

        #if its i_x
        elif(back==1):
             #update theh back
            if DPMATRIX[i][j][1][1]==0 : back=0
            i-=1
            t_p=t_p[:j]+'-'+t_p[j:]
        #if its i_y
        elif(back==2):
             #update theh back
            if DPMATRIX[i][j][1][2]==0 : back=0
            j-=1
            s_p=s_p[:i]+'-'+s_p[i:]

    #add remaining gaps
    for _xx in range(i):
        t_p=t_p[:0]+'-'+t_p[0:]
    for _xx in range(j):
        s_p=t_p[:0]+'-'+s_p[0:]

    return DPMATRIX,s_p,t_p


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
inputs=fasta_inputs("3.txt")
a=11
b=1
dp_matrix,s_p,t_p=GlobalAlignmmentAffineGapPenalty(inputs[0],inputs[1],matrix,a,b)
score=score_calc(s_p,t_p,a,b,matrix)
print(int(score))
print(s_p)
print(t_p)
