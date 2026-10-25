diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
dobry = 0
spatny = 0

for diameter in diameters:
    if diameter <= 25.05 and diameter >= 24.95:
        print("1:", diameter, "mm   OK")
        dobry += 1
    else:
        print("0:", diameter, "mm   VELKÝ")
        spatny += 1
procento = (spatny / len(diameters)) * 100
print("Zmetků:",spatny,"z",len(diameters))
print("Procento zmetků:",procento,"%")



