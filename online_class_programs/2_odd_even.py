#EvenOdd(If else)
# n=int(input("N:"))
# if (n//2)*2==n:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")

# n=int(input("N:"))
# if (n//2)*2==n-1:
#     print(f"{n} is Odd")
# else:
#     print(f"{n} is Even")

# Bitwise Operator
# n=int(input("N:"))
# if n&1==0:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")


# n even nos
n = int(input('n: '))

for i in range(1, 2*n+1):
	if i%2==0:
		print(i, end=' ')

for i in range(2, 2*n+1, 2):
	print(i, end=" ")

# n odd nos
for i in range(1, 2*n+1):
	if i%2 != 0:
		print(i, end=' ')

for i in range(1, 2*n+1, 2):
	print(i, end=" ")
