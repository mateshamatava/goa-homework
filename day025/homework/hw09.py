# 10. შექმენით ფუნქცია, მიიღებთ სტრინგს. თქვენი დავალებაა მაგ სტრინგს მოაშოროთ ყველანაირი ცარიელი ადგილი და დატოვოთ მხოლოდ რიცხვები, სიმბოლოები და ასოები

def remove_spaces(string):
    no_space_string = string.replace(" ", "")
    return no_space_string