# 3) შექმენით ფუნქცია, მიიღებთ ორ რიცხვს, დააბრუნეთ ამ რიცხვების სხვაობა
def sxvaoba(a,b):
    if a > b :
        return a - b
    elif a == b:
        return "სხვაობა არ არის"
    else:
        return b - a

num = int(input("enter num:"))
num1 = int(input("enter num:"))
print(sxvaoba(num,num1))
