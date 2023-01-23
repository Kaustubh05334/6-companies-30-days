def totalFruit(self, fruit: list[int]) -> int: 
        l = i = 0
        m = 0    
        basket = [-1,-1]                    
        
        for r in range(len(fruit)):           
            if fruit[r] != basket[1]:    
                if fruit[r] != basket[0]:
                    l = i
                i = r
                basket[0], basket[1] = basket[1], fruit[r]
            m = max(m, r - l + 1)

        return m