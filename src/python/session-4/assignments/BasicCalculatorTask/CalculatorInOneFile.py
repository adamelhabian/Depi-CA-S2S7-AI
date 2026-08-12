

print("Welocme to the Simple Calculator!")
print("Select an Operation:")
print("1. Addition (+)\n" \
"2. Subtraction (-)\n" \
"3. Multiplication (*)\n" \
"4. Division (/)")

while(True):

    
    user_input=input("Enter your Choice (1/2/3/4) or 'exit' to quit: ")
    if(user_input.lower()=='exit'):
        print("Existing the calculator. GoodBye")
        break
    elif (user_input not in ['1','2','3','4']):
         print("Invalid Choice")
         continue
    else:
        while(True):
            try:
                num1=float(input("Enter first number :"))
                num2=float(input("Enter second number :"))
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")
            

        if(user_input == '1'):
            print(f"{num1} + {num2} = {num1+num2}")
        elif(user_input == '2'):
                    print(f"{num1} - {num2} = {num1-num2}")
        elif(user_input == '3'):
                    print(f"{num1} * {num2} = {num1*num2}")
        elif(user_input == '4'  ):
            if(num2 != 0):        
                print(f"{num1} / {num2} = {num1/num2}") 
            else:
                print("Can't Divide by Zero")    
            








