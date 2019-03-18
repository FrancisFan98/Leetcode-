class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1, i2 = None, None
        distance = float("inf")
        for i, v in enumerate((words)):
               
            if v == word1:
                i1 = i
            elif v == word2:
                i2 = i
            distance = min(abs(i1-i2), distance) if i1 != None and i2 != None else distance
            
        return distance