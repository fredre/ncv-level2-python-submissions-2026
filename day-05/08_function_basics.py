def order():
    print("place order")
    
def get_order():
    print("preparing order")
    return("order ready")

def place_order(item):
    print(f"order placed for : {item}")
    
def calculate_total(item):
    price = 25.5
    vat = 15/100
    item_price = (price + int(len(item)))*(1+vat)
    return item_price
    
    
order()
myfood = input("what do you want ")
place_order(myfood)
msg=get_order()
print(msg)
money = calculate_total(myfood)
print (f"it costs {money:.2f}")