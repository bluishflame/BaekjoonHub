T = int(input())
 
for t in range(1, T  +1) :
    N = float(input())
 
    result = ""
 
    overflow = False
 
    for _ in range(12):
        N *= 2
        if N >= 1:
            result += "1"
            N -= 1
        else:
            result += "0"
 
        if N==0:
            break
 
    if N != 0:
        print(f"#{t} overflow")
    else:
        print(f"#{t} {result}")