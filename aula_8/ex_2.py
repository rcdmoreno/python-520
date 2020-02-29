# 1  2  3  4  5   6  7   8
# 1, 1, 2, 3, 5, 8, 13, 21

# f(n) = f(n-1) + f(n-2)
def fib_comum(n):
    a = 1
    b = 1
    for i in range(n-2):
        temp = b + a
        b = a
        a = temp
    return a

def fib(n):
    a, b = 1, 1
    for i in range(n-2):
        a, b = a + b, a
    return a
    
print(fib_comum(8))