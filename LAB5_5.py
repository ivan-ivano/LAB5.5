def f(n):
    global depth
    global level

    if n == 1:
        k = 1
        level += 1
    elif n % 2 == 0:
        k = 2 * f(n / 2) - 1
        level += 1
    else:
        k = 2 * f(n - 1) + 1
        level += 1

    if depth < level:
        depth = level

    print("level = ", level)

    if k > n1:
        return n1
    else:
        return k


n = int(input('n = '))
n1 = n
depth = 0
level = 0

if __name__ == '__main__':
    print("№", f(n), "  ", "depth = ", depth)
