import random



numbers = range(100)
yellow_card = random.sample(numbers,15)
blue_card = random.sample(numbers,15)




try:
    if yellow_card != [] and blue_card != []:
        for i in random.sample(numbers,1):
            print("Value is :" ,i)
            if i in yellow_card and blue_card:
                yellow_card.remove(i)
                blue_card.remove(i)
                
                print("Value removed :" ,yellow_card,  blue_card , i)
                
            elif i in blue_card:
                blue_card.remove(i)
                
                print("Value removed (Blue Card) :" , blue_card , i)
            elif i in yellow_card:
                yellow_card.remove(i)
                
                print("Value removed (Yellow ) :" ,yellow_card, i)
            else:
                print("Nothing")
    elif yellow_card == [] and blue_card != []:
        print("Yellow card wins.")
    elif yellow_card != [] and blue_card == []:
        print("Blue card wins.")
    else :
        print("It is draw!")
    
    
            
except ValueError:
    print("Nothing")
        
  
       
    








