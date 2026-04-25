phonebook={
"Sara":"9876543210",
"David":"9123456780",
"Surya": "9988776655"
}

phonebook["RIDDHI"]="8796557224"
print(phonebook)

name=input("Enter a name to search: ")
print("Number:", phonebook.get(name,"Not Found"))

delete_name=input("Enter a name to delete: ")

if delete_name in phonebook:
    del phonebook[delete_name]
    print(delete_name,"deleted successfully.")
else:
    print("Cannot dlete. Name not found. ")

print("\nUpdated phonebook: ", phonebook)