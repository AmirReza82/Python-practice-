

# tamrin 1
adad = [10,20,30,40,50]
print(f"tol barabr ast ba : {len(adad)}")
print(f"kochek tarin : {min(adad)}")
print(f"bozorg tarin : {max(adad)}")

# tamrin 2
print(30 in adad)

# tamrin 3
adad2 = [15,25,45,15,30,65,45,75,65]
print(sorted(set(adad2)))

# tamrin 4
print(adad[1:4])

# tamrin 5
student = ['amir', ' matin ' , 'mahan' , 'ali' , 'reza']
for i in student:
    print(f"salam khely khosh amadi {i.title()}")
    print("mofagh bashi " + i.title() + "\n")
print("bye")

# tamrin 6
# ravesh tolani
tavan3 = []
for i in range(1,11):
    t = i ** 3
    tavan3.append(t)
print(f"tavan3 : {tavan3}")

# ravesh kotah
taa = [va ** 3 for va in range(1,11)]
print(f"tavan 3 :{taa}")

# tamrin 7

print(sum(adad))


# tamrin 8

tavan2 = [tav ** 2 for tav in range(1,21)]
print(tavan2)

# tamrin 9
print(f"aadad zoj: {list(range(2,51,2))}")