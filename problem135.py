class Solution:
    def candy(self, ratings: List[int]):
        # Dictiory with all candy
        candy = {}
        for i in range(len(ratings)):
            candy[i] = 1
        # Left to right way: check if next has higher rate, we will increase their candy
        for i in range(len(ratings)-1):
            if ratings[i] > ratings[i+1]:
                if candy[i] <= candy[i+1]:
                    candy[i] += 1
            elif ratings[i] < ratings[i+1]:
                if candy[i+1] <= candy[i]:
                    candy[i+1] = candy[i] + 1
        # Right to left: Check if our initial candy arrangement is valid
        right = len(ratings)-1
        while right > 0:
            # If left neighbor has higher rate and lower and equal candy,
            # we will add more candy to left neighbor
            if ratings[right] < ratings[right-1]:
                if candy[right-1] <= candy[right]:
                    candy[right-1] = candy[right]+1 
            right -= 1
        ans = 0
        for k in candy:
            ans += candy[k]
        return ans        
    
    def ChatSolution(self, ratings):
            n = len(ratings)
            candies = [1] * n  # Initialize everyone with 1 candy
        
            # Left to right pass
            for i in range(1, n):
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1
        
            # Right to left pass
            for i in range(n - 2, -1, -1):
                if ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i], candies[i + 1] + 1)
        
            return sum(candies)
