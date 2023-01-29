def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        sumx=0
        for i in asteroids:
            if mass+sumx>=i:
                sumx+=i
            else:
                return False
        return True