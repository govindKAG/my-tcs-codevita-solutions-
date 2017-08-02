##from itertools import permutations,chain
##base = '0123456789'
##
##c = 1
##d = {}
##for p in permutations(base,10):
##    #if c < 10 : print(''.join(itertools.chain(*p)))
##    d[''.join(chain(*p))] = c
##    c = c + 1
##    
##
###print(d['0123456789'])
################
##t = [] 
##n = int(input('enter the number of cases \n'))
##
##for i in range(n):
##    t.append(input())
##m = 1
##for e in t:
##    m = m*d[e]
##
##print(m % 23456)
##    
##
from math import factorial

def sri(st, low , high):
    countr = 0
    for i in range(low+1,high+1):
        if st[i] < st[low]:
            countr = countr+1
    return countr

def rank(sr):
    l = 10
    m = factorial(l)
    r = 1
    for i in range(l):
        m = m//(l-i)
        cr = sri(sr,i,l-1)
        r = r+ cr*m
    return int(r)
t = [] 
n = int(input('enter the number of cases \n'))

for i in range(n):
    t.append(input(""))
m = 1
for e in t:
    m = m*rank(e)

print(m % 23456)
    

#print(int(rank('0123456789')))
