def tt(prefix):
	tochk = {}
	sol = {}
	for utime in range(5):
		for hexTimes in range(5):
			for btimes in range(5):
				for chkflag in b'abcdef0123456789':
					for chk in b'abcdef0123456789':
						q = flag[:prefix]+bytes([chkflag])+flag[prefix+1:]
						t = q[:prefix]+bytes([chk])
						for _ in range(utime):
							t = urlenc(t).encode()
							q = urlenc(q).encode()
						for _ in range(btimes):
							q = base64.b64encode(q)
							t = base64.b64encode(t)
						for _ in range(hexTimes):
							q = q.hex().encode()
							t = t.hex().encode()

						if(q[:72] == t[:72]):
							qw = q[:prefix]+bytes([chk])
							qw = qw.decode()
							ww = t[:72]

							if(ww not in tochk):
								if(chkflag == chk):
									tochk[ww] = qw
									sol[ww] = (hexTimes,btimes,utime)
								else:
									tochk[ww] = False
									sol[ww] = False
							else:
								tochk[ww] = False
								sol[ww] = False
	z = {}
	for k in tochk:
		if(tochk[k] and tochk[k] not in z):
			z[tochk[k][-1:]] = sol[k]
	return z


# def tt2(prefix):
# 	tochk = {}
# 	sol = {}
# 	for utime in range(7):
# 		for hexTimes in range(7):
# 			for btimes in range(3):
# 				for chkflag in b'abcdef0123456789':
# 					for chk in b'abcdef0123456789':
# 						q = flag[:prefix]+bytes([chkflag])+flag[prefix+1:]
# 						t = q[:prefix]+bytes([chk])
# 						for _ in range(btimes):
# 							q = base64.b64encode(q)
# 							t = base64.b64encode(t)
# 						for _ in range(hexTimes):
# 							q = q.hex().encode()
# 							t = t.hex().encode()
# 						for _ in range(utime):
# 							t = urlenc(t).encode()
# 							q = urlenc(q).encode()

# 						if(q[:72] == t[:72]):
# 							qw = q[:prefix]+bytes([chk])
# 							qw = qw.decode()
# 							ww = t[:72]

# 							if(ww not in tochk):
# 								if(chkflag == chk):
# 									tochk[ww] = qw
# 									sol[ww] = (hexTimes,btimes,utime)
# 								else:
# 									tochk[ww] = False
# 									sol[ww] = False
# 							else:
# 								tochk[ww] = False
# 								sol[ww] = False
# 	z = {}
# 	for k in tochk:
# 		if(tochk[k] and tochk[k] not in z):
# 			z[tochk[k][-1:]] = sol[k]
# 	return z
