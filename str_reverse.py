def reverse_string(s):
	s= list[s]
	for i in range(len(s) //2):
		temp=s[i]
		s[i]=s[len(s)-i-1]
		s[len(s)-i-1]=temp
	return " ".join(s)
