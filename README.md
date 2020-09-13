# thu_courses2ics
清华大学本科生课表转换为.ics文件的工具，可直接把课表导入Apple、outlook、华为等系统日历，随手查看。

## 使用方法/Usage
0. clone repository：下载整个repos到本地
1. 登陆进入清华大学本科生选课系统 `http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do#`
2. 选择：课表查询->一级课表，右上角点击“导出为XLS”，下载课表的excel文件
3. 在`config.py`中按照提示更改各项信息。需要填入刚刚下载的excel文件的路径
4. 下载依赖项：`pip3 install -r requirements.txt`
5. 用`python3`运行`main.py`，获得`ics`文件，拖入需要导入的日历，或者在日历软件里找”导入“即可。

## 可能的BUG
测试样例目前还很少，某些特殊课程的存在可能导致导入失败：如重修课，冲突选课等。

## 声明
这是本萌新第一个repos，觉得可能对同学们很有用；不过代码能力较弱，请大家多多包涵。欢迎提建议，指出bug。欢迎pull request，欢迎star。
