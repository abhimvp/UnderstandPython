def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        print(f"ForLoop: i here is {i} & stack here is {stack} & result here is {result}")
         
        while stack and nums[stack[-1]] <= nums[i]:
            print(f"Entered while loop & stack here is {stack} & stack[-1] is {stack[-1]}")
            stack.pop()
            print(f"After popping stack here is {stack}")
        if stack:
            print(f"If: stack here is {stack}")
            result[i] = nums[stack[-1]]
            print(f"result here is {result}")
        stack.append(i)
        print(f"stack here is {stack}")
    return result


# Example usage
nums = [4, 5, 2, 25]
output = next_greater_element(nums)
print(output)  # Output: [5, 25, 25, -1]
