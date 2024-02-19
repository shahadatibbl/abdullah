# while True:
#     print ('choose an operator:')
#     print('a for addition')
#     print('s for substruction')
#     print('m multiplication')
#     print('d for division')

#     operator = input().lower()
#     if operator == 'a':
#         num1 = float(input('Enter First Number:'))
#         num2 = float(input('Enter Second Number:'))
#         print('The sum is:' + str(num1+num2))

#     elif operator == 'b':
#         num1 = float(input('Enter First Number:'))
#         num2 = float(input('Enter Second Number:'))
#         print('The Substruction is:' + str(num1-num2))

#     elif operator == 'c':
#         num1 = float(input('Enter First Number:'))
#         num2 = float(input('Enter Second Number:'))
#         print('The multiplication is:' + str(num1*num2))

#     elif operator == 'd':
#         num1 = float(input('Enter First Number:'))
#         num2 = float(input('Enter Second Number:'))
#         print('The division is:' + str(num1/num2))

#     else:
#         print ('Invalid Entry')
        

# list = ["apple", "orange", "banana"]
# print(list)
# list = ["apple", 120, 3.5, "orange", "banana"]
# print(len(list))

# a = ["apple", 120, 3.5, "orange", True, "banana"]
# print (type(a))

# a = list(("apple", 120, 3.5, "orange", True, "banana"))
# print(a)


# a = {'age' : 45, 'country' : 'India'}
# b = a['country']
# print (len(b))

# x = 5


# f = open("Hello.txt", "r")
# print(f.read())

# f = open("C:\\Users\Abirtraders\\Desktop\\Hello.txt", "r")
# print(f.read())
# f = open("c:\\Users\\Abirtraders\\Desktop\\Hello.txt", "r")
# print(f.read())

# f = open("c:\\Users\\Abirtraders\\Desktop\\Hello.txt", "r")
# print(f.readline())
# f = open("c:\\Users\\Abirtraders\\Desktop\\Hello.txt", "r")
# for x in f:
#   print(x)

# f = open("c:\\Users\\Abirtraders\\Desktop\\Hello.txt", "r")
# print(f.readline())
# f.close()
a = (lambda x, y: x*y)(2,8)
print(a)

