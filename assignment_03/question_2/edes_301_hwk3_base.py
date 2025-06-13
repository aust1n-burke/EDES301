import math
import string


def rem_div(input, div):
    rem = input%div
    dig_lib = [str(d) for d in range(10)] + list(string.ascii_uppercase)
    quo = input//div
    rem = dig_lib[rem]
    return (quo, rem)

def give_base_form(input, base):

    if input == 0:
        return 0

    digits = []

    while (input > 0):
        quo, rem = rem_div(input, base)

        digits.append(rem)
        input = quo

    digits.reverse()
    digits = "".join(str(d) for d in digits)

    return digits

def print_answers(num):
    print(f"Original number: {num}")
    print(f"Binary: {give_base_form(num, 2)}")
    print(f"Octal: {give_base_form(num, 8)}")
    print(f"Hex: {give_base_form(num, 16)}")
    print()

print_answers(64206)
print_answers(48879)
print_answers(57005)
print_answers(34370)
print_answers(79225)

