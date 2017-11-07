n = 1
while n <= 100:
    if n > 12:
        break
    print(n)
    n = n +1
print('END')

print('*****demo continue*****')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

