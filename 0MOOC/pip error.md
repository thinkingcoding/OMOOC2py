学习bottle：
PS C:\Users\Shen> pip install bottle
Traceback (most recent call last):
  File "C:\Python27\Scripts\pip-script.py", line 9, in <module>
    load_entry_point('pip==1.5.6', 'console_scripts', 'pip')()
  File "C:\Python27\lib\site-packages\pkg_resources\__init__.py", line 558, in load_entry_point
    return get_distribution(dist).load_entry_point(group, name)
  File "C:\Python27\lib\site-packages\pkg_resources\__init__.py", line 2682, in load_entry_point
    return ep.load()
  File "C:\Python27\lib\site-packages\pkg_resources\__init__.py", line 2355, in load
    return self.resolve()
  File "C:\Python27\lib\site-packages\pkg_resources\__init__.py", line 2361, in resolve
    module = __import__(self.module_name, fromlist=['__name__'], level=0)
  File "C:\Python27\lib\site-packages\pip\__init__.py", line 13, in <module>
    from pip.commands import commands, get_summaries, get_similar_commands
  File "C:\Python27\lib\site-packages\pip\commands\__init__.py", line 6, in <module>
    from pip.commands.bundle import BundleCommand
  File "C:\Python27\lib\site-packages\pip\commands\bundle.py", line 6, in <module>
    from pip.commands.install import InstallCommand
  File "C:\Python27\lib\site-packages\pip\commands\install.py", line 5, in <module>
    from pip.req import InstallRequirement, RequirementSet, parse_requirements
  File "C:\Python27\lib\site-packages\pip\req\__init__.py", line 3, in <module>
    from .req_install import InstallRequirement
  File "C:\Python27\lib\site-packages\pip\req\req_install.py", line 30, in <module>
    from pip.utils import (
  File "C:\Python27\lib\site-packages\pip\utils\__init__.py", line 88, in <module>
    def rmtree(dir, ignore_errors=False):
  File "C:\Python27\lib\site-packages\pip\_vendor\retrying.py", line 47, in wrap
    @six.wraps(f)
AttributeError: 'module' object has no attribute 'wraps'
google之，该错误是因为pip的安装出了问题。简单粗暴的方法是删除文件重新安装。
检查C:\Python27\Lib\site-packages，发现pip相关的有三个文件夹
图：C:\Users\Shen\OneDrive\图片\屏幕快照
重装pip
 - 尝试在powershell输入pip uninstall pip，出现同上错误提示。
 - 尝试输入python -m pip uninstall pip setuptools, 出错。
 - 删除上述文件夹的pip文件夹。重新运行get-pip.py。
 - 提示安装成功。
- 在powershell 输入pip install bottle。成功。