
def pair_finder(list):
    pairs = []
    for i, num1 in enumerate(list):
        for j, num2 in enumerate(list[i + 1:]):
            if num1 + num2 == 7:
                pairs.append((num1, num2))

    return pairs

list = [1, 2, 3, 4, 5]

# str turns result of pair_finder(list) into string. "[1:-1]" removes brackets from output
result = str(pair_finder(list))[1:-1]

print(result)