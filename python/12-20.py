
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(x):
    z = []
    for a in range(len(x)):
        z += x[a]
    return z

print flatten(n)
