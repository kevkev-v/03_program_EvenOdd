# -------------------------------------------------------#
# Program: Is your number, even or odd?
# -------------------------------------------------------#

number = int(input("Which number do you want to check? "))

if number % 2 == 0: #Even numbers can be divided by 2 with no remainder
    print("(This is an even number)")
else:
    print("(This is an odd number)")