# By Kwame Boamah Friday, October 11, 2019


def address():
    return input("Where do you live (M)ontgomery County, (H)oward County, Prince George's (PG) County, or (E)lsewhere?")


def age():
    return int(input("How old are you?"))


def discounts(location, age_v):
    if age_v < 5:
        return 0
    elif age_v >= 65:
        if location == "M" or "E":
            return 30
        else:
            return 60
    elif location == "H":
        if age_v < 14:
            return 28.70
        else:
            return 35
    elif location == "PG":
        if age_v >= 65:
            return 32.36
        else:
            return 35
    else:
        if location == "E":
            return 70
        if location == "E" and age_v >= 65:
            return 35
        if location == "M" or "H" or "E" or "PG" and 5 <= age_v < 65:
            return 70



def main():
    print("Welcome to the Adventure Park Ticket Booth!")
    location = address()
    age_v = age()
    if age_v <= 0:
        return int(input("The age entered is invalid. Please enter valid age."))
    discounts(location, age_v)
    print("Your Ticket price is", discounts(location, age_v))


main()
