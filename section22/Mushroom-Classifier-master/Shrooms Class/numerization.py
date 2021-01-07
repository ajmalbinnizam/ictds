#shrooms
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.inf)

shrooms = pd.read_csv('mushrooms.csv')

train_labels = np.zeros([6500, 2], dtype = int)
test_labels  = np.zeros([1624, 2], dtype = int)

train_data = np.zeros([6500, 22], dtype = int)
test_data = np.zeros([1624, 22], dtype = int)

#labels
labels = shrooms['class']
for index, item in enumerate(labels):
	if index <= 6499:
		if item == 'p':
			train_labels[index][0] = 1
		elif item == 'e':
			train_labels[index][1] = 1	
	if index > 6499:
		if item == 'p':
			test_labels[index - 6500][0] = 1
		elif item == 'e':
			test_labels[index - 6500][1] = 1

def numerize(discriminator, my_list, my_index):
	for index, item in enumerate(my_list):
		for i, letter in enumerate(discriminator):
			if index <= 6499:
				if item == letter:
					train_data[index][my_index] = i
			if index > 6499:
				if item == letter:	
					test_data[index - 6500][my_index] = i

#Data
#cap shape
cap_shape = shrooms['cap-shape']
a = ['b','c','x','f','k','s']
numerize(a, cap_shape, 0)

#cap surface				
cap_surface = shrooms['cap-surface']
b = ['f','g','y','s']
numerize(b, cap_surface, 1)

#cap color
cap_color = shrooms['cap-color']
c = ['n','b','c','g','r','p','u','e','w','y']
numerize(c, cap_color, 2)

#bruises
bruises = shrooms['bruises']
for index, item in enumerate(bruises):
	if index <= 6499:
		if item == 't':
			train_data[index][3] = 0
		elif item == 'f':
			train_data[index][3] = 1	
	if index > 6499:
		if item == 't':
			test_data[index - 6500][3] = 0
		elif item == 'f':	
			test_data[index - 6500][3] = 1

#odor
odor = shrooms['odor']
d = ['a','l','c','y','f','m','n','p','s']							
numerize(d, odor, 4)

#gill_attachment
gill_attachment = shrooms['gill-attachment']				
e = ['a','d','f','n']							
numerize(e, gill_attachment, 5)

#gill spacing
gill_spacing = shrooms['gill-spacing']			
f = ['c','w','d']	
numerize(f, gill_spacing, 6)

#gill-size				
gill_size = shrooms['gill-size']
for index, item in enumerate(gill_size):
	if index <= 6499:
		if item == 'b':
			train_data[index][7] = 0
		elif item == 'n':
			train_data[index][7] = 1	
	if index > 6499:
		if item == 'b':
			test_data[index - 6500][7] = 0
		elif item == 'n':	
			test_data[index - 6500][7] = 1

#gill-color
gill_color = shrooms['gill-color']
g = ['k','n','b','h','g','r','o','p','u','e','w','y']							
numerize(g, gill_color, 8)	

#stalk shape
stalk_shape = shrooms['stalk-shape']					
for index, item in enumerate(stalk_shape):
	if index <= 6499:
		if item == 'e':
			train_data[index][9] = 0
		elif item == 't':
			train_data[index][9] = 1
	if index > 6499:
		if item == 'e':
			test_data[index - 6500][9] = 0
		elif item == 't':	
			test_data[index - 6500][9] = 1

#stalk-root
stalk_root = shrooms['stalk-root']
h = ['b','c','u','e','z','r','?']	
numerize(h, stalk_root, 10)	

#stalk-surface-above-ring
ssar = shrooms['stalk-surface-above-ring']
i = ['f','y','k','s']	
numerize(i, ssar, 11)

#stalk-surface-below-ring
ssbr = shrooms['stalk-surface-below-ring']
numerize(i, ssbr, 12)

#stalk-color-above-ring
scar = shrooms['stalk-color-above-ring']
j = ['n','b','c','g','o','p','e','w','y']	
numerize(j, scar, 13)

#stalk-color-below-ring
scbr = shrooms['stalk-color-below-ring']	
numerize(j, scbr, 14)

#veil-type
vt = shrooms['veil-type']
k = ['p', 'u']
numerize(k, vt, 15)

#veil-color
vc = shrooms['veil-color']
l = ['n','o','w','y']
numerize(l, vc, 16)

#ring-number
rn = shrooms['ring-number']
m = ['n','o','t']
numerize(m, rn, 17)

#ring-type
rt = shrooms['ring-type']
n = ['c','e','f','l','n','p','s','z']
numerize(n, rt, 18)

#spore-print-color
spc = shrooms['spore-print-color']
o = ['k','n','b','h','r','o','u','w','y']
numerize(o, spc, 19)

#population
pop = shrooms['population']
p = ['a','c','n','s','v','y']
numerize(p, pop, 20)

#habitat
hab = shrooms['habitat']
q = ['g','l','m','p','u','w','d']
numerize(q, hab, 21)


print(train_data)

'''
np.savetxt('M_Train_data.txt', train_data)
np.savetxt('M_Train_labels.txt', train_labels)
np.savetxt('M_Test_data.txt', test_data)
np.savetxt('M_Test_labels.txt', test_labels)
'''