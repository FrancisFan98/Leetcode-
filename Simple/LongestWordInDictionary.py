class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        rs, ws = "", set(words)
        
        for w in ws:
            if len(w) > len(rs) or (len(w) == len(rs) and w < rs):
                if all([w[:i] in ws for i in range(1, len(w))]):
                    rs = w
        return rs

"""class node(object):
    def __init__(self, char):
        self.val = char
        self.children = []
        self.found = False
        
    
        

class Solution(object):
    def add(self, root, word):
        if not word:
            root.found = True
            return 
        
        child_v = [child.val for child in root.children]
        index = child_v.index(word[0]) if word[0] in child_v else -1
        
        if index != -1:
            self.add(root.children[index], word[1:])
            
        else:
            root.children.append(node(word[0]))
            self.add(root.children[-1], word[1:])
        
    
    def dfs(self, root, n):
        if not root or not root.found :
            return ""
        

        level = []
        
        for child in root.children:
            nextL = self.dfs(child, n+1)
            level.extend([root.val + s for s in nextL])
        
        if not level: 
            level.append(root.val)
        
        return level
        
    def longestWord(self, words):
        
        root = node("")
        root.found = True
        
        for word in words:
            self.add(root, word)
        
        answers = self.dfs(root, 0)
        
        return min([answer for answer in answers if len(answer) == len(max(answers, key = len))]) 
        
    """

