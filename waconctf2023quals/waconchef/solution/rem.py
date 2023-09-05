import base64
import random

def urlenc(v):
	s = ''
	for i in v:
		s += '%'+hex(i)[2:]
	return s
flag = b'abcef0123456789'

def nnn(prefix):
	defs = [
		lambda x:x.hex().encode(),
		lambda x:base64.b64encode(x),
		lambda x:urlenc(x).encode(),
		lambda x:base64.b32encode(x),
		lambda x:x,
	]
	totry = []
	for _ in range(random.randint(5,7)):
		totry.append(random.choice(defs))

	tochk = {}
	for chkflag in b'abcdef0123456789':
		for chk in b'abcdef0123456789':
			q = flag[:prefix]+bytes([chkflag])+flag[prefix+1:]+b'XX'
			t = q[:prefix]+bytes([chk])
			for z in totry:
				q = z(q)
				t = z(t)
			if(q[:72] == t[:72]):
				# isgood = True
				# for ewrwer in b'abcdef0123456789':
				# 	q2 = flag[:prefix]+bytes([chkflag])+flag[prefix+1:]+bytes([ewrwer])
				# 	t2 = q2[:prefix]+bytes([chk])
				# 	for z in totry:
				# 		q2 = z(q2)
				# 		t2 = z(t2)
				# 	if(q2[:72] != t[:72]):
				# 		isgood = False
				# 		break
				# if(not isgood):
				# 	continue
				qw = q[:prefix]+bytes([chk])
				qw = qw.decode()
				ww = t[:72]

				if(ww not in tochk):
					if(chkflag == chk):
						tochk[ww] = qw
					else:
						tochk[ww] = False
				else:
					tochk[ww] = False
	if(len(tochk) >= 16):
		dd = []
		for i in totry:
			dd.append(defs.index(i))
		return dd
	return False
q = []
for er in range(10,16):
	g = 0
	while(True):
		z = nnn(er)
		if(z):
			q.append(z)
			print(z)
			break
print(q)

# [0, 4, 2, 1, 2, 2]
# [3, 0, 2, 0, 4, 3]
# [0, 4, 2, 0, 0, 4]
# [0, 1, 1, 3, 2]
# [1, 1, 1, 0, 2]
# [4, 2, 2, 4, 1]
# [2, 4, 1, 3, 4, 3]
# [3, 2, 1, 4, 1, 4]
# [1, 4, 4, 2, 0]
# [4, 1, 1, 2, 1]
# [1, 2, 3, 4, 4, 4]
# [4, 4, 0, 2, 4]