vowel = ['a', 'e', 'i', 'o', 'u']

while True : 
	sen = input()
	
	if sen == '#' : 
		break
	
	cnt = 0
	sen = sen.lower()
	
	for i in sen : 
		if i in vowel : 
			cnt += 1
			
	print(cnt)
