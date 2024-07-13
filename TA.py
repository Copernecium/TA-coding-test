#list all word and price by using tuple
necessary = {'Noodle_cup':20, 'Fried_egg':24, 'Pad_thai':40, 'Krapao_extra':50, 'water':6}
not_necessary = {'Chocolate':22, 'Pepsi':18, 'Lemon_tea':15}

#making funtion
def wowza(input_here):
    #split each food into list
    splitword = input_here.split(" ")
    
    #making summary of all
    summary_not_ness = 0
    summary_ness = 0
    notincatalog = 0
    
    #making loop of list
    for i in splitword:
        
        #checking type of food
        if i in not_necessary:
            summary_not_ness+=not_necessary[i]
        elif i in necessary:
            summary_ness+=necessary[i]
        else:
            #print("there is something not in catalog")
            notincatalog+=1
    
    #print output
    print("necessary :",summary_ness,"Baht\n"+"not necessary :",summary_not_ness,"Baht\n"+"total :",summary_ness+summary_not_ness,"Baht")
    if notincatalog != 0:
        print("there is" ,notincatalog, "thing not in catalog")
    
    print("==========================================================================")
wowza("Chocolate Pepsi Lemon_tea")
wowza("Noodle_cup Fried_egg Pad_thai Krapao_extra water")
wowza("Noodle_cup Pepsi Fried_egg water Chocolate Krapao_extra Lemon_tea wowza za")