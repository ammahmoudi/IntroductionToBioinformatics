
def EditDistanceAlignment(s, t):
    m, n = len(s), len(t)
    #check the simple states
    if m==0 or n==0:
        return m+n
    #make the dp matrix with zereos
    DPMATRIX = [[0]*(n+1) for _i in range(m+1)]
    #initializing
    for i in range(m+1):
        DPMATRIX[i][0] = i
    for j in range(n+1):
        DPMATRIX[0][j] = j
    #filling matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            left = DPMATRIX[i-1][j] + 1
            down = DPMATRIX[i][j-1] + 1
            left_down = DPMATRIX[i-1][j-1]
            if s[i-1] != t[j-1]:
                left_down += 1
            DPMATRIX[i][j] = min(left, down, left_down)
 
    edit_distance = DPMATRIX[m][n]
#making s_p and t_p
    s_p, t_p = "", ""
    i, j = len(s), len(t)
    #back
    while (i>0 and j>0):
        left = DPMATRIX[i][j-1]
        top = DPMATRIX[i-1][j]
        left_top = DPMATRIX[i-1][j-1]
        min_p = min(left, top, left_top)
        if DPMATRIX[i][j]==min_p:
            s_p = s[i-1]+s_p
            t_p = t[j-1]+t_p
            i -= 1
            j -= 1
        else:
            if (min_p==left and min_p==top) or (min_p!=left and min_p!=top):
                s_p = s[i-1]+s_p
                t_p = t[j-1]+t_p
                i -= 1
                j -= 1
            elif min_p!=left and min_p==top:
                s_p = s[i-1]+s_p
                t_p = "-"+t_p
                i -= 1
            elif min_p==left and min_p!=top:
                s_p = "-"+s_p
                t_p = t[j-1]+t_p
                j -= 1
    return s_p,t_p,edit_distance,DPMATRIX
f = open("2.txt", "r")
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

s_p,t_p,e,dis_mat=  EditDistanceAlignment(inputs[0],inputs[1]) 
print(e)
print(s_p)
print(t_p)