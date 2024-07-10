# COUNT NO OF DIGITS
n = abs(int(input("n: "))) # abs converts -ve nos to +ve
count = 0
while n != 0:
	count += 1
	n //= 10

print(c)
# ctrl + c ==> keyboard interrupt




# Reversing a number
n = abs(int(input("n: ")))
print(int(str(n)[::-1])) 
# or
n = abs(int(input("n: ")))
res = 0
while n != 0:
	rem = n % 10
	res = res * 10 + rem
	n //= 10
print(res)





# counting 0s, evens and odds in a number

n = abs(int(input("n: ")))
zero_count, even_count, odd_count = 0, 0, 0
for i in str(n):
	if int(i) == 0:
		zero_count += 1
	elif int(i) % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
print(f'zeros: {zero_count}\nevens: {even_count}\nodd: {odd_count}')
# or
n = abs(int(input("n: ")))
zero_count, even_count, odd_count = 0, 0, 0
while n != 0:
	rem = n % 10
	if rem == 0:
		zero_count += 1
	elif rem % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	n //= 10
print(f'zeros: {zero_count}\nevens: {even_count}\nodd: {odd_count}')







# sum of odd digits and sum of even digits
n = abs(int(input("n: ")))
sum_even, sum_odd = 0, 0
while n != 0:
	rem = n % 10
	if rem % 2 == 0:
		sum_even += rem
	else:
		sum_odd += rem
	n //= 10
print(f'evens sum: {sum_even}\nodds sum: {sum_odd}')





# find max and min digit from given integer no
n = abs(int(input("n: ")))
min = 9
max = 0 
for i in str(n):
	if int(i) > max:
		max = int(i)
	if int(i) < min:
		min = int(i) 
print(f'Min: {min} \nMax: {max}')
# or
n = abs(int(input("n: ")))
min = 9
max = 0 
while n != 0:
	rem = n % 10
	if rem > max:
		max = rem
	if rem < min:
		min = rem 
	n //= 10

print(f'Min: {min} \nMax: {max}')