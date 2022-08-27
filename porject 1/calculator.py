import math
from tabulate import tabulate


table_p=['welcome']
print(tabulate(table_p,tablefmt='fancy_grid'))
name =input(" hello my dear please enter your name: ")
print('\n''hey',name)

rank=int(float(input("How many times do you want to use calculator?")))
i=0
for i in range(rank):
     i+=1
    
     print('\n','='*40,'\n'"would you like use to basic part or advanced? ")

     table_a=[["1)basic"],
             ['2)advanced']]
     print(tabulate(table_a,headers='firstrow',tablefmt='fancy_grid'))

     basic_or_advanced=int(input("answer: "))
     
     if basic_or_advanced==1:
        table_b=[["1)basic"],
                 ["2)basic sequence(No priority)"]]
        print(tabulate(table_b,headers='firstrow',tablefmt='fancy_grid'))
        select_basic=int(input("select:"))
        if select_basic==1:
            table_c=[["you are select basic you can use opration"],
            ['(+ or sum)'],
            ['(- or subtraction)'],
            ['(* or zarb)'],
            ['(** or power)'],
            ['(/ or split)'],
            ['(// or split int)'],
            ['(%  mod)']]
            print(tabulate(table_c,headers='firstrow',tablefmt='fancy_grid'))
            number1=float(input("Enter the number on the left side of the operation "))
            Operation=input("enter your a opration: ")
            number2=float(input("Enter the number on the right side of the operation "))
            if Operation=="+" or Operation=="sum":
                answer=(number1+number2)
                print('\n''\n',number1,'+',number2,'=',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="-"or Operation=="subtraction":
                answer=(number1-number2)
                print('\n''\n',number1,'-',number2,'=',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="*" or Operation== "zarb":
                answer=number1*number2
                print('\n','\n',number1,'*',number2,'=',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="/" or Operation== "split":
                if number2==0:
                    print("wrong")
                    print('\n',name,"you are use calculater",i,'order. ')
                else:
                    answer=number1/number2
                    print('\n''\n',number1,'/',number2,'=',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="//" or Operation== "split int":
                if number2==0:
                    print("wrong")
                    print('\n',name,"you are use calculater",i,'order. ')
                else :
                    answer=number1//number2
                    print('\n''\n',number1,'//',number2,'=',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="**" or Operation==  " power":
                answer=number1**number2
                print('\n''\n',number1,'**',number2,'=',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif Operation=="%" or Operation== "mod":
                answer=number1%number2
                print('\n''\n',number1,'%',number2,'=',answer)
                print('\n',name,"you are use calculater",i,'order. ')
        elif select_basic==2:
            while True:
                number = float(input("Enter a number: "))
                break
            while True:
                action = input("Enter the action (Enter 'DONE' to finish): ")
                if action.upper() == "DONE":
                    print("Resault: {}".format(number) , end="\n\n")
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
        else:
            print('wrong')    
            print('\n',name,"you are use calculater",i,'order. ')
            continue
            
     elif basic_or_advanced==2:
            table_d=[['selection'],
            ['1)abs'],
            ['2)Trighanbes'],
            ['3)sqrt'],
            ['4)even or odd'],
            ['5)log10'],
            ['6)kmm'],
            ['7)bmm'],
            ['8)factorial'],
            ['9)Convert radians to degrees'],
            ['10)convert degrees to radians'],
            ['11)ceil'],
            ['12)floor'],
            ['13)exp'],
            ['14)log(x,b)'],
            ['15)int(x)'],
            ['16)hypot(x,y)'],
            ['17)power(x,y)'],
            ['18)convert number'],
            ['19)convert temprature'],
            ['20)BMI'],
            ['21)area'],
            ['22)prime']]

            print(tabulate(table_d,headers='firstrow',tablefmt='fancy_grid'))

            select=int(input("select : "))
            
            if select==1:
                number=float(input("enter your number: "))
                answer=abs(number)
                print('\n',name,'your anwer is: ',answer)
                print('\n',name,"you are use calculater",i,'order. ')
                
            elif select==2:
                table_e=[['selection'],
                ['1)sin'],
                ['2)cos'],
                ['3)tan'],
                ['4)arsin'],
                ['5)arcos'],
                ['6)artan'],
                ['7)arsinh'],
                ['8)arcosh)']
                ['9)COT']]
                print(tabulate(table_e,headers='firstrow',tablefmt='fancy_grid'))
                
                select2=int(float(input("select= ")))
                number2=float(input("enter your number: "))
                if select2==1:
                    answer=math.sin(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==2:
                    answer=math.cos(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==3:
                    answer=math.tan(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==4:
                    answer=math.asin(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==5:
                    answer=math.acos(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==6:
                    answer=math.atan(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==7:
                    answer=math.asinh(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==8:
                    answer=math.acosh(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select2==9:
                    answer=math.cos(number2)/math.sin(number2)
                    print('\n',name,'your anwer is: ',answer)
                    print('\n',name,"you are use calculater",i,'order. ')
                else:
                    print(name,',','\n','wrong')
                    break

                
            elif select==3:
                number3=float(input("enter your number: "))
                answer=math.sqrt(number3)
                print('\n',name,'your anwer is: ',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif select==4:
                number4=float(input("enter number"))
                if(number4%2==0):
                    print("your number is even")
                    print('\n',name,"you are use calculater",i,'order. ')
                else:
                    print("your number is odd")
                    print('\n',name,"you are use calculater",i,'order. ')
            elif select==5:
                number5=float(input("enter number"))
                answer=math.log10(number5)
                print('\n',name,'your anwer is: ',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif select==6:
                number6=int(float(input('enter number: ')))
                number7=int(float(input('enter number: ')))
                answer= math.lcm(number6, number7)
                print('\n',name,'your anwer is: ',answer)
                print('\n',name,"you are use calculater",i,'order. ')
            elif select==7:
                number8=int(float(input('enter number: ')))
                number9=int(float(input('enter number: ')))
                print("bmm: " , math.gcd(number8, number9))
                print('\n',name,"you are use calculater",i,'order. ')
            elif select==8:
                number10 = float(input("please Enter  number: "))
                if number10 < 0:
                    print("Sorry, factorial does not exist for negative numbers")
                    print('\n',name,"you are use calculater",i,'order. ')
                else:
                    result = math.factorial(number10)
                    print("The factorial of {} is: {}".format(number10, result))
                    print('\n',name,"you are use calculater",i,'order. ')
            elif select==9:
                 number11 = float(input("please Enter  number: "))
                 answer=math.degrees(number11)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==10:
                 number12 = float(input("please Enter  number: "))
                 answer=math.radians(number12)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==11:
                 number13 = float(input("please Enter  number: "))
                 answer=math.ceil(number13)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==12:
                 number14 = float(input("please Enter  number: "))
                 answer=math.floor(number14)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==13:
                 number15=float(input("please Enter  number: "))
                 answer=math.exp(number15)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==14:
                 x=float(input("please Enter  x: "))
                 b=float(input("please Enter  b: "))
                 answer=math.log(x,b)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==15:
                 number17=float(input("please Enter  your numbers: "))
                 answer=math.trunc(number17)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==16:
                 number18=float(input("please Enter  number: "))
                 number19=float(input("please Enter  number: "))
                 answer=math.hypot(number18,number19)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==17:
                 x=float(input("please Enter  x: "))
                 y=float(input("please Enter  y : "))
                 answer=math.pow(x,y)
                 print('\n',name,'your anwer is: ',answer)
                 print('\n',name,"you are use calculater",i,'order. ')
            elif select==18:
                table_h=[['convert'],
                ['1)bin--->dec'],
                ['2)bin--->oct'],
                ['3)bin--->hex'],
                ['4)oct--->dec'],
                ['5)oct--->bin'],
                ['6)oct--->hex'],
                ['7)hex--->dec'],
                ['8)hex--->bin'],
                ['9)hex--->oct'],
                ['10)dec--->bin'],
                ['11)dec--->oct'],
                ['12)dec--->hex']]
                print(tabulate(table_h,headers='firstrow',tablefmt='fancy_grid'))
                
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
                    print('\n',name,"you are use calculater",i,'order. ')
                        
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
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
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select==10:
                    number = int(input("Enter number: "))
                    print(bin(number))
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select==11:
                    number = int(input("Enter number: "))
                    print(oct(number))
                    print('\n',name,"you are use calculater",i,'order. ')
                elif select==12:
                    number = int(input("Enter number: "))
                    print(hex(number))
                    print('\n',name,"you are use calculater",i,'order. ')
            elif select==19:
                    temperture=int(float(input("enter temprrture: ")))
                
                    table_j=[["Please select one of the conversions below for the entered temperature"],
                    ["1)c---->f"],
                    ["2)f---->c"],
                    ["3)k---->f"],
                    ["4)f---->k"],
                    ["5)c---->k"],
                    ["6)k---->c"]]
                    print(tabulate(table_j,headers='firstrow',tablefmt='fancy_grid'))
                
                    choose=int(float(input("Which one do you choose? ")))
                    if choose==1:
                        farenheit=temperture(9/5)+32
                        print("your tempercher with conversion is: ",farenheit,"farenheit")
                        print('\n',name,"you are use calculater",i,'order. ')
                    elif choose==2:
                        celsius=(temperture-32)*(5/9)
                        print("your tempercher with conversion is: ",celsius,"celsius")
                        print('\n',name,"you are use calculater",i,'order. ')
                    elif choose==3:
                        farenheit=(temperture-273.15)*(5/9)+32
                        print("your tempercher with conversion is: ",farenheit,"farenheit")
                        print('\n',name,"you are use calculater",i,'order. ')
                    elif choose==4:
                        kelvin=(temperture-32)*(5/9)+273.15
                        print("your tempercher with conversion is: ",kelvin,"kelvin")
                        print('\n',name,"you are use calculater",i,'order. ')
                    elif choose==5:
                        kelvin=(temperture+273.15)
                        print("your tempercher with conversion is: ",kelvin,"kelvin")
                        print('\n',name,"you are use calculater",i,'order. ')
                    elif choose==6:
                        celsius=(temperture-273.15)
                        print("your tempercher with conversion is: ",celsius,"celsius")
                        print('\n',name,"you are use calculater",i,'order. ')
                    else:
                        print('we dont have your select ')
                        print('\n',name,"you are use calculater",i,'order. ')
                        break
            elif select==20:    
                length=(float(input("enter your length with metr: ")))
                wieght=(float(input('enter your wieght with kg: ')))
                BMI=(wieght/(length**2))
                if BMI>=16 and BMI<18.5:
                    print(" your BMI is: ", BMI,'/n'"body wiegth deficit")
                    print('\n',name,"you are use calculater",i,'order. ')
                elif BMI>=18.5 and BMI<24:
                    print(" your BMI is: ", BMI,'/n'"normal")
                    print('\n',name,"you are use calculater",i,'order. ')
                elif BMI>=24 and BMI<30:
                    print(" your BMI is: ", BMI,'/n'"wieght over") 
                    print('\n',name,"you are use calculater",i,'order. ') 
                elif BMI>=30 and BMI<35:
                    print(" your BMI is: ", BMI,'/n'"obesity first degree")     
                    print('\n',name,"you are use calculater",i,'order. ')
                elif BMI>=35 and BMI<40:
                    print(" your BMI is: ", BMI,'/n'"obesity second degree")  
                    print('\n',name,"you are use calculater",i,'order. ')
                elif BMI>=40:
                    print(" your BMI is: ", BMI,'/n'"obesity third degree")
                    print('\n',name,"you are use calculater",i,'order. ')
                else:
                    print("This interval was unpredictable.")
                    print('\n',name,"you are use calculater",i,'order. ')
            elif select==21:
                table_l=[['area selection'],
                ['1)Triangle'],
                ['2)circle'],
                ['3)Square'],
                ['4)Rectangle'],
                ['5)Cylinder'],
                ['6)sphere']]
                print(tabulate(table_l,headers='firstrow',tablefmt='fancy_grid'))
            
                select=int(input('select: '))
                if select==1:
                    base=float(input("enter base: "))
                    hieght=float(input('enter hieght:'))
                    if base<0 or hieght<0:
                        print("wrong")
                        print('\n',name,"you are use calculater",i,'order. ') 
                        continue
                    else:
                        area=(base*hieght)/2
                        print('area ia = ',area)
                        print('\n',name,"you are use calculater",i,'order. ')
                elif select==2:
                    pi=3.14
                    round=float(input("enter round: "))
                    if round<0:
                        print("wrong")
                        print('\n',name,"you are use calculater",i,'order. ') 
                        continue
                    else:
                        area=pi*(round**2)
                        print('area ia = ',area)
                        print('\n',name,"you are use calculater",i,'order. ')
                elif select==3:
                     side=float(input('enter side; '))
                     if side<0:
                        print("wrong")
                        print('\n',name,"you are use calculater",i,'order. ') 
                        continue
                     else:
                        area=side**2
                        print('area ia = ',area)
                        print('\n',name,"you are use calculater",i,'order. ')
                elif select==4:
                    Lengt=float(input('enter length: '))
                    width= float(input('enter width: '))
                    if Lengt<0 or width<0:
                        print("wrong")
                        print('\n',name,"you are use calculater",i,'order. ') 
                        continue
                    else:
                        area=width*Lengt
                        print('area ia = ',area)
                        print('\n',name,"you are use calculater",i,'order. ')
                elif select==5:
                    table_o=[['1)side area'],
                    ['2)total area']]
                    print(tabulate(table_o,headers='firstrow',tablefmt='fancy_grid'))
                    selectc=int(input('select = '))
                    if selectc==1:
                        height=float(input("enter hieght: "))
                        Radius=float(input("enter radius: "))
                        if height<0 or Radius<0:
                            print("wrong")
                            print('\n',name,"you are use calculater",i,'order. ') 
                            continue
                        else:
                            pi=3.14
                            side_area=2*pi*Radius*height
                            print("side area is: ",side_area)
                            print('\n',name,"you are use calculater",i,'order. ')
                    elif selectc==2:
                        height=float(input("enter hieght: "))
                        Radius=float(input("enter radius: "))
                        
                        if height<0 or Radius<0:
                            print("wrong")
                            print('\n',name,"you are use calculater",i,'order. ') 
                            continue
                        else:
                            pi=3.14
                            total_area=(2*pi*Radius*height)+(2*pi*Radius*Radius)
                            print(" total area is : ",total_area)
                            print('\n',name,"you are use calculater",i,'order. ')
                elif select==6:
                    pi=3.14
                    Radius=float(input("enter radius: "))
                    if Radius<0:
                        if  Radius<0:
                            print("wrong")
                            print('\n',name,"you are use calculater",i,'order. ') 
                            continue
                    else:
                        area=4*pi*(Radius**2)
                        print("area: ",area)
                        print('\n',name,"you are use calculater",i,'order. ')
        
                else:
                    print('wrong!')
                    print('\n',name,"you are use calculater",i,'order. ')       
            elif select==22:
                
                num=(int(input("enter number : ")))
                for i in range(2,num):
                        if num>1:
                            if num%i==0:
                                print(num,"is not prime")
                                break
                            else:
                                print(num,"is prime")
                                break
                        else:
                            print(num,"is not prime")
                            break
                           
            else:
                print ("wrong we dont have this number")
                print('\n',name,"you are use calculater",i,'order. ')
                continue
     else:
        print ("wrong we dont have this number")
        print('\n',name,"you are use calculater",i,'order. ')
        continue
print('\n''dear',name,',i hope this calculator can help you..:D')



                
