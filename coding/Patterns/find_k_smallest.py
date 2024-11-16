import heapq


def find_k_smallest(nums, k):
    print(
        "A max-heap is the opposite of a min-heap – the value of each node is greater than or equal to the value of its children. The largest element resides at the root."
    )
    max_heap = []  # Use a max-heap (negate values for heapq)
    print(f"max_heap here is {max_heap}")
    for num in nums:
        print(f"num here is {num} out of nums {nums}")
        if len(max_heap) < k:
            print(f"IF: len(max_heap) here is {len(max_heap)} & k here is {k}")
            heapq.heappush(max_heap, -num)  # Negate to simulate max-heap
            print(f"max_heap here is {max_heap}")
        else:
            print(f"ELSE: len(max_heap) here is {len(max_heap)} & k here is {k}")
            print(f"num here is {num} & -max_heap[0] here is {-max_heap[0]}")
            if num < -max_heap[0]:
                print(f"num here is {num} & max_heap[0] here is {-max_heap[0]}")
                print(f"max_heap here is {max_heap}")
                heapq.heappop(max_heap)
                print(f"max_heap here is {max_heap}")
                heapq.heappush(max_heap, -num)
                print(f"max_heap here is {max_heap}")
    return [-x for x in max_heap]  # Negate back to get original values


# Example
nums = [5, 2, 1, 3, 6, 0]
k = 3
k_smallest = find_k_smallest(nums, k)
print(k_smallest)  # Output: [1, 2]
