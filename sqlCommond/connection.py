import pymssql
from pyecharts import Pie
from pyecharts import Bar


con = pymssql.connect(host="localhost", user="sa", password="P@44w0rd", database="expense", charset="utf8")
cur = con.cursor()
if not cur:
	raise (NameError, "连接失败！")
cur.execute("	SELECT SUM(payment) pay,type FROM dbo.payment \
				GROUP BY type")

list = cur.fetchall()  # fetchall是接收所有的返回行
con.close()

# 定义2个列用来存放类型和开销
typelist = []
paylist = []
print(type(list), type(list[0]))
for i, (pay, type) in enumerate(list):
	typelist.append(type.encode('latin-1').decode('gbk')) # 解决中文乱码问题
	paylist.append(str(pay))

#pie = Pie("花费统计")
#pie.add("", typelist, paylist, is_label_show=True)
#pie.render()

bar = Bar("花费统计")
bar.add("", typelist, paylist, is_label_show=True)
bar.render()

