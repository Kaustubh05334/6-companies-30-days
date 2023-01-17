class Solution:
    def find_lowest_price(self, price, special, needs):
        if tuple(needs) in self.dp:
            return self.dp[tuple(needs)]
        cost = 0
        for i, need in enumerate(needs):
            cost += need * price[i]
        for offer in special:
            for i, need in enumerate(needs):
                if need < offer[i]:
                    break
            else:
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                # Update cost
                cost = min(cost, offer[-1] + self.find_lowest_price(price, special, new_needs))
        self.dp[tuple(needs)] = cost
        return cost
        
    def shoppingOffers(self, price, special, needs):
        self.dp = {}
        return self.find_lowest_price(price, special, needs)