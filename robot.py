def robotmovements(string):
    coordinate = [0,0]

    for s in string:
        if s == 'U':
            coordinate[1]+=1
        elif s == 'R':
            coordinate[0]+=1
        elif s == 'D':
            coordinate[1]-=1
        elif s == 'L':
            coordinate[0]-=1
    
    return coordinate

print(robotmovements("NONONO"))