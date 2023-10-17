from collections import Counter
import re
import os


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
    # base_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..')
    filename = os.path.join(os.getcwd(), 'challenges', 'CHK_R4.txt')
    prices = extract_prices_from_txt(filename)
    # prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40,
    #           'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60,}
    offers = {'A': [(5, 200), (3, 130)],
              'B': [(2, 45)],
              'F': [(3, 20)],
              'H': [(10, 80), (5, 45)],
              'K': [(2, 150)],
              'P': [(5, 200)],
              'Q': [(3, 80)],
              'U': [(3, 80)],
              'V': [(3, 130), (2, 90)]
              }
    skusCount = Counter(skus)

    # check illegal input
    for k in skus:
        if k not in prices:
            return -1

    total = 0

    # fix the number of item for checkout firstly via '2E get one B free'
    if 'E' in skusCount and skusCount['E'] >= 2:
        countFreeB = skusCount['E'] // 2
        skusCount['B'] = max(0, skusCount['B'] - countFreeB)

    # fix the number of item for checkout firstly via '3N get one M free'
    if 'N' in skusCount and skusCount['N'] >= 3:
        countFreeM = skusCount['N'] // 3
        skusCount['M'] = max(0, skusCount['M'] - countFreeM)

    # fix the number of item for checkout firstly via '3R get one Q free'
    if 'R' in skusCount and skusCount['R'] >= 3:
        countFreeQ = skusCount['R'] // 3
        skusCount['Q'] = max(0, skusCount['Q'] - countFreeQ)

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






