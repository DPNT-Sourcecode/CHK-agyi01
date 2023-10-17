from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(3, 130), (5, 200)], 'B': [(2, 45)], 'E':[(2, 0)]}
    itemCount = Counter(skus)

    # check illegal input
    for k in skus:
        if k not in prices:
            return -1

    total = 0
    for sku, count in itemCount.items():
        price = prices[sku]

        if sku in offers:
            for offerCount, offerPrice in sorted(offers[sku], reverse=True):  # get the best offer by sorting
                while count >= offerCount:
                    if sku == 'E' and offerPrice == 0:  # 2E get one B free
                        itemCount['B'] = max(0, itemCount['B'] - 1)
                    else:
                        total += offerPrice
                    count -= offerCount
    total += count * price

    return total






