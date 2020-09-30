"""
Program: coupon_calculations.py
Author: Jack Reser

program that accepts price, cash coupon and percent coupon.  Prints out the total price
"""


def calculate_price(price, cash_coupon, percent_coupon):
    UNDER_10 = 5.95
    UNDER_30 = 7.95
    UNDER_50 = 11.95
    SALES_TAX = 1.06

    price -= cash_coupon
    price -= (percent_coupon/100)*price
    price = price*SALES_TAX

    if (price<=10):
        price += UNDER_10
    elif (price<=30):
        price += UNDER_30
    elif (price<=50):
        price += UNDER_50
    else:
        return round(price,2)

    return round(price,2)


if __name__ == '__main__':
    print(calculate_price(15.99, 5, 30))

