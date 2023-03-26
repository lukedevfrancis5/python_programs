str = input("Enter a list of strings: ")

str_list = str.split(",")

shortest_len = len(str_list[0])

for string in str_list:
    if len(string) < shortest_len:
        shortest_len = len(string)


print(f"The shortest string in the list is {shortest_len}")
    