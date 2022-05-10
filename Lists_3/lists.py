"""Lists.

This script showcases basic operations of Python Lists.
"""
# A list in Python is a collection of ordered elements or values, separated by commas, with an index of "zero" for the first element.
# Index: 0 = "green", 1 = "blue", 2 = "red", 3 = "purple"

from pyrsistent import v


car_colection_colors = ["green", "blue", "red", "purple"]

# Lists commonly hold values of the same data type or different data types.
# Lists can even hold other lists!

my_favorite_things = ["travel", 6, 5, ["beach", "mountains", "city"], "tacos"]

# Create a list of countries where you have been.
print("I'm a citizen of the world...")
visited_countries = [
    "Mexico",
    "USA",
    "Spain",
    "Portugal",
    "Iceland",
    "Switzerland",
    "Holland",
    "Ireland",
    "Germany",
    "France",
    "Belgium"
]
print (visited_countries)
print ("--------------")

# user should use the index of their hometown.
print ("My hometown is:")
print (visited_countries[0])
print ("--------------")

# user can check their work with the index method
print("My favorite country is at...")
print(visited_countries)
print(visited_countries.index("Iceland"))
print("---------------")

# Set elements from index 2 to index 5 equal to some_of_our_places variable and print
print("We can access a portion of the list with a slice...")
some_of_our_places = visited_countries[2:5]
print(some_of_our_places)
print("---------------")

# Print every other element
print("Printing every other country")
every_other_country = visited_countries[::2]
print(every_other_country)

# Print the last element of the list
print("The last country is...")
last_country = visited_countries[-1]
print(last_country)

# Change a specified element within the list at the given index
print("Change the first element in the list...")
visited_countries[0] = "Las Vegas, NV"
print(visited_countries)

# Add an element to the end of the list
print("Adding a new place to the end of the list...")
visited_countries.append("Italy")
print(visited_countries)

# Remove an element to the end of the list
print("Removing a new place to the end of the list...")
visited_countries.remove("Italy")
print(visited_countries)

# Remove an element from the list based on the given index
print("Removing 'France' based off of its index")
france_index = visited_countries.index("France")
visited_countries.pop(france_index)
print(visited_countries)
print("---------------")

# Calculate the number of elements within the list
print("Calculating the number of Countries...")
print(len(visited_countries))
print("---------------")
