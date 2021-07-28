import sys
input_ = sys.stdin.readline

num = int(input_())

array = []
for i in range(num):
    grade = input().split()
    array.append([grade[0], int(grade[1]), int(grade[2]), int(grade[3])])

array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in array:
    print(i[0])