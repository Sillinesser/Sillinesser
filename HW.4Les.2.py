    #1.  Роздрукувати всі парні числа менші 100 
    #    (написати два варіанти коду: один використовуючи цикл while, 
    #    а інший з використанням циклу for).
#a)
#print(list(range(0,100,2)))

# b)
# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1

#c)
# for i in range(100):
#     if i % 2 == 0:
#         print(i)

#d)
# for i in range(0,100,2):
#     print(i)


    #2.  Роздрукувати всі непарні числа менші 100.
    #   (написати два варіанти коду: 
    #   один використовуючи оператор continue, а інший без цього оператора).
#a)
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)

#b)
#for i in range(100):
#     if i % 2 == 0:
#         print(i)
   
#3. Перевірити чи список містить непарні числа.
#   (Підказка: використати оператор break)

# a = [4, 1, 2, 6, 2]
# for j in a:
#     if j % 2 != 0:
#         print("Список містить непарні числа")
#         break
# else:
#     print("Список не містить непарні числа")
        