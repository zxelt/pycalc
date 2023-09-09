First = int(input("First Number: "))
Two = int(input("Secound Number: "))
Signe = input("Opperator (* - + /) : ")
if Signe == "+":
    Result = First + Two
elif Signe == "-":
    Result = First - Two
elif Signe == "*" or Signe == "x":
    Result = First * Two
elif Signe == "/" or Signe == ":":
    Result = First / Two
else:
    print("Invalid Operator")
    Result = "Invalid OPERATOR Error"
input(f"Result: {Result}")