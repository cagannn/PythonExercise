import random

uzunluk=int(input("Enter lenght of password which you want to create: "))
password=""
for i in range(0,uzunluk):
    tek_cift=random.randint(0,10)
    rand=random.randint(33,126)
    password=password+chr(rand)
print(f"Your password is:{password}")
