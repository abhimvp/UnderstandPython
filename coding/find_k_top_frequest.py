import heapq
from collections import Counter


def find_k_top_frequent(nums, k):
    print(f"nums here is {nums} & k is {k}")
    freq_count = Counter(nums)
    print(f"freq_count here is {freq_count}")
    min_heap = []
    print(f"min_heap here is {min_heap}")
    for num, freq in freq_count.items():
        print(f"num here is {num} & freq here is {freq} from {freq_count.items()}")
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
            print(f"IF: min_heap here is {min_heap}")
        else:
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))
                print(f"ELSE: min_heap here is {min_heap}")
    return [x[1] for x in min_heap]  # Extract elements from tuples


# Example
nums = [1, 1, 1, 2, 2, 3]
k = 2
top_k_frequent = find_k_top_frequent(nums, k)
print(top_k_frequent)  # Output: [1, 2]
