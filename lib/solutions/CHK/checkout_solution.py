from collections import Counter

+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+

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
            for offerCount, offerPrice in sorted(offers[sku], reverse=True): # get the best offer by sorting
                while count >= offerCount:
                    if sku == 'E' and offerPrice == 0




            offerCount, offerPrice = offers[sku]
            total += (count // offerCount) * offerPrice
            total += (count % offerCount) * price
        else:
            total += count * price

    return total





