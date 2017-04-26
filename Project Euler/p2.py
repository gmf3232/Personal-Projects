
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
