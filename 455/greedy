class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # we sort each array at the first
        g.sort()
        s.sort()
        
        g_pointer = 0
        total_children = len(g)
        total_happy_child = 0
        
        # iterate cookies array, as long as the greedy actor of child is satified, the child pointer 
        # shifts to the next
        for s_item in s:    
            if g_pointer <= total_children - 1:     
                if s_item >= g[g_pointer]:
                    g_pointer += 1
                    total_happy_child += 1
                else:
                    continue
        
        return total_happy_child
