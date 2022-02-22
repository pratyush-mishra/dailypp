
def findaverage(students):
    result = {}
    maxavg = 0
    for i in range(0, len(students)):
        if students[i][0] in result.keys():
            result[students[i][0]].append(int(students[i][1]))
        else:
            result[students[i][0]] = [int(students[i][1])]
    
    for student in result.keys():
        result[student] = int((sum(result[student]) / len(result[student])))
        if result[student] > maxavg:
            maxavg = result[student]
    
    
    return maxavg


array = [["Bob", "87"]]
print(findaverage(array))
