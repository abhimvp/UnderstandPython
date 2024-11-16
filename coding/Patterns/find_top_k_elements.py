import heapq


def find_top_k_elements(nums, k):
    min_heap = []
    print(f"min_heap here is {min_heap}")
    for num in nums:
        print(f"num here is {num} out of nums {nums}")
        if len(min_heap) < k:
            print(f"len(min_heap) here is {len(min_heap)} & k here is {k}")
            heapq.heappush(min_heap, num)
            print(f"min_heap here is {min_heap}")
        else:
            print(f"len(min_heap) here is {len(min_heap)} & k here is {k}")
            if num > min_heap[0]:  # Compare with the smallest in the heap
                print(f"num here is {num} & min_heap[0] here is {min_heap[0]}")
                print(f"min_heap here is {min_heap}")
                heapq.heappop(min_heap)
                print(f"min_heap here is {min_heap}")
                heapq.heappush(min_heap, num)
                print(f"min_heap here is {min_heap}")
    return min_heap


# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 3
top_k_elements = find_top_k_elements(nums, k)
print(top_k_elements)  # Output: [5, 6]
