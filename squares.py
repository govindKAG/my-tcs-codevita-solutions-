n = int(input(""))
num = int(input(""))
tl = []
for i in range(num):
    tl.append(input(""))

#n has the size of the grid , tl has list of all the other inputs
print(n," ",tl)

hl = [[1 for i in range(n-1)] for j in range(n)]
vl = [[1 for i in range(n)] for j in range(n-1)]

#print(hl , vl)
for i in tl:
    i = i.split(',')
    pos = i[0] 
    loc1 = int(i[1]) - 1
    loc2 = int(i[2]) - 1
    if pos == 'H':
        hl[loc1][loc2] = 0
    if pos == 'V':
        vl[loc2][loc1] = 0

square = 0
flag = False
for i in range(n-1):
    for j in range(n-1):
        m = max(i+1,j+1)
        for k in range(m,n):
            for u in range(k):
                for t in range(u):
                    print (i,t+j, "     ",k,t+j)
                    if (hl[i][t+j] != 1) or (hl[u][t+j]!=1):
                        flag = True
                        break
                    #print (t+i , j ,"   ",t+i, m)
                    #print (t+i,j, "     ",t+i, k)
                    if (vl[t+i][j] != 1) or (vl[t+i][u] != 1):
                        flag = True
                        break
                if flag == True :
                    flag = False
                else:
                    square = square +1
                


print(square)
    
    
