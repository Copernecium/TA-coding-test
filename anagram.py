def is_anagram(input_here):
    #step 1 checking input
    if len(input_here) != 2 or type(input_here) != list:
        return
    #step 2 remove non alphabet
    #create funtion can make you don't have to write the same code
    def convert(checkremove):
        c = ""
        for i in checkremove:
            if i.isalpha() == True:
                c += i
        #step 3 convert into set
        return set(c)
    convert1 = convert(input_here[0])
    convert2 = convert(input_here[1])
    #step 4 checking if it is the same one
    if convert1 == convert2:
        return True
    else:
        return False
print(is_anagram(["listen","silent"]))
print(is_anagram(["television"," it's one evil."]))
print(is_anagram(["listen", "silentness"]))
print(is_anagram(["hello", "hola" ]))