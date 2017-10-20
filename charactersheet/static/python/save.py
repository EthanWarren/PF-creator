__pragma__("alias","jq","$")
ids="""player
character
race
class
level
alignment
size
deity
description
strscore
strmod
dexscore
dexmod
conscore
conmod
intscore
intmod
wisscore
wismod
chascore
chamod
maxhp
currenthp
hpothermods1
hpothermods2
fortclassmod
fortconmod
fortothermod1
fortothermod2
fortsave
refclassmod
refdexmod
refothermod1
refothermod2
refsave
willclassmod
willwismod
willothermod1
willothermod2
willsave
acbonus
acdexmod
acsizemod
acothermods
ac
touchac
flatac
initdexmod
initothermods
init
ls
bs
ss
fs
bab
cmbbab
cmbstrmod
cmbsizemod
cmbothermods
cmb
cmdbab
cmdstrmod
cmddexmod
cmdsizemod
cmdothermods
cmd
meleebab
meleestrmod
meleesizemod
meleeothermods
melee
rangedbab
rangeddexmod
rangedsizemod
rangedothermods
ranged
acrobaticsranksmod
acrobaticsdexmod
acrobaticsothermods
acrobatics
apraiseranksmod
apraiseintmod
apraiseothermods
apraise
bluffranksmod
bluffchamod
bluffothermods
bluff
climbranksmod
climbstrmod
climbothermods
climb
craftranksmod
craftintmod
craftothermods
craft
diplomacyranksmod
diplomacychamod
diplomacyothermods
diplomacy
disable deviceranksmod
disable devicedexmod
disable deviceothermods
disable device
disguiseranksmod
disguisechamod
disguiseothermods
disguise
escape artistranksmod
escape artistdexmod
escape artistothermods
escape artist
flyranksmod
flydexmod
flyothermods
fly
healranksmod
healwismod
healothermods
heal
intimidateranksmod
intimidatechamod
intimidateothermods
intimidate
knowledge arcanaranksmod
knowledge arcanaintmod
knowledge arcanaothermods
knowledge arcana
knowledge dungeoneeringranksmod
knowledge dungeoneeringintmod
knowledge dungeoneeringothermods
knowledge dungeoneering
knowledge engineeringranksmod
knowledge engineeringintmod
knowledge engineeringothermods
knowledge engineering
knowledge geographyranksmod
knowledge geographyintmod
knowledge geographyothermods
knowledge geography
knowledge historyranksmod
knowledge historyintmod
knowledge historyothermods
knowledge history
knowledge localranksmod
knowledge localintmod
knowledge localothermods
knowledge local
knowledge natureranksmod
knowledge natureintmod
knowledge natureothermods
knowledge nature
knowledge nobilityranksmod
knowledge nobilityintmod
knowledge nobilityothermods
knowledge nobility
knowledge planesranksmod
knowledge planesintmod
knowledge planesothermods
knowledge planes
knowledge religionranksmod
knowledge religionintmod
knowledge religionothermods
knowledge religion
linguisticsranksmod
linguisticsintmod
linguisticsothermods
linguistics
perceptionranksmod
perceptionwismod
perceptionothermods
perception
perform actranksmod
perform actchamod
perform actothermods
perform act
perform comedyranksmod
perform comedychamod
perform comedyothermods
perform comedy
perform danceranksmod
perform dancechamod
perform danceothermods
perform dance
perform keyboardranksmod
perform keyboardchamod
perform keyboardothermods
perform keyboard
perform oritoryranksmod
perform oritorychamod
perform oritoryothermods
perform oritory
perform percussionranksmod
perform percussionchamod
perform percussionothermods
perform percussion
perform singranksmod
perform singchamod
perform singothermods
perform sing
perform stringedranksmod
perform stringedchamod
perform stringedothermods
perform stringed
perform windranksmod
perform windchamod
perform windothermods
perform wind
professionranksmod
professionwismod
professionothermods
profession
rideranksmod
ridedexmod
rideothermods
ride
sense motiveranksmod
sense motivewismod
sense motiveothermods
sense motive
slight of handranksmod
slight of handdexmod
slight of handothermods
slight of hand
spell craftranksmod
spell craftintmod
spell craftothermods
spell craft
stealthranksmod
stealthdexmod
stealthothermods
stealth
survivalranksmod
survivalwismod
survivalothermods
survival
swimranksmod
swimstrmod
swimothermods
swim
use magic deviceranksmod
use magic devicechamod
use magic deviceothermods
use magic device
spellknown
spellprep
specmag
sd0
sd1
sd2
sd3
sd4
sd5
sd6
sd7
sd8
sd9
abilities
racialtraites
feats
languages
cp
sp
gp
pp
geer
armourname
armourbonus
acp
armourmaxdex
armourspellfailure
armourspeed
shieldname
shieldbonus
scp
shieldspellfailure
acn1
acb1
acn2
acb2
acn3
acb3
acn4
acb4
melee1
melee2
weapon3
weapon4""".split("\n")
def save() :
    data={}
    for id in ids :
        data[id]=document.getElementById(id).value
    jq.ajax({"type":"POST","url":"/save/{}".format(document.getElementById("name").value),"contentType":"application/json","data":JSON.stringify(data)})
    event.preventDefault()
save()