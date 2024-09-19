#dictionary
d={'id':[101,102,103],'name':['john','mark','steeve'],'age':[23,24,25],}


print(d.keys())
print(d.values())
print(d.items())
print(d)


d.update({'name':['praveen','steeve','ram)']})
d.update({'id':[101,201,301]})

print(d)
print(d['id'])
print(d['name'])
print(d['age'])

