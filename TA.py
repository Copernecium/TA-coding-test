def wowza(input_here):
    if type(input_here) != list:
        return print("input is not list\n")
    for i in input_here:
        if type(i) != str and type(i) != list:
            return print("input inside is not list or string\n")
    
    necessary = {'Noodle_cup':20, 'Fried_egg':24, 'Pad_thai':40, 'Krapao_extra':50, 'water':6}
    not_necessary = {'Chocolate':22, 'Pepsi':18, 'Lemon_tea':15}
    
    itemtoremove = []
    for i in input_here:
        if type(i) == list:
            if i[1] == 1:
                necessary[i[0]] = i[2]
            if i[1] == 2:
                not_necessary[i[0]] = i[2]
            itemtoremove.append(i)
    for i in itemtoremove:
        input_here.remove(i)

    summary_not_ness = summary_ness = notincatalog = 0
    for wordsplit in input_here:
        splitword = wordsplit.split(" ")
        for i in splitword:
            if i in not_necessary:
                summary_not_ness+=not_necessary[i]
            elif i in necessary:
                summary_ness+=necessary[i]
            else:
                notincatalog+=1
                
    print("necessary :",summary_ness,"Baht"+"\n"+"not necessary :",summary_not_ness,"Baht\n"+"total :",summary_ness+summary_not_ness,"Baht")
    if notincatalog != 0:
        print("there is" ,notincatalog, "thing not in catalog")
    return [summary_ness,summary_not_ness,summary_ness+summary_not_ness,notincatalog]
    
print(wowza(["Noodle_cup Pepsi Fried_egg", "water Chocolate", "Krapao_extra Lemon_tea Coke"]))
print(wowza(["Noodle_cup Pepsi Fried_egg Soda", "water Chocolate", ["Coke",2,20], "Krapao_extra Lemon_tea Coke", ["Soda",2,15]]))
print(wowza(["Noodle_cup Pepsi Fried_egg”, “water Chocolate”, “Krapao_extra Lemon_tea Coke"]))