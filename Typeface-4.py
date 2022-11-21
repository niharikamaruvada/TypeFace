row = int(input())
col = int(input())
mat = []
for i in range(row):
	a = list(map(int, input().split()))

min_row = 100000
min_col = 100000
max_row. = -1
max_col = -1
for i in range(row):
	for j in range(col):
		if i < min_row:
			min_row = i
		if i > max_row:
			max_row = i
		if j < min_col:
			min_col = j
		if j > max_col:
			max_col = j
print("("+str(min_row)+","+str(min_col)+"),("+str(min_row)+","+str(max_col)+"),("+str(max_row)+","+str(min_col)+"),(+str(max_row)+","+str(max_col)+")")