nacti=input("načti počet sekund:")
hodiny=int(nacti)//3600
minuty=(int(nacti)%3600)//60
sekundy=int(nacti)%60
print(f"{hodiny}:{minuty:02d}:{sekundy:02d}")