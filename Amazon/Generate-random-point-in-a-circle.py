import random
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.rad= radius
        self.x=x_center
        self.y=y_center
    def randPoint(self):
        while True:
            tempx = random.uniform(self.x - self.rad, self.x + self.rad)
            tempy = random.uniform(self.y - self.rad, self.y + self.rad)
            if (tempx - self.x) ** 2 + (tempy - self.y) ** 2 <= self.rad ** 2:
                return [tempx, tempy]