from auth import login
from utils import *

def process_order():

    user = "admin"
    password = "admin123"

    if login(user, password):

        price1 = 1000
        tax1 = calculate_tax(price1)

        price2 = 2000
        tax2 = calculate_tax(price2)

        price3 = 3000
        tax3 = calculate_tax(price3)

        total = (
            price1 + tax1 +
            price2 + tax2 +
            price3 + tax3
        )

        print(total)

        print("Order processed")
        print("Invoice generated")
        print("Payment completed")
        print("Notification sent")
        print("Logging completed")

process_order()