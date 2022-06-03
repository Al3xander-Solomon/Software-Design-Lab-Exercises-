def multiply(m, n):
    if (n <= 1):
        return m
    else:
        return m + Multiply(m, n - 1)
