score = float(input())
if 0.0 <= score <= 1.0:
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("c")
    elif score >= 0.6:
        print("D")
    else: 
        print("F")
else:
    print("Error")