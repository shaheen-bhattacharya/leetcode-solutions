class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left = maxWidth
        lines = []
        curr = []
        for word in words:
            if len(word) <= left:
                if len(word) + 1 <= left:
                    curr.append(word + " ")
                    left += len(word) + 1
                else:
                    curr.append(word)
                    left += len(word)
            else:
                mod = len(curr) - 1
                if len(curr) == 1:
                    mod = len(curr)
                if curr[-1][-1] == " ":
                    curr[-1] = curr[-1][:-1]
                    left += 1
                j = 0
                while left > 0:
                    curr[j % mod] += " "
                    left -= 1
                    j += 1
                lines.append("".join(curr))
                curr = []
                left = maxWidth
        return lines





