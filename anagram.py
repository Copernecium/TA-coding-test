def is_anagram(a):
    if len(a) != 2 or type(a) != list:
        return
    def convert(b):
        c = ""
        for i in b:
            if i.isalpha() == True:
                c += i
        return set(c)
    convert1 = convert(a[0])
    convert2 = convert(a[1])
    # print("work",convert1,convert2)
    if convert1 == convert2:
        return True
    else:
        return False
# print(is_anagram(["asda","dsasd"]))
print(is_anagram(["listen","silent"]))
print(is_anagram(["television"," it's one evil."]))
print(is_anagram(["listen", "silentness"]))
print(is_anagram(["hello", "hola" ]))