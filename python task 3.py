import math
def persquare(list_1,x,y):
    for i in (list_1):
            if (math.isqrt(i) ** 2 == i):
                if (i>=x and i<y):
                    print(i,"is a perfect square")
                else:
                    continue
            else:
                continue

list_1=[1,2,4,8,64,122]
persquare(list_1, 1, 100)









