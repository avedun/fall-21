# oil change

services = {'Oil change': '$35', 'Tire rotation': '$19', 'Car wash': '$7'}
is_error = True

req = str(input('Enter desired auto service:\n'))
print('You entered: {}'.format(req))


for i in services:
    if i.lower() == req.lower():
        print('Cost of {}: {}'.format(i.lower(), services[i]))
        is_error = False

if is_error == True:
    print('Error: Requested service is not recognized')