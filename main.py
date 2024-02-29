base = int(input("Enter the base (from 2 to 9): "))
if base < 2 or base > 9:
    print("Invalid base")

number = input("Enter the number: ")
for digit in number:
    if int(digit) >= base:
        print("Invalid number")
        

decimal_number = int(number, base)
print("decimal system: ", decimal_number)
