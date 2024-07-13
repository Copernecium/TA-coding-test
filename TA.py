#step 1 making funtion
def wowza(input_here):
    
    #step 2 checking input
    if type(input_here) != str:
        print("input is not string\n"
              +"==========================================================================")
        return
    
    #step 3 list all word and price by using tuple
    necessary = {'Noodle_cup':20, 'Fried_egg':24, 'Pad_thai':40, 'Krapao_extra':50, 'water':6}
    not_necessary = {'Chocolate':22, 'Pepsi':18, 'Lemon_tea':15}
    
    #step 4 split each food into list
    splitword = input_here.split(" ")
    
    #step 5 making summary of all
    summary_not_ness = 0
    summary_ness = 0
    notincatalog = 0
    
    #step 6 making loop of list
    for i in splitword:
        
        #step 7 checking type of food
        if i in not_necessary:
            summary_not_ness+=not_necessary[i]
        elif i in necessary:
            summary_ness+=necessary[i]
        else:
            notincatalog+=1
    
    #step 8 print output
    print("necessary :",summary_ness,"Baht\n"+"not necessary :",summary_not_ness,"Baht\n"+"total :",summary_ness+summary_not_ness,"Baht")
    if notincatalog != 0:
        print("there is" ,notincatalog, "thing not in catalog")
    print("==========================================================================")
    
#step 9 using function to test
wowza([""])
wowza("Chocolate Pepsi Lemon_tea")
wowza("Noodle_cup Fried_egg Pad_thai Krapao_extra water")
wowza("Noodle_cup Pepsi Fried_egg water Chocolate Krapao_extra Lemon_tea wowza za")