class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        # Build the tree
        tree = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(child)
        
        #Calculate size of each subtree
        subtree_sizes = [0] * len(parents)
        def calc_subtree_size(node):
            size = 1
            for child in tree[node]:
                size += calc_subtree_size(child)
            subtree_sizes[node] = size
            return size
        calc_subtree_size(0)

        # Calculate score of each node
        max_score = 0
        cnt = 0

        for i in range(len(parents)):
            score = 1
            remaining_size = len(parents) - subtree_sizes[i]

            for child in tree[i]:
                score *= subtree_sizes[child]
            
            if remaining_size > 0:
                score *= remaining_size
            
            if score > max_score:
                max_score = score
                cnt = 1
            elif score == max_score:
                cnt += 1
        
        return cnt

        
        