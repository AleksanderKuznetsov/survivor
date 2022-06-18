"""
Getting the maximum discount when the entire list of goods is known.
Every third cheapest item is free
"""

def MaximumDiscount(count: int, price: list) -> int:
    """
    :param count: number of prices(items)
    :param price: prices
    :return: maximum discount
    """
    xchange = True
    discount = 0
    # Sort array in descending order.
    while xchange:
        xchange = False
        for i in range(count - 1):
            if price[i] < price[i + 1]:
                price[i], price[i + 1] = price[i + 1], price[i]
                xchange = True

    # Add up every third price.
    for i in range(count+1):
        if (i+1) % 3 == 0:
            discount += price[i]

    return discount
