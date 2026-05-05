# 1) შექმენით ფუნქცია, მიიღებთ რიცხვს, თუ კენტია დააბრუნეთ "კენტია", თუ ლუწი - "ლუწია"
def odd_or_even(num):
    if num % 2  == 0:
        print("ლუწი")
    else:
        print("კენტი")
num1 = int(input("entern num:"))
odd_or_even(num1)


