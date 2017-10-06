import bottle,random
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
    return bottle.static_file("charactersheet.html","./static")
@bottle.route("/js/<filename>")
def js(filename) :
    return bottle.static_file(filename,"./static/js/")
bottle.debug(True)
bottle.run(host="",port=80,server=bottle.PasteServer)