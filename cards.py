def answer(cards , n):
    operations = []
    #ccopy = cards[:]
    ans = 0
    j = n-1
    i = 0
    while(i<=j):
        #print(i,j)
        if cards[i] == cards[j]:
            i = i+1
            j = j-1
        elif (cards[i]>cards[j]):
            j= j -1
            cards[j] = cards[j]+ cards[j+1]
            operations.append([j,j+1])
            cards.pop(j+1)
            ans = ans + 1
        else:
            i=i+1
            cards[i] = cards[i]+ cards[i-1]
            operations.append([i,i-1])
            cards.pop(i-1)
            i= i - 1
            j = j-1
            ans = ans + 1

    return [ans , cards]

n = int(input(""))
li = input("")

l = [int(x) for x in li.split(" ")]
an = answer(l,n)
if len(an[1]) == 1:
    print("TRIVIAL MERGE")
else:
    print(str(an[0]))
    #print('\n')
    for i in an[1]:
        print(i,end = " ")



