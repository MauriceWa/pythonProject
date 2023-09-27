# with open("Numbers.txt", "w") as file:
#      file.write('\n' + input("Input a number between 0 and 10:"))
#      file.close()

# file = open("Numbers.txt").read().splitlines()
# print(int(file[-1]) + 3)
# file = open("Numbers.txt").read().splitlines()
# for line in file:
#     print(line + '\n')

file = open("Numbers.txt",)
lines_list = file.read().splitlines()
file.close()
file = open("Numbers.txt", "w")
for count, line in enumerate(lines_list):
    file.write(line +" "+ str(count) + "\n")

# read add numbers, write into file
#