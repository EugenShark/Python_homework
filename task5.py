from random import randint
nums = [str(randint(0, 99))for i in range(5)]
print(nums)
with open('my_file_nums.txt', 'w') as write:
    write.write(' '.join(nums))
with open('my_file_nums.txt') as read:
    a = read.read()
    new_list = a.split()
    print(sum(map(int, new_list)))
