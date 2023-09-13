numbers = {
  "1": "one",
  "2": "two",
  "3": "three"
}

userTXT = input("Enter number: ")
output = " "
for ch in userTXT:
  output += numbers.get(ch, "!")
print(output)