
# ترازو دیجیتال
vazn = [24, 65 , 39 , 48 , 95 , 45]
m = []
for v in vazn:
    if  v <= 90:
        print("vazn ghabel mohasebeh ast")
        t = v / 9.81
        m.append(t)
    else:
        print("vazn bish az hade mogaz")
print(m)
for g in m:
    print(f" germ : {g} kg")


# میانگین
number = [40 , 90 , 'ap' , 10 , 'zero']
h = 0
number.remove('ap')
number[-1] = 0
q = len(number)
for f in number:
    if f != str(f):
        h += f
        v = h / q
    elif f != int(f):
        h += f
        v = h / q
print(v)






# جدول ضرب
for i in range(1,10):
    for a in range(1,10):
        zarb = i * a
print(zarb)