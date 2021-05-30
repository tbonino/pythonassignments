def GetTotal(price, pounds, ounces):
    #variables
    total = float()
    #determine total
    total = price * (pounds + ounces/16)
    #rounding total price
    total = round(total, 2)

    return total
