class ling(object):
    def __init__(self,r):
        self.r = r
    def luas(self):
        
        l = 3.14 * self.r**2
        return l
    def kel(self):
        k = 3.14 * 2 * self.r
        return k
rad = int(input('input radius : '))
aling = ling(rad)
a = aling.luas()
b = aling.kel()
print(a, b)
