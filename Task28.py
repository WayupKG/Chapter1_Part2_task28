# def negative():
#     int_list = [5, -5, 4, -9, -78, 54, 0, 0]
#     res_list = []
#     for i in int_list:
#         if i > 0:
#             i *= -1
#         elif i < 0:
#             i *= -1
#         elif i == 0:
#             i = i
#         res_list.append(i)
#     print(f"Результат {res_list}")
# negative()

 # ----------------------------------------------
# Почему так нельзя
# def negative():
#     int_list = [5, -5, 4, -9, -78, 54, 0, 0]
#     res_list = []
#     for i in int_list:
#         i *= -1
#         res_list.append(i)
#     print(res_list)
# negative()