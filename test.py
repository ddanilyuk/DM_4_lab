import random

n = 3  # максимальна кількість вершин графа
colarr = [0 for i in range(n)]
# Генерація симетричної матриці


a = [[0, 1, 1],
     [1, 0, 1],
     [1, 1, 0]]
for r in range(n):  # 6 строк
    print(a[r])

def color(i):

    # Функція вибору фарби для розфарбування вершини з номером
    w = {0}
    print(i)
    for j in range(i):
        # print(j)
        if a[j][i] > 0:
            w.add(colarr[j])
    print(w)

    curcol = 0
    while True:
        curcol += 1
        if curcol not in w:
            break
        # print(curcol)
    return curcol

print("  ")
for i in range(n):
    colarr[i] = color(i)
    # print(colarr[i])
print(colarr)