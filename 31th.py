at = ('fire', 99, 12.88)
print(at)

print('at[0] =', at[0])
print('at[1] =', at[1])
print('at[2] =', at[2])
#print('at[3] =', at[3]) #index out of range

t1 = ('hello', 998, 12.88)
t2 = (77, 62, 44, 81)
t3 = t1 + t2
print('t3 =', t3)

print('-'*10 + 'After Deleting t3' + '-'*10)
del t3
#print('t3 =', t3)

t4 = t1 + t2
print(len(t4))
print(t1*3)
print(77 in t2)
print(78 in t2)

print('-'*10+'Traverse the tuple t4'+'-'*10)
for x in t4:
	print('item =', x)


print('-'*10+'index of the tuple t4'+'-'*10)
print(t4)
print(t4[0])
print(t4[-2])
print(t4[3:])

print('-'*10+'build-in function of tuple'+'-'*10)
#print(cmp(t1, t2))
print(len(t4))
print(max(t2))
print(min(t2))
arr = [12.88, 99, 76, 43]
print(arr)
print(tuple(arr))


print('-'*10+'multi-dimension tuple'+'-'*10)
t3 = (19, 22.8, 9.58, 1988)
t4 = (t1, t2, t3)
print('t4 =',t4)
print('t4[2] =', t4[2])
print('t4[0][0] =', t4[0][0])
print('t4[2][3] =', t4[2][3])
