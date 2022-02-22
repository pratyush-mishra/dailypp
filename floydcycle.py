def lengthofcycle(arr, start):

    n = len(arr)

    slow = arr[start]
    fast = arr[start]
    if n == 0 or start > n:
        return -1
    
    count = 0

    while slow < n and fast < n and arr[fast] < n:
        slow = arr[slow]
        fast = arr[fast]
        fast = arr[fast]
        count+=1
        
        if slow == fast:
            break
        
    if slow != fast:
        return -1
    
    else:
        return count
    

#    while True:
#        slow = arr[slow]
#        fast = arr[fast]
#        fast = arr[fast]
#        count+=1
#        if slow == fast:
#            break
    
#    return count


print(lengthofcycle([1,0], 0))
print(lengthofcycle([1, 2, 3, 1], 0))