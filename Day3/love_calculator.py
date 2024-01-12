print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + name2
new_name = name.upper()

T = new_name.count("T")
R = new_name.count("R")
U = new_name.count("U")
E = new_name.count("E")

total1 = str(T + R + U + E)

L = new_name.count("L")
O = new_name.count("O")
V = new_name.count("V")
E = new_name.count("E")

total2 = str(L + O + V + E)

x = int(total1 + total2)

if x < 10 or x > 90:
  print(f"Your score is {x}, you go together like coke and mentos.")

elif x >= 40 and x <=50:
  print(f"Your score is {x}, you are alright together.")

else:
  print(f"Your score is {x}.")

