n = 0
sum = 0
for n in range(0,101):# n 范围 0-100
    sum += n
    if n == 100:
        print (sum)
    elif n == 0:
        print ('get zero')
    elif n == 101:
        print ('get 101')
print(sum)