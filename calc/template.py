html = b"""
<html>
    <body>
        <form method="get" action="">
            a = <input type = "number" name = "a"><br><br>	
            b = <input type = "number" name = "b"><br><br>
            <input type="submit">
        </form>
	<p>
	Sum(a+b) = %(sum)s<br><br>
	Mul(a*b) = %(mul)s<br><br>
        %(error)s
	<p>
    </body>
</html>
"""

