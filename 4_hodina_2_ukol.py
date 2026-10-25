roky= set()
prestupny=0

for i in range(1890, 2031):
    roky.add(i)
for rok in roky:
    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        prestupny+=1
print("Počet přestupných let mezi lety 1890 a 2030:", prestupny)
    

