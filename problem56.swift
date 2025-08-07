class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        // sort them first
        var sortedIntervals = intervals
        sortedIntervals.sort {$0[0] < $1[0]}
        
        var start = sortedIntervals[0][0]
        var end = sortedIntervals[0][1]
        var answer : [[Int]] = []
        for i in sortedIntervals{
            if i[0] <= end{
                if i[1] > end{
                    end = i[1]
                }
            }
            else{
                answer.append([start,end])
                start = i[0]
                end = i[1]
            }
        }
        answer.append([start, end])
        return answer
    }
}