
#the pattern can be summarized as
# f(1) = 6
# f(i)  = f(i-1) + (16*i - 10)


def f (i):  #this funtion generates the ith number of the series 
    if i == 1 :
        return 6
    else:
        return f(i-1) + (16*i-10)


def accept(num): #this funtion prints out the answer
    numberList = []
    num = int((num**2 + num)/2) # how many numnbers there are in n lines 
    if num >= 1:
        for eachNum in range(num):
            numberList.append(str(f(eachNum+1)).zfill(5))
            
        numberList = iter(numberList)
        a = 1
        try:
            while(True):
                for b in range(a):
                    print(numberList.__next__()+" ",end = "")
                print("\n")
                a = a+1
        except:
            pass
            

    

number = int(input('enter the number of rows '))
accept(number)
