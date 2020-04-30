with open("my_file.txt") as read:
    strng = read.readlines()
    print(f'Количество срок в файле: {len(strng)}')
    b = 0
    for i in strng:
        a = ''.join(i.split())
        b += 1
        print(f'Количество букв в строке {b} - {len(a)}шт')
