import numpy as np
import random

r_l = [40, 80]
the_l = range(0, 300, 60)
mb = 42.5
k = 0
n = 0
d_l = [145, 400]

staticdyn = input("Static or Dynamic? ")
nm = int(input("number of masses: "))

def loc_choice(nm, the_l, r_l, d_l):
    the = {}
    r = {}
    m = {}
    d = {}
    wash = [5.62, 5.67, 5.81, 6.02, 6.03, 6.07, 6.1, 6.28, 6.33, 6.43, 6.73,
            7, 7.13, 7.19, 7.24, 7.57, 7.64, 7.68, 7.69, 7.73, 8.03, 8.24, 8.27,
            8.3]
    for i in range(nm):
        l = i + 1
        the_name = "the%d" % l
        r_name = "r%d" % l
        m_name = "m%d" % l
        d_name = "d%d" % l

        the[the_name] = random.choice(the_l)
        r[r_name] = random.choice(r_l)
        w = random.choice(wash)
        m[m_name] = mb + w
        wash.remove(w)
        d[d_name] = random.choice(d_l)

    the = list(the.values())
    r = list(r.values())
    m = list(m.values())
    d = list(d.values())
    return the, r, m, d

        

if staticdyn.upper() == "STATIC":
    while k < 10:
        v = 0
        h = 0
        the, r, m, d = loc_choice(nm, the_l, r_l, d_l)
        for i in range(nm):
            v += m[i]*r[i]*np.sin(the[i]*(np.pi/180))
            h += m[i]*r[i]*np.cos(the[i]*(np.pi/180))

        if (v < 1 and v > -1) and (h < 1 and h > -1):
            print(v, h)
            for i in range(nm):
                print(m[i])
                print(r[i])
                print(the[i])
            k += 1

elif staticdyn.upper() == "DYNAMIC":
    while k < 10:
        v = 0
        h = 0
        the, r, m, d = loc_choice(nm, the_l, r_l, d_l)
        for i in range(nm):
            v += m[i]*r[i]*d[i]*np.sin(the[i]*(np.pi/180))
            h += m[i]*r[i]*d[i]*np.cos(the[i]*(np.pi/180))

        if (v < 1 and v > -1) and (h < 1 and h > -1):
            print(v, h)
            for i in range(nm):
                print(m[i])
                print(r[i])
                print(the[i])
                print(d[i])
            k += 1

