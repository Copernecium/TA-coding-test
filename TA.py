nes = {'Noodle_cup':20, 'Fried_egg':24, 'Pad_thai':40, 'Krapao_extra':50, 'water':6}
nonnes = {'Chocolate':22, 'Pepsi':18, 'Lemon_tea':15}

def wowza(a):
    # v = "Chocolate Pepsi Lemon_tea"
    ans = a.split(" ")
    sumnon = 0
    sumnes = 0
    notincatalog = 0
    for i in ans:
        if i in nonnes:
            sumnon+=nonnes[i]
        elif i in nes:
            sumnes+=nes[i]
        else:
            print("there is something not in catalog")
            notincatalog+=1
    print("necessary :",sumnes,"Baht\n"+"not necessary :",sumnon,"Baht\n"+"total :",sumnes+sumnon,"Baht")
    if notincatalog != 0:
        print("there is" ,notincatalog, "thing not in catalog")
# wowza("Chocolate Pepsi Lemon_tea")
# wowza("Noodle_cup Fried_egg Pad_thai Krapao_extra water")
wowza("Noodle_cup Pepsi Fried_egg water Chocolate Krapao_extra Lemon_tea wowza za")