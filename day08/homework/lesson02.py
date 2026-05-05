# დაწერეთ კოდი, სადაც პროდუქტები რისიც ყიდვა გვინდა, ჯამში ღირს 22.50 ლარი, თუ გვაქვს ამაზე მეტი, მაშინ გამოვიტანოთ 
# 'ხურდა: 22.50 - ფული რაც გვაქვს', თუ არ გვყოფნის მაშინ გამოვიტანოთ: 'გაკლია 22.50 - რაც გვაქვს'

produktebipasi = int(input("enter you produktrbicpasi"))

if produktebipasi >22.50:
    
    print("ხურდა: 22.50 - ფული რაც გვაქვს")
    
elif produktebipasi <22.50:
    
    print("გაკლია: 22.50 - რაც გვაქვს")
    
else:
    
    print("vapshe ar mak puli")