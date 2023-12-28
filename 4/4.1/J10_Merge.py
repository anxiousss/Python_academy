def merge(tuple1, tuple2):
    result = []
    i = 0
    j = 0
    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] < tuple2[j]:
            result.append(tuple1[i])
            i += 1
        else:
            result.append(tuple2[j])
            j += 1
    result.extend(tuple1[i:])
    result.extend(tuple2[j:])
    return tuple(result)