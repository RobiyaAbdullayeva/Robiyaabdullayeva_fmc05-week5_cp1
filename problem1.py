languages = ("russian", "french", "spanish")

ask = input( "Enter your language in lowercase: ")

for i in languages:
    if ask == i:
        print("Available")
    else:
        print("Not available")