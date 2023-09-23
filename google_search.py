#На вход программе подается натуральное число n, затем n-строк, затем число k - количество поисковых запросов, затем k
#cтрок — поисковые запросы. Напишите программу, которая выводит все введенные строки,
# в которых встречаются одновременно все поисковые запросы.
# ls1 = ["Язык Python прекрасен", "C# - отличный язык программирования", "Stepik - отличная платформа",
#        "BEEGEEK FOREVER!", "язык Python появился 20 февраля 1991"]
# ls2 = ["язык", "python"]
# for i in ls2:
#     for j in range(len(ls1) - 1, -1, -1):
#         if i.lower() not in ls1[j].lower():
#             del ls1[j]
# print(*ls1)


ls = [4, 9, 7, 1, 0, 10]

#Пузырёк
# for i in range(len(ls) - 1):
#     for j in range(len(ls) - 1 - i):
#         if ls[j] > ls[j + 1]:
#             ls[j], ls[j + 1] = ls[j + 1], ls[j]
# print(ls)


#Сортировка выбором
# n = len(ls)
# for i in range(n):
#     #Находим максимальный элемент из неотсортированного списка
#     mx = max(ls[:n - i])
#     ls[n - 1 - i], ls[ls.index(mx)] = mx, ls[n - 1 - i]
# print(ls)


#На вход программе подается строка текста. Напишите программу, которая определяет, является ли введенная строка
# корректным телефонным номером. Строка текста является корректным телефонным номером, если она имеет формат:
# abc-def-hijk или
# 7-abc-def-hijk, где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9
# a = "7-983-432-8563".split("-")
# flag = True
# if len(a) > 2 and len(a) < 5:
#     if a[0] == "7":
#         for i in range(1, len(a) - 1):
#             if a[i].isdigit() and len(a[i]) == 3:
#                 continue
#             else:
#                 flag = False
#                 break
#
#     else:
#         for i in range(len(a) - 1):
#             if a[i].isdigit() and len(a[i]) == 3:
#                 continue
#             else:
#                 flag = False
#                 break
#     if a[-1].isdigit() and len(a[-1]) == 4 and flag:
#         print("YES")
#     else:
#         print("No")
# else:
#     print("NO")

#Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает
# первое простое число большее числа num.
# def get_next_prime(num):
#     if num == 1:
#         return 2
#     else:
#         for i in range(num + 1, num * 2):
#             count = 0
#             for j in range(1, i + 1):
#                 if i % j == 0:
#                     count += 1
#             if count == 2:
#                 return i
#
#
# # считываем данные
# n = 1
#
# # вызываем функцию
# print(get_next_prime(n))


#Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True, если пароль является надежным и False - в противном случае.
# def is_password_good(password):
#     flag_lowe = False
#     flag_upper = False
#     flag_digit = False
#     if len(password) > 7:
#         for i in password:
#             if i.isdigit():
#                 flag_digit = True
#             elif i == i.lower():
#                 flag_lowe = True
#             elif i == i.upper():
#                 flag_upper = True
#         if flag_lowe and flag_upper and flag_digit:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))

#Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
#возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и
# False  в противном случае.
# def is_one_away(word1, word2):
#     distinction = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 distinction += 1
#         if distinction == 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

#Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.
# def is_palindrome(text):
#     for i in ' ,.!?-':
#         text = text.replace(i,'').lower()
#     return text == text[::-1]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))

#Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка и False - в противном случае
# def is_valid_password(password):
#     ls = password.split(":")
#     if len(ls) == 3:
#         flag = False
#         count = 0
#         for i in range(1, int(ls[1]) + 1):
#             if int(ls[1]) % i == 0:
#                 count += 1
#         if count == 2:
#             flag = True
#         else: return False
#         if ls[0] == ls[0][::-1] and int(ls[2]) % 2 == 0 and flag:
#             return True
#         else: return False
#     else:
#         return False
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

#Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
#состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является правильной скобочной
#последовательностью и False в противном случае.
#Примечание
# 1. Правильной скобочной последовательностью называется строка, состоящая только из символов ( и ),
# где каждой открывающей скобке найдется парная закрывающая скобка (при этом каждая открывающая скобка должна быть
# левее соответствующей ей закрывающей скобки).
#Примечание 2. Следующий программный код:
# print(is_correct_bracket('()(()())'))
# print(is_correct_bracket(')(())('))
# должен выводить:
# True
# False
# def is_correct_bracket(text):
#     result = 0
#     for i in text:
#         if i == '(':
#             result += 1
#         elif i == ')':
#             result -= 1
#         if result < 0:
#             return False
#     if result == 0:
#         return True
#     else: return False
#
# #Более короткий и простой вариант
# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace("()", "")
#
#     return text == ""
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))