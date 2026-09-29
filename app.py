import os
import logging
from auth import login
from utils import calculate_tax

logging.basicConfig(level=logging.INFO)

def authenticate_user():
    user = os.getenv("APP_USER")
    password = os.getenv("APP_PASSWORD")
    return login(user, password)

def calculate_order_total():
    prices = [1000, 2000, 3000]
    total = 0

    for price in prices:
        total += price + calculate_tax(price)

    return total

def log_order_status(total):
    logging.info(f"Order Total: {total}")
    logging.info("Order processed")
    logging.info("Invoice generated")
    logging.info("Payment completed")
    logging.info("Notification sent")

def process_order():
    if authenticate_user():
        total = calculate_order_total()
        log_order_status(total)
    else:
        logging.error("Invalid credentials")

if __name__ == "__main__":
    process_order()
