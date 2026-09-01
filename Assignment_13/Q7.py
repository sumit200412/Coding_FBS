student = {
    "name": "Sumit",
    "age": 20,
    "city": "Pune"}

key = input("Enter key to remove: ")

if(key in student):
    del student[key]
    print(student)
else:
    print("Key not found")