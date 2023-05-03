def col(n):
    sp = [n]
    if n < 1:
        return []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sp.append(n)
    for i in sp:
        print(i, end=' ')



col(int(input()))