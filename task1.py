#Из списка вытащить цифры и распечатать те которые делятся на 2.

test = ['123', '112312', 'asdasd3', '1aaw4', 'asd13', '134', '128']

for char in test:
    if char.isdigit():
        char = int(char)
        if char % 2 == 0:
            print(char)