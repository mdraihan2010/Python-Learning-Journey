# একই নামের Local এবং Global Variable

name = "Raihan"

def show_name():
    name = "Rahim"
    print(name)

show_name()

print(name)


# Global name = "Raihan"
# Function-এর ভিতরে: Local name = "Rahim"
# Local Variable Priority পায়

# Function-এর বাইরে: Global name ব্যবহার হয়