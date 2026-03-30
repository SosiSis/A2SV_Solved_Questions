class Solution:
    def generateSubsets(self, index, ans, nums, subset):
        if index == len(nums):
            if subset not in ans:  # Avoid duplicates
                ans.append(list(subset))
            return

        # Include the current element
        subset.append(nums[index])
        self.generateSubsets(index + 1, ans, nums, subset)

        # Exclude the current element
        subset.pop()
        self.generateSubsets(index + 1, ans, nums, subset)

    def subsetsWithDup(self, nums):
        ans = []
        nums.sort()  # Sort to handle duplicates
        self.generateSubsets(0, ans, nums, [])
        return ans