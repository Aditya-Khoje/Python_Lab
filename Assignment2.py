print("Enter the number of persons : ")
person = int(input())

if person == 2:
    cost = 2500
elif person == 3:
    cost = 3500
elif person == 4:
    cost = 4500
else:
    cost = 4500+500*(person-4)

print("Is there any additional person(Y/N) : ")
ap = input()

if ap == 'Y':
    print("Enter number of additional person : ")
    addp = int(input())

if ap == 'Y':
    cost = cost + (addp*1000)

print("Is you are on business trip(Y/N) : ")
bt = input()

print("Enter your age : ")
age = int(input())

if bt == 'Y':
    cost = cost - (cost*(20/100))
elif age > 60:
    cost = cost - (cost*(15/100))

print("Cost of the room :", cost, " rs")
