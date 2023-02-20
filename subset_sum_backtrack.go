package main

import "fmt"

func subsetSumBacktrack(S []int, d int) []int {
    n := len(S)
    var path []int
    var result []int

    // Backtracking function
    var backtrack func(start, sum int)
    backtrack = func(start, sum int) {
        if sum == d {
            // Found a valid subset
            result = make([]int, len(path))
            copy(result, path)
            return
        }

        if sum > d || start == n {
            // Exceeded the target sum or reached the end of the array
            return
        }

        // Include the current element in the subset
        path = append(path, S[start])
        backtrack(start+1, sum+S[start])
        path = path[:len(path)-1]

        // Exclude the current element from the subset
        backtrack(start+1, sum)
    }

    backtrack(0, 0)
    return result
}

func main() {
    S := []int{1, 2, 3, 4, 5}
    d := 7
    subset := subsetSumBacktrack(S, d)
    fmt.Println("Subset that sums up to", d, ":", subset)
}
