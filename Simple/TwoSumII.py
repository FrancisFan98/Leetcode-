class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for num in numbers:
            if num not in table:
                table[target - num] = num
                continue
            first = numbers.index(table[num]) + 1

            second = numbers[first:].index(num) + first + 1
            return [first, second]
        return []   
            
