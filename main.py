def count_discount():
    input_prices = open_file("discount.in")
    discount_pers = (input_prices.pop(-1) / 100)
    sorted_prices_list = sort_prices(input_prices, discount_pers)
    final_sum = sum(sorted_prices_list)
    return round(final_sum, 2)


def sort_prices(prices: list, discount):
    prices.sort()
    for i in range(len(prices) // 3):
        max_price = prices.pop(-1)
        max_price = max_price - (max_price * discount)
        prices.insert((i * 3 + 2), round(max_price, 2))
    return prices


def insert_in(prices, discount_num):
    file = open("discount.in", 'w')
    for elem in prices:
        file.write(str(elem) + " ")
    file.write("\n" + str(discount_num))


def insert_out(result):
    file = open("discount.out", 'w')
    file.write(str(result))


def open_file(url):
    price_data = []
    with open(url) as file:
        for line in file:
            price_data.extend([float(item) for item in line.split()])
    return price_data


if __name__ == '__main__':
    insert_in([1, 2, 3, 4, 5, 6, 7], 100)
    print(count_discount())
    insert_out(count_discount())
