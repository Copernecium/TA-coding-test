#step 1 making function / สร้าง function ขึ้นมา
def is_anagram(input_here):
    
    #step 2 checking input if there is not 2 value inside or not lsit / เช็คข้อมูลที่รับมาว่ามีมากกว่าสองตัวหรือไม่ใช่ประเภท list
    if len(input_here) != 2 or type(input_here) != list:
        return
    
    #step 3 remove non alphabet / ลบตัวที่ไม่ใช่ตัวอักษรออกไป
    #create funtion can make you don't have to write the same code / ถ้าทำ function จะทำให้ลดบรรทัดการเขียนได้
    def convert(checkremove):
        c = ""
        for i in checkremove:
            if i.isalpha() == True:
                c += i
                
        #step 4 convert into set / แปลงข้อมูลเป็ฯประเภท set แล้วส่งกลับไป
        return set(c)
    
    #step 5 using function we make / ใช้ function ที่สร้างมา
    convert1 = convert(input_here[0])
    convert2 = convert(input_here[1])
    
    #step 6 checking if it is the match one / เช็คข้อมูลของ set ทั้งสองตัวว่าตรงกันไหม แล้วส่งค่าเป็น boolean
    if convert1 == convert2:
        return True
    else:
        return False
    
#step 7 using funtion to test / ใช้ function เต็มเพื่อ test
print(is_anagram(["listen","silent"]))
print(is_anagram(["television"," it's one evil."]))
print(is_anagram(["listen", "silentness"]))
print(is_anagram(["hello", "hola" ]))