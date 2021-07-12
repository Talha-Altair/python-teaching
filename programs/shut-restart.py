import os

a = int(input("yes or no 0/1"))

if a == 0:
    exit()
else:
    os.system("shutdown /s /t 10")