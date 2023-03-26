def even_sum(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
            
    print(f"The sum of even numbers in the list is {total}")



even_sum([1,2,3,4,5,6])

