# categorize numbers as even or odd


def categorize_number(num):
    categories = []
    for number in range(num):
        if num % 2 == 0:
            categories.append("even")
        else:
            categories.append("odd")

    return categories


# test the function
print(categorize_number(2))  # ['even', 'even']
print(categorize_number(7))  # ['odd', 'odd', 'odd', 'odd', 'odd', 'odd', 'odd']
print(categorize_number(0))  # []


# using list comprehension
def categorize_number_lc(num):
    return ["Even" if number % 2 == 0 else "Odd" for number in range(num)]


print(categorize_number_lc(2))  # Output:['Even', 'Odd']
print(
    categorize_number_lc(7)
)  # Output:['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']
print(categorize_number_lc(0))  # Output: []
