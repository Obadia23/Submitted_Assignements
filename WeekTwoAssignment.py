# Create an empty list

my_list = []
print(my_list)

# Append elements

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("my list after append:", my_list)

# Insert 15 at the second position

my_list.insert(1, 15)
print("my list after insert:", my_list)

# Extend the list

my_list.extend([50, 60, 70])
print("my list after extend:", my_list)

# Remove the last element

my_list.pop()
print("my list after pop:", my_list)

# Sort the list in ascending order

my_list.sort()
print("my list after sort:", my_list)

# Find and print the index of the value 30

index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)
