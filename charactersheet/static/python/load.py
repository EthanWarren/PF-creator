def loadsheet(data) :
    ds=data.replace("{","").replace("}","")
    dl=ds.split(",")
    data={}
    for kv in dl :
        k,v=kv.split(":")
        k=k.strip("'").replace("'","")
        v=v.strip("'").replace("'","")
        data[k]=v
    for loadid,loadvalue in data.items() :
        document.getElementById(loadid).value=loadvalue
window.loadsheet=loadsheet
loadsheet({})