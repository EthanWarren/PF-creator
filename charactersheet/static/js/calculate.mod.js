	(function () {
		var barbarian = {};
		var bard = {};
		var cleric = {};
		var druid = {};
		var fighter = {};
		var monk = {};
		var paladin = {};
		var ranger = {};
		var rogue = {};
		var skills = {};
		var sorcerer = {};
		var wizard = {};
		__nest__ (barbarian, '', __init__ (__world__.barbarian));
		__nest__ (bard, '', __init__ (__world__.bard));
		__nest__ (cleric, '', __init__ (__world__.cleric));
		__nest__ (druid, '', __init__ (__world__.druid));
		__nest__ (fighter, '', __init__ (__world__.fighter));
		__nest__ (monk, '', __init__ (__world__.monk));
		__nest__ (paladin, '', __init__ (__world__.paladin));
		__nest__ (ranger, '', __init__ (__world__.ranger));
		__nest__ (rogue, '', __init__ (__world__.rogue));
		__nest__ (sorcerer, '', __init__ (__world__.sorcerer));
		__nest__ (wizard, '', __init__ (__world__.wizard));
		__nest__ (skills, '', __init__ (__world__.skills));
		var classes = dict ({'barbarian': barbarian, 'bard': bard, 'cleric': cleric, 'druid': druid, 'fighter': fighter, 'monk': monk, 'paladin': paladin, 'ranger': ranger, 'rogue': rogue, 'sorcerer': sorcerer, 'wizard': wizard});
		var calc_size = function () {
			var race = document.getElementById ('race').value;
			if (__in__ (race, list (['elf', 'dwarf', 'human', 'halfelf', 'half elf', 'halforc', 'half orc']))) {
				document.getElementById ('size').value = 'medium';
			}
			else if (__in__ (race, list (['halfling', 'gnome']))) {
				document.getElementById ('size').value = 'small';
			}
		};
		var calc_hp = function () {
			var charclass = document.getElementById ('class').value;
			var level = int (document.getElementById ('level').value);
			document.getElementById ('maxhp').value = str ((((classes [charclass].table ['hp'] + ((level - 1) * classes [charclass].table ['hp']) / 2) + int (document.getElementById ('conmod').value) * level) + int (document.getElementById ('hpothermods1').value)) + int (document.getElementById ('hpothermods2').value) * level);
		};
		var calc_fort = function () {
			document.getElementById ('fortclassmod').value = str (classes [document.getElementById ('class').value].table [int (document.getElementById ('level').value)] ['fort']);
			document.getElementById ('fortconmod').value = document.getElementById ('conmod').value;
			document.getElementById ('fortsave').value = str (((int (document.getElementById ('fortclassmod').value) + int (document.getElementById ('fortconmod').value)) + int (document.getElementById ('fortothermod1').value)) + int (document.getElementById ('fortothermod2').value));
		};
		var calc_ref = function () {
			document.getElementById ('refclassmod').value = str (classes [document.getElementById ('class').value].table [int (document.getElementById ('level').value)] ['ref']);
			document.getElementById ('refdexmod').value = document.getElementById ('dexmod').value;
			document.getElementById ('refsave').value = str (((int (document.getElementById ('refclassmod').value) + int (document.getElementById ('refdexmod').value)) + int (document.getElementById ('refothermod1').value)) + int (document.getElementById ('refothermod2').value));
		};
		var calc_will = function () {
			document.getElementById ('willclassmod').value = str (classes [document.getElementById ('class').value].table [int (document.getElementById ('level').value)] ['will']);
			document.getElementById ('willwismod').value = document.getElementById ('wismod').value;
			document.getElementById ('willsave').value = str (((int (document.getElementById ('willclassmod').value) + int (document.getElementById ('willwismod').value)) + int (document.getElementById ('willothermod1').value)) + int (document.getElementById ('willothermod2').value));
		};
		var calc_bab = function () {
			var charclass = document.getElementById ('class').value;
			var level = int (document.getElementById ('level').value);
			document.getElementById ('bab').value = str (classes [charclass].table [level] ['bab']);
		};
		var calc_scores = function () {
			var strscore = int (document.getElementById ('strscore').value);
			var dexscore = int (document.getElementById ('dexscore').value);
			var conscore = int (document.getElementById ('conscore').value);
			var intscore = int (document.getElementById ('intscore').value);
			var wisscore = int (document.getElementById ('wisscore').value);
			var chascore = int (document.getElementById ('chascore').value);
			document.getElementById ('strmod').value = str (Math.floor ((strscore - 10) / 2));
			document.getElementById ('dexmod').value = str (Math.floor ((dexscore - 10) / 2));
			document.getElementById ('conmod').value = str (Math.floor ((conscore - 10) / 2));
			document.getElementById ('intmod').value = str (Math.floor ((intscore - 10) / 2));
			document.getElementById ('wismod').value = str (Math.floor ((wisscore - 10) / 2));
			document.getElementById ('chamod').value = str (Math.floor ((chascore - 10) / 2));
		};
		var calc_cmb = function () {
			document.getElementById ('cmbbab').value = document.getElementById ('bab').value;
			document.getElementById ('cmbstrmod').value = document.getElementById ('strmod').value;
			if (document.getElementById ('size').value == 'medium') {
				document.getElementById ('cmbsizemod').value = '0';
			}
			else if (document.getElementById ('size').value == 'small') {
				document.getElementById ('cmbsizemod').value = '-1';
			}
			document.getElementById ('cmb').value = str (((int (document.getElementById ('cmbbab').value) + int (document.getElementById ('cmbstrmod').value)) + int (document.getElementById ('cmbsizemod').value)) + int (document.getElementById ('cmbothermods').value));
		};
		var calc_cmd = function () {
			document.getElementById ('cmdbab').value = document.getElementById ('bab').value;
			document.getElementById ('cmdstrmod').value = document.getElementById ('strmod').value;
			document.getElementById ('cmddexmod').value = document.getElementById ('dexmod').value;
			if (document.getElementById ('size').value == 'medium') {
				document.getElementById ('cmdsizemod').value = '0';
			}
			else if (document.getElementById ('size').value == 'small') {
				document.getElementById ('cmdsizemod').value = '-1';
			}
			document.getElementById ('cmd').value = str (((((int (document.getElementById ('cmdbab').value) + int (document.getElementById ('cmdstrmod').value)) + int (document.getElementById ('cmddexmod').value)) + int (document.getElementById ('cmdsizemod').value)) + int (document.getElementById ('cmdothermods').value)) + 10);
		};
		var calc_melee = function () {
			var size = document.getElementById ('size').value;
			document.getElementById ('meleebab').value = document.getElementById ('bab').value;
			document.getElementById ('meleestrmod').value = document.getElementById ('strmod').value;
			if (size == 'medium') {
				document.getElementById ('meleesizemod').value = '0';
			}
			else if (size == 'small') {
				document.getElementById ('meleesizemod').value = '1';
			}
			document.getElementById ('melee').value = str (((int (document.getElementById ('meleebab').value) + int (document.getElementById ('meleestrmod').value)) + int (document.getElementById ('meleesizemod').value)) + int (document.getElementById ('meleeothermods').value));
		};
		var calc_ranged = function () {
			var size = document.getElementById ('size').value;
			document.getElementById ('rangedbab').value = document.getElementById ('bab').value;
			document.getElementById ('rangeddexmod').value = document.getElementById ('dexmod').value;
			if (size == 'medium') {
				document.getElementById ('rangedsizemod').value = '0';
			}
			else if (size == 'small') {
				document.getElementById ('rangedsizemod').value = '1';
			}
			document.getElementById ('ranged').value = str (((int (document.getElementById ('rangedbab').value) + int (document.getElementById ('rangeddexmod').value)) + int (document.getElementById ('rangedsizemod').value)) + int (document.getElementById ('rangedothermods').value));
		};
		var calc_skills = function () {
			var __iterable0__ = skills.list.py_keys ();
			for (var __index0__ = 0; __index0__ < __iterable0__.length; __index0__++) {
				var skill = __iterable0__ [__index0__];
				document.getElementById ('{}{}mod'.format (skill, skills.list [skill])).value = document.getElementById ('{}mod'.format (skills.list [skill])).value;
				document.getElementById ('{}'.format (skill)).value = str ((int (document.getElementById ('{}ranksmod'.format (skill)).value) + int (document.getElementById ('{}{}mod'.format (skill, skills.list [skill])).value)) + int (document.getElementById ('{}othermods'.format (skill)).value));
			}
			if (document.getElementById ('size').value == 'small') {
				document.getElementById ('stealthothermods').value = '4';
			}
		};
		var calc_race = function () {
			var race = document.getElementById ('race').value;
			var raceinfo = document.getElementById ('raceinfo');
			if (race == 'human') {
				raceinfo.innerHTML = '+2 any one ability score';
			}
			else if (race == 'half elf') {
				raceinfo.innerHTML = '+2 any one ability score';
				document.getElementById ('perceptionothermods').value = '2';
			}
			else if (race == 'half orc') {
				raceinfo.innerHTML = '+2 any one ability score';
				document.getElementById ('intimidateothermods').value = '2';
			}
			else if (race == 'halfling') {
				raceinfo.innerHTML = '+2dex,+2cha,-2 str';
				document.getElementById ('fortothermod1').value = '1';
				document.getElementById ('refothermod1').value = '1';
				document.getElementById ('willothermod1').value = '1';
				document.getElementById ('perceptionothermods').value = '2';
				document.getElementById ('climbothermods').value = '2';
				document.getElementById ('acrobaticsothermods').value = '2';
			}
			else if (race == 'gnome') {
				raceinfo.innerHTML = '+2cha,+2 con,-2 str';
				document.getElementById ('perceptionothermods').value = '2';
			}
			else if (race == 'elf') {
				raceinfo.innerHTML = '+2 int, +2 dex, -2 con';
				document.getElementById ('perceptionothermods').value = '2';
			}
			else if (race == 'dwarf') {
				raceinfo.innerHTML = '+2 con, +2 wis, -2 cha';
			}
		};
		var calc_init = function () {
			document.getElementById ('initdexmod').value = document.getElementById ('dexmod').value;
			document.getElementById ('init').value = str (int (document.getElementById ('initdexmod').value) + int (document.getElementById ('initothermods').value));
		};
		var calc_speed = function () {
			var race = document.getElementById ('race').value;
			if (__in__ (race, list (['gnome', 'halfling', 'dwarf']))) {
				document.getElementById ('ls').value = '20';
			}
			else {
				document.getElementById ('ls').value = '30';
			}
		};
		var calc_ac = function () {
			document.getElementById ('acbonus').value = str (((((int (document.getElementById ('armourbonus').value) + int (document.getElementById ('shieldbonus').value)) + int (document.getElementById ('acb1').value)) + int (document.getElementById ('acb2').value)) + int (document.getElementById ('acb3').value)) + int (document.getElementById ('acb4').value));
			if (int (document.getElementById ('dexmod').value) > int (document.getElementById ('armourmaxdex').value)) {
				document.getElementById ('acdexmod').value = document.getElementById ('armourmaxdex').value;
			}
			else {
				document.getElementById ('acdexmod').value = document.getElementById ('dexmod').value;
			}
			if (document.getElementById ('size').value == 'small') {
				document.getElementById ('acsizemod').value = '1';
			}
			else if (document.getElementById ('size').value == 'medium') {
				document.getElementById ('acsizemod').value = '0';
			}
			document.getElementById ('ac').value = str ((((int (document.getElementById ('acbonus').value) + int (document.getElementById ('acdexmod').value)) + int (document.getElementById ('acsizemod').value)) + int (document.getElementById ('acothermods').value)) + 10);
		};
		var calc_languages = function () {
			var languagestr = '';
			var race = document.getElementById ('race').value;
			if (race == 'human') {
				var languagestr = 'common';
			}
			else if (race == 'half elf') {
				var languagestr = 'common , elven';
			}
			else if (race == 'half orc') {
				var languagestr = 'common , orc';
			}
			else if (race == 'dwarf') {
				var languagestr = 'common , dwarven';
			}
			else if (race == 'elf') {
				var languagestr = 'common , elven';
			}
			else if (race == 'gnome') {
				var languagestr = 'common , gnome';
			}
			else if (race == 'halfling') {
				var languagestr = 'common , halfling';
			}
			document.getElementById ('languages').innerHTML = languagestr;
		};
		calc_race ();
		calc_size ();
		calc_scores ();
		calc_hp ();
		calc_fort ();
		calc_ref ();
		calc_will ();
		calc_ac ();
		calc_init ();
		calc_speed ();
		calc_bab ();
		calc_cmb ();
		calc_cmd ();
		calc_melee ();
		calc_ranged ();
		calc_skills ();
		calc_languages ();
		document.getElementById ('currenthp').value = document.getElementById ('maxhp').value;
		setInterval (calc_race, 3000);
		setInterval (calc_size, 3000);
		setInterval (calc_scores, 3000);
		setInterval (calc_hp, 3000);
		setInterval (calc_fort, 3000);
		setInterval (calc_ref, 3000);
		setInterval (calc_will, 3000);
		setInterval (calc_ac, 3000);
		setInterval (calc_init, 3000);
		setInterval (calc_speed, 3000);
		setInterval (calc_bab, 3000);
		setInterval (calc_cmb, 3000);
		setInterval (calc_cmd, 3000);
		setInterval (calc_melee, 3000);
		setInterval (calc_ranged, 3000);
		setInterval (calc_skills, 3000);
		setInterval (calc_languages, 3000);
		__pragma__ ('<use>' +
			'barbarian' +
			'bard' +
			'cleric' +
			'druid' +
			'fighter' +
			'monk' +
			'paladin' +
			'ranger' +
			'rogue' +
			'skills' +
			'sorcerer' +
			'wizard' +
		'</use>')
		__pragma__ ('<all>')
			__all__.calc_ac = calc_ac;
			__all__.calc_bab = calc_bab;
			__all__.calc_cmb = calc_cmb;
			__all__.calc_cmd = calc_cmd;
			__all__.calc_fort = calc_fort;
			__all__.calc_hp = calc_hp;
			__all__.calc_init = calc_init;
			__all__.calc_languages = calc_languages;
			__all__.calc_melee = calc_melee;
			__all__.calc_race = calc_race;
			__all__.calc_ranged = calc_ranged;
			__all__.calc_ref = calc_ref;
			__all__.calc_scores = calc_scores;
			__all__.calc_size = calc_size;
			__all__.calc_skills = calc_skills;
			__all__.calc_speed = calc_speed;
			__all__.calc_will = calc_will;
			__all__.classes = classes;
		__pragma__ ('</all>')
	}) ();
