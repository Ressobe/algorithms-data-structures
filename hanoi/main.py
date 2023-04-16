def hanoi(n, start, end):

    if n == 1:
        pm(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n - 1, start, other)
        pm(start, end)
        hanoi(n - 1, start, other)


def pm(start, end):
    print(f"{start} ---> {end}")
