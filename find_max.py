# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

list_input = input('Enter several numbers, separated by commas and spaces: ')
list_int = [int(s) for s in list_input.split(',')]
def find_max(list):
    # Write code here
    length = len(list)
    if length == 1:
        max = list[0]
        return max
    else:
        max = find_max(list[1:])
        if max > list[0]:
            return max
        else:
            return list[0]

maximum = find_max(list_int)
print(f"The maximum value is {maximum}")
# => 45
