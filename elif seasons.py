#seasons
input_month = input()
input_day = int(input())

mon_len = {'January': 31, 'March': 31, 'May': 31, 'July': 31, 'August': 31, 'October': 31,
           'December': 31, 'April': 30, 'June': 30, 'September': 30, 'November': 30, 'February': 28}

month_to_day = {'January': 1, 'February': 32, 'March': 60, 'April': 91,
    'May': 121, 'June': 152, 'July': 182, 'August': 213,
    'September': 244, 'October': 274, 'November': 305,
    'December': 335}

if (input_month not in month_to_day) or (input_day > mon_len[input_month] or input_day <= 0):
    print('Invalid')

else:
    day_to_szn = month_to_day[input_month] + input_day
    if 79 <= day_to_szn <= 171:
        print('Spring')
    elif 172 <= day_to_szn <= 264:
        print('Summer')
    elif 265 <= day_to_szn <= 354:
        print('Autumn')
    else:
        print('Winter')

