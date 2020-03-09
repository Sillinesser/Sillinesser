

# try:
#     a = int(input("Введіть ціле число:"))

#     if a%2 == 0:
#         print("введене число парне")
#     elif a==0:
#         print("Введене число не є парне і не є непарне")
#     else:
#         print("Введене число непарне")

# except Exception:
#     print("Error")





# def vik(age):
#     if age < 0:
#         raise ValueError("Введіть вік > 0")
#     elif age%2 == 0:
#         print("Вік парний")
#     else:
#         print("Вік непарний")
    
# try:
#     v = int(input("Введіть Ваш вік"))
#     vik(v)

# except ValueError:
#     print("Введіть вік > 0")

# except:
#     print("Помилка")



try:
    a,b = eval(input("Введіть два числа через кому"))
    print(a/b)

except SyntaxError:
    print("Comma is missing. Enter numbers separated by comma like this 1, 2")
except ZeroDivisionError:
    print("На 0 не ділю")
