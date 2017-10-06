<html>
<head>
<title>Dice Roller</title>
</head>
<body>
<form action="http://192.168.0.200/dice" method="post">
<b>Fill in a die expression such as "1d6" or "3d8+5."<br/>
Than hit the roll button to get your result.<br/>
</b>
<input type="text" name="dice">
<b>{{roll}}</b>
<input type="submit" name="rolled" value="Roll">
</form>
</body>
</html>