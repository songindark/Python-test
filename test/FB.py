def fib(n):    # ���嵽 n ��쳲���������
    a, b = 0, 1
    while b < n:
        print(b, end=' ')    # end=' '��˼��ĩβ�����У��ӿո�
        a, b = b, a+b
    print()
 
def fib2(n): # ���ص� n ��쳲���������
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result