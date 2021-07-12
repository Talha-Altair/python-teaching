a = 0

b = 1

# for i in range(20):
#     b = b + a
#     a,b = b,a
#     print(a)
count = 0


def make_fibonacci(f,s):
    global count
    count +=1
    c = f+s
    print(c)
    while count < 100:
        make_fibonacci(s,c)

make_fibonacci(0,1)

