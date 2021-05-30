#variables
hot = int()
sweetsour = int()
Continue = str()
rate = float()
total = float()
Type = str()
quantity = int()
total_wings = int()
subtotal = float()
discount = float()

#Set Parameters
hot = 0
sweetsour = 0

while Continue != 'Q':
    Type = str(input("Type:"))
    print()
    quantity = int(input("Quantity:"))
    print()
    if Type == "hot" and quantity <= 6:
        rate = 0.0
        hot = hot + quantity
    elif Type == "hot" and (quantity > 6 or quantity <= 12):
        rate = 0.1
        hot = hot + quantity
    elif Type == "hot" and (quantity > 12 or quantity <= 24):
        rate = 0.2
        hot = hot + quantity
    elif Type == "sour" and quantity <= 6:
        rate = 0.05
        sweetsour = sweetsour + quantity
    elif Type == "sour" and (quantity > 6 or quantity <= 12):
        rate = 0.1
        sweetsour = sweetsour + quantity
    elif Type == "sour" and (quantity > 12 or quantity <= 24):
        rate = 0.15
        sweetsour = sweetsour + quantity
    else: 
        rate = 0.25
        if Type == "hot":
            hot = hot + quantity
        else:
            sweetsour = sweetsour + quantity
    total_wings = hot + sweetsour
    subtotal = total_wings * 0.5
    discount = subtotal * rate
    total = subtotal - discount
    print("Total:", total)
    Continue = str(input("Continue:"))
