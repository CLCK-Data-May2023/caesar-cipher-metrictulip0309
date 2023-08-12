# add your code here
def encypt_func(txt, s):  
    result = ""  
  
  
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
# check the above function  
txt = input("Please enter a sentence: ")  
s = 4  
 
print("Shift pattern: " + str(s))  
print("The encrypted sentence is: " + encypt_func(txt, s))