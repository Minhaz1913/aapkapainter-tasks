def firstDuplicateSet(a):
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)

    return -1
print(firstDuplicateSet([1,2,3,2,1]))