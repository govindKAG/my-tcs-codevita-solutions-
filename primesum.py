def prime(x):
    if x > 1:
        for i in range(2, x + 1):
            if x % i == 0 and i != x and i != 1:
                return False
        else:
            return True
    else:
        return False

def canSum(num):
    for i in range(2,int(num/2)+1):
        if prime(i):
            if prime(num-i):
                return True

    return False


def final(num):
    count = 0
    for i in range(3,num+1):
        if canSum(i):
            count = count+1
    print(count)


final(15)
            
