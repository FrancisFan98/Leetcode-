class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        maxnum = 0
        curnum = 0
        mid = 0
        fruit = []
                
        for i in range(len(tree)):
            
            if len(fruit) < 2:
                if tree[i] not in fruit:
                    fruit.append(tree[i])
                curnum += 1
                maxnum = curnum
                mid = i
                continue
            
            if tree[i] != tree[i-1] and tree[i] in fruit:
                mid = i 
                curnum += 1
            elif tree[i] in fruit and tree[i] == tree[i-1]:
                curnum += 1
                
            else:                   #not in the list
                maxnum = max(maxnum, curnum)
                curnum = i - mid + 1
                mid = i
                fruit = [tree[i-1], tree[i]]
                fruit.append(tree[i])
        
            

        maxnum = max(curnum, maxnum)
        
        return maxnum
            
            
                
