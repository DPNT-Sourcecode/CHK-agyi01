from collections import Counter
import re


def extract_prices_from_txt(filename):
    with open(filename, 'r') as file:
        content = file.read()
    pattern = r"\|\s([A-Z])\s+\|\s(\d+)\s+\|"
    matches = re.finall(pattern, content)

    prices = {item: int(price) for item, price in matches}
    return prices


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    filename = ''
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40,
              'F': 10, 'G': 20, 'H': 35, 'I': 15, 'J': 40,}
    offers = {'A': [(5, 200), (3, 130)],
              'B': [(2, 45)],
              'F': [(3, 20)]}
    skusCount = Counter(skus)

    # check illegal input
    for k in skus:
        if k not in prices:
            return -1

    total = 0

    # fix the number of item for checkout firstly via '2E get one B free'
    if 'E' in skusCount and skusCount['E'] >= 2:
        countFree = skusCount['E'] // 2
        skusCount['B'] = max(0, skusCount['B'] - countFree)

    for sku, count in skusCount.items():
        price = prices[sku]
        if sku in offers:
            for offerCount, offerPrice in offers[sku]:  # get the best offer by sorting
                while count >= offerCount:
                    total += offerPrice
                    count -= offerCount
            total += count * price
        else:
            total += count * price

    return total




