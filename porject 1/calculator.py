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
        number1=float(input("Enter the number on the left side of the operation "))
        Operation=input("enter your a opration: ")
        number2=float(input("Enter the number on the left side of the operation "))
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
     if basic_or_advanced==2:
            print("please select :"'\n''_____________''\n''1)abs''\n''2)Trighanbes''\n''3)sqrt''\n''4)even or odd''\n''5)log''\n')
            select=int(float(input("select: ")))
            if select==1:
                number=int(float(input("enter your number: ")))
                answer=abs(number)
                print(answer)
            elif select==2:
                print('________________'"please select: "'\n''1)sin''\n''2)cos''\n''3)tan''\n''4)cot')
                select2=int(float(input("select= ")))
                number2=int(float(input("enter your number: ")))
                if select2==1:
                    answer=math.sin(number2)
                    print(answer)
                elif select2==2:
                    answer=math.cos(number2)
                    print(answer)
                elif select2==3:
                    answer=math.tan(number2)
                    print(answer)
                elif select==4:
                    answer=math.cot(number2)
                    print(answer)
            elif select==3:
                number3=int(float(input("enter your number: ")))
                answer=math.sqrt(number2)
                print(answer)
            elif select==4:
                number4=int(float(input("enter number")))
                if(number4%2==0):
                    print("your number is even")
                else:
                    print("your number is odd")
            elif select==5:
                number5=int(float(input("enter number")))
                answer=math.log(number5)
                print(answer)
     else:
        print ("wrong we dont have this number")
        break








            





    
  




        

