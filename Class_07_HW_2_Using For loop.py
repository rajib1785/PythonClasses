# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:19:14 2017

@author: Rajib
"""

# Home Task Type-1: left alligned triangle of * character
print('# Home Task Type-1: left alligned triangle of * character: ')
row_num = abs(int(input('Please enter desired row number: ')))
print('\n')
for line_num in range(row_num):
    for char_inline in range(line_num + 1):
        print('*', end='\t')
    print('\n')
print('Loop End Here\n')

# Home Task Type-2: right alligned triangle of * character
print('# Home Task Type-2: right alligned triangle')
row_num = abs(int(input('Please enter desired row number: ')))
for line_num in range(row_num):
    print((row_num-line_num-1)*'\t', end='')
    for char_inline in range(line_num + 1):
        print('*', end='\t')
    print('\n')
print('Loop End Here\n')

# Alternate of Type-2: right alligned triangle of * character
print('# Alternate of Type-2: right alligned triangle of * character')
row_num = abs(int(input('Please enter desired row number: ')))
for i in range(row_num):
    for j in range(1):
        print((row_num-i-1)*'\t', end='')
        print((i + 1)*'*\t', end='')
        print('\n')
print('Loop End Here \n')

# Home Task Type-3: left alligned inverted triangle of * character
print('# Home Task Type-3: left alligned inverted triangle of * character')
row_num = abs(int(input('Please enter desired row number: ')))
print('\n')
for line_num in range(row_num):
    for char_inline in range(row_num):
        print('*', end='\t')
    row_num -= 1
    print('\n')
print('Loop End Here\n')


# Home Task Type-4 number sequence in left alligned triangular form
print('# Home Task Type-4 number sequence in left alligned triangular form')
y = 0
print('\n')
for line_num in range(5):
    for char_inline in range(line_num + 1):
        print(y+1, end='\t')
        y += 1
        if y % 5 == 0:
            y = 0
    print('\n')
print('Loop End Here\n')


# Home Task Type-5 equlateral trianle of * character
print('# Home Task Type-5 equlateral trianle of * character')
row_num = abs(int(input('Please enter desired row number: ')))
for i in range(row_num):
    for j in range(1):
        print((row_num-i-1)*'   ', end='')
        print((2*i + 1)*' * ', end='')
        print('\n')
print('Loop End Here \n')
