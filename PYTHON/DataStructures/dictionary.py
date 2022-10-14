"""Dictionary is an ordered collection of items. Each item in a dictionary
has a key/value pair.
Items in dictionary are placing inside curly braces and separeted by commas.
They has a key and a corresonding value that is expressed as a pair(key:value).
Value can be of aany data type and can be repeted.
Key must be immutable type and must be unique"""

example_dict = {
    1: 'value_1',
    2: 'value_2',
    3: 'value_3'
}

print(example_dict[1])

# output: return value of key 1 --> 'value_1'

print(example_dict.get(2))

# output: return value of key 2 --> 'value_2'

example_dict[4] = 'value_4'

# output: add new key/value to dict --> {4:'value_4'}

example_dict.pop(2)

# output: remove item 2 from dict

for key, value in example_dict.items():
    print(key)

# output: print all keys from dictionary

for key, value in example_dict.items():
    print(value)

#  output: print all values from dictionary