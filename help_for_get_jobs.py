def input_keywords():
    n = 5
    i = 0
    keywords = []
    while i < n:
        a = input()
        if len(a) == 0:
            break
        else:
            keywords.append(a)
            i += 1
    return keywords