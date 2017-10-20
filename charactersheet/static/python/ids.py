import re
id=re.compile("id=\".*\"")
f=open("charactersheet.tpl","r+")
txt=f.read()
f.close()
elements=txt.split(">")
ids=[]
for element in elements :
    result=id.search(element)
    if result != None :
        ids.append(result.group())
ids2=[]
for id in ids :
    ids2.append(id.split("value")[0].strip())
ids=ids2
ids2=[]
for id in ids :
    ids2.append(id.split("=")[1])
ids=ids2
idstr="\n".join(ids)
idstr2=""
for char in idstr :
    if char != "\"" :
        idstr2=idstr2+char
idstr=idstr2
f=open("ids.txt","w")
f.write(idstr)
f.close()