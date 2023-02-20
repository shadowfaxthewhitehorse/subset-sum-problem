# solve the subset sum problem
#
# The problem is as follows: given a set S of n positive integers, and a positive integer d, 
# write a program to find that subset of S that sums up to d.
#
# This implementation uses backtracking.
#
# function subset_sum_backtrack()
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

# DEVNOTES
#
# The problem is as follows: given a set S of n positive integers, and a positive integer d, 
# write a program to find that subset of S that sums up to d.
# 
# S = {s_0, s_1, ..., s_n}
#
# The program defines a backtracking function backtrack, which takes two arguments: the starting index start and the current sum sum. The function 
# checks if the current sum equals the target sum d. If so, it appends the current path to the result array. If the current sum is greater than d 
# or the starting index equals the length of the input array, the function returns without modifying the result array.
#
# The function then recursively calls itself twice, once to include the current element in the subset and once to exclude it. The function updates 
# the current sum and the current path accordingly.
#
# Finally, the program calls subset_sum_backtrack with the input array S and the target sum d. It prints the resulting subset to the console.
#
# Note that this backtracking algorithm can be visualized as a tree, with each level i either adding element # i (s_i) or not adding it.
# 

# Example usage
S = [1, 2, 3, 4, 5]
d = 7
subset = subset_sum_backtrack(S, d)
print(f"Subset that sums up to {d}: {subset}")
