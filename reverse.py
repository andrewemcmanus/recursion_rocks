# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse` that accepts a ss and returns a reversed ss.

def reverse(ss):
    # Write code here
    length = len(ss)
    if length == 0:
        return ""
    if length == 1:
        return ss
    else:
        string = ss[length - 1] + reverse(ss[:-1])
        return string
        # print(ss[:-2])
newstring = input('Enter a string: ')
print(reverse(newstring))

# print(reverse(""))
# => ""
# print(reverse("a"))
# => "a"
# print(reverse("ab"))
# => "ba"
# print(reverse("computer"))
# => "retupmoc"
# print(reverse(reverse("computer")))
# => "computer"
