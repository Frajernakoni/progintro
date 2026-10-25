cislo=set()
for i in range(2, 101):
    cislo.add(i)

for i in cislo:
    for c in range(2, i+1):
        if i % c == 0 and i != c:
            break  
        elif i % c == 0 and i == c:
            print(i, "je prvočíslo")
        else:
            continue

zcislo=int(input("Zadejte číslo: "))
while zcislo>1:
    for i in range(2, zcislo + 1):
        if zcislo % i == 0:
            x=i
            zcislo=zcislo//x
            print(x)  
            break
