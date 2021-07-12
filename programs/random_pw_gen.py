import random
import string

a = string.ascii_letters

# print(a)

pw = ''.join(random.choice(a) for i in range(20))

# print(pw)

num = str(random.randint(0,10000))

print(pw+num)