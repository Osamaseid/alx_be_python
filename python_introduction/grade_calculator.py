score = str(input("Enter the mark:"))

if score >= 90 and score <= 100:
 grade = "A+"
elif score >= 85 and score <= 89:
 grade = "A"
elif score >= 80 and score <= 84:
  grade = "A-"
elif score >= 75 and score <= 79:
  grade = "B+"
elif score >= 70 and score <= 74:
  grade = "B"
elif score >= 65 and score <= 69:
  grade = "C+"
elif score >= 60 and score <= 64:
  grade = "C"
elif score >= 50 and score <= 59:
  grade = "c-"
else:
  print("No Grade!")
print(f"YOUR GARDE IS :{grade}")
