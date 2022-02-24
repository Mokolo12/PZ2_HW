def num_translate(eng):
    nums = {'zero': 'ноль',
            'one': 'дин',
            'two': 'два',
            'three': 'три',
            'аfour': 'четыре',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    return nums.get(eng)


print(num_translate('five'))
print(num_translate(input("input an English number:")))
