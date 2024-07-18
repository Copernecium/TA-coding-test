#step 1 making function / สร้าง function ขึ้นมา
def is_anagram(input_here):
    
    #step 2 checking input if there is not 2 value inside or not lsit / เช็คข้อมูลที่รับมาว่ามีมากกว่าสองตัวหรือไม่ใช่ประเภท list
    if len(input_here) != 2 or type(input_here) != list:
        return 
    
    #step 3 convert into set and get only alphabet / เปลี่ยนค่าที่รับมาให้เป็น set แล้วเอาแต่ตัวอักษร
    convert1 = set(x for x in input_here[0] if x.isalpha())
    convert2 = set(x for x in input_here[1] if x.isalpha())
    
    #step 4 checking if it is the match one / เช็คข้อมูลของ set ทั้งสองตัวว่าตรงกันไหม แล้วส่งค่าเป็น boolean
    return (convert1==convert2)
    
#step 5 using funtion to test / ใช้ function เต็มเพื่อ test
print(is_anagram(["listen","silent"]))
print(is_anagram(["television"," it's one evil."]))
print(is_anagram(["listen", "silentness"]))
print(is_anagram(["hello", "hola" ]))
