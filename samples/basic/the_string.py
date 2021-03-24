#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# s = 'Python-中文'
# print(s)
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))

s1 = 50
s2 = 60
r = (s2-s1)/s2*100
# 用%%来表示一个%：
print('%s, 成绩提升了 %0.1f%%' % ('小明', (s2-s1)/s2*100))
# format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}
print('{0}, 成绩提升了 {1:.1f}%'.format('小明', (s2-s1)/s2*100))
# 以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
print(f'小明, 成绩提升了 {r:.1f}%')
