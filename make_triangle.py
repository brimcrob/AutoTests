def make_triangle(n):
    for i in range(1, +1):
        yield '@' * i
        print('\n'.join(make_triangle(3)))


