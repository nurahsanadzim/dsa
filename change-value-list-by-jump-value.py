# given array of range number, and its type is string
# change the current value of array to "*" for first next value
# and next current value except "*", also change first and second next value
# and do it alternately
#
# example
# input: ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
# output: ['10', '*', '12', '*', '*', '15', '*', '17', '*', '*', '20']
#
# input: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# output: ['1', '*', '3', '*', '*', '6', '*', '8', '*', '*']

arr = list(map(str, range(1, 11)))
jump = 1
length = len(arr)

for i in range(length):
    if i == length - 1:
        break
    if arr[i] != "*":
        if jump == 1:
            jump += 1
            arr[i + 1] = "*"
        else:
            jump -= 1
            arr[i + 1] = "*"
            # as long as it hasn't reached the last assignment index
            if i + 2 != length:
                arr[i + 2] = "*"