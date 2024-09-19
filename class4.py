#dict or {key:value}
#empty dict = {}

g={'car':'bmw','bike':'hero','num':2,'mark':[56,98,45]}

print(g.keys())
print(g.values())
print(g.items())

print(g['bike'])

g['mark'][2]=23
print(g)

print(g.get('bike'))

g.update({'stud':['raj','ashin','raja']})
