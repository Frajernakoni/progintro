b=8
while b<=64:
    x=2**b-1
    print(f"{b:00d} bitů: 0 až {x:00}, {int(-x/2 - 0.5):00} až {int(x/2 - 0.5):00}")
    b=b*2
    