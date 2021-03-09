first, second, third = input().split()

for char in first:
    if char in ["a", "e", "i", "o", "u"]:
        first = first.replace(char, "%")

for char in second:
    if  char.isalpha() and char not in ["a", "e", "i", "o", "u"]:
        second = second.replace(char, "#")

third = third.upper()

print(first, second, third)