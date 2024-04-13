import random

uzunluk=int(input("Enter lenght of password which you want to create: "))
password=""
for i in range(0,uzunluk):
    rand=random.randint(33,126)
    password=password+chr(rand)
print(f"Your password is:{password}")
