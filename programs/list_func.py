a = [10,30,45,98,100]

# b = a.append(1000000)

# # print(a)

# bye = [i**i for i in range(10)]

# print(bye)

tram = 10

def printer():
    global tram

    tram = 20

    tram = tram + 1

    print(tram)

printer()

print(tram)
