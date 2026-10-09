delka=input("Zadajte délku v mm: ")
delka=float(delka)
delkacm:float= delka/10
delkam:float= delkacm/100
delkain:float= delkam/0.0254
print(f"{delka:.3f} mm")
print(f"{delkacm:.3f} cm")
print(f"{delkam:.3f} m")
print(f"{delkain:.3f} in")