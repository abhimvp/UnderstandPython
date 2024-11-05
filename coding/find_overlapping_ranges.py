def find_overlapping_ranges(intervals):
    print(intervals)
    intervals.sort(key=lambda x: x[0])  # Sort by start times
    print(intervals)
    overlapping = []
    print(overlapping)
    for i in range(len(intervals) - 1):
        print(i)
        current_interval = intervals[i]
        print(current_interval)
        next_interval = intervals[i + 1]
        print(next_interval)
        if next_interval[0] <= current_interval[1]:  # Check for overlap
            print("if")
            print(next_interval[0])
            print(current_interval[1])
            overlapping.append((current_interval, next_interval))
            print(overlapping)  
    return overlapping

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [17, 20]]
overlapping_ranges = find_overlapping_ranges(intervals)
print(overlapping_ranges)
# Output: [([1, 3], [2, 6]), ([15, 18], [17, 20])]