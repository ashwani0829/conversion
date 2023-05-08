from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
codes = CurrencyCodes()

rates = {
    'AUDUSD': 0.8371,
    'CADUSD': 0.8711,
    'USDCNY': 6.1715,
    'EURUSD': 1.2315,
    'GBPUSD': 1.5683,
    'NZDUSD': 0.7750,
    'USDJPY': 119.95,
    'EURCZK': 27.6028,
    'EURDKK': 7.4405,
    'EURNOK': 8.6651
}

while True:
    # user for inputs
    from_currency = input('From: ').upper()
    to_currency = input('To: ').upper()
    amount = float(input('Amount: '))

    # check if currency pair exists
    if f'{from_currency}{to_currency}' in rates:
        rate = rates[f'{from_currency}{to_currency}']
    elif f'{to_currency}{from_currency}' in rates:
        rate = 1 / rates[f'{to_currency}{from_currency}']
    else:
        print(f'Unable to find rate for {from_currency}/{to_currency}')
        continue

    result = amount * rate
    result = round(result, 2) if to_currency != 'JPY' else round(result)
    print(f'{codes.get_symbol(to_currency)} {result:.2f}')
