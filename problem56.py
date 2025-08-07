class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # no sorted i guess 
        # Op1 : bruto-force search 
        # Op2 : sorting array first 
        sortedIntervals = sorted(intervals) # So, all the elements are sorted by start
        
        # Know starts are in order
        answer = []
        start = sortedIntervals[0][0]
        end = sortedIntervals[0][1]
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] <= end:
                if sortedIntervals[i][1] > end:
                    end = sortedIntervals[i][1] # update new end
            else: # it means next start point is greater than end 
                answer.append([start, end]) # add to answer
                start = sortedIntervals[i][0]
                end = sortedIntervals[i][1] # update new start ande end points
        answer.append([start,end]) # becasue they are not added to answer yet
        return answer