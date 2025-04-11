#define variables and import functions
from docutils.utils import column_width
from numpy import integer
from colorama import Fore,Style,init
init(autoreset=True)
import datetime
stock=integer
price=float
#constants
sales_tax=0.10
discount_treshold=6500
discount_rate=0.05

#create product catalog
products={
    'Dove Body Wash':{'Stock':10,'Price': 100},
    'Fenty Lip Gloss':{'Stock':25,'Price': 2500},
    'Lavender Essential Massage Oil':{'Stock':35,'Price': 3500},
    'EOS Body Lotion':{'Stock':25,'Price': 1800},
    'Vaseline Coca Radiant Body Oil':{'Stock':15,'Price': 1800},
    'Dove Mens All 3 in 1 Body Wash':{'Stock':20,'Price': 1200},
    'Debbies Beard Care Kit':{'Stock':7,'Price': 2800},
    'Imogines Organic Castor Oil':{'Stock':15,'Price': 2550},
    'Sensual Lip Therapy Kit':{'Stock':15,'Price': 1500},
    'Blue Magic Hair Growth Oil':{'Stock':50,'Price': 500},
}
cart={}

def display_products():
    print('\n' + Fore.MAGENTA+              'Ella Beauty Care Product Catalog:')
    print('\n''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('{:<20} {:>33} {:>31}'.format('Product','Price','Stock'))
    for product, details in products.items():
        print('|{:^45}|{:^35}|{:^35}|'.format(
            Fore.BLUE + product + Style.RESET_ALL,
            Fore.GREEN + f'${details["Price"]}' + Style.RESET_ALL,
            Fore.YELLOW + str(details['Stock']) + Style.RESET_ALL,
        ))
    print('\n''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


def add_to_cart():
    while True:
        product=input('Enter product name:').lower().strip()
        product = next((p for p in products if p.lower() == product.lower()), None)
        if product:
            try:
                quantity = int(input('Enter the quantity of product you want to purchase:'))

                if quantity <= 0:
                    print('Amount entered must be greater than zero')
                    continue

            except ValueError:
                print('Invalid input. Please enter a valid number for quantity.')
                continue
            if quantity <= products[product]['Stock']:
                cart[product] = cart.get(product, 0) + quantity
                products[product]['Stock'] -= quantity
                print(f'{quantity} {product}(s) added to cart.')
            else:
                print('Not enough stock available for purchase')
        else:
            print('Product not found.')

        another_transaction = input('Would you like to add another item to the cart? y/n: ').lower().strip()
        if another_transaction != 'y':
            break


def remove_from_cart():

    product=input('Enter product name you want to remove:').lower().strip()
    if product in cart:
        products[product]['Stock'] +=cart[product]
        del cart[product]
        print(f'{product} removed from cart.')
    else:
        print('item not in cart')



def view_cart():
     print('++++++++++++++++++++++++++++++++View Shopping Chart+++++++++++++++++++++++++++++++++++++++++')
     total=0
     if not cart:
         print('Your cart is empty')
         return
     print(f'{"Product":<20}{"Quantity":<30}{"Unit Price":<30}{"Total"}')
     print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
     for product, qty in cart.items():
         price = products[product]['Price']
         subtotal = qty * price
         total += subtotal
         print(f'{product:<20}{qty:<35}{price:<35}{subtotal:<25.2f}')
     print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
     print(f'Your shopping cart total is ${total}. Additional taxes or discount will be applied at checkout')

def low_stock_alert():
    print('\n LOW STOCK!!!!:')
    low_stock={product:info['Stock'] for product,info in products.items() if info['Stock']<5}
    if low_stock:
        for product,stock in low_stock.items():
            print(f'{product} We only have {stock}left!')

    else:
        print('Items in stock!')


def checkout(): # cart checkout


    subtotal =0
    if not cart:
        print('Your cart is empty')
        return
    for product, qty in cart.items():
        price = products[product]['Price']
        subtotal += qty * price
    discount = 0
    if subtotal > discount_treshold:  # calculate discount
        discount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount
    taxes = discounted_subtotal * sales_tax
    total_amount_due = discounted_subtotal + taxes  # total amount calculation
    print(f'\nSubtotal: ${subtotal}')
    print(f'Discount: -${discount}')
    print(f'Taxes: +${taxes}')
    print(f'Total Amount Due: ${total_amount_due}')


    #process payment
    while True:
        try:
            payment_amount=float(input('Enter payment amount:'))
            if payment_amount>=total_amount_due:
                break
            print('Insufficient payment amount,please try again')
        except ValueError:
            print('Please enter a valid amount')
    change=payment_amount-total_amount_due #CHANGE DETAILS
    print(f'Change:          {change}')
    generate_a_receipt= input('Would you like to print a receipt? y/n: ').lower().strip()
    if generate_a_receipt == 'y':
        print('\n========+++++++++++++++++++++++++++++++++++++++++++++==========')
        print('              Welcome to Ella Beauty Care Mart         ')
        print('========+++++++++++++++++++++++++++++++++++++++++++++==========')
        print(f'Date: {datetime.datetime.now()}\n')
        print(f'{"Product":<12}{"Quantity":<20}{"Unit":<18}{"Total"}')

        for item in cart:
            unit = products[item]['Price']
            total_cost = cart[item] * unit
            print(item, {cart[item]}, unit, f'{total_cost:.2f}')
        print('=======+++++++++++++++++++++++++++++++++++++++++++++++==========')
        print(f'Subtotal:            ${subtotal:.2f}')
        print(f'Discount:            -${discount:.2f}')
        print(f'Taxes:               +${taxes:.2f}')
        print(f'Total Amount Due:    ${total_amount_due:.2f}')
        print(f'Change:              ${change:.2f}')
        print('======++++++++++++++++++++++++++++++++++++++++++++++++==========')
        print('++++++++++++++++++++++++++')
        print(f'THANK YOU FOR SHOPPING ELLA BEAUTY CARE')
        print('+++++++++++++++++++++++++++++++++++')
    cart.clear()
    if generate_a_receipt!='y':
        print('No receipt will be printed.')


    

def main_menu():

        while True:
          print('\n Welcome to Ella Beauty Care Mart')
          print('1.Display Products')
          print('2.Add item to Cart')
          print('3.Remove Item')
          print('4.View my cart')
          print('5.Checkout')
          print('6.Exit')
          try:
           choice=int(input('Enter your choice:'))
          except ValueError:
              print('Please enter a valid choice')
              continue

          if choice==1:
              display_products()
          elif choice==2:
              add_to_cart()
          elif choice==3:
              remove_from_cart()
          elif choice==4:
              view_cart()
          elif choice==5:
              checkout()
          elif choice==6:
              print('Exiting System!')
          else:
              print('Invalid choice')

if __name__ == "__main__":
    main_menu()

    























