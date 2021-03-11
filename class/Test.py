# noinspection PyPep8Naming
class Test(object):  # 定义父类
    __secretCount = 0  # 私有变量，两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问
    publicCount = 0  # 公开变量

    # noinspection PyPep8Naming
    def InstanceFun(self):  # 普通方法: 默认有个self参数，且只能被对象调用。
        print("InstanceFun")
        print('我是父类方法')
        print(self)

    @classmethod  # 类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上@classmethod 装饰器。
    def ClassFun(cls):
        print("ClassFun")
        print('我是类方法')
        print(cls)

    @staticmethod  # 静态方法:用 @staticmethod 装饰的不带self参数的方法叫做静态方法，。
    def StaticFun():  # 类的静态方法可以没有参数，可以直接使用类名调用
        print("StaticFun")
        print('我是静态方法')


class Child(Test):  # 定义子类
    def InstanceFun(self):  #
        print('我是子类方法')
        print("InstanceFun")
        print(self)


p = Test()
p.InstanceFun()  # 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
p.ClassFun()  # 输出ClassFun，打印类位置 <class '__main__.Test'>
p.StaticFun()  # 输出StaticFun
Test.StaticFun()  # 输出StaticFun

# Test.ClassFun() # 输出ClassFun，打印类位置 <class '__main__.Test'>
# Test.InstanceFun();  # 错误，TypeError: unbound method instanceFun() must be called with Test instance as first argument
# Test.InstanceFun(t);  # 输出InstanceFun，打印对象内存地址“<__main__.Test object at 0x0293DCF0>”
# t.ClassFun(Test);  # 错误   classFun() takes exactly 1 argument (2 given)

c = Child()  # 子类实例没有self
c.InstanceFun()  # 子类调用重写方法
super(Child, c).InstanceFun()  # 用子类对象调用父类已被覆盖的方法
