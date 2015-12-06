<p>欢迎你，{{userid}}</P>
<p>开始一个新故事:</p>
<form action='/index' method='GET'>
	<input name='title' type='text' size = '20' maxlength='40'/>
	<input value = '创建' name = 'save' type = 'submit'/>
</form>	
<p>注意：故事名不能重名！</p>
<p>{{information}}</p>
<b>浏览故事</b><p></p>
%for row in rows:
	<b>{{row[0]}}:</b> 
	{{row[1]}}  ...
	<a href='/{{row[0]}}'>进入</a>
	<p></p>
%end


