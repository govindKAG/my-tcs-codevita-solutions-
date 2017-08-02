import itertools as it
base = '0123456789'

tl = []
for p in it.permutations(base,10):
    tl.append(p)

tl = iter(tl)
ab = []
for i in tl :
	ab.append(''.join(it.chain(*i)))

d = {}

c = 1
for el in ab :
    d[el] = c
    c = c+1

############
t = [] 
n = int(input('enter the number of cases \n'))

for i in range(n):
    t.append(input())
m = 1
for e in t:
    m = m*d[e]

print(m % 23456)
    
