class balok(object):
    def __init__(self,p=1,l=1,t=1):
        self.p = p
        self.l = l
        self.t = t
    def luas(self):
        lu = 2*((self.p*self.l)+(self.p*self.t)+(self.l*self.t))
        return lu
    def vol(self):
        v = self.p * self.l * self.t
        return v
pp = int(input('panjang : '))
ll = int(input('lebar : '))
tt = int(input('tinggi : '))
a = balok(pp,ll,tt)
ll = a.luas()
vv = a.vol()
print(ll,vv)

