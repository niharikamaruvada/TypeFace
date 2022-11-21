
n = int(input())

possible_reverse = [1, 2, 5, 6, 8, 9, 0]
count = 0

for i in range(1, 100):
	temp = str(i)
	flag = 1
	for j in temp:
		if int(j) not in possible_reverse:
			flag = 1
			exit
		else:
			flag = 0
	if flag == 0:
		count = count + 1
	if count == n:
		print(i)
		exit