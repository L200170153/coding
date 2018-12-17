class Person(object):
    # Define the class parameter "name"
    name = "Person"
    age = 'age'
    p = 0
    l= 0
    def __init__(self, name = 'john doe', age = 3.14, p=0, l=0):
        # jika tidak diisi maka isinya adalah default pada diatas
        # self.name is the instance parameter
        self.name = name
        self.age = age
        self.p = p
        self.l = l
    def luas(self):
        pp = self.p
        ll = self.l
        l = pp * ll

j = Person() #mengganti person() dengan j, agar mudah saat memanggil class tsb
j.name = "Jeffrey" #memanggil class dengan var name
j.age = 20 #memanggil class dengan var age

print("{} name is {} {} years old".format(Person.name, j.name, j.age))
pw = int(input('p :'))
lw = int(input('l :'))
a = Person(pw,lw)
lu = a.luas()

print(lu)


