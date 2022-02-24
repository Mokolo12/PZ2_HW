from sys import getsizeof

tutors = [

    'Дарья', 'Анастасия', 'Денис', 'Маруся',

    'Крестина', 'Владислав', 'Максим'

]
klasses = [

    '9А', '7В', '9Б', '9В', '8Б',

]


def my_zip_gen():

    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))


if __name__ == '__main__':

    gen = my_zip_gen()
    print(type(gen))
    print(getsizeof(gen))
    print(*gen)
