dictionary = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_txt = []
with open("text_4.txt") as read:
    for i in read:
        i = i.split(' ', 1)
        new_txt.append(dictionary[i[0]] + ' ' + i[1])
with open('text_4_new.txt', 'w') as write:
    write.writelines(new_txt)
