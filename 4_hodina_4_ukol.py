i = 1
while i == 1:
    cislo = int(input("Zadejte liché číslo: "))
    if cislo % 2 == 0 or cislo <= 1:
        print("Zadejte kladné liché číslo větší než 1.")
    else:
        i = 0
x = cislo // 2

for i in range(1, cislo + 1, 2):
    for mezera in range(x):
        print(" ", end="")
    for hvezda in range(i):
        print("*", end="")
    print()
    x -= 1
x = 1
for i in range(cislo - 2, 0, -2):
    for mezera in range(x):
        print(" ", end="")
    for hvezda in range(i):
        print("*", end="")
    print()
    x += 1