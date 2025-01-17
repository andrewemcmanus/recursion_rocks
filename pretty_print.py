# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a function that accepts a complex dictionary and prints out all of its keys and all of its values.
# The dictionary can have dictionaries nested inside of it
# 'dictionary' is the dictionary that's currently being iterated over.
# 'indent' is a string representing the current level of indentation
# ...
# pretty_print(inner_dictionary, indent + '..');
# ...

def pretty_print(dictionary):
    # Write code here
    for keys in dictionary:
        instance = dictionary[keys]
        if isinstance(instance, dict):
            output = pretty_print(instance)
            print(output)
        else:
            print('false')

    return output
    # return newdict
            # return dictionary[keys]
    # return newdict


    # string = str(dictionary)
    # brackets = string.split(',')
    # for i in range(len(splitstring)):
    #     print(splitstring[i])


o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero"}, "d": 4}
o3 = {"a": 1, "b": 2, "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {"spiderman": {"name": "Peter Parker"}, "superman": {"name": "Clark Kent"}}}, "d": 4}

pretty_print(o2)
# print(pretty_print(o1, "-"))
# print(pretty_print(o2, " "))
# print(pretty_print(o3, ".."))
# ..a: 1
# ..b: 2
# ..c:
# ....name: Bruce Wayne
# ....occupation: Hero
# ....friends:
# ......spiderman:
# ........name: Peter Parker
# ......superman:
# ........name: Clark Kent
# ..d: 4
