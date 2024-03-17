def has_unique_characters(data):
    string = set(data)
    if len(data) == len(string):
        return True
    else:
        return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
