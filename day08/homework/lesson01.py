#  გააკეთეთ სისტემა სადაც თუ მომხმარებლის ასაკი ნაკლებია 18-ზე დაპტინტეთ 'დაბლოკილი ხარ', სხვა შემთხვევაში 'ზრდასრული ხარ'

sistema = int(input("enter you sistema"))

if sistema <18:
    print("dablokili xar")
    
elif sistema >18:
    print("zrdasruli xar")
    
else:
    print("arcerti")
    
    
# დაწერეთ კოდი რომელიც იქნება შუქნიშანის მსგავსი სისტემა, თუ სიტყვა არის 'მწვანე' გამოიტანეთ 'წადი', თუ ფერი არის ყვითელი 
# მაშინ გამოიტანე 'მოემზადე', სხვა შემთხვევაში, ანუ წითელზე 'გაჩერდი'
    
Shuknishani = int(input("enter you shuknishani"))
    
if Shuknishani <40:
        
    print("mwvanea wadi")
        
elif Shuknishani >5:
        
    print("yvitelia moemzade")
        
else:
    print("witelia gacherdi")
    