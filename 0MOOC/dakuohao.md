- 2015-11-21
- 今早发现gitbook发了一封信件，提醒我文章更新出错，前去查看，错误提示如下：
- Template render error: (/tmp/book/2nDev/w4ex0.md) [Line 85, Column 43]
  unexpected token: }} (In file '2nDev/w4ex0.md')
- 根据这一关键词google
- 进入下面页面：https://github.com/GitbookIO/gitbook/issues/637
- 原来{% raw %}{{ 和 }} {% endraw %}被gitbook的模板系统征用，为了要体现双大括号，必须在括号前加 {% raw %} {% raw %}，在括号后加{% endraw %}{% endraw %}
- 见说明：The latest version is 2.0.0-beta.5, {% raw %}{{ and }} {% endraw %}are used by the templating engine (http://help.gitbook.com/format/templating.html), with the latest versions we are escaping code blocks.
- You can also use: {% raw %} {% raw %}{{ and }} {% endraw %}{% endraw %} to escape these templating controls.