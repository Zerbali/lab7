# "Create a file based on a numeric array. Read the file, double each element, write the results to a new file, and additionally calculate their sum."


original_array = [1, 4, 7, 10, 5]

with open("original.txt", "w") as file:
    for num in original_array:
        file.write(str(num) + "\n")

doubled_array = []
total_sum = 0

with open("original.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        doubled = num * 2
        doubled_array.append(doubled)
        total_sum += doubled

with open("doubled.txt", "w") as file:
    for num in doubled_array:
        file.write(str(num) + "\n")

print("Sum of doubled numbers:", total_sum)
