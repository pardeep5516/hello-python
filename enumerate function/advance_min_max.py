numbers = [1, 2, 4, 6, 7, 8]

# print(max(numbers))
# print(min(numbers))


# def func(item):
#     return len(item)


names = ["alex", "alice", "abc", 'z']
# print(min(names, key=func))
# print(max(names, key=func))

# print(max(names,key= lambda item: len(item)))

students1 = {
    'alex': {'score': 50, 'age': 20},
    'alice': {'score': 60, 'age': 32},
    'tom': {"score": 70, 'age': 23}
}
students2 = [
    {'name': 'alex', 'score': 96, 'age': 27},
    {'name': 'alice', 'score': 80, 'age': 30},
    {'name': 'tom', 'score': 50, 'age': 25},
]
# print(max(students2,key= lambda item:item.get('age'))['name'])


print(max(students1, key=lambda item: students1[item]['score']))
