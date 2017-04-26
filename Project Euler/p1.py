# Problem 1: Find the sum of all multiples of 3 and 5 less than 1000
# Answer: 233168

i = 1
total = 0
while i < 1000:
    if i%15 == 0:
        total += i
    elif i%5 == 0:
        total += i
    elif i%3 == 0:
        total += i
    i += 1

print(total)
