# file = open("File1.txt").read().splitlines()
# line_number = 0
# for line in file:
#     print(str(line_number) + ": " + line)
#     line_number += 1


file = open("File1.txt").read().splitlines()
for count, line in enumerate(file):
    print(str(count) + ": " + line)

