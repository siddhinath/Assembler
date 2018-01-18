#import deque
def cipher():
	matrix=[[chr(i+65) for i in range(26)] for j in range(26)]
	for i in range(26):
		t=matrix[i][0:i]
		n=matrix[i][i:]
		matrix[i]=n+t
	#print(matrix)
	for i in matrix:
		print(i)
	Str=input().strip()
	key=input().strip()
	l=len(Str)
	k=len(key)
	d=l//k
	key=key*d
	key=key+key[0:(l%k)]
	print(key)
	temp=[]
	for i in range(len(Str)):
		s_i=ord(Str[i])-65
		k_i=ord(key[i])-65
		temp.append(matrix[k_i][s_i])
	
	print(temp)
	key_=12
	for i in Str:
		print(matrix[ord(i)-65][key_])
cipher()
