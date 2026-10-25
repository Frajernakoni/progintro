def hmotnost_trubky(d_out, d_in, l, density=7850):
    import math
    objem = math.pi * l * ((d_out / 2) ** 2 - (d_in / 2) ** 2)
    hmotnost = objem * density
    return hmotnost
print(hmotnost_trubky(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(hmotnost_trubky(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg 