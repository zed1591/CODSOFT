
def simple_calculator():
 

  try:
    numb1=input("Enter the first number:")
    numb2=input("Enter the second number:")
 
    num1=float(numb1)
    num2=float(numb2)
  except valueError:
    print("Error: please enter valid numeric value.")
    return

  print("choices")
  print("1 for addition")
  print("2 for subtraction")
  print("3 for multiplication")
  print("4 for division")
  print("5 for power")
  print("6 for modules")
  
  Option=int(input("Enter your choice want to calaculate(1-6):"))
  if Option ==1:
     result=num1+num2
     print(num1,'+', num2, "=", result)
  elif Option ==2:
     result=num1-num2
     print(num1, '-', num2, '=', result)
  elif Option ==3:
    result=num1*num2
    print(num1, '*', num2,'=', result)

  elif Option ==4:
    if num2 !=0:
      result=num1/num2
      print(num1, '/', num2, '=', result)
    else:
        result=("undifined/division by zero")
        print(result)

  elif Option ==5:
    result=num1**num2
    print(num1, '^', num2, '=', result)
  elif Option ==6:
    result=num1%num2
    print(num1,'%',num ,'=', result)
  
  else:
    print("invalid choice please enter 1-6")
    return

 
  
if __name__ == "__main__":

 simple_calculator()



