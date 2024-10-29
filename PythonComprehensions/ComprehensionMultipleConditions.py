# strings that start with 'a" and end in "y"
def match_strings(strings):
    """
    Returns a list of strings that start with 'a' and end with 'y'
    """
    matching_strings = []
    for string in strings:
        if len(string) <= 1:
            continue
        if string.startswith("a") and string.endswith("y"):
            matching_strings.append(string)
    return matching_strings


# Example usage
strings = ["apple", "banana", "cherry", "antelope", "zebra", "ally"]
result = match_strings(strings)
print(result)  # Output: [ 'ally']


# using list comprehension
def LC_match_strings(strings):
    """
    Returns a list of strings that start with 'a' and end with 'y'
    """
    valid_strings = [
        string
        for string in strings
        if len(string) > 1 and string.startswith("a") and string.endswith("y")
    ]
    
    valid_strings_1 = [
        string
        for string in strings
        if len(string) >=2
        if string[0] == "a"
        if string[-1] == "y"
    ]
    return valid_strings,valid_strings_1

# Example usage
strings = ["apple", "banana", "cherry", "antelope", "zebra", "ally"]
result = LC_match_strings(strings)
print(result)  # Output: [ 'ally']