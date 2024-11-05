numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
no_prime = []
for i in numbers:
    if i < 2:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        prime.append(i)
    else:
        no_prime.append(i)
print(prime)
print(no_prime)

