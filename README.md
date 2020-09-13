# thu_courses2ics
清华大学课表转换为.ics文件的工具，可直接导入Apple、outlook、华为等系统日历

## 使用方法/Usage
0. clone repository：下载整个repos到本地
1. 登陆进入清华大学本科生选课系统 `http://zhjwxk.cic.tsinghua.edu.cn/xklogin.do#`
2. 选择：课表查询->一级课表，右上角点击“导出为XLS”，下载课表的excel文件
3. 在`config.py`中按照提示更改各项信息。需要填入刚刚下载的excel文件的路径
4. 下载依赖项：pip3 install -r requirements.txt
5. 用python3运行main.py，获得ics文件，拖入需要导入的日历，或者在系统里找”导入“即可。
