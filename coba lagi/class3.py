class kotak(object):
    def __init__(self,p,l):
        self.p=p
        self.l=l
    def luas(self):
        l = self.p * self.l
        return l
    def kel(self):
        k = 2*(self.p+self.l)
        return k
pp = int(input('panjang : '))
ll = int(input('lebar : '))
ko = kotak(pp,ll)
print(ko.luas(),ko.kel())
