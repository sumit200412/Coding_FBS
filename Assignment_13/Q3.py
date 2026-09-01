student = {
    "name": "Sumit",
    "age": 20,
    "city": "Pune"
}

key = input("Enter key: ")

if(key in student):
    print("Key exists")
else:
    print("Key does not exist")