# Print all divisors of a number

# Taking input from user
num = int(input("Enter a number: "))

print("Divisors of", num, "are:")

# Loop to find divisors
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
