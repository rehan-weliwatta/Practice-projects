student = {"name" : "John Doe",
           "age" : 35,
           "address" : "New york"}

for key in student.keys(): #Accessing all the keys in dictionary
    print(key)

for val in student.values(): #Accessing all the values
    print(val)

for key,val in student.items(): # Accessing key and value pairs
    print(f"key is - {key} and value is - {val}")

del student["age"] #Deleting a key in a dictionary