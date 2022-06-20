
sayi = int(input("Faktöriyelini istediğiniz sayıyı giriniz. "))
faktoriyel = 1


if sayi < 0:
    print("Negatif sayıların faktoriyeli olmaz!")
elif sayi==0:
    print("Sonuç : 1") 
else:
    for n in range(1, sayi+1):
        faktoriyel = faktoriyel * n

    print("Sonuç : ", faktoriyel)