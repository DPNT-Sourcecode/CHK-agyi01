from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    offers = {'A': [(3, 130), (5, 200)], 'B': [(2, 45)]}
    skusCount = Counter(skus)

    # check illegal input
    for k in skus:
        if k not in prices:
            return -1

    total = 0

    # fix the number of item for checkout firstly via '2E get one B free'
    if 'E' in skusCount and 'E' >= 2:
        countFree = skusCount['E'] // 2
        countLeft = skusCount['E'] % 2
        skusCount['B'] = max(0, skusCount['B'] - countFree)
        skusCount['E'] = countLeft

    for sku, count in skusCount.items():
        price = prices[sku]
        if sku == 'B' and count > 2:



        if sku in offers:
            for offerCount, offerPrice in sorted(offers[sku], reverse=True):  # get the best offer by sorting
                while count >= offerCount:
                    tot

                        total += offerPrice
                    count -= offerCount
                skusCount[sku] = count

    total += count * price

    return total






