def get_summ (one, two, delimiter='&'):
    result = str(one) + str(delimiter) + str(two)
    return result.upper()

print(get_summ("Learn", "Python", " - "))


def format_price (price):
    try:
        #price = float(price)
        price = abs(int(float(price)))
        return f'Price {price}$'
    except ValueError:
        return 'неверный формат данных'

name = input("Введите цену: ")
print(format_price(name))
