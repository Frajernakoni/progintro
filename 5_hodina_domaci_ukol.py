lower=0
higher=0

def max_of_three(a,b,c):
    lower=a
    higher=a
    for i in (a,b,c):
        if i<lower:
            lower=i
        if i>higher:
            higher=i
    return("nejmenši je ",lower,"největší je ",higher)        
            

def format_price(kolik,currency="Kč"):
    return(f"{kolik:00}",currency)

print(max_of_three(3, 9, 5))             # 9
print(max_of_three(-1, -8, -3))          # -1
print(format_price(1800))                # 1800.00 Kč
print(format_price(72.5, currency="€"))  # 72.50 €