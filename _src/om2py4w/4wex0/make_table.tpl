%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>这个故事是这样的:</p>
<table border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>

<p>请你把故事接下去:</p>
<form action='/storychain/{{title}}' method="GET">
<input type="text" size="100" maxlength="400" name="main">
<input type="submit" name="save" value="保存">
</form>