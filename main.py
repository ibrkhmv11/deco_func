# def decorator(func):
#     def wrapper():
#             print("Funksiya boshlandi")
#             func()
#             print('Funksiya tugadi')
#
#     return wrapper
#
# @decorator
# def test():
#     print('Salom')
#
#
# test()
#
#
#
# def salomlash(ism):
#     def wrapper(func):
#         return f'Assalomu alaykum {ism}'
#
#
# def tanish(ism):
#     return f'Mening ismin "{ism}"'

# def decarator1(func):
#     def wrapper():
#         print("Dec1 ishlayapti")
#         func()
#     return wrapper
#
#
# def decarator2(func):
#     def wrapper():
#         print("Dec2 ishlayapti")
#         func()
#     return wrapper
#
# @decarator1
# @decarator2
# def salom():
#     print('Salom')
#
# salom()


# def decarator1(fund):
#     def wrapper(s):
#         nwe = [i for i in s if i % 2 == 0]
#         return fund(nwe)
#
#     return wrapper
#
#
# def decorator2(fund):
#     def wrapper(s):
#         nwe = [i for i in s if i > 0]
#         return fund(nwe)
#
#     return wrapper
#
#
#
# @decarator1
# @decorator2
# def hisobla(a):
#     return a
#
#
# a = [1, 2, 3, 4, 5, -3, -5, -43]
# print(hisobla(a))

# ====================================================================
#                              1  - misol

# def my_decorator(func):
#     def wrapper():
#         print("===== START =====")
#         print(func())      # bu yerda printni hisobiga None aytaradi
#         print("===== END =====")
#     return wrapper
#
#
# @my_decorator
# def salom():
#     print("Salom")
#
# salom()

# ====================================================================



# def salomlash(func):
#     def wrapper(ism):
#         hj =  f'Assalomu alaykum {ism}'
#         return func()
#     return wrapper
#
# @salomlash
# def tanish(ism):
#     return f'Mening ismim "{ism}"'
#
# print(tanish("ali"))



# def salomlash(func):
#     def wrapper(ism):
#         matn = func(ism)
#         return f'Assalomu alaykum {ism.title()}. {matn}'
#     return wrapper
#
# @salomlash
# def tanish(ism):
#     return f'Mening ismim "{ism.title()}".'
#
# print(tanish("ali"))

# ====================================================================
#                                2 - misol

# def show_data(func):
#     def wrapper(*args):
#         print(args)
#         return func(*args)
#     return wrapper
#
# @show_data
# def add(a, b):
#     return a + b
#
# print(add(1, 2))

# =====================================================================
#                               3 - misol

# def get_double(func):
#     def wrapper():
#         result = func()
#         return  result * 2
#     return wrapper
#
# @get_double
# def son():
#     return 12
#
# print(son())

# ====================================================================
#                               4 - misol

# a = [-5 , 3, -2, 10 , 7]
# def dec_musbat(func):
#     def wrapper(royhat):
#         new_data = [i for i in royhat if i > 0]
#         return func(new_data)
#     return wrapper
#
# @dec_musbat
# def show_data(data):
#     return data
#
# print(show_data(a))
# ====================================================================
#                               5 - misol

# def chiziq_dec(func):
#     def wrapper():
#         print("===============================")
#         func()
#         print("===============================")
#     return wrapper
#
# @chiziq_dec
# def salom():
#     print("            salom")
# salom()

#                               6 - misol
# def katta_harf(func):
#     def wrapper(ism):
#         katta_ism = ism.upper()
#         return func(katta_ism)
#     return wrapper
# @katta_harf
# def tanish(ism):
#     return f"Mening ismim {ism}"
#
# print(tanish("ali"))


#                             1 - misol
# def qoshimcha_dec(func):
#     def wrapper():
#         print("=========START==========")
#         print(func())
#         print("=========END==========")
#     return wrapper
# @qoshimcha_dec
# def salom():
#     print("salom")
# salom()


#                            2 - misol

# def show_args(func):
#     def wrapper(a , b):
#         print(a,b)
#         print(func(a,b))
#     return wrapper
# @show_args
# def add(a , b):
#     return a+b
# print(add(1,2))

#                            3 - misol
# def get_show(func):
#     def wrapper():
#         natija = func() * 2
#         return natija
#     return wrapper
# @get_show
# def show():
#     return 5
# print(show())

#                           4 - misol

# a = [-4 , 5 , -5 , 4, 332 , 23]
# def musbatlari(func):
#     def wrapper(royhat):
#         new_data = [i for i in royhat if i > 0]
#         return func(new_data)
#     return wrapper
#
# @musbatlari
# def yigindisi(data):
#     return sum(data)
#
# print(yigindisi(a))

#                         5 - misol
# def sana(func):
#     def wrapper(a,b):
#         wrapper.counter += 1
#         return func(a,b)
#     wrapper.counter = 0
#     return wrapper
#
# @sana
# def add(a , b):
#     return a+b
# print(add(4 , 5))
# print(add(4 , 5))
# print(add(4 , 5))
# print(add(4 , 5))
#
# print(f"Jami : Funksiya {add.counter} marta ishlatildi")


#                         6 - misol
# a = [ 3, 45, 6, 7, 45, 34, 232]
# def get_juft(func):
#     def wrapper(data):
#         new_data = [i for i in data if i % 2 == 0]
#
#         return func(new_data)
#     return wrapper
#
#
#
# @get_juft
# def sums(data):
#     return f"Faqat juft sonlar sum : {sum(data)}"
#
# print(sums(a))



#                         7 - misol
# import time
# def timer(func):
#     def wrapper(a , b):
#         start = time.time()
#         func(a, b)
#         end = time.time()
#         print(f"Bajarilish vaqti :" , end - start , "sekund")
#
#     return wrapper
#
# @timer
# def add(a, b):
#     return a + b
#
# print(add(1, 2))

#                        8 - misol
# A = [3, 56 , 43 , 23 , 343, 23 , 44, 32, - 43, - 2 , 32 , - 32 ]

# def juft_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if  i % 2 == 0 ]
#         return func(new_data)
#     return wrapper
#
# def musbat_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 0 ]
#         return func(new_data)
#     return wrapper
#
# @juft_deco
# @musbat_deco
# def func(data):
#     return data
#
# print(func(A))

#                                 8 - musbat

# a = [ 2,45 , 44 , 233 , 21 , 26 , 5]
#
# def tartibli_dec(func):
#     def wrapper(*args):
#         new_data = sorted(args[0])
#         return func(new_data)
#     return wrapper
#
# @tartibli_dec
# def returnr(data):
#     return data
#
# print(returnr(a))

# #                                  9 - musbat
# a = [3 , 45, 54, 34, 50 , 60 , 70 , 10 , 32, 43, -23 , -231 , -5]
#
# def musbat_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 0 ]
#         return func(new_data)
#     return wrapper
#
#
# def ten_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 10 ]
#         return func(new_data)
#     return wrapper
# def sort_deco(func):
#     def wrapper(*args):
#         new_data = sorted(args[0])
#         return func(new_data)
#     return wrapper
#
# @sort_deco
# @musbat_deco
# @ten_deco
# def show(data):
#     return data
#
# print(show(a))

#                                10 - misol

# a = [9 , 34 , 442 , -232, - 3 , 89 , -23]
#
# def musbat_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 0]
#         return func(new_data)
#     return wrapper
#
# def juft_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i % 2 == 0]
#         return func(new_data)
#     return wrapper
#
# def ten_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 10 ]
#         return func(new_data)
#     return wrapper
#
#
# @musbat_deco
# @juft_deco
# @ten_deco
# def show(data):
#     return data
#
# print(show(a))

#                              11 - misol
#
# import time

# def execution_time_deco(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         end = time.time()
#         execution_time = end - start
#
#         if execution_time > 1:
#             print("Sekin")
#         else:
#             print("Tez")
#
#         return result , execution_time
#     return wrapper
#
#
# @execution_time_deco
# def speed_test():
#     print("Ishlayapti ,lekin")
#
# speed_test()

#                              12 - misoll

# def str_dec(func):
#     def wrapper(strings):
#         new_data = strings.upper()
#         return func(new_data)
#     return wrapper
#
#
# @str_dec
# def show(str_data):
#     return str_data
#
#
# print(show("hello"))

#                                 13 - misol

# a = [-2 , 3 , 4 , 6, -8]
#
# def mus_dec(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i > 0 ]
#         return func(new_data)
#     return wrapper
#
# def juft_deco(func):
#     def wrapper(*args):
#         new_data = [i for i in args[0] if i % 2 == 0]
#         return func(new_data)
#     return wrapper
#
# def kv_deco(func):
#     def wrapper(*args):
#         new_data = [i**2 for i in args[0]]
#         return func(new_data)
#     return wrapper
# @mus_dec
# @juft_deco
# @kv_deco
# def show(data):
#     return data
# print(show(a))

#                      8 - misol
# a = [3, 45, 65, 3, 2, 32, 9, 44]
# def sort_dec(func):
#     def wrapper(datas):
#         result = sorted(datas)
#         return func(result)
#     return wrapper
# @sort_dec
# def returs(data):
#     return data
#
# print(returs(a))


#                          14 - misol
# import time
# def func_name_dec(func):
#     def wrapper(a, b):
#         start = time.time()
#         print(func.__name__)
#         print(func.__doc__)
#         natija = func(a , b)
#         end = time.time()
#         exec_time = end - start
#         print(f"Funksiya ishlash vaqti : {exec_time}")
#         return natija
#     return wrapper
#
# @func_name_dec
# def returs(a , b):
#     return a * b
#
# print(returs(1, 2))

#                             15 - misol
#
# def integer_dec(func):
#     def wrapper(a):
#         natija =  isinstance(a, int)
#         if natija:
#             return func(a)
#         else:
#             return "Faqat raqam kiriting"
#     return wrapper
#
#
#
#
# def ret(a):
#     return a
# print(ret(1))

#                              16 - misol

# def is_manf_dec(func):
#     def wrappper(a):
#         if a > 0 :
#             return func(a)
#         else:
#             return "Xatolik : manfiy bo'ldi !!! "
#
#     return wrappper
# @is_manf_dec
# def ret(data):
#     return data
#
# print(ret(-34))

#                               17 - misol

# def ret(func):
#     def wrapper(a , b):
#         natija = func(a, b)
#         with open("natija.txt" , "a") as f:
#             f.write(str(natija)+"\n")
#
#         return natija
#     return wrapper
# @ret
# def hisobla(a , b):
#     return a + b
#
# print(hisobla(1 , 2))
# print(hisobla(1 , 3))
# print(hisobla(1 , 4))








































































