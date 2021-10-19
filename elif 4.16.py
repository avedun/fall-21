highway_number = int(input())
is_odd = ''

is_odd = True if (highway_number % 2) == 0 else False

if (highway_number % 100) == 0 or 0 <= highway_number <=1000 == False:
    print('not valid')

elif 1 <= highway_number <= 99:
    print('I-{} is primary,'.format(highway_number), end=' ')
    if is_odd is True:
        print('going north/south.')
    else:
        print('going east/west.')

elif 100 <= highway_number <= 999:
    hn = highway_number // 100
    service = highway_number - (hn * 100)
    print('I-{} is auxiliary, serving I-{},'.format(highway_number, service), end=' ')
    if is_odd is True:
        print('going north/south.')
    else:
        print('going east/west.')
