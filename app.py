import os
from auth import login
from utils import calculate_tax

def process_order():

    user = os.getenv("APP_USER")
    password = os.getenv("APP_PASSWORD")

    if login(user, password):

     prices = [1000,2000,3000]

    total = 0

    for price in prices:
        total += price + calculate_tax(price)

    print(total)

        print("Order processed")
        print("Invoice generated")
        print("Payment completed")
        print("Notification sent")
        print("Logging completed")

    else:
        print("Invalid credentials")

if __name__ == "__main__":
    process_order()
