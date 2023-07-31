# Python program to print positive Numbers in a List

list1 = [-10, 22, -50, 65, -86, 91]
num = 0
while(num < len(list1)):
	if list1[num] >= 0:
		print(list1[num], end = " ")
	num += 1
	
