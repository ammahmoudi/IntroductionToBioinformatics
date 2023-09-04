import blosum as bl
import itertools
import math
def scoring(a,b,c,d):
    list=[a,b,c,d]
    score=0
    for i in range(4):
        for j  in (range(i,4)):
           
            if(i!=j and list[i]!=list[j]):
                score-=1
                # print(list[i]+":"+list[j])
    return score
def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def best_score(words_p):
    best=-math.inf
    for i in range(len(words_p)):
        for j in range(i,len(words_p)):
            if(i!=j):
                s=0
                for k in range(len(words_p[i])):
                    if(words_p[i][k]!=words_p[j][k]):s-=1
                print(s)
                best=max(best,s)
    return best

def MultipleAlignmentScoringMatrix(words):
    for xxp in range(len(words)):
        words[xxp]="$"+words[xxp]
        
           #print(words)
    m,n,v,w=len(words[0]),len(words[1]),len(words[2]),len(words[3])
    # #make the dp matrix with zereos
    DPMATRIX = [[[[[0]*2 for _i in range(w+1)]for _j in range(v+1)]for _k in range(n+1)]for _t in range(m+1)]
    
    # for i in range(1, m+1):
    #     DPMATRIX[i][0][0][0][0]=DPMATRIX[i-1][0][0][0][0]-1
    #     DPMATRIX[i][0][0][0][1]=3
    # for j in range(1, n+1):
    #     DPMATRIX[0][j][0][0][0]=DPMATRIX[0][j-1][0][0][0]-1
    #     DPMATRIX[0][j][0][0][1]=2
    # for k in range(1, v+1):
    #     DPMATRIX[0][0][k][0][0]=DPMATRIX[0][0][k-1][0][0]-1
    #     DPMATRIX[0][0][k][0][1]=1
    # for t in range(1, w+1):
    #     DPMATRIX[0][0][0][t][0]=DPMATRIX[0][0][0][t-1][0]-1
    #     DPMATRIX[0][0][0][t][1]=0
    # filling matrix
    for i in range(m+1):
        for j in range(n+1):
            for k in range(v+1):
               DPMATRIX[i][j][k][0][0]=-math.inf  
    for i in range(m+1):
        for j in range(n+1):
            for t in range(w+1):
               DPMATRIX[i][j][0][t][0]=-math.inf  
    for i in range(m+1):
        for t in range(w+1):
            for k in range(v+1):
               DPMATRIX[i][0][k][t][0]=-math.inf  
    for t in range(w+1):
        for j in range(n+1):
            for k in range(v+1):
               DPMATRIX[0][j][k][t][0]=-math.inf  

    DPMATRIX[0][0][0][0][0]=0

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1,v+1):
                for t in range(1,w+1):
                    incomings=[
                    DPMATRIX[i-1][j-1][k-1][t-1][0],
                    DPMATRIX[i-1][j][k][t][0]
                    ,DPMATRIX[i][j-1][k][t][0]
                    ,DPMATRIX[i][j][k-1][t][0]
                    ,DPMATRIX[i][j][k][t-1][0]

                    ,DPMATRIX[i-1][j-1][k][t][0]
                    ,DPMATRIX[i-1][j][k-1][t][0]
                    ,DPMATRIX[i-1][j][k][t-1][0]
                    ,DPMATRIX[i][j-1][k-1][t][0]
                    ,DPMATRIX[i][j-1][k][t-1][0]
                    ,DPMATRIX[i][j][k-1][t-1][0]

                    ,DPMATRIX[i-1][j-1][k-1][t][0]
                    ,DPMATRIX[i-1][j-1][k][t-1][0]
                    ,DPMATRIX[i-1][j][k-1][t-1][0]
                    ,DPMATRIX[i][j-1][k-1][t-1][0]
                    ]

                    scores=[
                        scoring(words[0][i-1],words[1][j-1],words[2][k-1],words[3][t-1])
                        ,scoring(words[0][i-1],'-','-','-')
                        ,scoring('-',words[1][j-1],'-','-')
                        ,scoring('-','-',words[2][k-1],'-')
                        ,scoring('-','-','-',words[3][t-1])

                        ,scoring(words[0][i-1],words[1][j-1],'-','-')
                        ,scoring(words[0][i-1],'-',words[2][k-1],'-')
                        ,scoring(words[0][i-1],'-','-',words[3][t-1])
                        ,scoring('-',words[1][j-1],words[2][k-1],'-')
                        ,scoring('-',words[1][j-1],'-',words[3][t-1])
                        ,scoring('-','-',words[2][k-1],words[3][t-1])

                        ,scoring(words[0][i-1],words[1][j-1],words[2][k-1],'-')
                        ,scoring(words[0][i-1],words[1][j-1],'-',words[3][t-1])
                        ,scoring(words[0][i-1],'-',words[2][k-1],words[3][t-1])
                        ,scoring('-',words[1][j-1],words[2][k-1],words[3][t-1])
                    ]
                    all_scores=[]
                    for _i in range(len(scores)):
                        all_scores.append(incomings[_i]+scores[_i])
                    #
                    # print(all_scores)
                    maxx=-math.inf
                    for px in range(15):
                        if maxx<= all_scores[px] :
                            maxx=all_scores[px]
                    DPMATRIX[i][j][k][t][0]=maxx

                    #DPMATRIX[i][j][k][t][1]=find_indices(all_scores,(DPMATRIX[i][j][k][t][0]))
                    e=0
                    DPMATRIX[i][j][k][t][1]=all_scores.index(DPMATRIX[i][j][k][t][0])
                    #if(all_scores[11]==all_scores[14] and DPMATRIX[i][j][k][t][114):e+=1
                   # print(e)
                    
                    # print(DPMATRIX[i][j][k][t][1])

# making s_p and t_p
    words_p = ["","","",""]

    i,j,k,t=len(words[0]),len(words[1]),len(words[2]),len(words[3])

    while (i > 0 and j > 0 and k>0 and t>0):

        pointer = DPMATRIX[i][j][k][t]
        #print(i,j,k,t)
        #print(pointer[1])
        # print(words_p[0]+":"+words_p[1]+":"+words_p[2]+":"+words_p[3])
        if(0 == pointer[1]):
           # print(words_p[0])
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            k-=1
            j-=1
            i-=1

            
        elif(1 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+"-"
            i-=1
            
            
        elif(2 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+"-"
            j-=1




    
        elif(3 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+"-"
            k-=1
            
        elif(4 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1

        elif(5 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+"-"
            j-=1
            i-=1

        elif(6 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+"-"
            k-=1
            i-=1


         
        elif(7 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            i-=1 
      
        elif(8 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+"-"
            k-=1
            j-=1
        elif(9 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            j-=1

        elif(10 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            k-=1

        elif(11 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+"-"
            k-=1
            j-=1
            i-=1

           
        elif(12 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+"-"
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            j-=1
            i-=1

        elif(13 == pointer[1]):
            words_p[0]=words_p[0]+words[0][i-1]
            words_p[1]=words_p[1]+"-"
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            k-=1
            i-=1

        elif(14 == pointer[1]):
            words_p[0]=words_p[0]+"-"
            words_p[1]=words_p[1]+words[1][j-1]
            words_p[2]=words_p[2]+words[2][k-1]
            words_p[3]=words_p[3]+words[3][t-1]
            t-=1
            k-=1
            j-=1
 

    for ok in range(len(words_p)):
        words_p[ok]=words_p[ok][::-1]
        words_p[ok]=words_p[ok][1:]
    #print(i,j,k,t)
    # for _xx in range(i):
    #     words_p[0]=words_p[0][:0]+'-'+words_p[0][0:]
    # for _xx in range(j):
    #     words_p[1]=words_p[1][:0]+'-'+words_p[1][0:]
    # for _xx in range(k):
    #     words_p[2]=words_p[2][:0]+'-'+words_p[2][0:]
    # for _xx in range(t):
    #     words_p[3]=words_p[3][:0]+'-'+words_p[3][0:]

    # i,j,k,t=len(words[0]),len(words[1]),len(words[2]),len(words[3])

    # while (i > 0 and j > 0 and k>0 and t>0):

    #     pointer = DPMATRIX[i][j][k][t]
    #     print(i,j,k,t)
    #     print(pointer[1])
    #     # print(words_p[0]+":"+words_p[1]+":"+words_p[2]+":"+words_p[3])
    #     if(0 == pointer[1])):
    #         t-=1
    #         k-=1
    #         j-=1
    #         i-=1

            
    #     elif(1 == pointer[1])):
    #         i-=1
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:]
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]


  
    #     elif(2 == pointer[1])):
    #         j-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]



    
    #     elif(3 == pointer[1])):
    #         k-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:]
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]  
    #     elif(4 == pointer[1])):
    #         t-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:]
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]

    #     elif(5 == pointer[1])):
    #         j-=1
    #         i-=1
            
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]

    #     elif(6 == pointer[1])):
    #         k-=1
    #         i-=1
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:] 
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]  


         
    #     elif(7 == pointer[1])):
    #         t-=1
    #         i-=1
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:]  
      
    #     elif(8 == pointer[1])):
    #         k-=1
    #         j-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]    
    #     elif(9 == pointer[1])):
    #         t-=1
    #         j-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #     elif(10 == pointer[1])):
    #         t-=1
    #         k-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:]

    #     elif(11 == pointer[1])):
    #         k-=1
    #         j-=1
    #         i-=1
    #         words_p[3]=words_p[3][:t]+'-'+words_p[3][t:]

           
    #     elif(12 == pointer[1])):
    #         t-=1
    #         j-=1
    #         i-=1
    #         words_p[2]=words_p[2][:k]+'-'+words_p[2][k:]
    #     elif(13 == pointer[1])):
    #         t-=1
    #         k-=1
    #         i-=1
    #         words_p[1]=words_p[1][:j]+'-'+words_p[1][j:] 

    #     elif(14 == pointer[1])):
    #         t-=1
    #         k-=1
    #         j-=1
    #         words_p[0]=words_p[0][:i]+'-'+words_p[0][i:]

    # print(i,j,k,t)
    # for _xx in range(i):
    #     words_p[0]=words_p[0][:0]+'-'+words_p[0][0:]
    # for _xx in range(j):
    #     words_p[1]=words_p[1][:0]+'-'+words_p[1][0:]
    # for _xx in range(k):
    #     words_p[2]=words_p[2][:0]+'-'+words_p[2][0:]
    # for _xx in range(t):
    #     words_p[3]=words_p[3][:0]+'-'+words_p[3][0:]


    return DPMATRIX,words_p,DPMATRIX[m][n][v][w][0]


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


# matrix = bl.loadMatrix("pam250.file")
inputs = fasta_inputs("6.txt")
gap = -5
#  dp_matrix, s_p, t_p, max_score = LocalAlignmentScoringMatrix(
#     inputs[0], inputs[1], matrix, gap)

# # printDpMatrix(dp_matrix)
# print(int(max_score))
# print(s_p)
# print(t_p)
#print(uniquePairs([1,2,3,4]))
dp_matrix,words_p,bestscore=MultipleAlignmentScoringMatrix(inputs)


print(bestscore)
for df in words_p:
    print(df)
# print(dp_matrix)
# print(scoring('-','A','G','T'))
# print(dp_matrix)
