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

//
// DEVNOTES
//
// The problem is as following: given a set S of n positive integers, and a positive integer d, write a program to find that subset of S that sums up to d.
//
// The program defines a backtracking function backtrack, which takes two arguments: the starting index start and the current sum sum. The function 
// checks if the current sum equals the target sum d. If so, it copies the current path to the result array. If the current sum is greater than d 
// or the starting index equals the length of the input array, the function returns without modifying the result array.
//
// The function then recursively calls itself twice, once to include the current element in the subset and once to exclude it. The function updates 
// the current sum and the current path accordingly.
//
// Finally, the main function calls subsetSumBacktrack with the input array S and the target sum d. It prints the resulting subset to the console.
//
//
func main() {
    S := []int{1, 2, 3, 4, 5}
    d := 7
    subset := subsetSumBacktrack(S, d)
    fmt.Println("Subset that sums up to", d, ":", subset)
}
