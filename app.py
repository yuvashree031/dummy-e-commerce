import os
import logging
from auth import login
from utils import calculate_tax

logging.basicConfig(level=logging.INFO)


def authenticate_user():
    user = os.getenv("APP_USER")
    password = os.getenv("APP_PASSWORD")

    if not user or not password:
        raise ValueError("APP_USER or APP_PASSWORD not set")

    return login(user, password)


def calculate_order_total(prices):
    total = 0

    for price in prices:
        # calculate_tax returns only tax amount
        total += price + calculate_tax(price)

    return total


def process_order():

    prices = [1000, 2000, 3000]

    if authenticate_user():

        total = calculate_order_total(prices)

        logging.info(f"Order Total: {total}")
        logging.info("Order processed")
        logging.info("Invoice generated")
        logging.info("Payment completed")
        logging.info("Notification sent")

    else:
        logging.error("Invalid credentials")


if __name__ == "__main__":
    try:
        process_order()
    except Exception as e:
        logging.exception(f"Application failed: {e}")