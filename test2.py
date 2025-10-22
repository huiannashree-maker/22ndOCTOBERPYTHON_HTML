# SIMPLE CALCULATOR USING SWITCH-CASE STATEMENT IN PYTHON
# ( + - * / // % **)

# PYTHON DONT'T ALLOW SWITCH CASE TILL 3.9 VERSION
# FROM 3.10 VERSION PYTHON HAS STARTED SWITCH CASE BUT THE OPERATOR IS MATCH-CASE

# step 1

print('==========SIMPLE CALCULATOR============')

num1=float(input('enter 1st num'))
num2=float(input('enter 2nd num'))

print("Select Operation: + - * / // % **")
op = input('enter selection...')

#step 2

match op:
    case'+':
        result = num1+num2
        print(f"Result is :{num1}+{num2}={result}")
    case'-':
        result = num1 - num2
        print(f"Result is  : {num1} -{num2}={result}")
    case'*':
        result = num1 * num2
        print(f"Result is : {num1} *{num2}={result}")
    case'/':
        if num2!=0:
            result = num1/num2
            print(f"Result is :{num1}+{num2}={result}")
        else:
            print("Error You cannot divide by 0")
    case'%':
        if num2!=0:
            result = num1//num2
            print(f"Result is :{num1}%{num2}={result}")
        else:
            print("Error You cannot divide by 0")
    case'**':
        result = num1 ** num2
        print(f"Result is :{num1}**{num2}={result}")
    case _:
        print("Invalid Operator Selected + - * / // % **")
print("===CALCULATOR ENDS HERE===")



    

                
    


    




        

      

