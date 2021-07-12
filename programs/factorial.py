a = 5
num =1

# for i in range(a):
#     n = n * (i+1)

# print(n)

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(4))