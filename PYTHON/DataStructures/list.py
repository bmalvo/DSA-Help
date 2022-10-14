"""List is a ordered colection of items.
To creating a list all the items in the list should be put in square brackets
and separeted by commas.
A list can be nested so it can contain any type of object- also another list.
A list is mutable. A user can search, add, shift, move and delete elements
from the list. """

example_list = ['item1', 'item2', 'item3', ['nested_item1', 'nested_item2']]

print(example_list[3]) 

# output: fourth element from list --> ['nested_item1', 'nested_item2']

example_list.append('item4')

# output: add object 'item4' to end of list -->
#  ['item1', 'item2', 'item3', ['nested_item1', 'nested_item2'], 'item4']

example_list.pop()

# output: delete last object from the list --> 'item4'
