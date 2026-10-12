class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        #tree[node] = number of heihgts in range(l, r)
        #7, 7, 6, 5, 4
        """
        [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
        """
        # people.sort(key = lambda x: (-x[0], x[1]))
        people.sort()

        print(people)
        n = len(people)
        q = deque()
        res = []
        for i in range(n):
            p = people[i]
            # if p[1] == 
        return res

            

