class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []
        
        index = None
        if x >= arr[-1]:
            arr.append(x)
            index = len(arr)-1
        else:
            for i in range(len(arr)):
                if x < arr[i]:
                    arr.insert(i, x)
                    index = i
                    break
                    
        left, right= index, index
        
        for i in range(k):
            if (left == 0) or (right + 1 < len(arr) and abs(arr[right + 1] - x) < abs(arr[left - 1] - x)):
                right += 1
            elif left - 1 >= 0:
                left -= 1
            else:
                break
        rs = arr[left:right + 1]
        rs.remove(x)
        return rs
        
                
