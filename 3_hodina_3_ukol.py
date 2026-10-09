slovo = input("Slovo: ")

print("Počet znaků:", len(slovo))
print("První znak:", slovo[0])
print("Poslední znak:", slovo[-1])
print("Velkými písmeny:", slovo.upper())
print("Pozpátku:", slovo[::-1])
print("Palindrom:", slovo.lower() == slovo[::-1].lower())