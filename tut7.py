def calculator():
 print("Enter first number")
 a = input()
 print("First number=", a)
 print("Enter second number")
 b = input()
 print("Second number=", b)
 c = input("Enter the operation.Use:\n'+' for addition,\n'-' for subtraction,\n'*'for multiplication,\n'/' for division"
           ",\n'//' for quotient,\n'%' for remainder,\n'**' for exponent\n")
 d1 = {"+": int(a) + int(b), "-": int(a) - int(b), "*": int(a)* int(b), "/": int(a)/int(b),"**":int(a)**int(b),
       "%":int(a) % int(b),"//":int(a) // int(b)}
 if c in d1:
  print("Solution=", d1[c])
  return d1[c]
 else:
  print("Invalid operation entered.")
calculator()
def again():
 print("Do you want to use the Calculator again?\nYes/No")
 i = input().capitalize()
 if i == "Yes":
  calculator()
  again()
 else:
  print("Thank You for using the Calculator.\nSee you next time.")
again()
