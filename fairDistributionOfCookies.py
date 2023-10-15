from ast import List


class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        bucket = [0] * k
        self.min_unfairness = float('inf')
        
        def backtrack(i, bucket):
            if i == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(bucket) - min(bucket))
                return
            
            if max(bucket) > self.min_unfairness: #prunning
                return
            for j in range(k):
                if bucket[j] + cookies[i] <= self.min_unfairness:
                    bucket[j] += cookies[i]
                    backtrack(i + 1, bucket)
                    bucket[j] -= cookies[i]
            return
        backtrack(0, bucket)
        return self.min_unfairness

solution = Solution()

cookies = [64,32,16,8,4,2,1,1000]
k = 8
expected_output = 1000

output = solution.distributeCookies(cookies, k)
print(output == expected_output)  # True
