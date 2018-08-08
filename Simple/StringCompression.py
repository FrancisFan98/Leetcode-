class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur = None
        count = 0
        index = 0
        
        while index < len(chars):
            if chars[index] != cur:
                if count and count > 1:
                    chars.insert(index, str(count))
                    index += 1
                cur = chars[index]
                count = 1
                index += 1
            else:
                del chars[index]
                count += 1
        if count and count > 1:
                    chars.insert(index, str(count))
        
        index = 0
        while index < len(chars):
            if len(chars[index]) > 1:
                cur = 0
                n = len(chars[index])
                text = chars[index]
                for cha in text:

                    chars.insert(cur + index, cha)
                    cur += 1
                del chars[cur + index ]
                index = index -1 + n
                
            else:
                index += 1
                pass
        
        return len(chars)
