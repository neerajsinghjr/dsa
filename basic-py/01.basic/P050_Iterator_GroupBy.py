from itertools import groupby

a_list = [
	("Animal", "cat"), 
	("Animal", "dog"), 
	("Bird", "peacock"), 
	("Bird", "pigeon")
]
  
print("Example 1...")
for key, group in groupby(a_list, lambda x : x[0]):
    print(key,':', list(group))

# Example 1...
# Animal : [('Animal', 'cat'), ('Animal', 'dog')]
# Bird : [('Bird', 'peacock'), ('Bird', 'pigeon')]

print("Example 2...")
for key, group in groupby(a_list, lambda x : x[1]):
    print(key,':', list(group))

# Example 2...	
# cat : [('Animal', 'cat')]
# dog : [('Animal', 'dog')]
# peacock : [('Bird', 'peacock')]
# pigeon : [('Bird', 'pigeon')]

records = [
    ['5000', '1234567890'],
    ['5000', '1234567890'],
    ['6000', '1234567890'],
    ['6000', '1234567890'],
    ['8000', '1234567890'],
]

print("Example 3...")
for key, group in groupby(records):
    print(key,':', list(group))

# Example 3...
# ['5000', '1234567890'] : [['5000', '1234567890'], ['5000', '1234567890']]
# ['6000', '1234567890'] : [['6000', '1234567890'], ['6000', '1234567890']]
# ['8000', '1234567890'] : [['8000', '1234567890']]

print("Example 4...")
for key, group in groupby(records, lambda x: x[0]):
    print(key,':', list(group))

# Example 4...
# 5000 : [['5000', '1234567890'], ['5000', '1234567890']]
# 6000 : [['6000', '1234567890'], ['6000', '1234567890']]
# 8000 : [['8000', '1234567890']]