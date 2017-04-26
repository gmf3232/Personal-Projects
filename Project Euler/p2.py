# Problem 2: Find the sum of even-valued fibonacci numbers that do not exceed
# 4,000,000
# Answer: 4613732

total = 0


front = 2
mid = 3
second = 5

while front < 4000000:
    if front % 2 == 0:
        total += front
    front = mid
    temp = mid
    mid = second
    second = temp + second

print(total)
