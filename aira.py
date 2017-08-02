import math 
def solve(a,b,c):
    d = b**2-4*a*c # discriminant

    if d < 0:
        return['b','b']
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return [int(x),int(x)]
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        return [int(x1),- int(x2)]
def airac(n):
    a0 = 1
    b0 = 2
    n = n+1
    for i in range(n):
        a0 = a0+ 2 *b0
        b0 = 2*a0  + b0

    return a0

def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return len(result)

def even(t):
    for i in t:
        if i % 2 == 0 : return i

##for i in range(5):
##    print (airac(i))
##
#n = airac(2)
#s = solve(1,1,-(((n**2)-1)/2))
N = int(input(''))
inc = 0
e = 0
while(True):
    
    n = airac(inc)
##    e = 0
    param = solve(1,1,-(((n**2)-1)/2))
    param.append(n)
    e = even (param)
   # print(pre , e)
    if e > N:
        #print(pre)
        break
    inc = inc +1

print(factors(e))
