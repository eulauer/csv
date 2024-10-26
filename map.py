import numpy as N

file = '_CORR_M1Cid_ph.csv'

csv = N.genfromtxt(file,names=True,delimiter=',',dtype=None)

iso = N.array(csv['iso'],str)
ort = N.array(list(set(iso)),str)

print (ort)

f = open('map.csv','w')

f.write('country,NObs\n')

for i in ort:

    id = N.where(iso==i)[0]
    
    tmp = N.mean(csv['NObs'][id])

    f.write('%s,%.1f\n'%(i,tmp))

f.close()