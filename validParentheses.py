class Solution(object):
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    valid = Solution()
    print(valid.isValid('(]'))
