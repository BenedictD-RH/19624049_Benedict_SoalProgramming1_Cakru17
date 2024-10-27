import datetime

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
octal = 0
basetype = [10,2,8,16]
converterhistory = []

def space(size) :
    for i in range(size) :
        print("")
        
def findbase(number) :
    for i in basetype :
        if number.endswith(f"({i})") :
            base = i

    return base

def validnumber(number) :
    validbase = False
    validdigit = False
    for i in basetype :
        if number.endswith(f"({i})") and len(number) >= 4:
            validbase = True
            if number.endswith("(2)") or number.endswith("(8)") == True :
                number = number[:-3]
            else :
                number = number[:-4]
    
            while number != "" :
                validdigit = False
                for k in range(i) :
                    if number.endswith(digits[k]) == True :
                        validdigit = True

                if validdigit == False :
                    break
                number = number[:-1]

    
    if validdigit and validbase == True :
        return True
    else :
        return False
                
                

def decimalconvert(decimal, base) :
    cap = 0
    number = ""
    
    while decimal > pow(base,cap) - 1 :
        cap = cap + 1
    
    while cap > 0 :
        for i in range(base - 1,-1,-1) :
            if decimal - i*pow(base,cap - 1) >= 0 :
                number = number + digits[i]
                decimal = decimal - i*pow(base,cap - 1)
                break
        cap = cap - 1
    
    return number + f"({base})"

def converttodecimal(number, base) :
    cap = 0
    decimal = 0
    
    while number != "" :
        for i in range (base-1,-1,-1) :
            if number.endswith(digits[i]) == True :
                decimal = decimal + i*pow(base,cap)
                number = number[:-1]
                break
        cap = cap + 1
    
    return decimal

def printhistory(history) :
    maxlength = 15
    for j in range(len(history)) :
        if maxlength < len(history[j][0]) :
            maxlength = len(history[j][0])
            
    border = "+" + ((maxlength + 2) * "-" ) + "+" + (21 * "-") + "+"
    print(border)
    
    for j in range(len(history)) :
        tablespace = (maxlength - len(history[j][0])) * " "
        print(f"| {history[j][0]}{tablespace} | {history[j][1]} |")
        print(border)
        


exitconverter = False
while exitconverter == False :
    print("<1> Convert Number")
    print("<2> History")
    print("<0> Exit")
    
    validinput = False
    while validinput == False :
        pickaction = input("Pick Tool : ")
        if pickaction == "1" or pickaction == "2" or pickaction =="0":
            validinput = True
        else :
            print("Input a valid option!")


    if pickaction == "1" :
        print("Input Format : number(basetype)")
        print("Binary(2) ; Octal (8) ; Decimal (10) ; Hexadecimal (16)")
        operationrecord = ""
        
        validinput = False
        while validinput == False :
            number = input("Input Number : ")
            if validnumber(number) == True:
                validinput = True
            else :
                print("Input a valid number, including the numerical base!")
        
        operationrecord = operationrecord + number
        inputbase = findbase(number)
        if number.endswith("(2)") or number.endswith("(8)") == True :
            number1 = number[:-3]
        else :
            number1 = number[:-4]
        
        print("Convert into?")
        print("<1> Decimal")
        print("<2> Binary")
        print("<3> Octal")
        print("<4> Hexadecimal")
        
        validinput = False
        while validinput == False :
            pickconvert = int(input("Pick Convert : "))
            if pickconvert == 1 or 2 or 3 or 4 :
                validinput = True
            else :
                print("Input a valid option!")
        
        convertednumber = converttodecimal(number1, inputbase)
        convertednumber = decimalconvert(convertednumber, basetype[pickconvert - 1])
        operationrecord = operationrecord + " => " + convertednumber
        print(operationrecord)
        operationtime = str(datetime.datetime.now())[:-7]
        converterhistory.insert(0, [operationrecord,operationtime])
        
        space(2)
        
    elif pickaction == "2" :
        printhistory(converterhistory)
        space(3)
    else :
        validinput == False
        while validinput == False : 
            yesorno = input("Exit Converter? [Y/N] : ")
            if yesorno == "Y" or "N" :
                validinput = True
            else :
                print("Input a valid option!")
        
        if yesorno == "Y" :
            exitconverter = True

              
    
          
            
