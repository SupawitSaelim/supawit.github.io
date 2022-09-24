discount = 0.15

def input_sale():
    i = int(input('Enter the price of the item: '))
    return i

def discount_sale(m):
    d = m * discount
    return d

def main():
    x = input_sale()
    result = x - discount_sale(x) 
    print('The price of the item is: %d' %(result))

main()
