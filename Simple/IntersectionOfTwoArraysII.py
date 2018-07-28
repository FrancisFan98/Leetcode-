class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        rs = []
        while nums1 and nums2:
            if nums1[0] == nums2[0]:
                rs.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
                
            else:
                if nums1[0] < nums2[0]:
                    nums1.pop(0)
                    
                else:
                    nums2.pop(0)
                    
        return rs
