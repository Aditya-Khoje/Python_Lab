# Assignment - 1

print("Enter your basic pay : ")
base_salary = int(input())
payable_salary = base_salary + (0.1 * base_salary)+(0.05 * base_salary)
net_salary = payable_salary-(0.02 * payable_salary)
print("Net payable salary is : ", net_salary)
