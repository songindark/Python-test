#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('Tracy in d =', 'Tracy' in d)
print('d.get(\'Tracy\', -1) =', d.get('Tracy', -1))
print('Thomas in d =', 'Thomas' in d)
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))
