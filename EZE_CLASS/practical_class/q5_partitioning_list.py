import math

def SieveNow(T):
    A = []
    B = []
    C = []
    for num in T:
        if num % 2 == 1:
            A.append(num)
        elif num % 2 == 0:
            B.append(num)
        if math.sqrt(num).is_integer():
            C.append(num)
    return A, B, C

T = [100, 25, 66, 71, 81, 36, 3, 78, 90, 54]
A, B, C = SieveNow(T)
print("A:", A)
print("B:", B)
print("C:", C)
