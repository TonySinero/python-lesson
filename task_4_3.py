mai = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in mai.keys():
    print(f'{key}{str(len(key))}')

#------------------------------------------------

mai = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
while mai:
    for key in mai.keys():
        print(f'{key}{str(len(key))}')
    break