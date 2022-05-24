number = int(input("Enter number : "))

if number >= 0:
    print("Square root of number : ", (number)**0.5)
else:
    print("Square root of number can not be calculated")

print("Square of number : ", (number)**2)
print("Cube of number : ", (number)**3)

if number == 1 or number == 0:
    print(number, "is neither a prime number nor a composite number.")
elif number > 1:
    for i in range(2, int((number/2)+1)):
        if (number % i) == 0:
            print(number, "is not a prime number.")
            break
else:
    print(number, "is a prime number.")
