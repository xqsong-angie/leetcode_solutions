#20250920
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]
        for k in range(n-3):
            for i in range(k+1,n-1):
                left=i+1
                right=n-1
                if nums[k]>=0 and target>=0 and nums[k]>target:
                    break
                else:
                    while left<right:
                        if nums[k]+nums[i]+nums[left]+nums[right]==target:
                            res.append((nums[k],nums[i],nums[left],nums[right]))
                            left+=1
                            right-=1
                        elif nums[k]+nums[i]+nums[left]+nums[right]<target:
                            left+=1
                        else:
                            right-=1
        return list(set(res))
                    

 #20260606               
    class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            # https://www.geeksforgeeks.org/dsa/find-four-elements-that-sum-to-a-given-value-set-2/#using-hashing-on3-time-and-on-space
            
            # Initialize a set to store unique 
            # quadruplets as sorted tuples
            res_set = set()
            n = len(nums)

            # Iterate to fix the first two elements
            for i in range(n):
                for j in range(i + 1, n):

                    # Set to track elements seen 
                    # so far for the third loop
                    s = set()

                    # Loop to fix the third element and find the fourth
                    for k in range(j + 1, n):
                        sum_val = nums[i] + nums[j] + nums[k]
                        last = target - sum_val

                        # If the fourth required element is already seen
                        if last in s:
                            curr = sorted([nums[i], nums[j], nums[k], last])
                            res_set.add(tuple(curr))

                        # Add current number to the set for future lookup
                        s.add(nums[k])

            return [list(t) for t in res_set]