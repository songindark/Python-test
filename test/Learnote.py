# -*- coding: utf-8 -*-
#list和tuple是Python内置的有序集合，一个可变，一个不可变,只有1个元素的tuple定义时必须加一个逗号,t = (1,)来消除歧义：
L = [
    ['Apple', 'google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['ada', 'Bart', 'Lisa']
]
print(len(L))
#添加末尾
L.append(['Adam'])
#删除末尾(如果不填参数则删除最后一个)
L.pop(3)
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][-1])
#引用永远为中括号,从零开始到负一
#列表生成式中后面if为判断条件不能加else
L2 =[s.lower() for s in L if isinstance(s,str)==True]
print(L2)
L2 =[x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

#循环
#if if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
n = 0
L=[]
while n < 10:
    n = n + 1
    if n % 2 == 7: # 执行break语句
        break# break语句会结束当前循环
    elif n % 2 == 1: # 如果n是奇数，执行continue语句
        continue # continue语句会"直接"继续下一轮循环，后续的append()语句不会执行
    L.append(n)
    pass
print(L)

#函数
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def mul(x, y=1, *num):#参数定义的顺序必须是：1必选参数、2默认参数(y=1)、3可变参数(*num)、4命名关键字参数(如果没有可变参数，就必须加一个*作为特殊分隔符。)5关键字参数(**kw是关键字参数，kw接收的是一个dict。)
    xy=x * y
    for i in num:#分号与四个空格是必须格式
        xy=i*xy
    return xy

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('累乘测试成功!')
		
#切片与递归
def trim(s):#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
    if s[:1] == " ":#寻找空格切片切成[首:尾:间距]
        return trim(s[1:])##函数嵌套递归
    elif s[-1:] == " ":#寻找空格切片切成[首:尾:间距]
        return trim(s[:-1])#函数嵌套递归
    else:
        return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('切片测试成功!')
#迭代
def findMinAndMax(L):
    if len(L)<1:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if i<min:
            min = i
        if i>max:
            max = i
    return min,max
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('迭代测试成功!')