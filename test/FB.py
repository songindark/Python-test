def fib(n):  # 定义到 n 的斐波那契数列,print
    a, b = 0, 1
    while b < n:
        if b == 377:
            # raise Exception('b 不能 377。a 的值为: {}'.format(a))
            break
        else:
            print(b, end=' ')  # end=' '意思是末尾不换行，加空格
            a, b = b, a + b  # a=b b=a+b n=b
    return

def fib2(n):  # 返回到 n 的斐波那契数列 return
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    print('程序自身在运行')
    fib(200)
else:
    print('我来自另一模块')
