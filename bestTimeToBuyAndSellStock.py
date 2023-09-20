class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        difference = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                difference = max(currentProfit, difference)
            else:
                left = right
            right += 1
        return difference


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 9, 5, 6, 3, 2]))
