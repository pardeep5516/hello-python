# sort

# fruits = ['apple', 'mango','grapes']
# fruits.sort()
# print(fruits)

# fruits = ('apple', 'mango','grapes')
# print(sorted(fruits))
# print(fruits)

# s = {'apple', 'mango', 'grapes'}
# print(sorted(s))


guitars = [
    {
        'model': 'yamaha f310', 'price': 8400
    },
    {
        'model': 'yamaha m310', 'price': 9400
    },
    {
        'model': 'yamaha s310', 'price': 7400
    },
    {
        'model': 'yamaha g310', 'price': 8900
    }
]

print(sorted(guitars, key=lambda d: d['price'], reverse=True))
