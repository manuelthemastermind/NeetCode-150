def max_sum(arr):
    #initialize caches
    cache_include = {}
    cache_exclude = {}

    def maximum_sum_include(i):
        #establish the base case
        if i < 0:
            return float('-inf')
        if i == 0:
            return arr[0]
        if i not in cache_include:
            exclude_current = arr[i]
            include_current = maximum_sum_include(i-1) + arr[i]
            cache_include[i] = max(exclude_current, include_current)
        return cache_include[i]

    def maximum_sum_exclude(i):
        if i < 0:
            return 0
        if i == 0:
            return 0
        if i not in cache_exclude:
            gap_current = maximum_sum_include(i-1)
            include_current = maximum_sum_exclude(i-1) + arr[i]
            cache_exclude[i] = max(gap_current, include_current)
        return cache_exclude[i]

    maximum_with_gap = max(maximum_sum_include(i) for i in range (len(arr)))
    maximum_without_gap = max(maximum_sum_exclude(i) for i in range (len(arr)))

    return max(maximum_with_gap, maximum_without_gap)

def test_case_from_stdin():
    return [int(x) for x in input().strip().split(' ')]

def main():
    t = int(input())
    for index in range(t):
        input()  # To handle the empty line before each test case (if needed)
        arr = test_case_from_stdin()
        print(max_sum(arr))
    return 0

if __name__ == "__main__":
    main()

