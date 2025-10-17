try:
  a  = float(input("enter frist number :"))
  b  = float(input("enter second number :"))

  print(f"addition:{a + b}")
  print(f"subtraction:{a - b}")
except valueError:
  print("please enter valid number.")
