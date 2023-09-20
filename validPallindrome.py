# class Solution:
#     def isPallindrome(self, s: str) -> bool:
#       #two line O(n)
#       s = [i for i in s.lower() if i.isalnum()] #O(n)
#       return s == s[::-1] #O(n)

class Solution:
    def isPallindrome(self, s: str) -> bool:
        # O(1)
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i+1, j-1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPallindrome("A man, a plan, a canal: Panama"))
