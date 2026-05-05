# პირიქით, მიიღებთ სიას, ყველა ელემენტი იქნება დიდი ასოებით დაწერილი, უნდა გააერთიანოთ და შემდეგ ყველა ასო პატარა ასოდ გარდაქმნათ.
def list_to_lower_string(word_list):
    word = "".join(word_list)
    lower_word = word.lower()
    return lower_word