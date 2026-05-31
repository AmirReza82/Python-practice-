
# menu  ghaza

fehrest = ['ghorme' , 'ghemeh' , 'pasta' , 'abgosht' ]
f = "ghazaeh mord alagheh man " + fehrest[3]
print(f)

# azafeh kardan be menu

print("azafeh kardan ghazaeh bishtar")
fehrest.append('makaroni')
fehrest.append('kabab')
fehrest.append('kaleh pacheh')
print(fehrest)
fehrest.insert(0 , 'jigar')
fehrest.insert(5 , 'ash reshteh')
print(fehrest)

# tagheer dadan menu

fehrest[3] = 'kotlet'
print(fehrest)

# hazf ghaza az menu

del fehrest[3]
print(fehrest)
az = fehrest.pop()
print(az + " tamam shod")
fehrest.remove('kabab')
print(fehrest)

# moratab kardan menu

fehrest.sort()
print(fehrest)

# teadad ghzaeh menu
print(len(fehrest))




