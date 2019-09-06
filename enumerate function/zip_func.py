# zip function
user_id = ['user1', 'user2,''user3']
# user_id = ['user1', 'user2']
names = ['alex', 'alice', 'tom']
last_names = ['yadav', 'sha', 'lua']
#('user1', 'alex')('user2','alice')

# print(list(zip(user_id,names)))
# print(dict(zip(user_id,names,last_names)))
print(list(user_id, names, last_names))


example = [('a', 1), ('b', 2)]
print(dict(example))
