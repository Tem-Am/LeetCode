class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):

        # base case
        if len(intervals) == 0:
            return [newInterval]
        # Make new array with no overlapping
        answer = [] # new interval with new point
        change = True
        middle = False
        for i in intervals:
            if i[0] <= newInterval[0] <= i[1] and i[0] <= newInterval[1] <= i[1]:
                answer.append(i)    
                change = False
            # find the point where new start of interval exist 
            elif newInterval[0] <= i[0] <= newInterval[1] or newInterval[0] <= i[1] <= newInterval[1]: 
                if i[0] < newInterval[0]:
                    newInterval[0] = i[0] # update new interval start
                # find the exist point for new interval one
                if newInterval[1] < i[1]:
                    newInterval[1] = i[1] # update new interval end
                middle = True
            else:
                if middle:
                    answer.append(newInterval)
                    middle = False
                    change = False
                answer.append([i[0], i[1]]) # no need for any changes 
        
        if change:
            answer.append(newInterval)
        answer.sort()
        return answer