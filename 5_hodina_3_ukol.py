def summary(values):
    return {
        "mean": mean(values),
        "median": median(values),
        "std_dev": std_dev(values),
        "min": min_max(values)[0],
        "max": min_max(values)[1]
    }
def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 1:
        return values[n // 2]
    else:
        mid1 = values[n // 2 - 1]
        mid2 = values[n // 2]
        return (mid1 + mid2) / 2
def mean(values):
    return(sum(values)/len(values))
def std_dev(values):
    mean_value = mean(values)
    variance = sum((x - mean_value) ** 2 for x in values) / len(values)
    return variance ** 0.5
def min_max(values):
    lowest=128
    highest=0
    for i in values:
        if i < lowest:
            lowest = i
        if i > highest:
            highest = i
    return (lowest, highest)    
            
data = [2, 4, 4, 4, 5, 5, 7, 9]
print(summary(data))
# {'mean': 5.0, 'median': 4.5, 'std_dev': 2.0, 'min': 2, 'max': 9}