# Change program 3 to also ask for a number.
# Display their name (one letter at a time on each line)
# and repeat this for the number of times they entered.

name = input('what\'s your name?:')
#name = 4132321
number = int(input('how many times?:'))
try:
    object_1 = iter(name)
except TypeError as te:
    print(name, 'is not iterable')
for char2 in range(number):
    for char in name:
        print(char)



