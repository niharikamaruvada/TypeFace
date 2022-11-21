

n = int(input())

binary_number = ""
while n > 0:
	binary_number = str(n%3)+binary_number
	n = n // 3
print(binary_number)