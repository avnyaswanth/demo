# Remove duplicates from a string
def removeDuplicate(str, n):	
	idx = 0
	for i in range(0, n):
		for j in range(0, i + 1):
			if (str[i] == str[j]):
				break		
		if (j == i):
			str[idx] = str[i]
			idx += 1
			
	return "".join(str[:index])

str= "this is hitesh"
n = len(str)
ans = removeDuplicate(list(str), n))
print(ans)
