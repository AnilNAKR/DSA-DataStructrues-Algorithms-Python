import math
def PrimeOrNot(value):
    root = int(math.sqrt(value))
    prime_num = []
    for i in range(2,root+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0 and count <= 2:
                count += 1
        if count == 2:
            prime_num.append(i)
    for i in prime_num:
        count = 0
        if value % i == 0:
            print("Value is not Prime")
            break
        else:
            count += 1
        if count == len(prime_num):
            print("Not Number")
        else:
            print("Prime")
            break

PrimeOrNot(1039)