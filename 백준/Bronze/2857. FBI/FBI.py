FBI=[]

for i in range(1,6):
    S = input()
    if "FBI" in S:
        FBI.append(i)
if len(FBI) == 0:
    print("HE GOT AWAY!")
else:
    print(*FBI)