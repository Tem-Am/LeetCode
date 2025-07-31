class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        // Two numbers
        // If we create hash table where numbers and save index/index for value
        var table: [Int : Int] = [:]
        for i in 0...nums.count-1{
            table[nums[i]] = i // add num as key and index as value
        }
        // loop it again
        for i in 0...nums.count-1{
            if let num2 = table[target-nums[i]]{
                if num2 != i {
                    return [i , num2]
                }
            }
        }
        return []
    }
}