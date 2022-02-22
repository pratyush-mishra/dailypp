
def isAnagram(words):

    result = {}

    for word in words:
        count = [0] * 26
        for s in word:
            count[ord(s) - ord("a")]+=1
        if tuple(count) in result:
            result[tuple(count)].append(word)
        else:
            result[tuple(count)] = [word]

    return result.values()

print(isAnagram(["one", "two", "owt"]))