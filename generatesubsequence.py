def gensubsequence(string, length):
    result = []
    for i in range(0,len(string)-length+1):
        sequence = string[i:i+length]
        result.append(sequence)
    return result
print(gensubsequence("abcdef", 2))

