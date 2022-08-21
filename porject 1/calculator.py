import math
space="              "
space2="       "
space3="    "
rank=int(float(input("How many times do you want to use calculator?")))
for i in range(rank):
     print("would you like use to basic part or advanced? ")
     print(" ________________""\n""|""1)basic",space2,"|\n""|",space,"|\n""|",space,"|\n""|",space,"|\n""|""2)advanced",space3,"|\n""|""________________""|")
     basic_or_advanced=int(input("answer: "))
     if basic_or_advanced==1:
        print('='*10,'selection','='*10,'\n'"1)basic"'\n'"2)basic sequence")
        select_basic=int(input("select:"))
        if select_basic==1:
            print("you are select basic you can use opration"'\n''(+ or sum)''\n''(- or subtraction)''\n''(* or zarb)''\n''(** or power)''\n''(/ or split)''\n''(// or split int)''\n''(%  mod)') 
            number1=float(input("Enter the number on the left side of the operation "))
            Operation=input("enter your a opration: ")
            number2=float(input("Enter the number on the right side of the operation "))
            if Operation=="+" or Operation=="sum":
                answer=(number1+number2)
                print(answer)
            elif Operation=="-"or Operation=="subtraction":
                answer=(number1-number2)
                print(answer)
            elif Operation=="*" or Operation== "zarb":
                answer=number1*number2
                print(answer)
            elif Operation=="/" or Operation== "split":
                if number2==0:
                    print("wrong")
                else:
                    answer=number1/number2
                    print(answer)
            elif Operation=="//" or Operation== "split int":
                if number2==0:
                    print("wrong")
                else :
                    answer=number1//number2
                    print(answer)
            elif Operation=="**" or Operation==  " power":
                answer=number1**number2
                print(answer)
            elif Operation=="%" or Operation== "mod":
                answer=number1%number2
                print(answer)
        elif select_basic==2:
            while True:
                number = float(input("Enter a number: "))
                break
            while True:
                action = input("Enter the action (Enter 'DONE' to finish): ")
                if action.upper() == "DONE":
                    print("Resault: {}".format(number) , end="\n\n")
                    break
                elif action == "-":
                    pass
                elif action == "*":
                    pass
                elif action == "/":
                    pass
                elif action == "+":
                    pass
                else:
                    print("** Your action isn't avalable **")
                    continue
                number2 = float(input("Enter a number: "))
                if action == "+":
                    number += number2
                elif action == "-":
                    number -= number2
                elif action == "*":
                    number *= number2
                elif action == "/":
                    if number % number2 != 0:
                        q = input("Do you like to round it? [yes/no] ")
                    if q.lower() == "yes":
                        number /= number2
                        number = float(round(number))   
                    else:
                        number /= number2
                    
                    continue
            
     elif basic_or_advanced==2:
            print('='*10,'selection','='*10,'\n''1)abs''\n''2)Trighanbes''\n''3)sqrt''\n''4)even or odd''\n''5)log10''\n''6)kmm''\n''7)bmm''\n''8)factorial''\n''9)Convert radians to degrees''\n''10)convert degrees to radians''\n''11)ceil''\n''12)floor''\n''13)exp''\n''14)log(x,b)''\n''15)int(x)''\n''16)hypot(x,y)''\n''17)power(x,y)''\n''18)convert number')
            select=int(float(input("select: ")))
            if select==1:
                number=float(input("enter your number: "))
                answer=abs(number)
                print(answer)
            elif select==2:
                print('='*10,'selection','='*10,'\n'"please select: "'\n''1)sin''\n''2)cos''\n''3)tan''\n''4)arsin''\n''5)arcos''\n''6)artan''\n''7)arsinh''\n''8)arcosh')
                select2=int(float(input("select= ")))
                number2=float(input("enter your number: "))
                if select2==1:
                    answer=math.sin(number2)
                    print(answer)
                elif select2==2:
                    answer=math.cos(number2)
                    print(answer)
                elif select2==3:
                    answer=math.tan(number2)
                    print(answer)
                elif select2==4:
                    answer=math.asin(number2)
                    print(answer)
                elif select2==5:
                    answer=math.acos(number2)
                    print(answer)
                elif select2==6:
                    answer=math.atan(number2)
                    print(answer)
                elif select2==7:
                    answer=math.asinh(number2)
                    print(answer)
                elif select2==8:
                    answer=math.acosh(number2)
                    print(answer)
                
            elif select==3:
                number3=float(input("enter your number: "))
                answer=math.sqrt(number3)
                print(answer)
            elif select==4:
                number4=float(input("enter number"))
                if(number4%2==0):
                    print("your number is even")
                else:
                    print("your number is odd")
            elif select==5:
                number5=float(input("enter number"))
                answer=math.log10(number5)
                print(answer)
            elif select==6:
                number6=int(float(input('enter number: ')))
                number7=int(float(input('enter number: ')))
                answer= math.lcm(number6, number7)
                print(answer)
            elif select==7:
                number8=int(float(input('enter number: ')))
                number9=int(float(input('enter number: ')))
                print("bmm: " , math.gcd(number8, number9))
            elif select==8:
                number10 = float(input("please Enter  number: "))
                if number10 < 0:
                    print("Sorry, factorial does not exist for negative numbers")
                else:
                    result = math.factorial(number10)
                    print("The factorial of {} is: {}".format(number10, result))
            elif select==9:
                 number11 = float(input("please Enter  number: "))
                 answer=math.degrees(number11)
                 print(answer)
            elif select==10:
                 number12 = float(input("please Enter  number: "))
                 answer=math.radians(number12)
                 print(answer)
            elif select==11:
                 number13 = float(input("please Enter  number: "))
                 answer=math.ceil(number13)
                 print(answer)
            elif select==12:
                 number14 = float(input("please Enter  number: "))
                 answer=math.floor(number14)
                 print(answer)
            elif select==13:
                 number15=float(input("please Enter  number: "))
                 answer=math.exp(number15)
                 print(answer)
            elif select==14:
                 x=float(input("please Enter  x: "))
                 b=float(input("please Enter  b: "))
                 answer=math.log(x,b)
                 print(answer)
            elif select==15:
                 number17=float(input("please Enter  your numbers: "))
                 answer=math.trunc(number17)
                 print(answer)
            elif select==16:
                 number18=float(input("please Enter  number: "))
                 number19=float(input("please Enter  number: "))
                 answer=math.hypot(number18,number19)
                 print(answer)
            elif select==17:
                 x=float(input("please Enter  x: "))
                 y=float(input("please Enter  y : "))
                 answer=math.pow(x,y)
                 print(answer)
            elif select==18:
                print('='*10,'convert','='*10,'\n''selec: ''\n''1)bin--->dec''\n''2)bin--->oct''\n''3)bin--->hex''\n''4)oct--->dec''\n''5)oct--->bin''\n''6)oct--->hex''\n''7)hex--->dec''\n''8)hex--->bin''\n''9)hex--->oct''\n''10)dec--->bin''\n''11)dec--->oct''\n''12)dec--->hex')
                select=int(input('select:'))
                if select==1:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print('dec',(sums))
                        
                elif select==2:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print(oct(sums))
                elif select==3:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print(hex(sums))
                elif select==4:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(sums)
                elif select==5:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(bin(sums))
                elif select==6:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(hex(sums))
                elif select==7:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(sums)
                elif select==8:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(bin(sums))
                elif select==9:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(oct(sums))
                elif select==10:
                    number = int(input("Enter number: "))
                    print(bin(number))
                elif select==11:
                    number = int(input("Enter number: "))
                    print(oct(number))
                elif select==12:
                    number = int(input("Enter number: "))
                    print(hex(number))
            else:
                    print('we dont have your select ')
                    break
     else:
        print ("wrong we dont have this number")
        break
