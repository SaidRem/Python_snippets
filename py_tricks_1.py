# 1. List comprehension

from random import randint
my_list = [randint(1, 10) for _ in range(1, 1000)]
# print(my_list)

# 2 Zip

names = ['Alice', 'Bob', 'Josh', 'Erika', 'Maria']
ages = [23, 30, 43, 18, 20]
likes = ['Cherry', 'icecream', 'lemon', 'strawberry', 'orange']
container = zip(names, ages, likes)
for c in container:
    print('{} is {} year old and likes {}'.format(*c))

# 3. Counter 

from collections import Counter

# for i in range(1, 11):
#     print(f'{i} : occures {my_list.count(i)} times')

my_counter = Counter(my_list)
# for c in my_counter:
#     print(f'{c} : occures {my_counter[c]} times')

# for name in set(names):
#     print(f'{name}: {names.count(name)} occurences')

for c in my_counter.most_common(3):
    print(f'{c[0]}: {c[1]} occurences.')

# 4. Enumerating

for i, customer in enumerate(names, 1):
    print(f'{i} : {customer}')

# 5. Parameter expansion


def proc_stud_info(name, last_n, fav_topic, score):
    print(name, last_n, fav_topic, score)


student = ['Alice', 'Smith', 'math', 'A']
proc_stud_info(*student)

student = dict(name='Alice', last_n='Smith', fav_topic='math', score='A')
proc_stud_info(**student)

# 6. Type annotation


def some_computations(a: int, b: int):
    return a + b
