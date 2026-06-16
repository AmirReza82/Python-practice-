# تمرین اول: ناوگان پهپاد ها

drones = [
    {
        'id': 1,
        'battery': 90 ,
        'status': 'idle',
    },
    {
        'id': 2,
        'battery': 25 ,
        'status': 'idle',
    }
]
c = 0
for drone in drones:
    if drone['status'] == 'idle':
        c = c + 1
print(f"ready pahpad : {c}")

p = 0
for dr in drones:
    p = p + dr['battery']
h = p / len(drones)
print(f"average battery level is {h}")


# تمرین دوم: ماموریت ماهواره
satellite = {
    's-1':{
        'altitude': 550,
        'targets': ['tehran' , 'paris' , 'berlin'],
    },
    's-2':{
        'altitude': 700,
        'targets': ['tokyo' , 'london'],
    }
}
#2_1
print(len(satellite['s-1']['targets']))
print(len(satellite['s-2']['targets']))


for d in satellite.values():
    mj = len(d['targets'])
    print(f"tedade targets : {mj}")
#2_2
m = len(satellite['s-1']['targets'])
n = len(satellite['s-2']['targets'])
print(f"jame targets : {m + n}")

t = 0
for q in satellite.values():
    lk = len(q['targets'])
    t = t + lk
print(f"majmo hame targets : {t}")

#2_3
maxx = 0
for hj,de in satellite.items():
    nbv = len(de['targets'])
    if nbv > maxx:
        maxx = nbv
        na = hj
print(f"satelite ba bishtarin targets : {na} , ba tadad {maxx} ")
#2_4
average = 0
for av in satellite.values():
    average = average + av['altitude']
he = average / len(satellite)
print(f"average altitude mahvare ha barabar ast ba  :{he}")

# نمرین سوم : کمپانی مهندسان

company = {
    'engineering':{
        'employees':[
            {'name': 'ali' , 'salary' : 3000},
            {'name': 'sara' , 'salary' : 3500},
    ]
},
    'ai': {
        'employees':[
            {'name': 'reza' , 'salary' : 5000},
       ]
    }
}
#3_1
for ho in company.values():
    hg = 0
    for emp in ho['employees']:
        hg = hg + emp['salary']
    print(f"hoghogh har bakhsh : {hg}")

#3_2
hgg = 0
for hoo in company.values():
    for empp in hoo['employees']:
        hgg = hgg + empp['salary']
print(f"hoghogh kol bakhsh : {hgg}")

#3_3
maxi = 0
for lh in company.values():
    for eu in lh['employees']:
        if eu['salary'] > maxi:
            maxi = eu['salary']
            kd = eu['name']
print(f"bishtarin hoghogh : {kd},{maxi}")

#3_4
for we in company.values():
    mi = 0
    for hg in we['employees']:
        mi = mi + hg['salary']
    gy = mi / len(we['employees'])
    print(f"average har bakhsh : {gy}")

#3_5
ms = 0
ta = 0
for ea in company.values():
    for lq in ea['employees']:
        ms = ms + lq['salary']
        ta = ta + 1
    io = ms / ta
print(f"hoghogh gy : {io}")













# تمرین چهارم: قروشگاه آنلاین

store = {
    'am': [
        {'name': 'laptop' , 'price' : 1200},
        {'name': 'moese' , 'price' : 50},
    ],
    'ap':[
        {'name': 'phone' , 'price' : 800},
        {'name': 'headphone' , 'price' : 100},
    ]


}