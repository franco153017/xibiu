# Arrays (w'ell use the numpy library)
import numpy as np

#create an array
array = np.array([1, 2, 3, 4, 5])
print("array:", array)
      
 # Accessing elements
print("First element:",array[0])
print("last element element:",array[-1])
        
 # Slicing
print(" elements from 1 to 3:", array[1:3])

# List  
my_list = [1, 2, 3, 4, 5]
print("list", my_list)

# Append an element
my_list.append(6)
print("list after append:", my_list)
 
 # Insert an element at specific position
my_list.Insert (2, 7)
print("list after insert:", my_list)

# Remove an element
my_list.remove(4)
print("list after remove:", my_list)

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print( "tuple:", my_tuple)

# acessing elements ( same as lists)
print("first element:", my_tuple[0])
print("last element:", my_tuple[-1])

#loops
#for loop
fruits = ["aplle", "banana", "cherry"]
for fruit in fruits:
 print(fruit)

 # while loop
 i = 0
 while i < 5:
    print(i)
    i += 1

    #looping over a list with indices
    my_list = [1, 2, 3, 4, 5]
    for i, elemnt in enumerate(my_list):
       print(f"Index {i}: {element}")