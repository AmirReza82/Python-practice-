
# tamrin list 1

mehmanan = ['ali ' ,'shayan' , 'matin']
print(mehmanan[0] + " khosh amadi")
print(mehmanan[1] + " khosh amadi")
print(mehmanan[2] + " khosh amadi")
mehmanan[1] = 'reza'
print(mehmanan[0] + " khosh amadi")
print(mehmanan[1] + " khosh amadi")
print(mehmanan[2] + " khosh amadi")
# tamrin list 2;

mehmanan.append('mohammad')
mehmanan.insert(0 , 'mahan')
mehmanan.insert(3 , 'sasan')
print(mehmanan)
print("ba arse sharmandegi  moshkel  kambode faza daram ")
m1 = mehmanan.pop()
print(m1 + " ba arse mazerat shoma davat nisti")
"""print(mehmanan)"""
m2 = mehmanan.pop()
print(m2 + " ba arse mazerat shoma davat nisti")
"""print(mehmanan)"""
m3 = mehmanan.pop()
print(m3 + " ba arse mazerat shoma davat nisti")
m4 = mehmanan.pop()
print(m4 + " ba arse mazerat shoma davat nisti")
print(mehmanan[0] + ","+ mehmanan[1] + "shoma davat hastid")
# tamrin list 3

del mehmanan[0]
del mehmanan[1]
print(mehmanan)