def isBalanced(s):
    if(len(s) % 2 != 0):
        return 'NO'
    
    stack = []
    for char in s:
        if char in ['{', '(', '[']:
            stack.append(char)
        else:
            if not stack:
                return 'NO'
            
            top_value = stack.pop()
            if (char == '}' and top_value!= '{'):
                return 'NO'
            elif (char == ')' and top_value!= '('):
                return 'NO'
            elif (char == ']' and top_value!= '['):
                return 'NO'
    
    if not stack:
        return 'YES'
    else:
        return 'NO'



print(isBalanced('{{}}'))
print(isBalanced(']{[]'))
print(isBalanced('[()]'))
print(isBalanced('['))