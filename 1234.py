# # with open('baza-dannih.txt') as f:
# #     content = f.read(14)
# #     print(content[11:13])
#
# with open('baza-dannih.txt') as f:
#     some = '1231231321321321321321321321321'
#     f.writelines()

with open('example.txt', 'w') as f:
    f.write('Первая часть\n')
    user_data = int(input())
    f.write(user_data)