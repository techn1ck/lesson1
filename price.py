def get_summ (one, two, delimiter='&'):
    result = str(one) + str(delimiter) + str(two)
    return result.upper()

print(get_summ("Learn", "Python", " - "))


def format_price (price):
    price = abs(int(price))
    return f'Price {price}$'

print(format_price(56.24))