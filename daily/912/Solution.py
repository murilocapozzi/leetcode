class Solution(object):
    def sortArray(self, nums):
        
        def partition(nums, low, high):
            pivot = nums[low]
            i = low
            j = i + 1

            while j <= high:
                if nums[j] <= pivot:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1

            nums[low], nums[i] = nums[i], nums[low]

            return i

        def quickSort(nums, low, high):
            if low >= high: return

            pivot = partition(nums, low, high)
            quickSort(nums, low, pivot - 1)
            quickSort(nums, pivot + 1, high)

        quickSort(nums, 0, len(nums) - 1)
        return nums
        