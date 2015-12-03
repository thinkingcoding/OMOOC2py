%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>这个故事是这样的:</p>
<p><b>{{title}}</b></p>
%for row in sorted(rows):
	<p>{{row[1][0]}}
	by {{row[1][1]}}
	at {{row[1][2]}}</p>
%end

<p>请你把故事接下去:</p>
<form action='/{{title}}' method="GET">
<input type="text" size="100" maxlength="400" name="main">
<input type="submit" name="save" value="保存">
</form>
{{information}}

<a href='/'>返回到首页</a>