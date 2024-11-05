def merge_intervals(intervals):
    print(f"before sort : intervals : {intervals}")
    intervals.sort(key=lambda x: x[0])  # Sort by start times
    print(f"after sort : intervals : {intervals}")
    merged = []
    print(f"merged : {merged}")
    if intervals:
        merged.append(intervals[0])
        print(f"initial merge : {merged}")

    for interval in intervals[1:]:
        print(f"interval : {interval} & merged : {merged}")
        last_end = merged[-1][1]
        print(f"last_end : {last_end}")
        print(f"interval[0] : {interval[0]} ")
        if interval[0] <= last_end:

            merged[-1][1] = max(last_end, interval[1])
            print(f"IF:merged : {merged}")
        else:
            merged.append(interval)
            print(f"ELSE:merged : {merged}")

    return merged


# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)  # Output: [[1, 6], [8, 10], [15, 18]]
