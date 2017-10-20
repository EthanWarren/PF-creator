import barbarian,bard,cleric,druid,fighter,monk,paladin,ranger,rogue,sorcerer,wizard,skills
classes={"barbarian":barbarian,"bard":bard,"cleric":cleric,"druid":druid,"fighter":fighter,"monk":monk,"paladin":paladin,"ranger":ranger,"rogue":rogue,"sorcerer":sorcerer,"wizard":wizard}
def calc_size() :
    race=document.getElementById("race").value
    if race in ["elf","dwarf","human","halfelf","half elf","halforc","half orc"] :
        document.getElementById("size").value="medium"
    elif race in ["halfling","gnome"] :
        document.getElementById("size").value="small"
def calc_hp() :
    charclass=document.getElementById("class").value
    level=int(document.getElementById("level").value)
    document.getElementById("maxhp").value=str(classes[charclass].table["hp"]+(level-1)*classes[charclass].table["hp"]/2+int(document.getElementById("conmod").value)*level+int(document.getElementById("hpothermods1").value)+int(document.getElementById("hpothermods2").value)*level)
def calc_fort() :
    document.getElementById("fortclassmod").value=str(classes[document.getElementById("class").value].table[int(document.getElementById("level").value)]["fort"])
    document.getElementById("fortconmod").value=document.getElementById("conmod").value
    document.getElementById("fortsave").value=str(int(document.getElementById("fortclassmod").value)+int(document.getElementById("fortconmod").value)+int(document.getElementById("fortothermod1").value)+int(document.getElementById("fortothermod2").value))
def calc_ref() :
    document.getElementById("refclassmod").value=str(classes[document.getElementById("class").value].table[int(document.getElementById("level").value)]["ref"])
    document.getElementById("refdexmod").value=document.getElementById("dexmod").value
    document.getElementById("refsave").value=str(int(document.getElementById("refclassmod").value)+int(document.getElementById("refdexmod").value)+int(document.getElementById("refothermod1").value)+int(document.getElementById("refothermod2").value))
def calc_will() :
    document.getElementById("willclassmod").value=str(classes[document.getElementById("class").value].table[int(document.getElementById("level").value)]["will"])
    document.getElementById("willwismod").value=document.getElementById("wismod").value
    document.getElementById("willsave").value=str(int(document.getElementById("willclassmod").value)+int(document.getElementById("willwismod").value)+int(document.getElementById("willothermod1").value)+int(document.getElementById("willothermod2").value))
def calc_bab() :
    charclass=document.getElementById("class").value
    level=int(document.getElementById("level").value)
    document.getElementById("bab").value=str(classes[charclass].table[level]["bab"])
def calc_scores() :
    strscore=int(document.getElementById("strscore").value)
    dexscore=int(document.getElementById("dexscore").value)
    conscore=int(document.getElementById("conscore").value)
    intscore=int(document.getElementById("intscore").value)
    wisscore=int(document.getElementById("wisscore").value)
    chascore=int(document.getElementById("chascore").value)
    document.getElementById("strmod").value=str(Math.floor((strscore-10)/2))
    document.getElementById("dexmod").value=str(Math.floor((dexscore-10)/2))
    document.getElementById("conmod").value=str(Math.floor((conscore-10)/2))
    document.getElementById("intmod").value=str(Math.floor((intscore-10)/2))
    document.getElementById("wismod").value=str(Math.floor((wisscore-10)/2))
    document.getElementById("chamod").value=str(Math.floor((chascore-10)/2))
def calc_cmb() :
    document.getElementById("cmbbab").value=document.getElementById("bab").value
    document.getElementById("cmbstrmod").value=document.getElementById("strmod").value
    if document.getElementById("size").value == "medium" :
        document.getElementById("cmbsizemod").value="0"
    elif document.getElementById("size").value == "small" :
        document.getElementById("cmbsizemod").value="-1"
    document.getElementById("cmb").value=str(int(document.getElementById("cmbbab").value)+int(document.getElementById("cmbstrmod").value)+int(document.getElementById("cmbsizemod").value)+int(document.getElementById("cmbothermods").value))
def calc_cmd() :
    document.getElementById("cmdbab").value=document.getElementById("bab").value
    document.getElementById("cmdstrmod").value=document.getElementById("strmod").value
    document.getElementById("cmddexmod").value=document.getElementById("dexmod").value
    if document.getElementById("size").value == "medium" :
        document.getElementById("cmdsizemod").value="0"
    elif document.getElementById("size").value == "small" :
        document.getElementById("cmdsizemod").value="-1"
    document.getElementById("cmd").value=str(int(document.getElementById("cmdbab").value)+int(document.getElementById("cmdstrmod").value)+int(document.getElementById("cmddexmod").value)+int(document.getElementById("cmdsizemod").value)+int(document.getElementById("cmdothermods").value)+10)
def calc_melee() :
    size=document.getElementById("size").value
    document.getElementById("meleebab").value=document.getElementById("bab").value
    document.getElementById("meleestrmod").value=document.getElementById("strmod").value
    if size == "medium" :
        document.getElementById("meleesizemod").value="0"
    elif size == "small" :
        document.getElementById("meleesizemod").value="1"
    document.getElementById("melee").value=str(int(document.getElementById("meleebab").value)+int(document.getElementById("meleestrmod").value)+int(document.getElementById("meleesizemod").value)+int(document.getElementById("meleeothermods").value))
def calc_ranged() :
    size=document.getElementById("size").value
    document.getElementById("rangedbab").value=document.getElementById("bab").value
    document.getElementById("rangeddexmod").value=document.getElementById("dexmod").value
    if size == "medium" :
        document.getElementById("rangedsizemod").value="0"
    elif size == "small" :
        document.getElementById("rangedsizemod").value="1"
    document.getElementById("ranged").value=str(int(document.getElementById("rangedbab").value)+int(document.getElementById("rangeddexmod").value)+int(document.getElementById("rangedsizemod").value)+int(document.getElementById("rangedothermods").value))
def calc_skills() :
    for skill in skills.list.keys() :
        document.getElementById("{}{}mod".format(skill,skills.list[skill])).value=document.getElementById("{}mod".format(skills.list[skill])).value
        document.getElementById("{}".format(skill)).value=str(int(document.getElementById("{}ranksmod".format(skill)).value)+int(document.getElementById("{}{}mod".format(skill,skills.list[skill])).value)+int(document.getElementById("{}othermods".format(skill)).value))
    if document.getElementById("size").value == "small" :
        document.getElementById("stealthothermods").value="4"
def calc_race() :
    race=document.getElementById("race").value
    raceinfo=document.getElementById("raceinfo")
    if race == "human" :
        raceinfo.innerHTML="+2 any one ability score"
    elif race == "half elf" :
        raceinfo.innerHTML="+2 any one ability score"
        document.getElementById("perceptionothermods").value="2"
    elif race == "half orc" :
        raceinfo.innerHTML="+2 any one ability score"
        document.getElementById("intimidateothermods").value="2"
    elif race == "halfling" :
        raceinfo.innerHTML="+2dex,+2cha,-2 str"
        document.getElementById("fortothermod1").value="1"
        document.getElementById("refothermod1").value="1"
        document.getElementById("willothermod1").value="1"
        document.getElementById("perceptionothermods").value="2"
        document.getElementById("climbothermods").value="2"
        document.getElementById("acrobaticsothermods").value="2"
    elif race == "gnome" :
        raceinfo.innerHTML="+2cha,+2 con,-2 str"
        document.getElementById("perceptionothermods").value="2"
    elif race == "elf" :
        raceinfo.innerHTML="+2 int, +2 dex, -2 con"
        document.getElementById("perceptionothermods").value="2"
    elif race == "dwarf" :
        raceinfo.innerHTML="+2 con, +2 wis, -2 cha"
def calc_init() :
    document.getElementById("initdexmod").value=document.getElementById("dexmod").value
    document.getElementById("init").value=str(int(document.getElementById("initdexmod").value)+int(document.getElementById("initothermods").value))
def calc_speed() :
    race=document.getElementById("race").value
    if race in ["gnome","halfling","dwarf"] :
        document.getElementById("ls").value="20"
    else :
        document.getElementById("ls").value="30"
def calc_ac() :
    document.getElementById("acbonus").value=str(int(document.getElementById("armourbonus").value)+int(document.getElementById("shieldbonus").value)+int(document.getElementById("acb1").value)+int(document.getElementById("acb2").value)+int(document.getElementById("acb3").value)+int(document.getElementById("acb4").value))
    if int(document.getElementById("dexmod").value) > int(document.getElementById("armourmaxdex").value) :
        document.getElementById("acdexmod").value=document.getElementById("armourmaxdex").value
    else :
        document.getElementById("acdexmod").value=document.getElementById("dexmod").value
    if document.getElementById("size").value == "small" :
        document.getElementById("acsizemod").value="1"
    elif document.getElementById("size").value == "medium" :
        document.getElementById("acsizemod").value="0"
    document.getElementById("ac").value=str(int(document.getElementById("acbonus").value)+int(document.getElementById("acdexmod").value)+int(document.getElementById("acsizemod").value)+int(document.getElementById("acothermods").value)+10)
def calc_languages() :
    languagestr=""
    race=document.getElementById("race").value
    if race == "human" :
        languagestr="common"
    elif race == "half elf" :
        languagestr="common elven"
    elif race == "half orc" :
        languagestr="common orc"
    elif race == "dwarf" :
        languagestr="common dwarven"
    elif race == "elf" :
        languagestr="common elven"
    elif race == "gnome" :
        languagestr="common gnome"
    elif race == "halfling" :
        languagestr="common halfling"
    document.getElementById("languages").innerHTML=languagestr
calc_race()
calc_size() 
calc_scores()
calc_hp()
calc_fort()
calc_ref()
calc_will()
calc_ac()
calc_init()
calc_speed()
calc_bab()
calc_cmb()
calc_cmd()
calc_melee()
calc_ranged()
calc_skills()
calc_languages()
document.getElementById("currenthp").value=document.getElementById("maxhp").value
setInterval(calc_race,3000)
setInterval(calc_size,3000)
setInterval(calc_scores,3000)
setInterval(calc_hp,3000)
setInterval(calc_fort,3000)
setInterval(calc_ref,3000)
setInterval(calc_will,3000)
setInterval(calc_ac,3000)
setInterval(calc_init,3000)
setInterval(calc_speed,3000)
setInterval(calc_bab,3000)
setInterval(calc_cmb,3000)
setInterval(calc_cmd,3000)
setInterval(calc_melee,3000)
setInterval(calc_ranged,3000)
setInterval(calc_skills,3000)
setInterval(calc_languages,3000)