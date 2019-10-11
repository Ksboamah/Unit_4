# By Kwame Boamah Friday, October 11, 2019


def address():
    return input("Where do you live (M)ontgomery County, (H)oward County, Prince George's (PG) County, or (E)lsewhere?")


def age():
    return int(input("How old are you?"))

def price(location, price_1):
    if location == "M":
        return price_1 == 60
    else:
        return price_1 == 70

def discounts(location, age_v, price_1):



def main():
    print("Welcome to the Adventure Park Ticket Booth!")
    location = address()
    age_v = age()
    price_1 = price(location, price_1)
    if age_v <= 0:
       return int(input("The age entered is invalid. Please enter valid age."))
    discounts(location, age_v, price_1)