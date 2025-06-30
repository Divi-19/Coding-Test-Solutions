a = int(input("Enter a number (a): "))

if a % 2 == 0:
    a -= 1

odd_numbers = [i for i in range(1, a + 1, 2)]

print(", ".join(map(str, odd_numbers)))
