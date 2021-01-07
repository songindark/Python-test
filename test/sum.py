#累加
n = 0
sum = 0
for n in range(0,101):# n 范围 0-100,大于等于并小于
    sum += n
    if n == 100:
        print (sum)
    elif n == 0:
        print ('get zero')
    elif n == 101:
        print ('get 101')
    # else:
    #     print('get else')
    else:
        pass
        continue
print("1 到 %d 之和为: %d" % (n,sum))
