#На вход программе подается натуральное число n, затем n-строк, затем число k - количество поисковых запросов, затем k
#cтрок — поисковые запросы. Напишите программу, которая выводит все введенные строки,
# в которых встречаются одновременно все поисковые запросы.
ls1 = ["Язык Python прекрасен", "C# - отличный язык программирования", "Stepik - отличная платформа",
       "BEEGEEK FOREVER!", "язык Python появился 20 февраля 1991"]
ls2 = ["язык", "python"]
for i in ls2:
    for j in range(len(ls1) - 1, -1, -1):
        if i.lower() not in ls1[j].lower():
            del ls1[j]
print(*ls1)


ls = [4, 9, 7, 1, 0, 10]

#Пузырёк
for i in range(len(ls) - 1):
    for j in range(len(ls) - 1 - i):
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
print(ls)


#Сортировка выбором
n = len(ls)
for i in range(n):
    #Находим максимальный элемент из неотсортированного списка
    mx = max(ls[:n - i])
    ls[n - 1 - i], ls[ls.index(mx)] = mx, ls[n - 1 - i]
print(ls)


#На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка
# корректным телефонным номером. Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk, где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9
a = "7-983-432-8563".split("-")
flag = True
if len(a) > 2 and len(a) < 5:
    if a[0] == "7":
        for i in range(1, len(a) - 1):
            if a[i].isdigit() and len(a[i]) == 3:
                continue
            else:
                flag = False
                break

    else:
        for i in range(len(a) - 1):
            if a[i].isdigit() and len(a[i]) == 3:
                continue
            else:
                flag = False
                break
    if a[-1].isdigit() and len(a[-1]) == 4 and flag:
        print("YES")
    else:
        print("No")
else:
    print("NO")
