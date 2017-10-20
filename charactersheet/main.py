import bottle,random,glob,os
def calc_roll(dice) :
    try :
        num,sides=dice.split("d")
        if not num :
            num=1
        num=int(num)
    except :
        return "invalid"
    if "+" in sides :
        addnum=int(sides.split("+")[1])
        sides=int(sides.split("+")[0])
    else :
        sides=int(sides)
        addnum=0
    dicelist=[]
    for i in range(num) :
        dicelist.append(random.randint(1,sides))
    return sum(dicelist)+addnum
@bottle.route("/")
@bottle.route("/index")
def index() :
    return bottle.template("templates/index.tpl",title="Home")
@bottle.route("/dice",method="GET")
def dice() :
    return bottle.template("templates/dice.tpl",roll="")
@bottle.route("/dice",method="POST")
def dice() :
    return bottle.template("templates/dice.tpl",roll=calc_roll(bottle.request.POST.dice))
@bottle.route("/charactersheet")
def charactersheet() :
    global sheets
    sheets={}
    for filename in glob.glob("sheets/*.txt") :
        f=open(filename,"r+")
        sheets[filename.split("/")[1].split(".")[0]]={}
        for id in f.readlines() :
            if len(id.split(":")) < 2 :
                continue
            else :
                sheets[filename.split("/")[1].split(".")[0]][id.split(":")[0].strip()]=id.split(":")[1].strip()
        f.close()
    return bottle.template("templates/charactersheet.tpl",data=sheets)
@bottle.route("/js/<filename>")
def js(filename) :
    return bottle.static_file(filename,"./static/js/")
@bottle.route("/save/<name>",method="POST")
def save(name) :
    data=bottle.request.json
    f=open("sheets/{}.txt".format(name),"w")
    datastr=""
    for id in data.keys() :
        datastr=datastr+"{}:{}\n".format(id,data[id])
    datastr.strip()
    f.write(datastr)
    f.close()
@bottle.route("/charactersheet",method="POST")
def delete() :
    os.system("rm \"sheets/{}.txt\"".format(bottle.request.POST.delname))
    return bottle.template("templates/charactersheet.tpl",data=sheets)
bottle.debug(True)
bottle.run(host="192.168.0.200",port=80)