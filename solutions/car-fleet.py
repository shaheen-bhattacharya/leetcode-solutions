class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n = len(position)
        items = [(position[i], speed[i], i) for i in range(n)]
        parent = [i for i in range(n)]
        items.sort()
        res = 0

        for i in range(n-2, -1, -1):
            pos, spd, idx = items[i]
            np, ns, nidx = items[parent[i+1]]
            if spd <= ns:
                res += 1
            else:
                time = (target - np)/ns
                if time < (target - pos)/spd:
                    res += 1
                    continue
                parent[i] = parent[i+1]
        return res+1





