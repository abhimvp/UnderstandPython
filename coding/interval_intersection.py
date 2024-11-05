def interval_intersections(firstList, secondList):
    print(f"firstList : {firstList}")
    print(f"secondList : {secondList}")
    i, j = 0, 0
    print(f"i : {i} & j : {j}")
    result = []
    print(f"result : {result}")

    while i < len(firstList) and j < len(secondList):
        print(f"while loop: i : {i} & j : {j}")
        start = max(firstList[i][0], secondList[j][0])
        print(
            f"start = max(firstList[{i}][0]: {firstList[i][0]}, secondList[{j}][0]: {secondList[j][0]}) : {start}"
        )
        end = min(firstList[i][1], secondList[j][1])
        print(
            f"end = min(firstList[{i}][1]: {firstList[i][1]}, secondList[{j}][1]: {secondList[j][1]}) : {end}"
        )

        print(f"if: start : {start} <= end : {end}")
        if start <= end:
            result.append([start, end])
            print(f"if: result : {result}")

        print(f"if: firstList[i][1] : {firstList[i][1]}")
        print(f"if: econdList[j][1] : {secondList[j][1]}")

        if firstList[i][1] < secondList[j][1]:

            i += 1
            print(f"if: i : {i}")
        else:
            j += 1
            print(f"else: j : {j}")

    return result


# Example usage
firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
intersections = interval_intersections(firstList, secondList)
print(intersections)  # Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
