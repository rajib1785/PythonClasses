
##### compare 3 numbers and output

Num_1 = int(input('Please enter 1st number, a: '))
Num_2 = int(input('Please enter 2nd number, b: '))
Num_3 = int(input('Please enter 3rd number, c: '))

#### check equality ######

if Num_1 == Num_2 == Num_3:
    print('a = b = c')
elif Num_1 == Num_2:
    print('a = b and c is different')
elif Num_2 == Num_3:
    print('b = c and a is different')
elif Num_1 == Num_3:
    print('a = c and b is different')

#### check inequality and order ######

elif Num_1 > Num_2:
    if Num_2 > Num_3:
        print('a > b > c')
    elif Num_3 > Num_1:
        print('c > a > b')
    else:
        print('a > b > c')
elif Num_2 > Num_3:
    if Num_3 > Num_1:
        print('b > c > a')
    else:
        print('b > a > c')
else:
    print('c > b > a')

### End #####
