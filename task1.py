class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print("{:3d}".format(self.matrix[i][j]), end='')
            print()
        return str()

    def __add__(self, other):
        pass


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[9, 8], [7, 6], [5, 4]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
