#Matritsa determinantini hisoblovchi funksiya yaratib olamiz
def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
rows = 2
cols = 2
# Matritsa elementlarini qabul qilish
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Matrix element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)
# Matritsaning qiymatlarini ekranga chiqaramiz
print("Matritsa:")
for row in matrix:
    print(row)
# Matritsaning determinantini hisoblaymiz
det = determinant(matrix)
print("Determinant: ", det)
