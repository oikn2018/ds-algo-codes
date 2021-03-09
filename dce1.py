string = input().lower()
if not string.isalnum():
    print("Invalid String")
else:
    if '8' in string:
        string = string.replace('8','')
    if '53' in string:
        string = string.replace('53', '')

    print(string)
