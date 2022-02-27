"""map() function in python"""

# def square(n):
#     return n * n
#
#
# my_list = [1.43, 2.34, 3.46, 4.56, 5.312, 6.76, 7.798, 8.432, 9.86]
# new_list = map(square, my_list)
# new_list = map(round, new_list)
# print(new_list)
# for i in new_list:
#     print(i, end=" ")

# def my_str(s):
#     return s.upper()
#
#
# my_strs = "I love coding in python, So I am a pythoneer!!"
#
# new_str = map(my_str, my_strs)
# for i in new_str:
#     print(i, end='')
#
# def multiply(num):
#     return num * 10
#
#
# my_num = [2, 3, 4, 5, 6, 7, 8, 9]
# new_num = map(multiply, my_num)
# print(list(new_num))

#
# def tuple_map(n):
#     return n.upper()
#
#
# my_tuple = ('html', 'css', 'javascript', 'python', 'java', 'flutter')
# new_tuple = map(tuple_map, my_tuple)
# print(list(new_tuple))


# def dict_map(n):
#     return n.upper()
#
#
# my_dict = {'HTML': 'HyperText MarkUp Lang', 'CSS': 'Cascading Style Sheets'}
# new_dict = map(dict_map, my_dict.values())
# print(list(new_dict))

#
# my_num_list = [2, 3, 4, 5, 6, 7, 8, 9]
#
# new_num_list = map(lambda x: x ** 2, my_num_list)
# print(list(new_num_list))

# def myList(list1, list2):
#     return list1 * list2
#
#
# my_list1 = [2, 3, 4, 5, 6, 7, 8, 9]
# my_list2 = [9, 8, 7, 6, 5, 4, 3, 2]
#
# new_list = map(myList, my_list1, my_list2)
# print(list(new_list))


# def my_tup_list(list1, tuple1):
#     return list1 + " = " + tuple1
#
#
# my_list = ['a', 'b', 'c', 'd']
# my_tuple = ('PHP', 'Python', 'C++', 'C')
#
# new_tup_list = map(my_tup_list, my_list, my_tuple)
# print(list(new_tup_list))

# import time
#
# for i in "Time of wait before sleep is 2 seconds":
#     print(i, end="")
#     time.sleep(2)
#
# import asyncio
#
#
# async def display():
#     await asyncio.sleep(5)
#     for i in "Time of sleep is 1 seconds":
#         print(i, end="")
#
#
# print("This execution delayed!!")
# asyncio.run(display())

# from threading import Event
#
# print("This message will be display after 10 seconds of wait!!\nPlease relax, and enjoy while the message is "
#       "processed!!")
#
#
# def display():
#     print("\nThe wait is over, Hee is the message, and thank you for waiting!!")
#
#
# Event().wait(10)
# display()

#
# from threading import Timer
#
# print("Ouch You gotta wait 10 seconds before your report is printed!!")
#
#
# def display():
#     print("Here is your report, sorry for keeping you waiting!!")
#
#
# t = Timer(10, display)
# t.start()

# help("modules")



