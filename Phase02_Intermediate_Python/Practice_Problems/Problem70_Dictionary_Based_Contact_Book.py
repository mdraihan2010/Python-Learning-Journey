# dictionary ব্যবহার করে একটি simple contact book তৈরি করো।

contact_book = {
    "Raihan": "01711111111",
    "Hasan": "01822222222",
    "Karim": "01933333333"
}

name = input("Enter contact name: ")

if name in contact_book:
    print("Phone number:", contact_book[name])
else:
    print("Contact not found.")