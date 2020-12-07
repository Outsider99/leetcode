class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i]==0:
                flowerbed[i] = 1
                x += 1
        if x >= n:
            return True
        else:
            return False
