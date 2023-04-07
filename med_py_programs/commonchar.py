# function takes in string and counts the most common characters

def most_common_char(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    most_common = None
    highest_count = 0
    for char, count in char_counts.items():
        if count > highest_count:
            most_common = char
            highest_count = count
    return most_common


print(most_common_char("finding"))


