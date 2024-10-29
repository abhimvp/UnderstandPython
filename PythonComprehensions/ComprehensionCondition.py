# get all the even numbers from 0 to 50
def get_even_numbers(max_num):
    """Return a list of even numbers from 0 to max_num"""
    even_numbers = []
    for num in range(max_num + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print(get_even_numbers(10)) #[0, 2, 4, 6, 8, 10]

# using list comprehension - [ value_to_include_in_list  for_loop contidion]
def get_even_numbers_comprehension(max_num):
    """Return a list of even numbers from 0 to max_num using list comprehension"""
    return [num for num in range(max_num + 1) if num % 2 == 0]

print(get_even_numbers_comprehension(10)) #[0, 2, 4, 6, 8, 10]