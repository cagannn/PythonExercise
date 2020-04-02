#Kelimenini içinde istenen harften kaç tenae olduğunu bulan fonksiyon
#a=kelime, b=kaçtane olduğu bulunması istenen harf
def bul(a,b):
    sayac=0;
    t=len(a)
    for i in range(t):
        if (a[i]==b):
            sayac=sayac+1

    return sayac
