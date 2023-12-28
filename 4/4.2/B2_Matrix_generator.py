def make_matrix(size, value=0):
    if isinstance(size, int):
        matrix = []

        for i in range(size):
            m = []
            for j in range(size):
                m.append(value)

            matrix.append(m)

        return matrix

    else:
        size = list(size)
        x, y = size[0], size[1]

        matrix = []

        for i in range(y):
            m = []
            for j in range(x):
                m.append(value)

            matrix.append(m)

        return matrix

