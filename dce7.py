parent = input()
hasChildren = input()
parentCom = 0.05
children = []
if hasChildren == "Y":
    parentCom = 0.10
    children = input().split(",")
print("Total Members: ", 1+len(children))
print("Commission Details")
schemeAmount = 5000
childCom = 0.05

print(parent, ":", (parentCom * schemeAmount))
if hasChildren == "Y":
    print(parent, ":", len(children) * (parentCom * schemeAmount))
    for child in children:
        print(child, ":", childCom * schemeAmount)