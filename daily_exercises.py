# By Kwame Boamah


def user_number():
    return int(input("Pick a number! Any number!"))


def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


def numb():
    return int(input("Pick a number."))


def check():
    return int(input("Choose another number."))


def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


def side_option_1():
    int(input("Pick a side."))


def side_optioj_2():
    int(input("Pick another side."))

def s_o_3():
    int()
def is_triangle():
    if s3 < s1 + s2
        return "No!"
    elif s2 < s1 + s3
        return "No!"
    elif s3 < s2 + s3
        return "No!"
    elif s1 + s2 <= s3
        return "Yes"
    elif s1 + s3 <= s2
        return "Yes!"
    elif s2 + s3 <= s1
        return "Yes!"


def main():
    num = user_number()
    even_or_odd(num)
    print("Your number", num, "is", even_or_odd(int(num)))
    print("Ever wonder if two numbers are divisible? Well wonder no more because that's what I'm for.")
    num1 = numb()
    num2 = check()
    print("Your problem was", is_divisible(num1, num2), ".")


main()
