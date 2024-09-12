# This is some practice on slicing arrays in Python.
# It will rely on the use of a colon, and the indexes of the list.

list_one = [5, 10, 15, 20, 25, 30]

# For the first task, copy list_one into List_one_copy
# Remember, to access elements in a list, use brackets
# at the end of the list's name: list_one[!!here!!]
list_one_copy = [5, 10, 15, 20, 25, 30]
print (list_one)
print (list_one_copy)
# Now use a print statement to check your work!
# # Code Here # #

# Now, select all numbers greater than 10 from list_one!
over_10 = [num for num in list_one if num > 10]

# Now use a print statement to check your work!
# # Code Here # #
print (over_10)
# Next, store all the numbers less than 20 in under_20.
# Recall that when using a colon, the number on the right when
# called is not included in the slice.
under_20 = [num for num in list_one if num < 20]

# Now use a print statement to check your work!
# # Code Here # #
print (under_20)

# For the last task, here is a list of names:
names_list = ["Frank", "Sally", "Grant", "Amelia", "Ricardo", "Rachelle"]
second_name = names_list [1]
fourth_name = names_list [3]
# Select the 2nd through the 4th names in names_list
median_names = [second_name, fourth_name]

# Now use a print statement to check your work!
# # Code Here # #
print (median_names)