no="Num1"

length=""
def string_creater(no,length):
    
    length=int(input("enter a no : "))
    
    for i in range (0,length):
        k=str(i+1)
        string=""
        string=no+k
        print(string)
        
        num=int(input("enter your no: "))
        kn=num
        symbol=["+","-","×","÷"]
        print("which symbol do you want to use ",symbol)
        sign=input("enter a BODMAS sign: ")
        num2=int(input("enter another no: "))
        total=""
        if sign == "+":
            total=kn+num2
            
        if sign == "-":
            total=kn-num2
        if sign == "×":
            total=kn*num2
        if sign == "÷":
            total=kn/num2
        print("the answer is :  ",total)              
    
    
    return num
    
string_creater(no,length)
