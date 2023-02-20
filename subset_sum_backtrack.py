def subset_sum_backtrack(S, d):
    n = len(S)
    path = []
    result = []

    # Backtracking function
    def backtrack(start, sum):
        if sum == d:
            # Found a valid subset
            result.extend(path[:])
            return

        if sum > d or start == n:
            # Exceeded the target sum or reached the end of the array
            return

        # Include the current element in the subset
        path.append(S[start])
        backtrack(start+1, sum+S[start])
        path.pop()

        # Exclude the current element from the subset
        backtrack(start+1, sum)

    backtrack(0, 0)
    return result

# Example usage
S = [1, 2, 3, 4, 5]
d = 7
subset = subset_sum_backtrack(S, d)
print(f"Subset that sums up to {d}: {subset}")
