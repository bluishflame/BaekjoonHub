word = input()

for i in word : 
    if i.isupper() == True : 
        print(i.lower(), end='')
    else :
        print(i.upper(), end='')