import random
import os

with open('file.txt', 'r', encoding='UTF8') as input_file:
    text = input_file.read().split('\n')
lst_t = dict()
lst_l = dict()
for i in text:
    if not i:
        continue
    a = i
    a = a.replace(' ', '')
    a = a.split('-')
    b = a[1].split('/')
    lst_t[a[0]] = b


def test(lst, nums=-1):
    lst = lst.copy()
    if nums == -1:
        nums = int(input('Кол-во тестов'))
        if nums == -1:
            nums = len(lst)

    for i in range(nums):
        b = random.choice(list(lst))
        print(b)
        c = lst[b]
        d = input('На русском: \n')
        del lst[b]
        while d.lower() not in c:
            d = input('неправильно \n')
            if d == 'next':
                break
        print('nice!')
    main()

def learn(lst):
    main_lst = dict()
    nums = int(input('Кол-во слов'))
    if nums == -1:
        nums = len(lst)
    for i in range(nums):
        b = random.choice(list(lst))
        print(b, *lst[b])
        d = input('\n')
        while d.lower() != 'да':
            d = input()
        main_lst[b] = lst[b]
    f = input('Тест по словам')
    if f.lower() == 'да':
        test(main_lst, len(main_lst))
    os.system('clear')
    main()

def main():
    answer = input('Что вы хотите сделать?\n Тест или Учить \n')
    if answer.lower() == 'тест':
        test(lst_t)
    elif answer.lower() == 'учить':
        learn(lst_t)
    exit(0)

main()