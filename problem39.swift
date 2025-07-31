class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var answer : [[Int]] = []
        // backtrack
        func backtrack( _ start : Int, _ current : [Int], _ total  : Int ){
            if total == target{
                answer.append(current)
                return
            } 
            if total > target{
                return
            }

            // loop all the numbers
            for i in start...candidates.count-1{
                var newCurrent = current
                newCurrent.append(candidates[i])
                backtrack(i, newCurrent, total + candidates[i])
            }
        }
        backtrack(0, [], 0)
        return answer
    }
}