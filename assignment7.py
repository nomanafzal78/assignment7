name = input("enter your name: ")
num1 = int(input("enter your 1st favoruite number: "))
num2 = int(input("enter your second favorite number: "))
num3 = int(input("enter your third favorite number: "))

print(f"Hello, {name}! Let's explore your favorite numbers:")

numbers = [num1, num2, num3]
even_odd_info = []

for num in numbers:
    if num%2 ==0:
        print(f"The number {num} is even.")
        even_odd_info.append((num, "even"))
    else:
        print(f"The number {num} is odd.")
        even_odd_info.append((num, "odd"))


for num in numbers:
    square = num ** 2
    print(f"The number {num} and its square: ({num}, {square})")



sum_numbers = sum(numbers)
print(f"The sum of your numbers is {sum_numbers}")


is_prime = True

if is_prime<1:
    is_prime== False

else:
    for i in range (2, sum_numbers):
       if sum_numbers %i ==0:
          is_prime =False
          break
       
if is_prime:
    print(f"Wow, {sum_numbers} is a prime number!")

else:
    print(f"{sum_numbers} is not a prime number.")
    



