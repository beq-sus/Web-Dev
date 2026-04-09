# 1
n = int(input())

for i in range(n):
    for j in range(n):
        if j < n - 1 - i:
            print(0, end=" ")
        elif j == n - 1 - i:
            print(1, end=" ")
        else:
            print(2, end=" ")
    print()


# 2
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ok = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            ok = False

if ok:
    print("yes")
else:
    print("no")


# 3
n, m = map(int, input().split())

max_sum = -1
max_row = 0

for i in range(n):
    row = list(map(int, input().split()))
    s = sum(row)
    if s > max_sum:
        max_sum = s
        max_row = i

print(max_sum)
print(max_row)


# 4
n, m = map(int, input().split())

max_value = -1
max_i = 0
max_j = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] > max_value:
            max_value = row[j]
            max_i = i
            max_j = j

print(max_value)
print(max_i, max_j)


# 5
n, m = map(int, input().split())

winner = 0
best_throw = -1
best_sum = -1

for i in range(n):
    row = list(map(int, input().split()))
    row_max = max(row)
    row_sum = sum(row)

    if row_max > best_throw:
        best_throw = row_max
        best_sum = row_sum
        winner = i
    elif row_max == best_throw:
        if row_sum > best_sum:
            best_sum = row_sum
            winner = i

print(winner)


# 6
n, m = map(int, input().split())

global_max = -1
count = 0

for i in range(n):
    row = list(map(int, input().split()))
    row_max = max(row)

    if row_max > global_max:
        global_max = row_max
        count = 1
    elif row_max == global_max:
        count += 1

print(count)


# 7
n, m = map(int, input().split())

global_max = -1
winners = []

for i in range(n):
    row = list(map(int, input().split()))
    row_max = max(row)

    if row_max > global_max:
        global_max = row_max
        winners = [i]
    elif row_max == global_max:
        winners.append(i)

print(len(winners))
for x in winners:
    print(x, end=" ")