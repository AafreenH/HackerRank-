n = input().split()
b = int(n[0])
kb = list(map(int,input().rstrip().split()))
usb = list(map(int,input().rstrip().split()))
x = len(kb)
y = len(usb)
res = []
if min(kb) + min(usb) > b:
	res1 = -1
else:
	for i in range(x):
		for j in range(y):
			cost = kb[i] + usb[j]
			if cost < b:
				res.append(cost)
print(max(res))


