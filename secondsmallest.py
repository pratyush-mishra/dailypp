import math

def secondsmallest(array):
    minimum = math.inf
    second_min = math.inf
    for i in range(0,len(array)):
        if array[i] < minimum:
            second_min = minimum
            minimum = array[i]
        
        elif array[i] < second_min and array[i] != minimum:
            second_min = array[i]
    return second_min


numbers = [1, 3, 5, 7, 9]
print(secondsmallest(numbers))