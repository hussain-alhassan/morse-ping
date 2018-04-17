arr = []

arr.append(3)
arr.append(7)
arr.append(23)
arr.append(23)



for i in range (len(arr)-1):
	#print arr[i]
	#print arr[i+1]
	
	if (arr[i] == arr[i+1]):
		print '======='
	else:
		print '!=!=!='

	