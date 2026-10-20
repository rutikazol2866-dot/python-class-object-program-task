class mall:
    def __init__(self,n,s,c,l,f):
        self.name = n
        self.shop = s
        self.city = c
        self.location = l
        self.floors = f

m1 = mall("phonix mall", 20, "pune", "viman nagar", 5)        
m2 = mall("amanora mall", 100,"pune", "hadasar", 14)
m3 = mall("season mall", 120, "pune", "hadpsar", 6)
m4 = mall("city mall", 40, "mumbai", "andheri", 3)
m5 = mall("westent mall", 70, "pune", "aundh", 2)

print(m1.name)
print(m1.shop)
print(m1.city)
print(m1.location)
print(m1.floors)

mall_list = []
m2 = mall("amanora mall", 100,"pune", "hadasar", 14)
mall_list.append(m2)

for mall in mall_list:
    print(m2.name,m2.city,m2.floors)