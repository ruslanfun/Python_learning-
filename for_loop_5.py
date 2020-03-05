
number = int(input('enter number between 1 and 12:'))
number1 = int()


for array1 in range(12):
    number1 = number1 + 1
    if number <= 12:
        result = (number1 * number)
        print(str(number1) + '*' + str(number) + '=' + str(result))
    else:
        print('Read the task again!')
        quit()



